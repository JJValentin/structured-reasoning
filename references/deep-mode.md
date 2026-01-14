# Deep Mode: Atom of Thoughts

Deep dive into the networked, verification-based reasoning approach.

---

## Overview

Deep Mode builds a directed acyclic graph (DAG) of thought atoms, each with explicit dependencies, confidence levels, and verification status. This enables rigorous reasoning with traceable logic chains.

**Best for**:
- Ambiguous, complex problems
- High-stakes decisions requiring confidence
- Multiple competing hypotheses
- Problems with non-linear dependencies

**Based on**: "Atom of Thoughts for Markov LLM Test-Time Scaling" (Teng et al., 2025)

---

## The 5 Atom Types

### Premise (P)

**Purpose**: Establish known facts and constraints as the foundation.

**Characteristics**:
- Highest confidence (typically 0.85-1.0)
- No dependencies (given as input)
- Should be verifiable or explicitly stated
- Cannot be derived (that's reasoning)

**When to create**:
- Stating user requirements
- Documenting system constraints
- Recording verified facts
- Capturing expert knowledge

**Template**:
```markdown
## [P1] PREMISE (confidence: 0.95)
The system must handle 10,000 concurrent users at peak load.
Dependencies: none
Source: Product requirements document v2.3
```

**Confidence guide**:
| Source | Confidence |
|--------|------------|
| Documented requirement | 0.95-1.0 |
| Measured data | 0.90-0.98 |
| Expert statement | 0.85-0.95 |
| Reasonable assumption | 0.70-0.85 |

**Common mistakes**:
- Stating opinions as premises
- Including reasoning in premise
- Missing source attribution
- Over-confident assumptions

---

### Reasoning (R)

**Purpose**: Draw logical conclusions from premises and other reasoning.

**Characteristics**:
- Derived confidence (based on dependencies)
- Must cite dependencies explicitly
- Should be a single logical step
- Chain multiple R atoms for complex logic

**When to create**:
- Making logical deductions
- Combining multiple facts
- Drawing inferences
- Identifying implications

**Template**:
```markdown
## [R1] REASONING (confidence: 0.85)
Given that the system must handle 10,000 users (P1) and each server instance 
supports 1,000 concurrent connections (P2), we need at minimum 10 server instances.
Dependencies: P1, P2
Logic: 10,000 / 1,000 = 10 (minimum)
```

**Confidence calculation**:
```
R.confidence = min(dependency_confidences) * logic_strength

Where logic_strength:
- 1.0 = mathematical/definitional (A=B, B=C, therefore A=C)
- 0.9 = strong inference (highly likely given premises)
- 0.8 = moderate inference (probable but not certain)
- 0.7 = weak inference (possible but uncertain)
```

**Common mistakes**:
- Skipping logical steps
- Not citing dependencies
- Confidence higher than weakest dependency
- Mixing reasoning with hypothesis

---

### Hypothesis (H)

**Purpose**: Propose solutions or explanations to be verified.

**Characteristics**:
- Speculative (typically 0.30-0.80 confidence)
- Based on reasoning atoms
- Must be testable/falsifiable
- Multiple hypotheses can compete

**When to create**:
- Proposing a solution
- Suggesting an explanation
- Offering alternatives
- Guessing at causes

**Template**:
```markdown
## [H1] HYPOTHESIS (confidence: 0.65)
A 12-server cluster with nginx load balancer will provide adequate capacity 
with 20% headroom for traffic spikes.
Dependencies: R1, R2
Testable by: Load testing with simulated 12,000 concurrent users
Falsifiable if: Response time exceeds 200ms at 10,000 users
```

**Confidence starting points**:
| Basis | Initial Confidence |
|-------|-------------------|
| Strong reasoning chain | 0.65-0.80 |
| Moderate reasoning | 0.50-0.65 |
| Educated guess | 0.35-0.50 |
| Wild speculation | 0.20-0.35 |

**Common mistakes**:
- Not making hypothesis testable
- Too vague to falsify
- Missing dependencies
- Only one hypothesis (need alternatives)

---

### Verification (V)

**Purpose**: Test hypotheses and update confidence based on evidence.

**Characteristics**:
- References the hypothesis being tested
- Contains explicit pass/fail criteria
- Updates hypothesis confidence
- Can partially verify (some tests pass, some fail)

**When to create**:
- After forming a hypothesis
- When evidence becomes available
- To compare competing hypotheses
- Before drawing conclusions

**Template**:
```markdown
## [V1] VERIFICATION (confidence: 0.85)
Testing H1 (12-server cluster hypothesis):

| Test | Criterion | Result | Notes |
|------|-----------|--------|-------|
| Capacity | Handle 10k users | PASS | Achieved 11,200 in load test |
| Response time | < 200ms p95 | PASS | Measured 145ms p95 |
| Failover | Survive 2 node loss | PASS | 10 nodes sufficient |
| Cost | Within $5k/month budget | WARN | $4,800 - close to limit |

Overall: 3 PASS, 1 WARN, 0 FAIL
Dependencies: H1
Effect on H1: Confidence increased from 0.65 to 0.82
```

**Verification outcomes**:
| Result | Effect on Hypothesis |
|--------|---------------------|
| All PASS | Confidence += 0.15-0.25 |
| Mostly PASS, some WARN | Confidence += 0.05-0.15 |
| Mixed PASS/FAIL | Confidence unchanged or slight decrease |
| Mostly FAIL | Confidence -= 0.15-0.30 |
| All FAIL | Hypothesis rejected (confidence < 0.30) |

**Common mistakes**:
- Vague pass/fail criteria
- Not updating hypothesis confidence
- Confirmation bias (ignoring failures)
- Missing important tests

---

### Conclusion (C)

**Purpose**: State final verified recommendations.

**Characteristics**:
- Based on verified hypotheses
- High confidence (typically 0.75-0.95)
- Actionable recommendation
- Acknowledges remaining uncertainty

**When to create**:
- After verification completes
- When hypothesis confidence >= 0.80
- To answer the original question
- To provide final recommendation

**Template**:
```markdown
## [C1] CONCLUSION (confidence: 0.82)
Deploy a 12-server nginx cluster for the production API.

Based on:
- V1: Load testing verified capacity and response time
- H1: Architecture hypothesis validated

Confidence factors:
- Strong: Capacity verified (0.95)
- Strong: Response time verified (0.90)
- Moderate: Cost within budget but tight (0.75)

Remaining uncertainty:
- Long-term cost as traffic grows
- Untested: Behavior during actual traffic spikes (vs synthetic)

Recommended next steps:
1. Deploy to staging for 1 week
2. Implement cost monitoring alerts
3. Plan capacity review at 80% utilization
Dependencies: V1, H1
```

**Common mistakes**:
- Concluding without verification
- Ignoring remaining uncertainties
- Confidence not justified by evidence
- Not actionable

---

## Dependency Graphs

### Notation

```
[P1] ─┬─→ [R1] ─→ [H1] ─→ [V1] ─→ [C1]
[P2] ─┘              ↑
[P3] ─→ [R2] ────────┘
```

### Valid Dependency Patterns

| From | To | Valid | Explanation |
|------|----|-------|-------------|
| P | R | Yes | Reasoning from premises |
| P | H | Yes | Direct hypothesis from fact |
| R | R | Yes | Chained reasoning |
| R | H | Yes | Hypothesis from reasoning |
| H | V | Yes | Verification tests hypothesis |
| V | C | Yes | Conclusion from verification |
| H | C | Yes | Conclusion from verified hypothesis |
| V | H | No | Verification doesn't create hypotheses |
| C | * | No | Conclusions are terminal |
| * | P | No | Premises have no dependencies |

### Dependency Rules

1. **No cycles**: A → B → C → A is invalid
2. **No orphans**: Every atom except P must have dependencies
3. **No dead ends**: Every non-C atom should lead toward C
4. **Traceability**: Every C must trace back to at least one P

---

## Confidence System

### Calibration Guide

| Confidence | Verbal | Meaning |
|------------|--------|---------|
| 0.95-1.00 | Certain | Would bet everything on it |
| 0.85-0.94 | Very confident | Strong evidence, unlikely wrong |
| 0.75-0.84 | Confident | Good evidence, probably right |
| 0.65-0.74 | Moderate | Reasonable belief, could be wrong |
| 0.50-0.64 | Uncertain | Coin flip, need more evidence |
| 0.35-0.49 | Doubtful | More likely wrong than right |
| 0.20-0.34 | Very doubtful | Probably wrong, worth checking |
| < 0.20 | Disbelieve | Would bet against it |

### Propagation Rules

**Reasoning from premises**:
```
R.confidence = min(P1.conf, P2.conf, ...) * inference_strength
```

**Hypothesis from reasoning**:
```
H.confidence = min(R1.conf, R2.conf, ...) * speculation_factor
speculation_factor = 0.7 to 0.9 based on how speculative
```

**Conclusion from verification**:
```
C.confidence = H.confidence_after_verification * completeness
completeness = (tests_passed / tests_total)
```

### Updating Confidence

After verification:
```
if all_tests_pass:
    H.new_confidence = min(H.confidence + 0.20, 0.95)
elif most_pass:
    H.new_confidence = H.confidence + 0.10
elif mixed:
    H.new_confidence = H.confidence  # unchanged
elif most_fail:
    H.new_confidence = H.confidence - 0.15
elif all_fail:
    H.new_confidence = max(H.confidence - 0.30, 0.10)
    H.status = "rejected"
```

---

## Decomposition

### When to Decompose

| Trigger | Example | Action |
|---------|---------|--------|
| Low confidence | H1 at 0.55 | Break into verifiable sub-hypotheses |
| Multiple unknowns | H1 has 3 uncertain aspects | Separate into H1.1, H1.2, H1.3 |
| Too complex | Can't test H1 directly | Create testable sub-components |
| Conflicting evidence | Some tests pass, some fail | Isolate the failing aspect |

### Decomposition Process

**Before**:
```markdown
## [H1] HYPOTHESIS (confidence: 0.55)
The caching layer will solve our performance issues.
Dependencies: R1
```

**After decomposition**:
```markdown
## [H1] HYPOTHESIS (confidence: 0.55, DECOMPOSED)
The caching layer will solve our performance issues.
Dependencies: R1
Decomposed into: H1.1, H1.2, H1.3

## [H1.1] SUB-HYPOTHESIS (confidence: 0.70)
Redis can handle our read throughput (50k ops/sec).
Dependencies: R1, P4
Parent: H1

## [H1.2] SUB-HYPOTHESIS (confidence: 0.60)
Cache hit rate will exceed 80% for our access patterns.
Dependencies: R2
Parent: H1

## [H1.3] SUB-HYPOTHESIS (confidence: 0.50)
Cache invalidation strategy will maintain data consistency.
Dependencies: R3
Parent: H1
```

### Decomposition Rules

1. **Independence**: Sub-hypotheses should be independently testable
2. **Completeness**: Sub-hypotheses should cover parent's scope
3. **Depth limit**: Don't decompose beyond 3 levels
4. **Progress**: Each decomposition should increase testability

---

## Contraction

### When to Contract

| Trigger | Action |
|---------|--------|
| All sub-atoms verified | Contract with averaged confidence |
| Depth > 4 | Force contraction to prevent over-analysis |
| Diminishing returns | Sub-decomposition not adding value |
| Time constraint | Contract with current best estimate |

### Contraction Process

**Before contraction**:
```markdown
## [H1.1] SUB-HYPOTHESIS (confidence: 0.88, verified)
## [H1.2] SUB-HYPOTHESIS (confidence: 0.75, verified)
## [H1.3] SUB-HYPOTHESIS (confidence: 0.82, verified)
```

**After contraction**:
```markdown
## [H1] HYPOTHESIS (confidence: 0.82, CONTRACTED)
The caching layer will solve our performance issues.
Contracted from: H1.1 (0.88), H1.2 (0.75), H1.3 (0.82)
New confidence: average = 0.82
Status: verified (all sub-hypotheses verified)
```

### Contraction Calculation

```
contracted_confidence = weighted_average(sub_confidences)

Or, more conservatively:
contracted_confidence = min(sub_confidences) * 0.9 + average(sub_confidences) * 0.1
```

---

## Termination

### Termination Conditions

| Condition | Check | Action |
|-----------|-------|--------|
| High-confidence conclusion | C.confidence >= 0.85 | Terminate with recommendation |
| Maximum depth | depth >= 5 | Force contraction, then conclude |
| All hypotheses resolved | All H verified or rejected | Select best, conclude |
| No viable hypotheses | All H rejected | Report failure, suggest new approach |
| User acceptance | User says "good enough" | Conclude with current state |

### Termination Output

```markdown
## TERMINATION REPORT

**Status**: High-confidence conclusion reached

**Final Conclusion**: [C1]
Confidence: 0.87

**Atom Summary**:
- Premises: 4 (all high confidence)
- Reasoning: 3 (chain intact)
- Hypotheses: 2 created, 1 verified, 1 rejected
- Verifications: 2 completed
- Conclusions: 1 (accepted)

**Remaining Uncertainties**:
- [List any WARN results from verification]
- [List any untested aspects]

**Dependency Path** (C1):
P1 → R1 → H1 → V1 → C1
P2 → R1
P3 → R2 → H1
```

---

## Visual Representations

### Status Dashboard

```
Atoms: P:4 R:3 H:2 V:2 C:1
       [====] [===] [==] [==] [=]

Depth: 2/5 [##___]

Confidence Distribution:
  0.9+ : ### (3 atoms)
  0.8-0.9: #### (4 atoms)
  0.7-0.8: ## (2 atoms)
  <0.7 : # (1 atom)

Best Path: P1→R1→H1→V1→C1 (0.87)
```

### Dependency Graph (ASCII)

```
     [P1:0.95]──┐
                ├──[R1:0.88]──┐
     [P2:0.90]──┘             │
                              ├──[H1:0.82]──[V1:0.85]──[C1:0.87]
     [P3:0.92]──[R2:0.85]─────┘

     [P4:0.88]──[R3:0.80]──[H2:0.45]──[V2:REJECTED]
```

---

## Best Practices

### Do

- Start with clear premises
- Keep atoms atomic (single concept)
- Cite all dependencies explicitly
- Be conservative with confidence
- Create multiple hypotheses
- Verify before concluding

### Don't

- Skip verification for "obvious" conclusions
- Inflate confidence without evidence
- Create orphan atoms
- Decompose beyond 3-4 levels
- Ignore rejected hypotheses
- Rush to conclusion

### Quality Checklist

- [ ] All premises have sources
- [ ] Reasoning chains are complete
- [ ] Hypotheses are testable
- [ ] Verification has clear criteria
- [ ] Conclusion confidence is justified
- [ ] No orphan atoms
- [ ] Dependency graph is acyclic
