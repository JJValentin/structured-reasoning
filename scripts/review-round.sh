#!/usr/bin/env bash
# review-round.sh: run ONE round of the adversarial review loop (Sol Loop) on a decision brief.
# Same contract as the OpenCode bounded review loop: one reviewer at a time, no subagents,
# round 1 full, later rounds delta-only, host judges every finding.
#
# Usage:  review-round.sh <brief.md> <run-dir> <round-number> [sol|opus|fable]
#   brief.md:  round 1 = full decision brief with draft pick.
#              round 2+ = revised decision + findings ledger + open findings only.
#   run-dir:   durable dir for this decision, e.g. ~/.hermes/reports/review-loop/<date>-<topic>
#   reviewer:  default sol for either Claude or GPT hosts; independence is a fresh context.
#              opus needs an authorized design/diagnostic exception or explicit selection;
#              fable needs Joshua's approval. No automatic family switch or Opus closing.
#              A failed/unavailable round never authorizes a model fallback.
#   REVIEW_SCOPE=full forces a full three-angle review on a later round (the double-check round).
# Exit: 0 = valid review; 1 = invalid/failed round (ERROR sentinel written, raw reply kept as
#       r<N>-review.md.invalid); 2 = usage error.
# Output: <run-dir>/r<N>-brief.md, r<N>-review.md, r<N>.log; appends to <run-dir>/meta.txt.
# Prints the review file path on the last line. A failed call writes an ERROR sentinel.
#
# Pinned model IDs (updated 2026-10-15). Never use bare CLI aliases: 'fable'/'opus' float to
# the newest release silently. Override with SOL_MODEL / OPUS_MODEL / FABLE_MODEL.

set -uo pipefail

BRIEF="${1:?usage: review-round.sh <brief.md> <run-dir> <round> [sol|opus|fable]}"
RUN="${2:?run-dir required}"
N="${3:?round number required}"
WHO="${4:-sol}"
[ -f "$BRIEF" ] || { echo "brief not found: $BRIEF" >&2; exit 2; }
case "$N" in ''|*[!0-9]*) echo "round must be a number" >&2; exit 2;; esac
[ "$N" -le 5 ] || { echo "round $N exceeds the hard ceiling of 5" >&2; exit 2; }

SOL_MODEL="${SOL_MODEL:-gpt-6.1-sol}"
SOL_EFFORT="${SOL_EFFORT:-high}"
OPUS_MODEL="${OPUS_MODEL:-claude-opus-5-5}"
FABLE_MODEL="${FABLE_MODEL:-claude-fable-5-1}"
TIMEOUT="${REVIEW_TIMEOUT:-300}"

mkdir -p "$RUN"
cp "$BRIEF" "$RUN/r$N-brief.md"
OUTF="$RUN/r$N-review.md"
LOGF="$RUN/r$N.log"

if [ "$N" -eq 1 ] || [ "${REVIEW_SCOPE:-}" = "full" ]; then
  SCOPE=$'FULL REVIEW of the current decision. Attack it from three angles, in this order:\n- Red team: the strongest case that the draft recommendation is wrong.\n- Premise: is this the right question, the right binding constraint, the right option set?\n- Pre-mortem: assume it was adopted and failed 90 days later; the most likely failure path and what would have caught it early.\nThen flag any other serious issue you see.'
else
  SCOPE=$'ROUND '"$N"$' (delta only). Review ONLY the revised decision, the findings ledger and the open findings. For each prior finding: RESOLVED or NOT RESOLVED, one line. Then flag any new BLOCKER or SERIOUS problem the revision itself created. Do not reopen findings marked resolved, and do not re-review unchanged parts.'
fi

PROMPT=$'You are the single independent reviewer in a bounded adversarial review loop for a decision. Do not rubber-stamp. Do not launch subagents, tools that call other models, or your own reviewers. Do not expand the decision\'s scope; recommend the smallest change that fixes each problem.\n\nSeverity:\n- BLOCKER: the decision is wrong, or it causes serious harm that cannot easily be undone.\n- SERIOUS: a material gap that would change the plan if fixed.\n- NIT: wording or preference. Label it NIT; the host will decline it.\nUnsupported assertions cannot be BLOCKER or SERIOUS.\n\n'"$SCOPE"$'\n\nReply under 400 words, in this shape:\nVERDICT: AGREE | AGREE-WITH-CHANGES | DISAGREE\nFINDINGS: one per line as  F<n> [BLOCKER|SERIOUS|NIT] finding -> concrete fix  (round 2+: prior findings by their ID first)\nONE-LINE RECOMMENDATION:\n\nBrief follows:\n\n'

t0=$(date +%s)
rm -f "$OUTF"   # never let a stale review from an earlier attempt count as this one
case "$WHO" in
  sol)
    MODEL="$SOL_MODEL effort=$SOL_EFFORT"
    { printf '%s' "$PROMPT"; cat "$BRIEF"; } \
      | timeout "$TIMEOUT" codex exec -m "$SOL_MODEL" -c model_reasoning_effort="\"$SOL_EFFORT\"" \
          --skip-git-repo-check -o "$OUTF" - >"$LOGF" 2>&1
    RC=$? ;;
  opus)
    MODEL="$OPUS_MODEL"
    { printf '%s' "$PROMPT"; cat "$BRIEF"; } \
      | timeout "$TIMEOUT" claude -p --model "$OPUS_MODEL" >"$OUTF" 2>"$LOGF"
    RC=$? ;;
  fable)
    MODEL="$FABLE_MODEL"
    { printf '%s' "$PROMPT"; cat "$BRIEF"; } \
      | timeout "$TIMEOUT" claude -p --model "$FABLE_MODEL" >"$OUTF" 2>"$LOGF"
    RC=$? ;;
  *) echo "unknown reviewer: $WHO (sol|opus|fable)" >&2; exit 2 ;;
esac
SECS=$(( $(date +%s) - t0 ))

# A round counts only if the call exited 0 AND the reply has a valid verdict and a findings section.
VERDICT=$(grep -m1 -o -E 'VERDICT:?\**:? *\**(AGREE-WITH-CHANGES|AGREE|DISAGREE)' "$OUTF" 2>/dev/null \
  | grep -o -E 'AGREE-WITH-CHANGES|AGREE|DISAGREE' || true)
REASON=""
if [ "$RC" -ne 0 ]; then REASON="exit=$RC"
elif [ ! -s "$OUTF" ]; then REASON="empty output"
elif [ -z "$VERDICT" ]; then REASON="no valid VERDICT line"
elif ! grep -q -i 'FINDINGS' "$OUTF"; then REASON="no FINDINGS section"
fi

if [ -n "$REASON" ]; then
  [ -s "$OUTF" ] && mv "$OUTF" "$OUTF.invalid"
  echo "ERROR: $WHO round $N invalid ($REASON); see $LOGF" > "$OUTF"
  echo "r$N | $(date +%F' '%T) | reviewer=$WHO model=$MODEL | FAILED ($REASON) | verdict=none | ${SECS}s" >> "$RUN/meta.txt"
  echo "$OUTF"
  exit 1
fi

echo "r$N | $(date +%F' '%T) | reviewer=$WHO model=$MODEL | ok | verdict=$VERDICT | ${SECS}s" >> "$RUN/meta.txt"
echo "$OUTF"
