---
name: structured-reasoning
description: Multi-mode structured reasoning with GPT-5.2 thinker for Type 1 decision validation
metadata: {"clawdbot":{"always":true,"emoji":"🧠"}}
---

# Structured Reasoning Skill

Use this skill for complex decisions, especially Type 1 irreversible decisions.

## The Engineering Flywheel for Decisions

All structured reasoning follows the 8-phase Engineering Flywheel:

### Phase 1: Problem Framing (Requirements)
Define the decision through clear requirements:
- **What is the success criteria?** (the outcome, not the solution)
- **What are the hard constraints?** (time, money, reversibility, dependencies)
- **What does "done" look like?** (specific, testable)
- **What would failure look like?** (to avoid)

**Output:** Clear decision objective with measurable success criteria

### Phase 2: Context Gathering (AS-IS State)
Map the current state:
- Read relevant files, data, prior decisions (memory_search)
- Understand what currently exists and WHY
- Gather market/competitor/customer context
- Review constraints and dependencies

**Output:** Complete picture of current reality

### Phase 3: First Principles (Deconstruct)
Break down to fundamentals:

1. **Identify assumptions** - List everything being assumed. Challenge each one.
   - "Why do we believe this?"
   - "Is this actually true, or just conventional wisdom?"
   - "What if the opposite were true?"

2. **Find bedrock truths** - What do we KNOW to be true?
   - Separate facts from interpretations
   - Separate data from narratives
   - Identify what's measurable vs. opinion

3. **Expose the real problem** - Why does this decision need to be made?
   - "What problem are we actually solving?"
   - "Why does this problem exist?"
   - "What's wasteful in the current approach?"

4. **Build up from basics** - Don't reason by analogy
   - Build from first principles ("given these truths, what logically follows?")
   - Question "best practices" - they're someone else's solution

**Output:**
- Assumptions challenged: [list]
- Bedrock truths: [list]
- Real problem: [statement]
- Waste identified: [what's unnecessary]

### Phase 4: Creative Synthesis (TO-BE Solution)
Generate options from first principles:
- Build 2-4 options from fundamentals (not by analogy)
- Each option should honor constraints and truths
- Design the simplest path for each option
- Don't constrain to "how it's usually done"

**Output:** 2-4 viable options with rationale

### Phase 5: Validation & Delete (Prune + Validate)
Test options and prune complexity:
- Does each option actually meet requirements?
- What can we delete and still succeed?
- Which option is simplest while meeting all constraints?
- **Spawn @thinker for Type 1 decisions** (see Thinker Integration)

**Output:** Pruned options + thinker validation (if Type 1)

### Phase 6: Execute (Decision)
Make the call:
- DECISION: Clear statement
- CONFIDENCE: High/Medium/Low
- RATIONALE: Why this option (reference flywheel phases)

### Phase 7: Review (Verification)
Set review criteria:
- NEXT ACTION: Specific first step
- REVIEW TRIGGER: When to revisit this decision
- SUCCESS METRICS: How we'll know if it worked

### Phase 8: Update Memory
Capture learnings:
- Update MEMORY.md with decision and rationale
- Log to daily notes
- Document pattern for future similar decisions

---

## The Flywheel for Decisions

```
Problem Framing → Context Gathering → First Principles → Creative Synthesis
        ↓                                                         ↓
Update Memory ← Review ← Execute ← Validation & Delete (+ Thinker for Type 1)
```

All decisions flow through 8 phases. Depth varies by mode.

## Auto-Trigger Conditions

Automatically invoke this skill when:
- Type 1 decisions: contracts, partnerships, major purchases, architecture choices
- Multi-factor analysis: comparing options with tradeoffs
- Debugging: something failed and the cause is not obvious
- Strategy/planning: business decisions, offer architecture, campaign planning
- Disagreement or conflict: weighing competing perspectives

Do NOT use for: simple factual questions, quick tasks, low-stakes Type 2 decisions, casual conversation.

## Thinker Model

The thinker alias maps to openai-codex/gpt-5.2 with extended thinking enabled.
Use it for consensus validation on Type 1 decisions.

## Reasoning Modes

All modes follow the 8-phase flywheel. The mode determines depth and thinker usage.

### 1. Light Mode - Quick Flywheel
For medium-complexity, reversible decisions (Type 2). 2-3 minutes.

**Compressed flywheel:**
1. Problem Framing: 1-2 sentence decision statement
2. Context Gathering: Quick memory_search or file check
3. First Principles: Challenge 1-2 key assumptions
4. Creative Synthesis: Generate 2-3 options
5. Validation & Delete: Pick simplest option that works
6. Execute: State decision
7. Review: Set next action
8. Update Memory: Quick note to daily log

**Skip thinker for Type 2 - decide today.**

### 2. Deep Mode - Full Flywheel + Thinker
For Type 1 irreversible decisions. 5-10 minutes.

**Full 8-phase flywheel:**
- Run all phases completely (no shortcuts)
- Phase 5 (Validation): Spawn @thinker for consensus validation
- Synthesize thinker feedback before Phase 6 (Execute)

**Thinker spawn pattern:**
```javascript
sessions_spawn({
  task: "Validate this Type 1 decision. SITUATION: [summary]. MY RECOMMENDATION: [choice and rationale]. Challenge this: 1. What am I missing? 2. Strongest counter-argument? 3. Agree or disagree and why? 4. Blind spots?",
  model: "thinker",
  thinking: "high",
  label: "thinker-validation"
})
```

**After thinker responds:** Synthesize with your analysis, then proceed to Phase 6.

### 3. Consensus Mode - Extended Flywheel
For highest-stakes Type 1 decisions:
- Architecture decisions that lock you in
- Pricing or positioning that affects revenue
- Contracts or partnerships

**Full flywheel with extended validation:**
- Phases 1-4: Standard
- Phase 5: Spawn @thinker with FULL context (all 8 phases so far)
- Request thinker to run their own flywheel independently
- Compare results, resolve conflicts
- Phase 6-8: Proceed with consensus decision

## Decision Framework

**Reversibility test:**
- **YES (Type 2):** Light Mode - compressed flywheel, decide today, no thinker
- **NO (Type 1):** Deep Mode - full flywheel + thinker validation
  - **Highest stakes:** Consensus Mode - thinker runs independent flywheel

**Complexity test:**
- Simple/obvious → Skip structured reasoning entirely
- Medium complexity → Light Mode
- Complex with tradeoffs → Deep Mode
- Irreversible + high stakes → Consensus Mode

## Thinker Integration (Phase 5: Validation)

The thinker model (GPT-5.2) provides external validation during Phase 5:
- **Consensus validation:** Second opinion on Type 1 decisions
- **Blind spot detection:** Catches things Opus might miss
- **Devil's advocate:** Argues against your position
- **Sanity check:** Validates reasoning is sound
- **Independent flywheel:** Can run full 8-phase independently (Consensus Mode)

**When to spawn thinker:**
- Type 1 decisions: MANDATORY (Deep Mode or Consensus Mode)
- Type 2 decisions: SKIP (decide faster without thinker)

**Spawn pattern (Deep Mode):**
```javascript
sessions_spawn({
  task: "Validate this Type 1 decision. SITUATION: [summary]. MY RECOMMENDATION: [choice and rationale]. Challenge this: 1. What am I missing? 2. Strongest counter-argument? 3. Agree or disagree and why? 4. Blind spots?",
  model: "thinker",
  thinking: "high",
  label: "thinker-validation"
})
```

**Spawn pattern (Consensus Mode):**
```javascript
sessions_spawn({
  task: "Run your own independent Engineering Flywheel on this decision: [full context from phases 1-4]. Provide: 1. Your Problem Framing 2. Your First Principles analysis 3. Your options 4. Your recommendation 5. Where you disagree with my approach",
  model: "thinker",
  thinking: "high",
  label: "thinker-consensus"
})
```

## Output Format

Always end structured reasoning with flywheel outputs:

### Phase 6: Execute (Decision)
**DECISION:** [Clear statement]
**CONFIDENCE:** High/Medium/Low
**RATIONALE:** [Why this option - reference flywheel phases]

### Phase 7: Review (Verification)
**NEXT ACTION:** [Specific first step]
**REVIEW TRIGGER:** [When to revisit this decision]
**SUCCESS METRICS:** [How we'll know if it worked]

### Phase 8: Update Memory
Log decision to:
- `MEMORY.md` (if significant pattern/learning)
- `memory/YYYY-MM-DD.md` (all decisions)
- Relevant project/skill docs (if workflow changed)
