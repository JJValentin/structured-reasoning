# Structured Reasoning

A decision discipline for agent skills (Claude Code, Hermes, Codex). Version 3.0.0.

It forces the same sequence on any call that is expensive to reverse: frame the problem,
name the one binding constraint, pull prior context from memory, challenge assumptions,
generate real options, and for irreversible calls, pressure-test the draft in a bounded
adversarial review loop before committing.

## Modes

- **Fast Mode**: reversible, cheap-to-undo calls. Decide solo; the user sees the decision, not the steps.
- **Review Loop Mode** (the "Sol Loop"): irreversible or high-stakes calls, or when asked to "sol loop" something.
  One independent reviewer at a time, round 1 full (red team, premise, pre-mortem), rounds 2+ delta only,
  3-round budget (5 with a recorded serious risk). The host judges every finding; the reviewer never decides.

Route with the reversibility test: "if this is wrong, how hard is it to walk back?"

## The Loop

1. Frame
2. Constraint check (Theory of Constraints: one binding constraint, typed)
3. Gather context from durable memory
4. First principles
5. Options (2-4 real ones)
6. Pressure-test (prune in Fast Mode; review loop in Review Loop Mode)
7. Decide + record

Every run ends with the output contract: DECISION, CONFIDENCE, RATIONALE, REVIEW, NEXT ACTION,
REVIEW TRIGGER, SUCCESS METRICS.

## Files

- `SKILL.md`: the skill
- `scripts/review-round.sh`: runs one review round via the `codex` or `claude` CLI, validates the
  verdict, and writes `r<N>-brief.md`, `r<N>-review.md` and `meta.txt` into a run directory

```
bash scripts/review-round.sh <brief.md> <run-dir> <round> [sol|opus|fable]
```

Model IDs are pinned in the script; override with `SOL_MODEL`, `OPUS_MODEL`, `FABLE_MODEL`.

## Install

Copy this folder into your skills directory (for Claude Code: `~/.claude/skills/structured-reasoning/`).

## Changes in 3.0.0

- Replaced the Light / Deep / Consensus / Hybrid modes and the parallel advisor panel with
  Fast Mode and a single-reviewer Review Loop.
- Added the Theory of Constraints step and the findings ledger with severity rules.
- Added `scripts/review-round.sh`; removed the v2 `references/` docs.

## License

MIT
