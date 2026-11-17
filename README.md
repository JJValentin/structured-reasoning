# Structured Reasoning

An agent skill for making decisions that are expensive to reverse. Works with Claude Code
and any agent that loads `SKILL.md` skills (Codex, OpenCode, Hermes and similar).

It makes your agent follow the same sequence on every real decision: frame the problem,
name the one binding constraint, check what was already decided, challenge assumptions,
generate real options, and, for irreversible calls, pressure-test the draft with an
independent reviewer before committing.

## Two modes

| Mode | When | What happens |
|---|---|---|
| **Fast Mode** | Reversible, cheap to undo | The agent reasons through the 7 steps quietly and gives you the decision |
| **Review Loop** | Irreversible or high-stakes, or you ask for it | A separate reviewer attacks the draft (red team, premise, pre-mortem). The agent fixes or rebuts each finding. Max 3 rounds. You get the real verdict, including anything still open |

The router is one question: *"If this is wrong, how hard is it to walk back?"*

## Install

**Claude Code** (personal skills):

```bash
git clone https://github.com/JJValentin/structured-reasoning ~/.claude/skills/structured-reasoning
```

For a single project, clone into `.claude/skills/structured-reasoning` inside the repo instead.

**Other agents:** put the folder wherever your agent loads skills from. The skill is plain
Markdown; only the optional review script needs a shell.

**Update:** `git -C ~/.claude/skills/structured-reasoning pull`

## Use

It triggers on its own before recommendations and hard-to-undo calls. You can also ask:

- "Help me decide between X and Y"
- "Think this through carefully"
- "Review loop this plan"
- "Double check this" (adds one full review round with a fresh reviewer)

Every run ends with the same contract: DECISION, CONFIDENCE, RATIONALE, REVIEW, NEXT ACTION,
REVIEW TRIGGER, SUCCESS METRICS.

## The review script (optional)

Review Loop needs an independent reviewer. If your agent has a subagent tool, it can use that.
Otherwise `scripts/review-round.sh` runs one round through the
[Codex CLI](https://github.com/openai/codex) or the
[Claude Code CLI](https://docs.claude.com/claude-code):

```bash
cp templates/review-brief.md brief.md   # fill it in
REVIEW_MODEL=<model-id> bash scripts/review-round.sh brief.md ./review-runs/my-decision 1 codex
```

- Reviewer: `codex` (default) or `claude`
- `REVIEW_MODEL`: pin an exact model ID so every round uses the same reviewer (otherwise the CLI default)
- `REVIEW_EFFORT`: codex reasoning effort, default `high`
- `REVIEW_TIMEOUT`: seconds per round, default `300`
- `REVIEW_SCOPE=full`: force a full review on a later round

Each round writes `r<N>-brief.md`, `r<N>-review.md` and a line in `meta.txt`. A failed or
malformed reply is never counted as a review: the script writes an `ERROR` sentinel and exits 1.

## Files

```
SKILL.md                    the skill
scripts/review-round.sh     one review round via codex or claude CLI
templates/review-brief.md   brief template for the reviewer
```

## Contributing

Issues and pull requests welcome. Keep changes small, keep `SKILL.md` tool-agnostic, and
test the script with `bash -n scripts/review-round.sh` plus one real round before opening a PR.

## License

MIT
