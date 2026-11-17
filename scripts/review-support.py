#!/usr/bin/env python3
"""Review runner and shared prompt renderer; standard library only."""
import json
import os
from pathlib import Path
import re
import signal
import subprocess
import sys
import time
from datetime import datetime

TEMPLATE = Path(__file__).resolve().parent.parent / "templates/reviewer-prompt.md"


def render(brief, number, scope):
    text = TEMPLATE.read_text()
    common = text.split("<!-- FULL -->", 1)[0]
    section = re.search(rf"<!-- {scope.upper()} -->\n(.*?)<!-- /{scope.upper()} -->", text, re.S)
    if not section:
        raise ValueError("missing prompt scope section")
    return (common.replace("{{SCOPE}}", section[1].strip())
            .replace("{{ROUND}}", str(number)).replace("{{BRIEF}}", brief))


def parse_reply(raw, log, who, identity_file):
    """Use runner/provider metadata, never the reviewer's claim about itself."""
    models, primary_models, chunks, source, provider_error = set(), set(), [], "missing", False
    try:
        data = json.loads(raw)
        events = data if isinstance(data, list) else [data]
    except ValueError:
        events = []
        for line in raw.splitlines():
            try:
                events.append(json.loads(line))
            except ValueError:
                pass
    for event in events:
        if not isinstance(event, dict):
            continue
        if event.get("is_error") or event.get("type") == "error":
            provider_error = True
        message = event.get("message", {})
        if event.get("type") == "assistant" and isinstance(message, dict) and message.get("model"):
            primary_models.add(message["model"])
        usage = event.get("modelUsage", {})
        if isinstance(usage, dict) and usage:
            models.update(usage)
            source = "modelUsage"
        if isinstance(event.get("result"), str):
            chunks.append(event["result"])
        part = event.get("part", {})
        if not isinstance(part, dict):
            continue
        if part.get("type") == "text" and isinstance(part.get("text"), str):
            chunks.append(part["text"])
        if part.get("modelID") and part.get("providerID"):
            models.add(f'{part["providerID"]}/{part["modelID"]}')
            source = "event-model"
    if primary_models:
        models, source = primary_models, "assistant-message"
    if who == "codex":
        log = log.split("\nuser\n", 1)[0]
        models.update(re.findall(r"^model:\s*(\S+)\s*$", log, re.M))
        source = "cli-header" if models else source
    if who == "opencode":
        # OpenCode versions without model fields in JSON report it in LLM logs.
        for line in log.splitlines():
            if "service=llm" in line and "small=false" in line:
                provider = re.search(r"\bproviderID=(\S+)", line)
                model = re.search(r"\bmodelID=(\S+)", line)
                if provider and model:
                    models.add(f"{provider[1]}/{model[1]}")
                    source = "llm-log"
    if identity_file.is_file() and identity_file.read_text().strip():
        models.add(identity_file.read_text().strip())
        source += "+adapter-receipt"
    return "\n".join(chunks) if chunks else raw, models, source, provider_error


def run(args):
    if len(args) not in (3, 4):
        raise ValueError("usage: review-round.sh <brief.md> <run-dir> <round:1-5> [codex|claude|opencode|cmd]")
    brief, folder, number = args[:3]
    who = args[3] if len(args) == 4 else "codex"
    if not re.fullmatch(r"[1-5]", number):
        raise ValueError("round must be 1-5; hard ceiling is 5")
    number = int(number)
    if not Path(brief).is_file():
        raise ValueError(f"brief not found: {brief}")
    model = os.environ.get("REVIEW_MODEL", "").strip()
    if not model or re.search(r"\s|[|]", model):
        raise ValueError("REVIEW_MODEL must be an exact model ID")
    if model.split("/")[-1].isalpha() or "latest" in model.lower():
        raise ValueError("floating model aliases are not allowed; pin an exact ID")
    command = os.environ.get("REVIEW_CMD", "")
    if command:
        who = "cmd"
    if who not in {"codex", "claude", "opencode", "cmd"} or (who == "cmd" and not command):
        raise ValueError("select codex, claude, opencode, or cmd with REVIEW_CMD")
    scope = os.environ.get("REVIEW_SCOPE") or ("full" if number == 1 else "delta")
    if scope not in {"full", "delta"} or (number == 1 and scope != "full"):
        raise ValueError("round 1 must be full; REVIEW_SCOPE must be full or delta")
    timeout = float(os.environ.get("REVIEW_TIMEOUT", "300"))
    if not 0 < timeout < float("inf"):
        raise ValueError("REVIEW_TIMEOUT must be finite and positive")
    effort = os.environ.get("REVIEW_EFFORT", "high")
    if effort not in {"minimal", "low", "medium", "high", "xhigh", "max"}:
        raise ValueError("invalid REVIEW_EFFORT")
    run_dir = Path(folder).resolve()
    run_dir.mkdir(parents=True, exist_ok=True)
    if number > 3 and not (run_dir / "allowance.md").is_file():
        raise ValueError("rounds 4-5 require allowance.md recording a concrete serious risk before use")
    if number > 3 and not (run_dir / "allowance.md").read_text().strip():
        raise ValueError("allowance.md must name the concrete serious risk")
    meta = run_dir / "meta.txt"
    history = meta.read_text().splitlines() if meta.exists() else []
    pin = {"reviewer": who, "model": model, "effort": effort if who == "codex" else "adapter", "command": command}
    pin_path = run_dir / "reviewer.json"
    if pin_path.exists() and json.loads(pin_path.read_text()) != pin:
        raise ValueError("reviewer/model/options changed within this decision; checkpoint and obtain an authorized exception")
    attempts = [line for line in history if line.startswith(f"r{number} |")]
    resumed = os.environ.get("REVIEW_RESUME", "") == "1"
    if any(" | ok |" in line for line in attempts):
        raise ValueError(f"round {number} already has a verified review; start round {number + 1}")
    auto_retry_ok = len(attempts) == 1 and "class=recoverable" in attempts[-1]
    if attempts and not auto_retry_ok and not resumed:
        raise ValueError("only one same-model retry of a recoverable failure is allowed; pause otherwise "
                         "(after the user authorizes resuming on the same pinned reviewer, rerun with REVIEW_RESUME=1)")
    if number > 1 and not any(line.startswith(f"r{number-1} |") and " | ok |" in line for line in history):
        raise ValueError("previous round has no verified receipt; do not skip/reset rounds")
    brief_text = Path(brief).read_text()
    prompt = render(brief_text, number, scope)
    pin_path.write_text(json.dumps(pin, indent=2) + "\n")
    # Preserve each attempt; never let stale output count as a new result.
    prefix = run_dir / f"r{number}-attempt{len(attempts)+1}"
    raw_path, log_path = Path(f"{prefix}.raw"), Path(f"{prefix}.log")
    identity_file = Path(f"{prefix}.identity")
    (run_dir / f"r{number}-brief.md").write_text(brief_text)
    (run_dir / f"r{number}-prompt.md").write_text(prompt)
    output = run_dir / f"r{number}-review.md"
    output.write_text(f"ERROR: round {number} pending validation\n")
    argv = {
        "codex": ["codex", "exec", "--skip-git-repo-check", "--ephemeral", "--sandbox", "read-only", "-m", model,
                  "-c", f'model_reasoning_effort="{effort}"', "-o", str(raw_path), "-"],
        "claude": ["claude", "-p", "--model", model, "--output-format", "stream-json", "--verbose", "--no-session-persistence", "--tools", "",
                   "--disable-slash-commands", "--setting-sources", "", "--strict-mcp-config",
                   "--mcp-config", '{"mcpServers":{}}', "--prompt-suggestions", "false",
                   "--system-prompt", "Follow the supplied independent review contract."],
        "opencode": ["opencode", "run", "--format", "json", "--print-logs", "--model", model, "--title", "Decision review"],
        "cmd": ["bash", "-c", command],
    }[who]
    env = {**os.environ, "REVIEW_MODEL": model, "REVIEW_IDENTITY_FILE": str(identity_file)}
    start, rc, timed_out = time.monotonic(), 0, False
    with log_path.open("w") as log_file:
        # Codex puts its selected model and effort in its startup header.
        stdout_path = log_path if who == "codex" else raw_path
        with stdout_path.open("a" if who == "codex" else "w") as stdout_file:
            try:
                process = subprocess.Popen(argv, stdin=subprocess.PIPE, stdout=log_file if who == "codex" else stdout_file,
                                           stderr=log_file, env=env, start_new_session=True)
                try:
                    process.communicate(prompt.encode(), timeout=timeout)
                except subprocess.TimeoutExpired:
                    timed_out = True
                    os.killpg(process.pid, signal.SIGKILL)
                    process.communicate()
                rc = process.returncode
            except OSError as exc:
                log_file.write(str(exc))
                rc = 127
    seconds = int(time.monotonic() - start)
    raw = raw_path.read_text(errors="replace") if raw_path.exists() else ""
    log = log_path.read_text(errors="replace")
    (run_dir / f"r{number}.log").write_text(log)
    reply, models, identity_source, provider_error = parse_reply(raw, log, who, identity_file)
    actual = ",".join(sorted(models)) or "unknown"
    verdicts = re.findall(r"^\s*(?:\*\*)?VERDICT(?:\*\*)?\s*:\s*(?:\*\*)?\s*(AGREE-WITH-CHANGES|AGREE|DISAGREE)(?:\*\*)?\s*$", reply, re.M)
    reason = ""
    failure_class = "recoverable"
    if timed_out:
        reason, failure_class = "timeout", "availability"
    elif rc != 0:
        reason = f"exit={rc}"
        # An unsuccessful provider call without a known local/format error is not safe to retry blindly.
        failure_class = "configuration" if re.search(r"unknown model|invalid model|model.*not found|no such file", log + raw, re.I) else "availability"
    elif provider_error:
        reason, failure_class = "provider error response", "availability"
    elif models != {model}:
        reason, failure_class = "missing or mismatched model identity", "identity"
    elif who == "codex" and not re.search(rf"^reasoning effort:\s*{re.escape(effort)}\s*$", log, re.M):
        reason, failure_class = "missing or mismatched reasoning effort", "identity"
    elif not reply.strip():
        reason = "empty output"
    elif len(verdicts) != 1:
        reason = "no single valid VERDICT line"
    elif not re.search(r"^\s*(?:\*\*)?FINDINGS(?:\*\*)?\s*:", reply, re.M):
        reason = "no FINDINGS section"
    # Availability errors override an otherwise valid-looking review or error classification.
    if re.search(r"rate.?limit|quota|capacity|overloaded|provider.?unavailable|transport error|connection (?:error|refused|reset)|authentication failed|unauthorized", log + raw, re.I):
        if rc != 0 or not verdicts:
            reason, failure_class = reason or "provider unavailable", "availability"
    verdict = verdicts[0] if not reason else "none"
    if reason:
        Path(str(output) + ".invalid").write_text(raw)
        output.write_text(f"ERROR: {who} round {number} invalid ({reason}); class={failure_class}; see {log_path}\n")
        status = f"FAILED ({reason}) class={failure_class}"
    else:
        output.write_text(reply.strip() + "\n")
        status = "ok"
    with meta.open("a") as handle:
        handle.write(f"r{number} | {datetime.now():%F %T} | reviewer={who} model={actual} requested={model} effort={pin['effort']} identity={identity_source} scope={scope}{' resume=user' if resumed and attempts else ''} | {status} | verdict={verdict} | {seconds}s\n")
    print(output)
    return 1 if reason else 0


if __name__ == "__main__":
    try:
        if len(sys.argv) > 1 and sys.argv[1] == "render":
            # Same bytes for a native fresh-context reviewer and every CLI adapter.
            if len(sys.argv) not in (4, 5) or not re.fullmatch(r"[1-5]", sys.argv[3]):
                raise ValueError("usage: review-support.py render <brief.md> <round:1-5> [full|delta]")
            n = int(sys.argv[3])
            s = sys.argv[4] if len(sys.argv) == 5 else ("full" if n == 1 else "delta")
            if s not in {"full", "delta"} or (n == 1 and s != "full"):
                raise ValueError("invalid scope; round 1 must be full")
            print(render(Path(sys.argv[2]).read_text(), n, s), end="")
            sys.exit(0)
        if len(sys.argv) < 2 or sys.argv[1] != "run":
            raise ValueError("expected run or render")
        sys.exit(run(sys.argv[2:]))
    except (ValueError, OSError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(2)
