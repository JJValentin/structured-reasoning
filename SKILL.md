---
name: structured-reasoning
description: |
  Adaptive reasoning framework for systematic problem-solving. Routes Type 1 (irreversible) vs Type 2 (reversible) decisions, then selects Direct, Light, Deep, Consensus, or Hybrid mode based on task characteristics.
  Use when you need to think through problems, reason systematically, analyze options, make decisions, debug issues, get consensus, or want structured analysis.
  Triggers: "think through", "structured reasoning", "atom of thoughts", "get consensus", "sequential thinking", "reason deeply"
license: MIT
metadata:
  version: 2.3.0
  sources:
    - Sequential Thinking MCP (arben-adm)
    - Atom of Thoughts for Markov LLM Test-Time Scaling (Teng et al., 2025)
    - TerminaI Cognitive Architecture (Prof-Harita, 2025)
    - Joshua's Type 1/Type 2 Decision Framework (PROTOCOLS.md)
    - Quint Code First Principles Framework (m0n0x41d)
    - SAFLA Learning Loop (ruvnet/SAFLA)
    - A-MEM Agentic Memory (agiresearch/A-mem, NeurIPS 2025)
---

# Structured Reasoning

Adaptive framework for systematic problem-solving with 5 reasoning modes:

| Mode | Purpose | Best For |
|------|---------|----------|
| **Direct** | Skip reasoning | Trivial lookups, simple facts |
| **Light** | Fast, linear | Clear problems, time-constrained |
| **Deep** | Rigorous, networked | High-stakes, Type 1 decisions |
| **Consensus** | Parallel advisors | Open-ended, multiple viable paths |
| **Hybrid** | Adaptive escalation | Uncertain complexity |

---

## Quick Start

Simply describe your problem. Claude auto-selects the appropriate mode.

```
User: Should I take this client project?
Claude: [ROUTER] Type 1 (irreversible) → Deep Mode + EA reminder
```

```
User: What content should I create this week?
Claude: [ROUTER] Type 2 (reversible) | Multiple paths → Consensus Mode
```

To force a mode: `sequential thinking`, `atom of thoughts`, `get consensus`

---

## Decision Router (Always First)

**Step 1:** Determine Type 1 or Type 2

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
          +----------+  +-----------------+
          |   DEEP   |  | SELECT BY       |
          |  + EA    |  | CHARACTERISTICS |
          +----------+  +-----------------+
```

### Type 1 Signals (→ Deep Mode)

| Signal | Examples |
|--------|----------|
| Hard to undo | Clients, contracts, major purchases |
| Significant consequences | Partnerships, public positioning |
| Involves others' timelines | External commitments |
| Keywords | "should I", "commit to", "sign", "accept" |

**Protocol:** Always Deep Mode. Include EA reminder: "Sleep on this."

### Type 2 Signals (→ Framework Selection)

| Signal | Examples |
|--------|----------|
| Easy to undo | Content, tool choices, task order |
| Low cost if wrong | Pricing experiments, outreach |
| Keywords | "which", "how to", "what's best", "optimize" |

**Protocol:** Route by characteristics. Bias toward motion.

### Framework Selection (Type 2)

| Task Signal | Mode | Why |
|-------------|------|-----|
| Trivial, single-step | Direct | Skip overhead |
| Clear linear path | Light | Sequential efficient |
| Debugging/diagnosis | Light | Hypothesis → test |
| Multiple viable paths | Consensus | Parallel evaluation |
| High stakes Type 2 | Deep | Need verification |

---

## Triggers

| Trigger | Mode | Use When |
|---------|------|----------|
| `think through this` | Auto | Let router decide |
| `structured reasoning` | Auto | Explicit invocation |
| `just answer` | Direct | Skip reasoning |
| `quick answer` | Direct | Speed priority |
| `sequential thinking` | Light | Linear progression |
| `think step by step` | Light | Simple, time-constrained |
| `walk me through` | Light | Educational |
| `get consensus` | Consensus | Multiple perspectives |
| `evaluate options` | Consensus | Compare paths |
| `what's the best approach` | Consensus | Open-ended |
| `atom of thoughts` | Deep | High-stakes |
| `reason deeply` | Deep | Need verification |
| `decompose this problem` | Deep | Multiple unknowns |
| `Type 1 decision` | Deep + EA | Force irreversible protocol |
| `Type 2 decision` | Router | Force reversible routing |

---

## Quick Reference

```
+----------------+------------------+------------------+------------------+
|    DIRECT      |      LIGHT       |    CONSENSUS     |      DEEP        |
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
+----------------+------------------+------------------+------------------+
| Output:        | Output:          | Output:          | Output:          |
| Answer only    | Stage progress   | Advisor matrix   | Atom network     |
|                | [###____] 60%    | Winner + reason  | Confidence vals  |
+----------------+------------------+------------------+------------------+
```

### Type 1 vs Type 2

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

## Direct Mode

**When:** Trivial questions, simple lookups, no decision required.
**What:** Immediate response without reasoning structure.
**Output:** Direct answer only.

```
User: What's the capital of France?
Claude: Paris.
```

**Escalation:** If complexity emerges, escalate to Light or Consensus.

---

## Light Mode (Sequential Thinking)

**When:** Clear problems, time-constrained, linear cause-effect.
**What:** Progress through 5 stages linearly.
**Output:** Stage-by-stage progress with final recommendation.

| Stage | Purpose |
|-------|---------|
| 1. Problem Definition | Frame the problem, constraints, success criteria |
| 2. Research | Gather facts, identify gaps, note assumptions |
| 3. Analysis | Examine options, trade-offs, risks |
| 4. Synthesis | Combine insights into recommendation |
| 5. Conclusion | Final answer with next steps |

**Progress format:**
```
## [Stage 3/5] ANALYSIS
Progress: [######____] 60%
```

**Escalation:** If 3+ viable options emerge, consider Deep Mode.

→ Full methodology: [references/light-mode.md](references/light-mode.md)

---

## Deep Mode (Atom of Thoughts)

**When:** Type 1 decisions, high stakes, need explicit confidence tracking.
**What:** Build networked thought atoms with dependencies and verification.
**Output:** Atom graph with confidence values and verified conclusion.

| Atom | Symbol | Purpose | Confidence |
|------|--------|---------|------------|
| Premise | P | Given facts, constraints | 0.9-1.0 |
| Reasoning | R | Logical deductions | 0.6-0.9 |
| Hypothesis | H | Proposed solutions | 0.3-0.8 |
| Verification | V | Tests hypotheses | 0.5-0.95 |
| Conclusion | C | Verified recommendations | 0.7-0.95 |

**Termination:** Confidence ≥0.85, max depth 5, or all hypotheses resolved.

**Output format:**
```
## [P1] PREMISE (confidence: 0.95)
The API must handle 10,000 req/s.
Dependencies: none

## [H1] HYPOTHESIS (confidence: 0.70)
12-node cluster provides capacity.
Dependencies: R1

## [C1] CONCLUSION (confidence: 0.85)
Deploy 12-node cluster.
Dependencies: V1, H1
```

→ Full methodology: [references/deep-mode.md](references/deep-mode.md)

---

## Consensus Mode (Parallel Advisors)

**When:** Open-ended Type 2 decisions, multiple viable paths, trade-offs unclear.
**What:** Run 3-5 parallel advisors, compare proposals, select best.
**Output:** Advisor matrix with winner and rationale.

| Advisor | Perspective | Question |
|---------|-------------|----------|
| **Enumerator** | Comprehensive | "What are ALL the ways?" |
| **Pattern Matcher** | Historical | "What worked before?" |
| **First Principles** | Fundamental | "If we started fresh?" |
| **Contrarian** | Challenge | "What if opposite is true?" |
| **Pragmatist** | Execution | "What's fastest to ship?" |

**Output format:**
```
| Advisor | Proposal | Confidence | ICE |
|---------|----------|------------|-----|
| Enumerator | Video series | 0.75 | 21 |
| Pattern Matcher | Twitter thread | 0.80 | 23 |
| Pragmatist | Thread→video | 0.85 | 24 |

Winner: Thread→video (ICE: 24)
```

**Early return:** If any advisor hits 80%+ confidence, can return early.

→ Full methodology: [references/consensus-mode.md](references/consensus-mode.md)

---

## Hybrid Mode

**When:** Uncertain complexity, may need escalation mid-analysis.
**What:** Start Light, escalate to Deep when triggers detected.
**Output:** Transitions from stages to atoms mid-stream.

### Escalation Triggers

| Trigger | Detection | Action |
|---------|-----------|--------|
| Confidence drop | Uncertainty in Synthesis | Escalate to Deep |
| Branch point | Multiple viable paths | Convert to hypotheses |
| Contradiction | Conflicting information | Create verification |
| Complexity spike | Stage unwieldy | Decompose into atoms |
| User request | "go deeper", "verify" | Immediate escalation |

**Transition:** Convert Light Mode findings to atoms:
- Problem Definition → P atoms
- Research → P atoms (facts) + R atoms
- Analysis options → H atoms (competing hypotheses)

→ Full methodology: [references/mode-selection-guide.md](references/mode-selection-guide.md)

---

## Commands

| Command | Action |
|---------|--------|
| `/reset` | Clear session, start fresh |
| `/status` | Show current progress |
| `/route` | Show Decision Router output |
| `/switch direct` | Force Direct Mode |
| `/switch light` | Force Light Mode |
| `/switch consensus` | Force Consensus Mode |
| `/switch deep` | Force Deep Mode |
| `/escalate` | Trigger hybrid escalation |
| `/conclude` | Force conclusion with current evidence |
| `/ice` | Run ICE scoring on options |
| `/ea` | Insert EA reminder |
| `/sr-save` | Save reasoning to knowledge base |
| `/sr-query` | Search past decisions |
| `/sr-context` | Show project context |
| `/sr-load` | Load past decision for reference |
| `/sr-decay` | Check premises for staleness |
| `/sr-init` | Initialize knowledge base in project |
| `/sr-outcome <id> <success\|partial\|failure>` | Record decision outcome |
| `/sr-learn` | Batch update confidences from outcomes |
| `/sr-confidence <id>` | Show confidence history |
| `/sr-evolve` | Trigger memory evolution pass |
| `/sr-hubs` | Show hub memories (5+ references) |

### Status Output

**Light Mode:**
```
Mode: Light (Sequential)
Stage: 3/5 (Analysis)
Progress: [######____] 60%
```

**Deep Mode:**
```
Mode: Deep (Atomic)
Atoms: P:4 R:3 H:2 V:1 C:0
Depth: 2/5
Best hypothesis: H1 (0.78)
```

---

## Validation Checklists

### Light Mode
- [ ] Each stage builds on previous
- [ ] Constraints identified in Problem Definition
- [ ] Analysis examines trade-offs
- [ ] Conclusion is actionable

### Deep Mode
- [ ] All premises have high confidence (>0.85)
- [ ] Reasoning atoms cite dependencies
- [ ] Hypotheses are testable/falsifiable
- [ ] No orphan atoms

### Consensus Mode
- [ ] At least 3 advisors consulted
- [ ] Contrarian perspective addressed
- [ ] Winner has clear rationale

---

## Anti-Patterns

| Avoid | Why | Instead |
|-------|-----|---------|
| Skipping stages (Light) | Incomplete analysis | Progress sequentially |
| Orphan atoms (Deep) | Unconnected reasoning | Ensure dependencies |
| Premature conclusion | Unverified assumptions | Complete verification |
| Over-decomposition | Analysis paralysis | Contract at depth >4 |
| Confidence inflation | False certainty | Be conservative |
| Mode thrashing | Wasted effort | Commit; escalate with trigger |
| Ignoring Contrarian | Miss blind spots | Always address challenges |
| Single hypothesis | Anchoring risk | Generate ≥2 before verifying |
| Skipping bias audit | Blind spots | Run BA before Conclusion |
| Using stale premises | Outdated reasoning | Check `/sr-decay` regularly |

---

## Extension Points

1. **Custom Reasoning Modes**
   - Location: `references/modes/` (create new mode files)
   - Mechanism: Follow Light/Deep mode template structure
   - Use case: Domain-specific reasoning (legal, medical, financial)

2. **Advisor Additions**
   - Location: `references/consensus-mode.md` → The Advisors section
   - Mechanism: Add new advisor following existing pattern
   - Use case: Domain-specific perspectives (technical, business)

3. **MCP Tool Integration**
   - Location: `references/consensus-mode.md` → MCP Tool Integration
   - Mechanism: Map advisor to external tool query
   - Use case: Ground advisors in real-time data

4. **Decision Filter Customization**
   - Location: Decision Router section in SKILL.md
   - Mechanism: Add domain-specific Type 1/Type 2 signals
   - Use case: Adjust reversibility thresholds per context

5. **Persistence Integration**
   - Location: `references/persistence.md`
   - Mechanism: JSON-based knowledge base in `.claude/reasoning/`
   - Use case: Query past decisions, track evidence staleness, audit trail

---

## Integration

This skill connects to related skills for comprehensive agent development:

- **context-engineering** — For understanding context constraints when building SR-enabled agents. Context degradation patterns affect reasoning quality; apply context optimization when SR sessions grow long.
- **evaluation** — For systematic quality measurement of reasoning outputs. Use evaluation rubrics to assess SR decision quality; LLM-as-judge can validate SR conclusions.
- **memory-systems** — For persistent memory beyond SR's built-in knowledge base. Complex agents may need both SR persistence and external memory systems.
- **multi-agent-patterns** — For distributing SR across multiple agents. Coordinator agents can use SR while sub-agents handle isolated subtasks.

---

## References

- [Light Mode Details](references/light-mode.md) - Complete stage guidance
- [Deep Mode Details](references/deep-mode.md) - Atom mechanics, bias audit, staleness
- [Consensus Mode Details](references/consensus-mode.md) - Parallel advisor patterns
- [Mode Selection Guide](references/mode-selection-guide.md) - Decision framework
- [Persistence Layer](references/persistence.md) - Knowledge base and commands
- [Worked Examples](references/worked-examples.md) - Complete walkthroughs

---

## Changelog

### v2.3.0 (Current)
- **SAFLA Learning Loop**: Decisions now track outcomes; confidence propagates through linked memories
- **A-MEM Memory Evolution**: New memories trigger context updates on related existing memories
- **Keyword Auto-Linking**: Jaccard similarity auto-populates `related` arrays (no embeddings required)
- **Hub Detection**: High-connectivity memories (5+ references) surfaced in `/sr-context`
- **Usage-Weighted Staleness**: Frequently-used memories decay slower
- **Optional Forgetful Backend**: Semantic search upgrade available via MCP
- **New Commands**: `/sr-outcome`, `/sr-learn`, `/sr-confidence`, `/sr-evolve`, `/sr-hubs`

### v2.2.0
- **Persistence Layer**: Knowledge base in `.claude/reasoning/` for storing decisions and premises (inspired by Quint Code)
- **Competing Hypotheses**: Deep Mode now requires ≥2 hypotheses before verification (anti-anchoring)
- **Bias Audit (BA)**: New atom type checks for anchoring, confirmation, availability, sunk cost bias
- **Premise Staleness**: Decay tracking with configurable thresholds and warnings
- **Anti-Anchoring Protocol**: Prompts for alternatives when first hypothesis is formed
- **New Commands**: `/sr-save`, `/sr-query`, `/sr-context`, `/sr-load`, `/sr-decay`, `/sr-init`

### v2.1.0
- Optimized SKILL.md to ≤500 lines (Progressive Disclosure Architecture)
- Added Extension Points section
- Enhanced description with trigger keywords
- Moved detailed methodology to references (single source of truth)

### v2.0.0
- Decision Router: Type 1/Type 2 filter runs first
- Direct Mode: Skip reasoning for trivial tasks
- Consensus Mode: Parallel advisors (5 perspectives)
- ICE Integration: Tie-breaker scoring
- EA Integration: Emotional Authority reminder for Type 1
- MCP Tool Integration for advisors

### v1.0.0
- Initial release with Light, Deep, Hybrid modes
