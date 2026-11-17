# Reviewer execution and receipts

Read before every native or CLI round. Policy and allowance remain in SKILL.md.

## Adapters

The shell entry point resolves its renderer/template relative to itself, regardless of cwd.
Dependencies: Bash, Python 3 and the chosen reviewer CLI.

- `codex`: `REVIEW_MODEL=<exact-id>` and `REVIEW_EFFORT=high` (default). Fresh ephemeral,
  read-only execution. Verify model and effort in its CLI startup header. This records the
  CLI's selected model, not a server-side attestation of the model that served tokens.
- `claude`: exact `REVIEW_MODEL`; fresh non-persistent print invocation, tools disabled;
  parse result and assistant message model from streaming JSON. Aggregate `modelUsage` can
  include auxiliary calls; it does not identify the primary reviewer. No resume/continue.
- `opencode`: `REVIEW_MODEL=provider/exact-model`; fresh invocation without session/continue;
  parse text and model telemetry from JSON or its LLM log. Missing identity fails closed.
- `cmd`: `REVIEW_CMD` overrides the selected CLI. It is a trusted shell command that reads
  the entire rendered prompt on stdin and emits the review on stdout. Set `REVIEW_MODEL`
  separately; the command must explicitly select it and start a fresh context. Never resume.

For example, an arbitrary command can emit Claude JSON including its provider identity:

```sh
REVIEW_MODEL=<exact-id> \
REVIEW_CMD='claude -p --model "$REVIEW_MODEL" --output-format stream-json --verbose --no-session-persistence --tools "" --prompt-suggestions false' \
bash <skill-dir>/scripts/review-round.sh brief.md ./review-runs/topic 1 cmd
```

For a plain-text command, a wrapper must extract the provider-reported exact model ID from
its response/runner metadata and write it to the supplied `REVIEW_IDENTITY_FILE` path.
The script exports `REVIEW_MODEL` and that unique path for the invocation. Do not echo the
requested ID or use reviewer self-identification as evidence. JSON metadata is checked
against any sidecar too; disagreement, multiple reviewer models or missing identity fails the round.
Provider-specific options for custom commands belong in that pinned command and receipt.

`REVIEW_TIMEOUT` defaults to 300 seconds. `REVIEW_SCOPE=full` forces a later full three-angle
round; otherwise round 1 is full and later rounds delta. The hard ceiling is five. Before
rounds 4-5 the host must record a concrete serious risk in nonempty `allowance.md`, not a
placeholder; record the extended allowance in the decision receipt. The host judges substance.

## One prompt for both routes

`templates/reviewer-prompt.md` contains common instructions, the FULL and DELTA variants,
and the reply contract. `scripts/review-support.py render <brief.md> <round> [full|delta]`
selects the scope and inlines the brief. Send those bytes verbatim to a fresh native reviewer;
the CLI runner uses exactly the same renderer and saves `rN-prompt.md`. Do not duplicate
or paraphrase the instructions in the brief or another script.

## Receipts and failure

Keep one run directory per decision, including a double check and any failed attempts:

- `rN-brief.md`, `rN-prompt.md`, `rN-review.md`, `rN.log`.
- `rN-attemptA.raw`, `.log`, optional `.identity`: preserved for every attempt.
- `meta.txt`: append-only requested/observed model, identity source, options, scope, status,
  actual verdict and seconds, for successes and failed attempts.
- `reviewer.json`: pinned model/options/command. An authorized exception must be recorded
  by the host before updating this pin; keep all earlier receipts and round count.
- `ledger.md`: host judgments, severity downgrades as rebuttals, and open/disputed findings.

Native runs preserve equivalent fields and raw replies using returned runner model/options.
CLI identity evidence is version-dependent; never replace absent telemetry with a guess.

Exit 0 means a valid reply with matching model identity. Exit 1 writes an ERROR sentinel,
retains rejected raw output in `.invalid` and attempt files, and appends the failure class.
Exit 2 rejects usage, pin changes, retry limits or allowance without running the provider.
A verdict must be one valid standalone VERDICT line plus a FINDINGS section, with exit 0.
A valid review is not necessarily approval: the host must still judge and disclose findings.

There is no automatic retry. Empty/malformed replies with verified identity are recoverable:
one same-model retry at most, logged as another attempt of that round, within existing
allowance/authority. Capacity, quota, rate-limit, transport, timeout, provider unavailable,
configuration or identity failures pause for correction/user direction. Checkpoint draft,
ledger and receipts; report review unavailable and hold the irreversible step. When the user
authorizes resuming, rerun the same round with the same pin and `REVIEW_RESUME=1`; the attempt is
logged with `resume=user` and keeps the round count. Never
silently switch to a different/pricier model, reset the budget, fabricate review or use Fast Mode.

## Keeping reviewers current

Before a new decision, inspect the live provider/runner catalog and select an exact model
ID within authorization/cost limits. Never use floating aliases or implicit CLI defaults.
Update `REVIEW_MODEL` or the native target, run one real round and confirm `meta.txt` has
matching observed identity, `ok` and an actual verdict. Keep that exact model/options for
the decision. Mid-decision refresh requires a recorded authorized exception, not a reset.

## Shared-resource and performance decisions

Containment is not proof: a cap can replace kills with throttling and timeouts. Before
rollout, run a bounded replay with the interactive control plane live and explicit pass
criteria for completion, OOM, PSI, swap, latency and queue wait. Size the limits from those
results. A cap alone does not establish an operational fix.
