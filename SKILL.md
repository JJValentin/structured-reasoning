---
name: structured-reasoning
description: >-
  Use before any decision card, recommendation, or hard-to-undo call. Fast Mode
  (reversible, decide solo, silent) or Review Loop (irreversible or "sol loop": one
  independent Sol reviewer by default, bounded rounds, host judges every finding). Load
  proactively; triggers live in work-loop. Not for lookups or small reversible choices.
version: 3.0.0
author: Hermes Agent
license: MIT
platforms: [linux]
metadata:
  timelessness_score: 8
  hermes:
    tags: [reasoning, decisions, review-loop, sol-loop, delegation, type-1]
    related_skills: [delegation-routing, search-first, work-loop, coding-delegation]
---

# Structured Reasoning

A decision discipline for calls that are expensive to reverse. It forces the same
useful sequence every time: frame the real problem, gather context from memory,
challenge assumptions, generate real options, and for irreversible calls, pressure-test
the draft in a bounded adversarial review loop before committing.

## When to Use

**Be proactive (Joshua, 2026-10-15).** Don't wait to be asked. The triggers live in
`work-loop` (3. Decide), which is auto-loaded in every profile: before a
decision card, before a hard-to-undo call, when he asks you to decide, and when choosing
between approaches where the wrong one costs more than a day of rework.

- "Help me decide" / "what should I choose" on something with real stakes
- Type 1 decisions: contracts, partnerships, pricing/positioning lock-in, architecture, major spend
- "Compare these options" / "weigh the tradeoffs" with genuine tension
- "Think through this carefully" / "give me a second opinion" / "sol loop this"
- "Double check this" on a consequential artifact before it is wired in or shipped (a rule
  doc, a cut list, a plan): Review Loop on the artifact itself, with your response to any new
  input from the requester as the draft recommendation

Don't use for: factual lookups, low-stakes reversible choices, casual conversation,
or anything where the answer is obvious. If reversing the decision is cheap and fast,
skip the review and just decide.

## Route: which mode

Apply the **reversibility test** first, then the **stakes test**.

- **Reversible, cheap to undo** -> Fast Mode. Decide solo, today. Silent: the user sees the
  decision card or recommendation it produced, plus one line saying you reasoned it through,
  never the seven steps.
- **Irreversible OR high-stakes-if-wrong** -> Review Loop Mode.
- **Joshua says "sol loop"** -> Review Loop Mode, whatever the stakes.

When unsure, ask one question: "if this is wrong, how hard is it to walk back?"
Hard to walk back = Review Loop.

## The Loop (both modes run this; Review Loop mode adds the reviewer at step 6)

1. **Frame.** State success in one line, the hard constraints, and what failure looks like.
   Done when: you can name the single thing that would make this a mistake.
2. **Constraint check (Theory of Constraints, added 2026-08-15).** Before generating options,
   name the ONE binding constraint the decision must relieve: the bottleneck that makes every
   other improvement an illusion until it moves. Discipline from the `constraint-picker` skill:
   ONE constraint, not three, not two; existential factors override everything; distinguish
   input drought (inputs stopped, raise them) from conversion problem (inputs fine, process
   broken, diagnose before adding volume); when an outcome dropped, look 1-2+ weeks back at the
   leading inputs before blaming quality. Options that don't act on the named constraint are
   decoration. Done when: the constraint is written in one sentence and typed
   (input drought / conversion problem / existential).
3. **Gather context.** Pull prior decisions and relevant facts from durable memory before
   reasoning from scratch: `gbrain_recall(entity=...)` and/or `gbrain_query(...)`. Separate
   a settled decision from a provisional example or an option the requester now asks you to
   re-evaluate. When they say "check all options" or otherwise challenge the premise, reset
   the option set before researching or recommending; do not optimize the most recently
   mentioned format by default. Done when: you've checked whether this was decided or discussed
   before, and labelled each prior item as settled or provisional.
4. **First principles.** Challenge 1-3 load-bearing assumptions, including your constraint
   pick from step 2. Build up from what's actually true, not from analogy or default. Done
   when: you've named at least one assumption you can't verify.
   For a rework or restructure, check that the plan acts on the symptom the requester actually
   named; a plan that reorganizes everything except that symptom is betting on an untested
   cause. Offer a cheap test of the cause (a small baseline or side-by-side) before the rebuild;
   if the requester declines or lacks the history to supply samples, proceed and let their
   review of the first real outputs be the check.
5. **Options.** Generate 2-4 real options from the fundamentals (not one option plus strawmen).
   Each must state how it moves the named constraint.
   For each, the simplest path that could work. Done when: at least two options survive a first cut.
6. **Pressure-test.** Fast Mode: prune to the simplest option that meets the constraints.
   Review Loop Mode: run the loop (below). Done when: you have a leading option AND you've
   heard the strongest case against it.
7. **Decide + record.** Produce the output contract below, then persist the decision, its
   rationale and the review receipt to memory: `gbrain_put_page(...)` (or
   `gbrain_add_timeline_entry` on the relevant page).
   Done when: the decision is written where future-you will find it.

## Review Loop Mode (the Sol Loop, for decisions)

This is strategic decision/plan review, not Theo's code `sol-loop`. Both use bounded
adversarial review, but this skill owns decision verdicts and its own receipt; code review
runs Theo's unmodified `sol-loop` with the letter's settings. Neither workflow requires a
model-family switch. Theo's 3-provider `council` is separate, run only when Joshua asks.

The host does NOT delegate the decision. The reviewer attacks; the host judges every finding,
fixes with the smallest change or pushes back with evidence, and writes the final call.

### Rules

- **One independent reviewer at a time: `sol` (GPT-6.1 Sol, high) by default**, whether
  the host is Opus or GPT/Sol. Independence means a separate review context, not a different
  model family. Keep the reviewer model across rounds and carry the findings ledger; in T3,
  each round is a fresh `delegate_task`, never a continued child thread. The reviewer may not
  launch subagents or other reviewers. Opus main chat/strategy remains normal. Opus review
  needs Joshua's explicit selection or a concrete design/taste or observed Sol diagnostic
  limit within authority (`work-loop` Models); prefer a bounded consult
  followed by Sol review. Security/high risk affects checks/allowance, not model family;
  there is no mandatory Opus closing round. Fable/Astra still require Joshua's approval.
- **Round 1 is full.** The reviewer covers three angles in order: red team (strongest case
  the draft is wrong), premise (right question, constraint, options), pre-mortem (it failed in
  90 days: why). Then anything else serious.
- **Round 2+ is delta only:** the revised decision, the findings ledger, open findings. Each
  prior finding gets RESOLVED / NOT RESOLVED; then any new problem the revision created.
- **Severity:** BLOCKER (wrong or seriously harmful and hard to undo), SERIOUS (material gap
  that would change the plan), NIT (decline it). Severity is the reviewer's label. You may
  upgrade it; a downgrade is a rebuttal and must be recorded as one.
- **Budget: 3 rounds per decision, 5 only after recording a concrete serious risk** (large or
  irreversible money, legal/contract, security/auth, data loss, public reputation). A ceiling,
  not a quota.
- **Done means the reviewer accepted the CURRENT revision:** its last round on the current text
  returned AGREE, or only NITs remain, with no open BLOCKER/SERIOUS. If you change the decision
  after the reviewer's last word, that change needs another round. Budget spent before that =
  the revision is **UNVERIFIED** and goes to Joshua as such.
  **Exhaustion never means approval:** open BLOCKER/SERIOUS findings go to Joshua.
- **Disclose the actual verdict.** Never report approval the reviewer didn't give, and never
  hide a finding you rebutted that the reviewer still disputes.
- **"Double check" from Joshua** adds one FULL three-angle round on the current decision by a
  fresh independent Sol reviewer unless he explicitly selected another authorized model
  (run with `REVIEW_SCOPE=full`). A fresh reviewer limited to the delta could not challenge the original
  blind spots. It is one extra round recorded in the same receipt, never a silent budget reset.

### Run it

1. Write the round-1 brief (steps 1-5 of the Loop, the named constraint, the decisions already
   settled, and your **draft recommendation** so the reviewer has something to attack). Inline
   any artifact under review; the reviewer is a fresh CLI context and cannot read your files.
2. In T3, use a fresh T3 `delegate_task` per round, an explicit live Sol target and the
   round brief plus ledger; verify the returned model/options and preserve the same receipt
   fields below. Outside T3, use the script for one round:
   ```
   RUN=~/.hermes/reports/review-loop/$(date +%F)-<topic>
   bash ~/.hermes/skills-shared/structured-reasoning/scripts/review-round.sh <brief.md> "$RUN" 1 sol
   ```
   It writes `r1-brief.md`, `r1-review.md`, and appends a line to `meta.txt` (reviewer, model,
   status, verdict, seconds). The reply shape lives in the script; don't restate it in the brief.
3. **Judge each finding** and append to `$RUN/ledger.md`:
   `F<n> | severity | finding | FIXED (the change) | REBUTTED (evidence) | DECLINED (nit)`.
   Make the smallest justified change. Push back when the finding is wrong; don't expand scope.
4. If any BLOCKER/SERIOUS is open, or you changed the decision, write the round-N brief:
   frame and constraint in two lines, the revised decision, the ledger, the open findings.
   Repeat step 2's route: inside T3, a fresh `delegate_task` on Sol with the revised brief
   and ledger; outside T3, `review-round.sh <rN-brief.md> "$RUN" N sol`. Repeat 3-4 until
   the reviewer has accepted the current revision or the budget is spent.
5. **Write the receipt** into the decision record and to Joshua:
   `Review: Sol Loop, rounds N/3, reviewer <model from meta.txt>, final verdict <actual>,
   rebutted: F.., open: F..`. Up to 3 open BLOCKER/SERIOUS findings, ranked, one-line
   consequence each, plus "N more in ledger.md". Shorten what he reads, never what you disclose.
   Any change made after the last round is labelled **UNVERIFIED**.

If a round FAILS (script exits 1: timeout, error exit, empty or malformed reply), classify
it first. For a recoverable non-availability error, at most one same-model retry is allowed
within the existing authority and recorded allowance. Capacity, quota, rate-limit, transport
or provider unavailability means preserve the draft/checkpoint and pause; do not switch to
Opus or another model automatically. Review is **unavailable**, not skipped: tell Joshua and
hold the irreversible step until he decides. Never fall back to Fast Mode silently, reset
rounds or fabricate a review.

**Keeping the reviewers current.** Model IDs are pinned in `scripts/review-round.sh`. Never use
bare CLI aliases: `fable` and `opus` silently float to the newest release. To refresh, check
the live catalog (`~/.codex/models_cache.json`, T3 `orchestrator_capabilities`, or
`claude -p --model <id> --output-format json` and read `modelUsage`), update the IDs, run one
round, and confirm `meta.txt` shows ok. One-run override: `SOL_MODEL=... OPUS_MODEL=...`.

## Output Contract (always end with this)

- **DECISION:** clear statement
- **CONFIDENCE:** High / Medium / Low
- **RATIONALE:** why, referencing the loop; in Review Loop mode, name each finding you rebutted
- **REVIEW:** the receipt line (Review Loop mode only)
- **NEXT ACTION:** the specific first step
- **REVIEW TRIGGER:** the condition or date that reopens this
- **SUCCESS METRICS:** how you'll know it worked

## Common Pitfalls

1. **Running the loop on a reversible call.** Run the reversibility test first; cheap-to-undo
   goes Fast, unless Joshua said "sol loop".
2. **No draft pick in the brief.** Without one the reviewer just restates the options. Include
   your draft, the decisions already settled (so it attacks the plan, not settled choices), and
   3-4 pointed questions. If your draft departs from a settled decision, label it a departure
   Joshua must approve, not execution.
3. **Treating every finding as mandatory.** You judge. Fix the valid ones minimally, rebut the
   wrong ones with evidence, decline nits. Rubber-stamping the reviewer is as bad as ignoring it.
4. **Re-reviewing everything each round.** Later rounds are delta only. A full re-review burns
   the budget and invites the reviewer to reopen settled points.
5. **Hiding the reviewer's dissatisfaction.** Report the actual last verdict. Theo added
   verdict disclosure because his implementing agent sometimes buried the reviewer's objections.
6. **Skipping memory.** Steps 3 and 7 exist so decisions compound. Recall before deciding,
   persist the decision and receipt after.
7. **Equating containment with a proven operational fix.** For shared-resource or performance
   decisions, a cap can convert kills into throttling and timeouts. Require a bounded pre-rollout
   replay with the interactive control plane live, explicit completion, OOM, PSI, swap, latency
   and queue-wait pass criteria, then size the limits from its result.
8. **Fabricating a review on failure.** If the review file holds the ERROR sentinel, say so.
9. **Treating a format as selected because it was recently mentioned.** When a requester asks
   for a re-evaluation, generate and compare the full relevant format set before designing the
   content inside one format. Otherwise research becomes post-hoc justification for an anchor.
10. **Bringing back the parallel panel.** Retired 2026-10-15 by Joshua. If you need more
   breadth, that is the "double check" round with a fresh independent reviewer, normally
   Sol, not three simultaneous voices or an automatic family switch.

## Verification Checklist

- [ ] Ran the reversibility test and picked the right mode
- [ ] Named and typed the ONE binding constraint (step 2)
- [ ] Pulled prior context from gbrain before reasoning (step 3)
- [ ] Review Loop: brief had framing, constraint, options, settled decisions, AND a draft pick
- [ ] Review Loop: independent Sol reviewer by default regardless of host family; same reviewer model, fresh T3 task and ledger each round; any exception justified within authority
- [ ] Review Loop: every finding in `ledger.md` as fixed / rebutted / declined
- [ ] Review Loop: rounds 2+ were delta only; done = reviewer accepted the current revision (or budget spent and marked UNVERIFIED)
- [ ] Review Loop: a failed review was reported as unavailable and the irreversible step held
- [ ] Review Loop: receipt with actual verdict and open findings given to Joshua; post-review changes marked UNVERIFIED
- [ ] Output contract present and complete
- [ ] Decision + rationale + receipt persisted to gbrain (step 7)
