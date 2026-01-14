---
name: structured-reasoning
description: Unified reasoning framework with adaptive framework selection. Routes through Type 1/Type 2 decision filter first, then selects appropriate reasoning mode (Direct, Light, Deep, Consensus, Hybrid) based on task characteristics. Inspired by TerminaI's cognitive architecture.
license: MIT
metadata:
  version: 2.0.0
  sources:
    - Sequential Thinking MCP (arben-adm)
    - Atom of Thoughts for Markov LLM Test-Time Scaling (Teng et al., 2025)
    - TerminaI Cognitive Architecture (Prof-Harita, 2025)
    - Joshua's Type 1/Type 2 Decision Framework (PROTOCOLS.md)
---

# Structured Reasoning

A unified framework for systematic problem-solving with adaptive mode selection:
- **Decision Router**: First determines Type 1 (irreversible) vs Type 2 (reversible)
- **Direct Mode**: Skip reasoning for trivial tasks
- **Light Mode**: Fast, linear, stage-based sequential thinking
- **Deep Mode**: Rigorous, networked reasoning with explicit dependencies and verification
- **Consensus Mode**: Parallel advisors for open-ended problems with multiple viable paths
- **Hybrid Mode**: Start light, escalate to deep when complexity demands

---

## Quick Start

Simply describe your problem. Claude will auto-select the appropriate mode using the Decision Router.

```
User: Should I take this client project?

Claude: [Decision Router: Type 1 (irreversible) → Deep Mode with EA reminder]
```

```
User: What content should I create this week?

Claude: [Decision Router: Type 2 (reversible) + multiple viable paths → Consensus Mode]
```

To force a specific mode, use explicit triggers like `sequential thinking`, `atom of thoughts`, or `get consensus`.

---

## Decision Router (Always First)

Before selecting a reasoning mode, determine the decision type. This integrates with Joshua's Type 1/Type 2 framework.

```
                    PROBLEM ARRIVES
                          |
                          v
              +------------------------+
              |   TYPE 1 or TYPE 2?    |
              +------------------------+
                    |           |
                TYPE 1        TYPE 2
           (Irreversible)   (Reversible)
                    |           |
                    v           v
            +----------+    +------------------+
            |   DEEP   |    | FRAMEWORK SELECT |
            |   MODE   |    | (heuristics)     |
            | + EA     |    +------------------+
            | reminder |        |    |    |    |
            +----------+   Direct Light Cons Deep
```

### Type 1 Signals (→ Deep Mode)

| Signal | Examples |
|--------|----------|
| Hard to undo | Taking clients, signing contracts, major purchases |
| Significant consequences | Partnerships, public positioning, relationship commitments |
| Involves others' timelines | Commitments to external parties |
| High financial stakes | Large investments, pricing locks |
| Keywords | "should I", "commit to", "sign", "accept", "partner with" |

**Type 1 Protocol**: Always use Deep Mode. Include EA (Emotional Authority) reminder: "Sleep on this. Check again across different emotional states."

### Type 2 Signals (→ Framework Selection)

| Signal | Examples |
|--------|----------|
| Easy to undo | Content topics, offer tweaks, task order, tool choices |
| Low cost to be wrong | Pricing experiments, outreach approaches |
| Can iterate quickly | A/B tests, content formats, scheduling |
| Keywords | "which", "how to", "what's best", "optimize", "improve" |

**Type 2 Protocol**: Use heuristics to select framework, then execute. Bias toward motion.

### Framework Selection Heuristics (Type 2 Only)

After confirming Type 2, select framework based on task characteristics:

| Task Signal | Framework | Why |
|-------------|-----------|-----|
| Trivial, single-step | **Direct** | Skip reasoning overhead |
| Clear linear path | **Light** | Sequential stages efficient |
| Debugging/diagnosis | **Light** | Hypothesis → test → iterate |
| Multiple viable paths | **Consensus** | Parallel advisors find best |
| High stakes Type 2 | **Deep** | Need verification |
| Data processing/calculation | **Light + Tools** | Use external tools |

### Heuristic Keywords

```python
# Direct Mode triggers
DIRECT_KEYWORDS = ["what is", "tell me", "show me", "where is", "current time"]

# Light Mode triggers  
LIGHT_KEYWORDS = ["step by step", "walk through", "explain", "how do I"]

# Consensus Mode triggers
CONSENSUS_KEYWORDS = ["best approach", "which option", "compare", "evaluate options", 
                      "multiple ways", "what should I"]

# Deep Mode triggers (Type 2 context)
DEEP_TYPE2_KEYWORDS = ["verify", "confident", "certain", "critical", "important"]

# Debugging/Sequential triggers
DEBUG_KEYWORDS = ["why", "failing", "broken", "error", "debug", "fix", "not working"]
```

### Decision Router Output

When using the Decision Router, briefly state the routing decision:

```
[ROUTER] Type 2 (reversible) | Multiple viable content formats | → Consensus Mode
```

```
[ROUTER] Type 1 (irreversible client decision) | → Deep Mode | EA: Sleep on this
```

---

## Triggers

| Trigger | Mode | Use When |
|---------|------|----------|
| `think through this` | Auto (Router) | Let Claude route based on Type 1/2 + characteristics |
| `structured reasoning` | Auto (Router) | Explicit skill invocation with full routing |
| `just answer` | Direct | Trivial question, skip reasoning |
| `quick answer` | Direct | Speed over thoroughness |
| `sequential thinking` | Light | Want fast linear progression |
| `think step by step` | Light | Simple problems, time-constrained |
| `walk me through` | Light | Educational, sequential |
| `get consensus` | Consensus | Want multiple perspectives compared |
| `evaluate options` | Consensus | Multiple viable paths to compare |
| `what's the best approach` | Consensus | Open-ended with many valid options |
| `atom of thoughts` | Deep | Complex, high-stakes decisions |
| `reason deeply` | Deep | Need verification and confidence |
| `decompose this problem` | Deep | Multiple unknowns, need breakdown |
| `Type 1 decision` | Deep + EA | Force irreversible decision protocol |
| `Type 2 decision` | Router (Type 2) | Force reversible decision routing |

---

## Quick Reference

```
+----------------+------------------+------------------+------------------+
|    DIRECT      |      LIGHT       |    CONSENSUS     |      DEEP        |
|  (Skip Logic)  |   (Sequential)   | (Parallel Eval)  | (Atom Network)   |
+----------------+------------------+------------------+------------------+
| Just answer    | 5 linear stages  | 3-5 advisors     | P/R/H/V/C atoms  |
| No structure   | Problem→Research | run in parallel  | Explicit deps    |
|                | →Analysis→Synth  | Compare outputs  | 0-1 confidence   |
|                | →Conclusion      | Pick best path   | Verification     |
+----------------+------------------+------------------+------------------+
| USE WHEN:      | USE WHEN:        | USE WHEN:        | USE WHEN:        |
| - Trivial Q    | - Clear path     | - Open-ended     | - Type 1 (irrev) |
| - Lookup       | - Time pressure  | - Many options   | - High stakes    |
| - Simple fact  | - Linear flow    | - No clear best  | - Need certainty |
| - "What is X"  | - Debugging      | - Eval tradeoffs | - Complex deps   |
+----------------+------------------+------------------+------------------+
| Output:        | Output:          | Output:          | Output:          |
| Answer only    | Stage progress   | Advisor matrix   | Atom network     |
|                | [###____] 60%    | Winner + reason  | Confidence vals  |
+----------------+------------------+------------------+------------------+
```

### Type 1 vs Type 2 Quick Check

```
TYPE 1 (Irreversible)          TYPE 2 (Reversible)
─────────────────────          ───────────────────
→ Always Deep Mode             → Route by characteristics
→ Include EA reminder          → Bias toward motion
→ Sleep on it                  → ICE score if comparing
─────────────────────          ───────────────────
Clients, contracts,            Content, pricing tests,
partnerships, major            tool choices, outreach,
purchases, commitments         task order, experiments
```

---

## Mode Selection (Auto)

When mode is not explicitly specified, use the Decision Router:

### Step 1: Type Check (Always First)

| Signal | Type | Action |
|--------|------|--------|
| Irreversible consequences | Type 1 | → Deep Mode + EA reminder |
| Reversible/low-stakes | Type 2 | → Continue to Step 2 |

### Step 2: Framework Selection (Type 2 Only)

| Signal | Mode | Rationale |
|--------|------|-----------|
| Trivial lookup/fact | Direct | Skip reasoning overhead |
| "what is", "tell me" | Direct | Simple answer sufficient |
| Clear linear path | Light | No need for complexity |
| Debugging/diagnosis | Light | Hypothesis-test loop |
| Time constraint mentioned | Light | Speed priority |
| Multiple viable options | Consensus | Need parallel evaluation |
| "best approach", "compare" | Consensus | Open-ended comparison |
| High stakes Type 2 | Deep | Need verification |
| "verify", "confident" | Deep | Explicit confidence need |
| Complex dependencies | Deep | Need explicit tracking |
| Contradictory information | Deep | Need verification workflow |

**Default for Type 2**: Light Mode (can escalate via Hybrid if needed)
**Default for Type 1**: Deep Mode (never skip verification)

---

## Direct Mode (Skip Reasoning)

For trivial tasks where structured reasoning adds no value. Just answer.

### When to Use

- Simple lookups ("What is X?")
- Facts you know ("Current time")
- Single-step tasks ("Show me Y")
- No decision required

### Output Format

Just answer the question directly. No stages, no atoms, no structure.

```
User: What's the capital of France?
Claude: Paris.
```

### Escalation to Light

If the "trivial" question reveals complexity, escalate:

```
User: What's the best database?
Claude: [Seems trivial but actually depends on use case → Escalate to Light or Consensus]
```

---

## Light Mode (Sequential Thinking)

Progress through 5 stages linearly. Each stage builds on the previous.

### Stages

| # | Stage | Purpose | Key Questions |
|---|-------|---------|---------------|
| 1 | Problem Definition | Frame the problem | What exactly are we solving? What are constraints? |
| 2 | Research | Gather information | What do we know? What do we need to find out? |
| 3 | Analysis | Examine critically | What patterns emerge? What are the trade-offs? |
| 4 | Synthesis | Combine insights | What solutions emerge? How do pieces fit? |
| 5 | Conclusion | Final answer | What do we recommend? What are next steps? |

### Output Format

```markdown
## [Stage 2/5] RESEARCH
Progress: [####______] 40%

**Tags**: #architecture #performance #scalability
**Axioms Applied**: "Premature optimization is the root of all evil"
**Assumptions Challenged**: "We need real-time updates for all data"

[Stage content here - gathered information, findings, gaps identified]

---
Next: Stage 3 (Analysis) | Thoughts remaining: 3
```

### Adjusting Total Stages

- Can reduce to 3 stages for simple problems (Problem → Analysis → Conclusion)
- Can expand sub-stages if a stage becomes complex (triggers Hybrid escalation)

See: [references/light-mode.md](references/light-mode.md) for detailed guidance.

---

## Deep Mode (Atom of Thoughts)

Build a network of interconnected thought atoms with explicit dependencies and confidence tracking.

### Atom Types

| Type | Symbol | Purpose | Confidence Range |
|------|--------|---------|------------------|
| **Premise** | P | Given facts, constraints, requirements | 0.9-1.0 (known facts) |
| **Reasoning** | R | Logical deductions from other atoms | 0.6-0.9 (derived) |
| **Hypothesis** | H | Proposed solutions, theories | 0.3-0.8 (speculative) |
| **Verification** | V | Tests and validates hypotheses | 0.5-0.95 (evidence-based) |
| **Conclusion** | C | Final verified recommendations | 0.7-0.95 (verified) |

### Output Format

```markdown
## [P1] PREMISE (confidence: 0.95)
The API must handle 10,000 requests per second at peak load.
Dependencies: none

## [P2] PREMISE (confidence: 0.90)
Current infrastructure supports horizontal scaling up to 20 nodes.
Dependencies: none

## [R1] REASONING (confidence: 0.85)
Given P1 and P2, we need ~10 nodes minimum (1k req/s per node baseline).
Dependencies: P1, P2

## [H1] HYPOTHESIS (confidence: 0.70)
A 12-node cluster with load balancer provides adequate capacity with redundancy.
Dependencies: R1

## [V1] VERIFICATION (confidence: 0.80)
Testing H1:
  [PASS] Capacity: 12 x 1000 = 12,000 > 10,000 required
  [PASS] Redundancy: 2 spare nodes (17% buffer)
  [WARN] Assumption: Linear scaling (needs load test validation)
Dependencies: H1

## [C1] CONCLUSION (confidence: 0.75)
Deploy 12-node cluster. Validate scaling assumption in staging before production.
Dependencies: V1, H1

---
Atoms: P:2 R:1 H:1 V:1 C:1 | Depth: 3 | Best confidence: 0.75
```

### Decomposition Rules

When to decompose an atom into sub-atoms:

| Trigger | Action |
|---------|--------|
| Confidence < 0.6 | Break into smaller, more certain sub-atoms |
| Multiple unknowns | Separate into independent sub-problems |
| Conflicting evidence | Create parallel hypothesis branches |
| Atom too complex | Split into atomic (indivisible) pieces |

### Contraction Rules

When to contract sub-atoms back:

| Trigger | Action |
|---------|--------|
| All sub-atoms verified | Contract to parent with averaged confidence |
| Depth > 4 | Force contraction to prevent over-analysis |
| Diminishing returns | Sub-decomposition not adding clarity |

### Termination Conditions

Stop deep reasoning when:
- Conclusion confidence >= 0.85
- Maximum depth reached (default: 5)
- All hypotheses verified or rejected
- User explicitly accepts conclusion

See: [references/deep-mode.md](references/deep-mode.md) for detailed guidance.

---

## Hybrid Mode

Start with Light Mode for efficiency, automatically escalate to Deep Mode when complexity warrants.

### Escalation Triggers

| Trigger | Detection | Action |
|---------|-----------|--------|
| **Confidence Drop** | Uncertainty in Synthesis stage | Escalate unresolved aspects |
| **Branch Point** | Multiple viable paths discovered | Convert to competing hypotheses |
| **Contradiction** | Conflicting information found | Create verification workflow |
| **Complexity Spike** | Stage becoming unwieldy | Decompose into atoms |
| **User Request** | "go deeper", "verify this" | Immediate escalation |

### Transition Process

```
Light Mode: [Problem Definition] → [Research] → [Analysis] → ???
                                                      |
                                          Escalation Trigger Detected
                                                      |
                                                      v
Deep Mode:  Convert Analysis findings to:
            - P atoms (established facts)
            - R atoms (confirmed reasoning)
            - H atoms (unresolved questions become hypotheses)
            
            Continue with verification workflow...
```

### Escalation Output

```markdown
## ESCALATION: Light → Deep Mode

**Trigger**: Multiple viable architectures identified in Analysis stage
**Converting**: 3 options to competing hypotheses for rigorous comparison

### Preserved from Light Mode:
- P1: [From Problem Definition] System must handle 10k req/s
- P2: [From Research] Team has experience with Kubernetes
- R1: [From Analysis] Both monolith and microservices viable

### New Deep Mode Atoms:
- H1: Monolith with vertical scaling
- H2: Microservices with Kubernetes
- H3: Hybrid approach (core monolith + satellite services)

Proceeding with verification of each hypothesis...
```

See: [references/mode-selection-guide.md](references/mode-selection-guide.md) for detailed escalation patterns.

---

## Consensus Mode (Parallel Advisors)

For open-ended Type 2 decisions with multiple viable paths. Inspired by TerminaI's multi-advisor architecture.

### Core Concept

Instead of a single linear analysis, run **3-5 parallel "advisors"** that each propose a solution from different perspectives. Compare outputs and select the best path.

```
                    PROBLEM
                       |
         +-------------+-------------+
         |             |             |
         v             v             v
    [Advisor 1]   [Advisor 2]   [Advisor 3]
    Enumerator    Pattern       Contrarian
         |             |             |
         v             v             v
    [Proposal 1]  [Proposal 2]  [Proposal 3]
         |             |             |
         +-------------+-------------+
                       |
                       v
              [COMPARE & SELECT]
              Highest confidence
              or best ICE score
```

### The Advisors

| Advisor | Perspective | Asks |
|---------|-------------|------|
| **Enumerator** | List all options | "What are ALL the ways we could do this?" |
| **Pattern Matcher** | Match to known solutions | "What worked before in similar situations?" |
| **First Principles** | Build from fundamentals | "If we started from scratch, what would we do?" |
| **Contrarian** | Challenge assumptions | "What if the opposite is true? What are we missing?" |
| **Pragmatist** | Focus on execution | "What's the fastest path to a working solution?" |

### When to Use Consensus

| Signal | Confidence |
|--------|------------|
| "What's the best approach to X?" | High |
| Multiple valid options exist | High |
| Trade-offs aren't clear | High |
| Open-ended creative task | High |
| Single obvious answer | Low (use Direct/Light instead) |
| Need verification/confidence | Low (use Deep instead) |

### Output Format

```markdown
## CONSENSUS MODE: [Problem]

### Advisor Proposals

| Advisor | Proposal | Confidence | Rationale |
|---------|----------|------------|-----------|
| Enumerator | Option A: Video series | 0.75 | 5 formats identified, video has best reach |
| Pattern Matcher | Option B: Twitter thread | 0.80 | Similar topic went viral as thread last month |
| First Principles | Option C: Long-form blog | 0.70 | Core value is depth; blog delivers best |
| Contrarian | Option D: Skip content, DM directly | 0.60 | Content may not be needed; test direct outreach |
| Pragmatist | Option A: Video series | 0.85 | Already have recording setup; fastest to ship |

### Consensus Analysis

**Agreement**: Enumerator and Pragmatist both favor video (convergent signal)
**Dissent**: Contrarian challenges whether content is even the right approach
**High confidence**: Pattern Matcher's thread suggestion (0.80) based on prior evidence

### Recommendation

**Winner**: Twitter thread (Option B)
**ICE Score**: Impact 8 + Confidence 8 + Ease 7 = 23
**Rationale**: Proven format, fast to execute, can repurpose to video later

**Runner-up**: Video series (Plan B if thread underperforms)
```

### Early Return

If any advisor hits **80%+ confidence**, can return early without full comparison:

```
[Advisor: Pattern Matcher] Found exact prior art with 85% match → Early return
```

### Consensus with MCP Tools

When available, advisors can leverage external tools:

| Advisor | MCP Tool | Use |
|---------|----------|-----|
| Pattern Matcher | `linkup-search` | Find similar content that worked |
| Enumerator | `reddit-search` | Discover community preferences |
| First Principles | `youtube-search` | Research audience behavior |
| Contrarian | `dataforseo-trends` | Challenge assumptions with data |

### ICE Scoring (Tie-Breaker)

When advisors are close, use ICE to pick:

| Factor | Question | Score 1-10 |
|--------|----------|------------|
| **Impact** | If this works, how much does it move the needle? | |
| **Confidence** | How sure am I this will work? | |
| **Ease** | How easy is this to execute? | |

Add scores. Highest wins. Don't overthink.

### Escalation to Deep

If consensus reveals high-stakes implications or conflicting evidence that can't be resolved by comparison, escalate to Deep Mode:

```
[ESCALATION] Advisors disagree on fundamental assumption → Deep Mode verification needed
```

See: [references/consensus-mode.md](references/consensus-mode.md) for detailed advisor patterns.

---

## Commands

Control reasoning sessions with inline commands:

| Command | Action | Example |
|---------|--------|---------|
| `/reset` | Clear current session, start fresh | After completing a problem |
| `/status` | Show current progress | Check where you are |
| `/route` | Show Decision Router output | See Type 1/2 + framework |
| `/switch direct` | Force Direct Mode | Just answer, skip reasoning |
| `/switch light` | Force Light Mode | Want faster analysis |
| `/switch consensus` | Force Consensus Mode | Want parallel advisor eval |
| `/switch deep` | Force Deep Mode | Need more rigor |
| `/escalate` | Trigger hybrid escalation | Complexity increased |
| `/conclude` | Force conclusion with current evidence | Time constraint |
| `/ice` | Run ICE scoring on options | Tie-breaker for Type 2 |
| `/ea` | Insert EA reminder | For Type 1 decisions |

### Status Output Example

**Light Mode:**
```
Mode: Light (Sequential)
Stage: 3/5 (Analysis)
Progress: [######____] 60%
Tags used: #performance, #architecture, #cost
```

**Deep Mode:**
```
Mode: Deep (Atomic)
Atoms: P:4 R:3 H:2 V:1 C:0
Depth: 2/5
Confidence range: 0.65-0.95
Best hypothesis: H1 (0.78)
Termination: Not reached (need verification)
```

---

## Validation

### Light Mode Quality Checks

- [ ] Each stage clearly builds on previous
- [ ] Constraints identified in Problem Definition
- [ ] Research addresses knowledge gaps
- [ ] Analysis examines trade-offs
- [ ] Synthesis proposes concrete solutions
- [ ] Conclusion is actionable

### Deep Mode Quality Checks

- [ ] All premises have high confidence (>0.85)
- [ ] Reasoning atoms cite dependencies
- [ ] Hypotheses are testable/falsifiable
- [ ] Verification atoms have clear pass/fail criteria
- [ ] Conclusion confidence justified by verification
- [ ] No orphan atoms (all connected to dependency graph)

### Hybrid Quality Checks

- [ ] Escalation trigger clearly identified
- [ ] Light mode progress preserved as atoms
- [ ] No information lost in transition
- [ ] Deep mode continues from correct state

---

## Anti-Patterns

| Avoid | Why | Instead |
|-------|-----|---------|
| Skipping stages (Light) | Incomplete analysis | Progress sequentially |
| Orphan atoms (Deep) | Unconnected reasoning | Ensure all atoms have dependencies or dependents |
| Premature conclusion | Unverified assumptions | Complete verification before concluding |
| Over-decomposition | Analysis paralysis | Contract when depth > 4 or diminishing returns |
| Confidence inflation | False certainty | Be conservative; prefer 0.7 over 0.9 when uncertain |
| Mode thrashing | Wasted effort | Commit to mode; escalate only with clear trigger |
| Ignoring contradictions | Flawed conclusions | Create verification atoms for conflicts |

---

## Examples

See [references/worked-examples.md](references/worked-examples.md) for complete walkthroughs:

1. **Software Architecture** (Deep Mode) - Designing a caching layer
2. **Debugging** (Hybrid Mode) - Investigating intermittent errors
3. **Business Decision** (Deep Mode) - Build vs buy analysis
4. **General Problem-Solving** (Light Mode) - Planning a team event

---

<details>
<summary><strong>Deep Dive: Light Mode Stages</strong></summary>

### Stage 1: Problem Definition

**Purpose**: Frame the problem clearly before solving.

**Key Activities**:
- State the problem in one clear sentence
- Identify stakeholders and their concerns
- List explicit constraints (time, budget, technical)
- Define success criteria
- Identify what is NOT in scope

**Output Template**:
```
Problem: [One sentence problem statement]
Stakeholders: [Who cares about this?]
Constraints: [What limits our solution space?]
Success looks like: [Measurable outcomes]
Out of scope: [What we're NOT solving]
```

**Common Pitfalls**:
- Jumping to solutions before understanding problem
- Vague problem statements
- Missing key constraints
- Scope creep

### Stage 2: Research

**Purpose**: Gather information needed to analyze the problem.

**Key Activities**:
- List what we already know (facts)
- Identify knowledge gaps
- Gather relevant data/examples
- Consult documentation or prior art
- Note assumptions being made

**Output Template**:
```
Known facts:
- [Fact 1]
- [Fact 2]

Knowledge gaps:
- [Gap 1 - how we'll address it]
- [Gap 2 - acceptable to proceed without?]

Assumptions:
- [Assumption 1 - risk if wrong]
```

### Stage 3: Analysis

**Purpose**: Examine information critically to understand options.

**Key Activities**:
- Identify patterns in research
- List possible approaches
- Analyze trade-offs for each
- Identify risks and mitigations
- Challenge assumptions from Stage 2

**Output Template**:
```
Patterns observed:
- [Pattern 1]

Options identified:
| Option | Pros | Cons | Risk |
|--------|------|------|------|
| A      | ...  | ...  | ...  |
| B      | ...  | ...  | ...  |

Assumptions challenged:
- [Assumption] - [Why it might be wrong]
```

### Stage 4: Synthesis

**Purpose**: Combine insights into coherent solution(s).

**Key Activities**:
- Integrate analysis into recommendation(s)
- Address identified risks
- Consider implementation approach
- Identify dependencies and sequencing
- Prepare for stakeholder concerns

**Output Template**:
```
Recommended approach: [Clear recommendation]

Rationale:
- [Why this over alternatives]

Implementation outline:
1. [Step 1]
2. [Step 2]

Risk mitigations:
- [Risk] → [Mitigation]
```

### Stage 5: Conclusion

**Purpose**: Finalize recommendation with clear next steps.

**Key Activities**:
- State final recommendation clearly
- Summarize key reasoning
- List concrete next steps
- Identify decision points
- Note what would change the recommendation

**Output Template**:
```
RECOMMENDATION: [Clear, actionable statement]

Key reasoning:
- [Point 1]
- [Point 2]

Next steps:
1. [Immediate action]
2. [Follow-up action]

Revisit if:
- [Condition that would change recommendation]
```

</details>

<details>
<summary><strong>Deep Dive: Deep Mode Mechanics</strong></summary>

### Atom Lifecycle

```
Creation → Validation → Connection → [Decomposition] → Verification → [Contraction]
```

1. **Creation**: Define atom with type, content, initial confidence
2. **Validation**: Ensure content is atomic (indivisible) and clear
3. **Connection**: Link to dependencies (other atoms it relies on)
4. **Decomposition** (optional): Break into sub-atoms if too complex
5. **Verification**: For hypotheses, create verification atoms
6. **Contraction** (optional): Merge verified sub-atoms back

### Dependency Notation

```
[R1] depends on P1, P2
     ↓
[R1] REASONING (confidence: 0.85)
Given the constraints in P1 and capabilities in P2...
Dependencies: P1, P2
```

**Rules**:
- Premises (P) typically have no dependencies (they're given)
- Reasoning (R) depends on premises or other reasoning
- Hypotheses (H) depend on reasoning
- Verification (V) depends on the hypothesis being tested
- Conclusions (C) depend on verified hypotheses

### Confidence Calibration

| Confidence | Meaning | When to Use |
|------------|---------|-------------|
| 0.95-1.0 | Certain | Verified facts, mathematical truths |
| 0.85-0.94 | High | Strong evidence, expert consensus |
| 0.70-0.84 | Moderate | Good reasoning, some assumptions |
| 0.50-0.69 | Low | Speculation, limited evidence |
| 0.30-0.49 | Very Low | Guesses, needs verification |
| < 0.30 | Unreliable | Should not base decisions on |

**Confidence Propagation**:
- Derived atoms can't exceed confidence of weakest dependency
- `R1.confidence <= min(P1.confidence, P2.confidence)`
- Verification can increase hypothesis confidence (if passes)
- Verification can decrease hypothesis confidence (if fails)

### Decomposition Decision Tree

```
Is atom confidence < 0.6?
├── Yes → Can it be split into independent parts?
│   ├── Yes → Decompose into sub-atoms
│   └── No → Gather more evidence (research)
└── No → Is atom too complex to verify?
    ├── Yes → Decompose into verifiable pieces
    └── No → Proceed with current atom
```

### Contraction Mechanics

When sub-atoms are verified, contract back to parent:

```
Parent: H1 (confidence: 0.60, decomposed)
  └── H1.1 (confidence: 0.85, verified)
  └── H1.2 (confidence: 0.80, verified)
  └── H1.3 (confidence: 0.75, verified)

Contraction:
H1.confidence = average(H1.1, H1.2, H1.3) = 0.80
H1.status = verified (all sub-atoms verified)
```

### Termination Algorithm

```python
def should_terminate():
    # Check for high-confidence conclusion
    conclusions = [a for a in atoms if a.type == 'conclusion']
    if any(c.confidence >= 0.85 for c in conclusions):
        return True, "High-confidence conclusion reached"
    
    # Check for maximum depth
    if current_depth >= max_depth:
        return True, "Maximum depth reached"
    
    # Check for all hypotheses resolved
    hypotheses = [a for a in atoms if a.type == 'hypothesis']
    if all(h.verified or h.rejected for h in hypotheses):
        return True, "All hypotheses resolved"
    
    return False, "Continue reasoning"
```

</details>

<details>
<summary><strong>Deep Dive: Hybrid Escalation</strong></summary>

### When to Escalate

**Automatic Triggers** (Claude detects):

1. **Confidence Uncertainty**
   - In Synthesis stage, can't commit to single solution
   - Multiple options with similar merit
   - "It depends" feeling

2. **Information Conflict**
   - Research findings contradict each other
   - Stakeholder requirements conflict
   - Trade-offs are complex

3. **Complexity Explosion**
   - Single stage generating too much content
   - Nested sub-problems emerging
   - Can't hold full picture in linear flow

**Manual Triggers** (User requests):
- "Can you verify that?"
- "I need more confidence"
- "Go deeper on this"
- "What are the trade-offs?"
- `/escalate` command

### Escalation Process

**Step 1: Preserve Progress**
```
Light Mode Progress:
- Stage 1 (Problem Definition) → Convert to P atoms
- Stage 2 (Research) → Convert to P atoms (facts) + R atoms (analysis)
- Stage 3 (Analysis) → Convert to R atoms + H atoms (options)
```

**Step 2: Identify Escalation Point**
```
Escalation triggered in: Analysis
Reason: 3 viable options, can't differentiate without verification
```

**Step 3: Convert to Atoms**
```
FROM Light Mode:
- Problem: "Need caching solution for API"
- Research: "Redis and Memcached both viable"
- Analysis: "Redis has persistence, Memcached simpler"

TO Deep Mode:
[P1] API requires caching for 10k req/s (0.95)
[P2] Team has Redis experience (0.90)
[P3] Team has no Memcached experience (0.90)
[R1] Both Redis and Memcached can handle load (0.85) ← P1
[H1] Use Redis for persistence + familiarity (0.70) ← R1, P2
[H2] Use Memcached for simplicity (0.60) ← R1
```

**Step 4: Continue in Deep Mode**
```
[V1] Verify H1:
  [PASS] Performance: Redis handles 100k ops/s
  [PASS] Team familiarity: 3/4 devs know Redis
  [PASS] Persistence: Needed for session data
  Confidence: 0.85

[V2] Verify H2:
  [FAIL] Team familiarity: Learning curve
  [PASS] Simplicity: Fewer features to configure
  Confidence: 0.55

[C1] Recommend Redis (0.85) ← V1, H1
```

### De-escalation (Rare)

Can return to Light Mode if:
- Deep Mode reveals problem is simpler than thought
- Single hypothesis clearly dominates
- Time constraint requires faster conclusion

```
De-escalation:
- Deep Mode showed H1 clearly superior (0.90 vs 0.55)
- Returning to Light Mode for Synthesis and Conclusion
- Carrying forward: "Use Redis" as established fact
```

</details>

---

## References

- [Light Mode Details](references/light-mode.md) - Complete stage guidance
- [Deep Mode Details](references/deep-mode.md) - Atom mechanics and patterns
- [Consensus Mode Details](references/consensus-mode.md) - Parallel advisor patterns
- [Mode Selection Guide](references/mode-selection-guide.md) - Decision framework
- [Worked Examples](references/worked-examples.md) - Complete walkthroughs

---

## Changelog

### v2.0.0 (Current)
- **Decision Router**: Type 1/Type 2 filter runs first, routes to appropriate framework
- **Direct Mode**: Skip reasoning for trivial tasks
- **Consensus Mode**: Parallel advisors (Enumerator, Pattern Matcher, First Principles, Contrarian, Pragmatist)
- **ICE Integration**: Tie-breaker scoring for Type 2 decisions
- **EA Integration**: Emotional Authority reminder for Type 1 decisions
- **MCP Tool Integration**: Advisors can leverage external tools when available
- Updated triggers and commands
- Framework selection heuristics based on TerminaI cognitive architecture

### v1.0.0
- Initial release
- Light Mode (Sequential Thinking)
- Deep Mode (Atom of Thoughts)
- Hybrid Mode with escalation
- Session commands
- Four worked examples
