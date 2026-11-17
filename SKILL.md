---
name: structured-reasoning
description: Use when a consequential decision needs reasoning or review.
license: MIT
metadata:
  version: 3.0.0
  tags: [reasoning, decisions, review-loop, type-1, theory-of-constraints]
---

# Structured Reasoning

## Mode

Use before consequential recommendations/cards, hard-to-undo calls or choices risking over
a day of rework; also requests to decide, compare, think carefully, get a second opinion or
double check an artifact. Skip lookups, casual conversation and trivial choices.

Test reversibility, then stakes. Cheap to reverse: **Fast Mode**, decide solo; show the
recommendation plus one line that you reasoned it through, not seven steps. Irreversible OR
high stakes if wrong OR explicit review-loop request: **Review Loop**. Unsure? Ask: "If
wrong, how hard is this to walk back?" Hard means Review Loop.

## The Loop

1. **Frame.** State success, hard constraints and failure.
   Done when: the decisive failure is named.
2. **Constraint.** Name ONE bottleneck; existential factors override other improvements.
   Input drought: inputs stopped, raise them. Conversion: inputs fine, diagnose process before
   adding volume. For dropped outcomes inspect leading inputs 1-2+ weeks back before quality.
   Discard options not moving this constraint.
   Done when: constraint named/typed in one sentence.
3. **Context.** Recall durable memory. Label prior items settled/provisional. When asked to
   check all options or challenged on the premise, reset options before research; examples
   are not settled decisions.
   Done when: prior decisions checked/labelled.
4. **First principles.** Challenge 1-3 load-bearing assumptions, including the constraint.
   Restructuring must address the named symptom. Offer a cheap baseline/side-by-side cause
   test; if declined or samples unavailable, proceed within authority and use the user's
   review of first outputs as the check.
   Done when: an unverifiable assumption is named.
5. **Options.** Generate 2-4 real alternatives, not strawmen; state how each moves the
   constraint and its simplest workable path.
   Done when: at least two options survive.
6. **Pressure-test.** Fast Mode: pick the simplest option meeting constraints. Review Loop:
   use the procedure below.
   Done when: leading option faced strongest counterargument.
7. **Record.** Produce the output contract; persist decision, rationale and review receipt
   in durable memory.
   Done when: decision/evidence are retrievable.

## Review Loop

The host decides and judges findings; the reviewer attacks. Decision review, code review
and requested panels are separate; none requires switching model families.

### Reviewer and allowance

- One reviewer: strongest reasoning model within authorization/cost limits. Prefer another
  family when available within those limits; one provider works equally well. Independence:
  **separate fresh context each round**, even on the host's model. Reviewer cannot delegate.
- Pin exact model ID/options throughout. Never resume a reviewer; carry the ledger. Record
  authorized selection exceptions/reasons. Difficulty does not authorize a pricier model;
  risk raises checks or allowance.
- **3 rounds per decision; 5 only after recording a concrete serious risk** in `allowance.md`
  and the receipt: irreversible money, legal/contract, security/auth, data loss or public
  reputation. Ceiling, not quota. Model/run-directory changes never reset the count.
- Round 1: FULL red team, premise, pre-mortem in order, then other serious issues.
  Round 2+: DELTA revised decision, ledger and open findings; mark every prior finding
  RESOLVED / NOT RESOLVED, then new problems the revision created.
- **Double check**: one FULL fresh round (`REVIEW_SCOPE=full`), same receipt/model/allowance.
  No room: report exhaustion, never reset/exceed five.

### Run, judge, repeat

1. Fill `templates/review-brief.md`: frame, constraint, options, settled decisions, draft pick,
   3-4 pointed questions, inline artifact. Label departures as requiring user approval.
   Done when: draft and evidence are inlined.
2. `templates/reviewer-prompt.md` owns both scopes. Native route: send rendered bytes verbatim
   to a fresh reviewer; verify model/options from runner metadata, not self-identification.
   CLI: Python 3 plus selected CLI:
   ```sh
   python3 <skill-dir>/scripts/review-support.py render brief.md 1
   REVIEW_MODEL=<exact-id> bash <skill-dir>/scripts/review-round.sh brief.md ./review-runs/topic 1 codex
   ```
   Before every round read `templates/reviewer-runbook.md`: adapters, identity and receipt.
   Done when: valid reply/verified identity/options recorded.
3. Append every finding and host judgment to `ledger.md`:
   `F<n> | severity | finding | FIXED (change) / REBUTTED (evidence) / DECLINED (nit)`.
   BLOCKER: wrong/seriously harmful and hard to undo. SERIOUS: gap changing the plan.
   NIT: preference, decline. Upgrades allowed; downgrades rebut the reviewer's severity and
   must be recorded. Fix minimally or push back with evidence; avoid scope growth.
   Done when: every finding judged; disputes visibly open.
4. If serious findings remain or text changed, send the revised draft, frame/constraint in
   two lines, ledger and open findings to the next fresh context, same model. Done means
   reviewer accepted **current text**: AGREE or only NITs, no open BLOCKER/SERIOUS. Later
   changes need another round or are **UNVERIFIED**. Exhaustion is not approval; escalate.
   Done when: current text accepted or UNVERIFIED with open serious findings escalated.
5. Disclose `Review: rounds N/3 (or N/5, risk: ...), reviewer <observed model>, final verdict
   <actual>, rebutted: F.., open: F..`. Rank up to three open BLOCKER/SERIOUS and consequences,
   plus "N more in ledger.md". Preserve raw replies and disputed objections.
   Done when: receipt disclosed/saved; post-review edits labelled.

### Failure and refresh

Classify first: one same-model retry for recoverable empty/malformed replies only, within
authority/allowance. Capacity, quota, rate-limit, transport, timeout or provider
unavailable: checkpoint and pause. Identity/configuration failures also pause for correction. Resume only on the user's go, same
pinned reviewer and round (`REVIEW_RESUME=1`), recorded in the receipt.
Never switch automatically. Report review **unavailable** and hold the irreversible step;
never silently use Fast Mode, skip, fabricate approval or reset rounds. The runbook covers
ERROR/`.invalid` receipts and refreshing exact IDs against the live catalog before new decisions.

## Output contract (end with this)

- **DECISION:** clear statement
- **CONFIDENCE:** High / Medium / Low
- **RATIONALE:** why; name rebutted findings
- **REVIEW:** actual receipt, Review Loop only
- **NEXT ACTION:** specific first step
- **REVIEW TRIGGER:** condition/date reopening this
- **SUCCESS METRICS:** how to know it worked

## Common pitfalls

1. Cheap reversible call: Fast Mode unless review requested.
2. No draft: include draft, settled choices, approval-labelled departures and questions.
3. Obeying all findings: judge, fix minimally, rebut with evidence, decline nits.
4. Full review each round: delta except requested double check.
5. Hidden dissatisfaction: disclose actual verdict and disputes.
6. No memory: recall first; save decision, rationale and receipt.
7. Containment mistaken for proof: before shared-resource/performance rollout, run the
   bounded replay and operational pass criteria in `templates/reviewer-runbook.md`.
8. Fabricated review: disclose ERROR and hold the irreversible step.
9. Anchoring: compare all relevant options/formats before designing.
10. Default panels: get breadth with a fresh full double check, same ledger.

## Verification checklist

- [ ] Mode correct; ONE typed constraint; prior context/assumptions/options checked
- [ ] Brief complete; model/options pinned; fresh contexts; identity/exceptions recorded
- [ ] All findings judged; downgrades rebutted; disputes/open serious findings disclosed
- [ ] Scope/risk/allowance/count correct; current text accepted or UNVERIFIED
- [ ] Failure/retry/switch rules met; unavailable review holds irreversible step
- [ ] Actual verdict/changes disclosed; output complete; decision/rationale/receipt saved
