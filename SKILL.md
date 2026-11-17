---
name: structured-reasoning
description: >-
  Use before making a recommendation, presenting a decision, or committing to a
  hard-to-undo call. Fast Mode for reversible choices (decide solo, quietly); Review
  Loop for irreversible or high-stakes ones (one independent reviewer, bounded rounds,
  the host judges every finding). Not for lookups or small reversible choices.
version: 3.0.0
license: MIT
metadata:
  tags: [reasoning, decisions, review-loop, type-1, theory-of-constraints]
---

# Structured Reasoning

A decision discipline for calls that are expensive to reverse. It forces the same
useful sequence every time: frame the real problem, name the binding constraint, gather
prior context, challenge assumptions, generate real options, and for irreversible calls,
pressure-test the draft in a bounded adversarial review loop before committing.

## When to Use

Be proactive. Don't wait to be asked. Use it:

- Before presenting the user with a decision or recommendation that has real stakes
- Before a hard-to-undo call: contracts, partnerships, pricing or positioning lock-in,
  architecture, major spend, deletions, migrations
- When the user asks you to decide, compare options, or weigh tradeoffs with genuine tension
- When choosing between approaches where the wrong one costs more than a day of rework
- When the user says "think this through carefully", "second opinion", "review loop this",
  or "double check this" on a consequential artifact (a plan, a spec, a rule doc)

Don't use it for factual lookups, low-stakes reversible choices, casual conversation, or
anything where the answer is obvious. If reversing the decision is cheap and fast, skip
the review and just decide.

## Route: which mode

Apply the **reversibility test** first, then the **stakes test**.

- **Reversible, cheap to undo** -> Fast Mode. Decide solo. Quiet: the user sees the
  decision or recommendation, plus one line saying you reasoned it through, never the
  seven steps.
- **Irreversible OR high-stakes-if-wrong** -> Review Loop Mode.
- **The user asks for a review loop** -> Review Loop Mode, whatever the stakes.

When unsure, ask one question: "if this is wrong, how hard is it to walk back?"
Hard to walk back = Review Loop.

## The Loop (both modes; Review Loop adds the reviewer at step 6)

1. **Frame.** State success in one line, the hard constraints, and what failure looks like.
   Done when: you can name the single thing that would make this a mistake.
2. **Constraint check (Theory of Constraints).** Before generating options, name the ONE
   binding constraint the decision must relieve: the bottleneck that makes every other
   improvement an illusion until it moves. One constraint, not three. Existential factors
   (cash runway, legal exposure, health) override everything. Distinguish an **input
   drought** (inputs stopped: raise them) from a **conversion problem** (inputs fine, the
   process is broken: diagnose before adding volume). When an outcome dropped, look one to
   two weeks back at the leading inputs before blaming quality. Options that don't act on
   the named constraint are decoration.
   Done when: the constraint is one sentence and typed (input drought / conversion / existential).
3. **Gather context.** Check whatever durable memory you have (notes, decision logs, project
   docs, prior conversations, a memory tool) for prior decisions and relevant facts before
   reasoning from scratch. Separate a settled decision from a provisional example or an
   option the user now wants re-evaluated. When they say "check all options" or challenge
   the premise, reset the option set; don't optimize the most recently mentioned option by default.
   Done when: you've checked whether this was decided before, and labelled each prior item
   settled or provisional.
4. **First principles.** Challenge 1-3 load-bearing assumptions, including your constraint
   pick from step 2. Build up from what's actually true, not from analogy or default.
   For a rework or restructure, check that the plan acts on the symptom the user actually
   named; a plan that reorganizes everything except that symptom is betting on an untested
   cause. Offer a cheap test of the cause before the rebuild.
   Done when: you've named at least one assumption you can't verify.
5. **Options.** Generate 2-4 real options (not one option plus strawmen). Each states how
   it moves the named constraint, and the simplest path that could work.
   Done when: at least two options survive a first cut.
6. **Pressure-test.** Fast Mode: prune to the simplest option that meets the constraints.
   Review Loop Mode: run the loop below.
   Done when: you have a leading option AND you've heard the strongest case against it.
7. **Decide and record.** Produce the output contract below, then persist the decision, its
   rationale and any review receipt wherever durable memory lives for this user or project.
   Done when: the decision is written where a future session will find it.

## Review Loop Mode

The host does NOT delegate the decision. The reviewer attacks; the host judges every
finding, fixes with the smallest change or pushes back with evidence, and writes the final call.

### Rules

- **One independent reviewer at a time.** Independence means a separate, fresh context
  (a subagent, a second CLI, another model). A different model family helps but is not
  required. Keep the same reviewer model across rounds and carry the findings ledger. The
  reviewer may not launch its own subagents or reviewers.
- **Round 1 is full.** The reviewer covers three angles in order: red team (strongest case
  the draft is wrong), premise (right question, constraint, options), pre-mortem (it was
  adopted and failed in 90 days: why). Then anything else serious.
- **Round 2+ is delta only:** the revised decision, the findings ledger, the open findings.
  Each prior finding gets RESOLVED / NOT RESOLVED; then any new problem the revision created.
- **Severity:** BLOCKER (wrong, or seriously harmful and hard to undo), SERIOUS (material gap
  that would change the plan), NIT (decline it). You may upgrade a severity; a downgrade is a
  rebuttal and must be recorded as one.
- **Budget: 3 rounds per decision, 5 only after recording a concrete serious risk** (large or
  irreversible money, legal, security, data loss, public reputation). A ceiling, not a quota.
- **Done means the reviewer accepted the CURRENT revision:** its last round on the current
  text returned AGREE, or only NITs remain. If you change the decision after the reviewer's
  last word, that change needs another round or is labelled **UNVERIFIED**.
  **Running out of budget never means approval:** open BLOCKER/SERIOUS findings go to the user.
- **Disclose the actual verdict.** Never report approval the reviewer didn't give, and never
  hide a finding you rebutted that the reviewer still disputes.
- **"Double check"** from the user adds one FULL three-angle round on the current decision by
  a fresh reviewer (`REVIEW_SCOPE=full` with the script). A reviewer limited to the delta
  could not challenge the original blind spots. Record it in the same receipt.

### Run it

1. Write the round-1 brief from `templates/review-brief.md`: framing, the named constraint,
   options, decisions already settled, and your **draft recommendation** so the reviewer has
   something to attack. Inline any artifact under review; the reviewer is a fresh context
   and cannot see your files or conversation.
2. Run one round with whatever independent reviewer your environment offers:
   - **A subagent tool** (for example Claude Code's Agent/Task tool): spawn a fresh subagent
     per round with the reviewer prompt from `scripts/review-round.sh` plus the brief.
   - **The bundled script** (needs the `codex` or `claude` CLI):
     ```
     RUN=./review-runs/$(date +%F)-<topic>
     bash <skill-dir>/scripts/review-round.sh brief.md "$RUN" 1 codex
     ```
     It writes `r1-brief.md`, `r1-review.md` and a line in `meta.txt` (reviewer, model,
     status, verdict, seconds). The reply shape lives in the script.
3. **Judge each finding** and append it to `$RUN/ledger.md`:
   `F<n> | severity | finding | FIXED (the change) | REBUTTED (evidence) | DECLINED (nit)`.
   Make the smallest justified change. Push back when a finding is wrong; don't expand scope.
4. If any BLOCKER/SERIOUS is open, or you changed the decision, write the round-N brief:
   frame and constraint in two lines, the revised decision, the ledger, the open findings.
   Run the next round with the same reviewer. Repeat 3-4 until the reviewer accepts the
   current revision or the budget is spent.
5. **Write the receipt** into the decision record and to the user:
   `Review: rounds N/3, reviewer <model>, final verdict <actual>, rebutted: F.., open: F..`.
   Up to 3 open BLOCKER/SERIOUS findings, ranked, one-line consequence each, plus
   "N more in ledger.md". Shorten what they read, never what you disclose.

If a round fails (timeout, error, empty or malformed reply), retry once with the same
reviewer at most. If it still fails, review is **unavailable**, not skipped: tell the user
and hold the irreversible step until they decide. Never fall back to Fast Mode silently,
reset the round count, or fabricate a review.

## Output Contract (always end with this)

- **DECISION:** clear statement
- **CONFIDENCE:** High / Medium / Low
- **RATIONALE:** why, referencing the loop; in Review Loop mode, name each finding you rebutted
- **REVIEW:** the receipt line (Review Loop mode only)
- **NEXT ACTION:** the specific first step
- **REVIEW TRIGGER:** the condition or date that reopens this
- **SUCCESS METRICS:** how you'll know it worked

## Common Pitfalls

1. **Running the loop on a reversible call.** Run the reversibility test first.
2. **No draft pick in the brief.** Without one the reviewer just restates the options. Include
   your draft, the settled decisions (so it attacks the plan, not settled choices), and 3-4
   pointed questions. If your draft departs from a settled decision, label it a departure the
   user must approve.
3. **Treating every finding as mandatory.** You judge. Fix the valid ones minimally, rebut the
   wrong ones with evidence, decline nits. Rubber-stamping is as bad as ignoring.
4. **Re-reviewing everything each round.** Later rounds are delta only, or the reviewer reopens
   settled points and burns the budget.
5. **Hiding the reviewer's dissatisfaction.** Report the actual last verdict.
6. **Skipping memory.** Steps 3 and 7 exist so decisions compound.
7. **Equating containment with a fix.** A cap or limit can turn a failure into a slowdown
   without fixing it. Define pass criteria and test before rollout.
8. **Fabricating a review on failure.** If the review file holds the ERROR sentinel, say so.
9. **Anchoring on the last-mentioned option.** When asked to re-evaluate, compare the full
   option set before designing inside one option.
10. **Running a parallel panel by default.** Several simultaneous reviewers produce noise and
    split the ledger. For more breadth, run a "double check" round with a fresh reviewer.

## Verification Checklist

- [ ] Ran the reversibility test and picked the right mode
- [ ] Named and typed the ONE binding constraint (step 2)
- [ ] Checked prior context before reasoning (step 3)
- [ ] Review Loop: brief had framing, constraint, options, settled decisions, AND a draft pick
- [ ] Review Loop: one independent reviewer, same model, fresh context each round
- [ ] Review Loop: every finding in `ledger.md` as fixed / rebutted / declined
- [ ] Review Loop: rounds 2+ were delta only; done = reviewer accepted the current revision
- [ ] Review Loop: a failed review was reported as unavailable and the irreversible step held
- [ ] Review Loop: receipt with the actual verdict and open findings given to the user
- [ ] Output contract present and complete
- [ ] Decision and rationale persisted (step 7)
