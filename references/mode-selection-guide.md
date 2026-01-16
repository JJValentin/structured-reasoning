# Mode Selection Guide

How to choose between Direct, Light, Consensus, Deep, and Hybrid modes using the Decision Router.

---

## Decision Router Flowchart (v2.0)

**Always start with the Type check:**

```
                        START
                          |
                          v
            +---------------------------+
            |    TYPE 1 or TYPE 2?      |
            | (Irreversible/Reversible) |
            +---------------------------+
                    |           |
                 TYPE 1      TYPE 2
             (Irreversible) (Reversible)
                    |           |
                    v           v
            +----------+    +------------------+
            | DEEP     |    | Is it trivial?   |
            | MODE     |    | (single lookup)  |
            | + EA     |    +------------------+
            | reminder |        |          |
            +----------+       YES         NO
                                |          |
                                v          v
                          +---------+  +------------------+
                          | DIRECT  |  | Multiple viable  |
                          | MODE    |  | paths/options?   |
                          +---------+  +------------------+
                                           |          |
                                          YES         NO
                                           |          |
                                           v          v
                                    +-----------+  +---------+
                                    | CONSENSUS |  | LIGHT   |
                                    | MODE      |  | MODE    |
                                    +-----------+  | (Hybrid)|
                                                   +---------+
```

---

## Type 1 vs Type 2 Quick Reference

| Type 1 (Irreversible) | Type 2 (Reversible) |
|-----------------------|---------------------|
| Hard to undo | Easy to undo |
| Significant consequences | Low cost if wrong |
| Taking clients | Content topics |
| Signing contracts | Offer tweaks |
| Major partnerships | Task order |
| Big purchases | Tool choices |
| Relationship commitments | Pricing experiments |
| Public positioning | Outreach approaches |
| **-> Always Deep Mode** | **-> Route by characteristics** |
| **-> Include EA reminder** | **-> Bias toward motion** |

---

## Problem Characteristic Checklist

Score each characteristic, then sum for recommendation.

| Characteristic | Light (+1) | Deep (+1) |
|---------------|------------|-----------|
| Problem clarity | Well-defined | Ambiguous |
| Solution space | Limited options | Many options |
| Stakes | Standard | High/critical |
| Dependencies | Linear | Networked |
| Verification need | Implicit OK | Explicit required |
| Time constraint | Tight | Flexible |
| Confidence need | Standard | High certainty |
| Prior knowledge | Good understanding | Limited/uncertain |

**Scoring**:
- Light score 5+ : Use Light Mode
- Deep score 5+ : Use Deep Mode
- Scores within 2 : Use Hybrid (start Light, escalate if needed)

---

## Decision Matrix (v2.0)

| Situation | Type | Mode | Rationale |
|-----------|------|------|-----------|
| "What is X?" | 2 | Direct | Simple lookup |
| "Quick question about X" | 2 | Light | Speed priority |
| "How should we architect Y?" | 1 | Deep | High stakes, irreversible |
| "Debug this error" | 2 | Light/Hybrid | Start simple, escalate if complex |
| "Explain concept Z" | 2 | Light | Educational, linear flow |
| "Should we build or buy?" | 1 | Deep | Major decision, needs verification |
| "Should I take this client?" | 1 | Deep + EA | Irreversible commitment |
| "What content should I create?" | 2 | Consensus | Multiple viable options |
| "Best approach to X?" | 2 | Consensus | Open-ended, many paths |
| "Compare these options" | 2 | Consensus | Parallel evaluation needed |
| "Plan project timeline" | 2 | Light | Sequential by nature |
| "Root cause analysis" | 2 | Light (sequential) | Hypothesis-test loop |
| "Code review findings" | 2 | Light | Structured walkthrough |
| "Security assessment" | 1 | Deep | High stakes, needs confidence |
| "Meeting agenda" | 2 | Direct | Simple organization |
| "Which tool should I use?" | 2 | Consensus | Trade-offs to compare |

---

## Mode Comparison (v2.0)

### Strengths

| Direct | Light | Consensus | Deep |
|--------|-------|-----------|------|
| Instant | Fast | Comprehensive | Rigorous |
| No overhead | Intuitive | Multiple perspectives | Explicit confidence |
| Simple | Linear | Finds best option | Traceable logic |
| | Natural | Prevents blind spots | Handles ambiguity |
| | Easy to follow | Good for trade-offs | Good for verification |

### Weaknesses

| Direct | Light | Consensus | Deep |
|--------|-------|-----------|------|
| No reasoning | Can miss complexity | More overhead | Higher overhead |
| No verification | Implicit assumptions | Can't verify | Slower execution |
| May be wrong | Single path focus | Needs comparison | Can over-analyze |
| | May need restart | Not for Type 1 | More verbose |

### Best Use Cases

| Direct | Light | Consensus | Deep |
|--------|-------|-----------|------|
| Trivial lookups | Clear problems | Open-ended T2 | Type 1 decisions |
| Simple facts | Time-sensitive | Multiple options | High stakes |
| "What is X" | Debugging | Trade-off analysis | Need confidence |
| | Sequential | "Best approach?" | Complex deps |
| | Explanations | Comparisons | Verification |

---

## Hybrid Mode Patterns

### Pattern 1: Explore Then Commit

```
Light Mode: [Problem] -> [Research] -> [Analysis]
                                        |
                          Complexity detected
                                        |
                                        v
Deep Mode:              [Convert to atoms]
                        [Form hypotheses]
                        [Verify]
                        [Conclude]
```

**Use when**: Problem seems simple but reveals complexity during analysis.

### Pattern 2: Verify Critical Assumption

```
Light Mode: [Problem] -> [Research] -> [Analysis] -> [Synthesis]
                            |
               Critical assumption identified
                            |
                            v
Deep Mode:    [Create hypothesis from assumption]
              [Verify hypothesis]
              [Return to Light with result]
                            |
                            v
Light Mode:                        -> [Conclusion]
```

**Use when**: Most reasoning is straightforward but one assumption is risky.

### Pattern 3: Compare Options

```
Light Mode: [Problem] -> [Research] -> [Analysis: 3 options found]
                                              |
                          Can't differentiate without rigor
                                              |
                                              v
Deep Mode:              [H1: Option A]  [H2: Option B]  [H3: Option C]
                              |              |              |
                            [V1]           [V2]           [V3]
                              |              |              |
                              +------+-------+
                                     |
                                     v
                               [C1: Best option]
```

**Use when**: Analysis produces multiple viable options that need rigorous comparison.

---

## Escalation Triggers

### Automatic (Claude detects)

| Trigger | Signal | Response |
|---------|--------|----------|
| Uncertainty spike | "I'm not sure", "it depends" | Offer escalation |
| Multiple viable paths | 3+ options with similar merit | Suggest Deep |
| Contradiction found | Evidence conflicts | Escalate for verification |
| High-risk assumption | "Assuming X..." where X is critical | Escalate to verify |
| Complexity explosion | Stage producing 2+ pages | Decompose |

### Manual (User requests)

| Phrase | Interpretation | Action |
|--------|----------------|--------|
| "Go deeper" | Want more rigor | Escalate current aspect |
| "Verify that" | Need confidence | Create V atom |
| "How confident?" | Explicit confidence need | Switch to Deep |
| "What if X is wrong?" | Assumption challenge | Test as hypothesis |
| `/escalate` | Explicit command | Full escalation |

---

## De-escalation (Rare)

### When to De-escalate

| Situation | Action |
|-----------|--------|
| Deep Mode reveals simple answer | Return to Light for conclusion |
| One hypothesis clearly dominates | Skip remaining verification |
| Time constraint emerges | Contract and conclude |
| User satisfied early | Accept current best |

### De-escalation Process

```
Deep Mode: [Many atoms created]
                |
    One hypothesis at 0.92 confidence
    Others rejected or far behind
                |
                v
Light Mode: [Synthesis using verified result]
            [Conclusion with confidence note]
```

---

## Mode Indicators

### You're in the Right Mode If...

**Light Mode is correct when**:
- Stages flow naturally
- No stage exceeds 1 page
- Single recommendation emerges clearly
- User doesn't ask "are you sure?"

**Deep Mode is correct when**:
- Multiple hypotheses compete (>=2 required)
- Verification adds new information
- Confidence tracking is useful
- Dependencies are non-trivial
- Bias audit catches reasoning errors before conclusion

**Hybrid was the right call when**:
- Escalation resolved a stuck point
- Verification changed the recommendation
- Initial simple approach would have failed

### Warning Signs

**Light Mode may be wrong if**:
- Stuck on a stage for too long
- Saying "it depends" frequently
- Making critical assumptions
- Multiple valid conclusions possible

**Deep Mode may be wrong if**:
- Atoms are trivially verified
- Single hypothesis dominates immediately
- Decomposition isn't adding clarity
- Feels like bureaucratic overhead

---

## Quick Reference Card (v2.2)

```
DECISION ROUTER: Type 1 -> Deep | Type 2 -> Select by characteristics

+-----------+-----------+-----------+-----------+-----------+
|  DIRECT   |   LIGHT   | CONSENSUS |   DEEP    |  HYBRID   |
+-----------+-----------+-----------+-----------+-----------+
| Trivial   | Clear     | Open-end  | Type 1    | Uncertain |
| Single Q  | Linear    | Multiple  | High      | Start     |
| Lookup    | Time      | options   | stakes    | simple    |
|           | pressure  | Trade-off | >=2 hypo  | Escalate  |
+-----------+-----------+-----------+-----------+-----------+
| Triggers: | Triggers: | Triggers: | Triggers: | Triggers: |
| "what is" | "step by" | "best     | "Type 1"  | "think    |
| "tell me" | "walk me" | approach" | "verify"  | through"  |
| "quick"   | "explain" | "compare" | "atom of" | (auto)    |
|           |           | "options" | "deeply"  |           |
+-----------+-----------+-----------+-----------+-----------+
| Output:   | Output:   | Output:   | Output:   | Output:   |
| Answer    | 5 stages  | Advisor   | P/R/H/V   | Stages->  |
| only      | Progress  | matrix    | BA/C      | Atoms     |
|           | bar       | + winner  | + conf    |           |
+-----------+-----------+-----------+-----------+-----------+

TYPE 1 (Irreversible): Clients, contracts, partnerships, purchases
                       -> Always Deep + EA reminder ("Sleep on it")
                       -> Requires >=2 hypotheses + Bias Audit before Conclusion

TYPE 2 (Reversible):   Content, pricing, tools, experiments
                       -> Route by characteristics, bias toward motion
```
