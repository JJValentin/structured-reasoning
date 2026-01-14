# Light Mode: Sequential Thinking

Deep dive into the linear, stage-based reasoning approach.

---

## Overview

Light Mode provides fast, intuitive problem-solving through 5 sequential stages. Each stage builds naturally on the previous, mimicking how humans naturally work through problems.

**Best for**:
- Clear, well-defined problems
- Time-constrained situations
- Standard verification needs
- Linear cause-effect relationships

---

## The 5 Stages

### Stage 1: Problem Definition

**Purpose**: Ensure you're solving the right problem before investing effort.

**Time allocation**: ~10-15% of total effort

**Key questions**:
- What exactly is the problem? (one sentence)
- Who is affected and how?
- What constraints exist? (time, budget, technical, political)
- What does success look like? (measurable)
- What is explicitly OUT of scope?

**Output checklist**:
- [ ] Problem statement is one clear sentence
- [ ] Stakeholders identified
- [ ] At least 3 constraints listed
- [ ] Success criteria are measurable
- [ ] Scope boundaries defined

**Template**:
```markdown
## [Stage 1/5] PROBLEM DEFINITION
Progress: [##________] 20%

**Problem Statement**: 
[One sentence describing what needs to be solved]

**Stakeholders**:
- [Stakeholder 1]: [Their primary concern]
- [Stakeholder 2]: [Their primary concern]

**Constraints**:
- Time: [Deadline or time limit]
- Budget: [Financial constraints]
- Technical: [System/platform limitations]
- Other: [Political, regulatory, etc.]

**Success Criteria**:
- [ ] [Measurable outcome 1]
- [ ] [Measurable outcome 2]

**Out of Scope**:
- [What we're NOT solving]
- [Adjacent problems to ignore for now]

---
Next: Stage 2 (Research)
```

**Common mistakes**:
- Stating the solution as the problem ("We need to use Redis")
- Vague statements ("Make it better")
- Missing key stakeholders
- Forgetting non-functional constraints

---

### Stage 2: Research

**Purpose**: Gather the information needed to analyze options.

**Time allocation**: ~20-25% of total effort

**Key questions**:
- What do we already know for certain?
- What don't we know that we need to find out?
- What has been tried before?
- What do experts/documentation say?
- What assumptions are we making?

**Output checklist**:
- [ ] Known facts listed with sources
- [ ] Knowledge gaps identified
- [ ] Each gap has a plan to address (or accept)
- [ ] Assumptions explicitly stated
- [ ] Risk of each assumption noted

**Template**:
```markdown
## [Stage 2/5] RESEARCH
Progress: [####______] 40%

**Tags**: #[domain] #[technology] #[concern]

**Known Facts**:
| Fact | Source | Confidence |
|------|--------|------------|
| [Fact 1] | [Documentation/testing/expert] | High/Medium/Low |
| [Fact 2] | [Source] | High/Medium/Low |

**Knowledge Gaps**:
| Gap | Impact if Unknown | Resolution Plan |
|-----|-------------------|-----------------|
| [Gap 1] | [What breaks?] | [How to find out] |
| [Gap 2] | [Impact] | [Acceptable to proceed?] |

**Prior Art**:
- [Previous attempt 1]: [Outcome and lessons]
- [Similar problem elsewhere]: [What they did]

**Assumptions**:
| Assumption | Risk if Wrong | Mitigation |
|------------|---------------|------------|
| [Assumption 1] | [What happens?] | [How to verify later] |

---
Next: Stage 3 (Analysis)
```

**Common mistakes**:
- Confusing opinions with facts
- Not sourcing claims
- Ignoring knowledge gaps
- Unstated assumptions

---

### Stage 3: Analysis

**Purpose**: Examine information critically to understand the solution space.

**Time allocation**: ~25-30% of total effort

**Key questions**:
- What patterns emerge from the research?
- What options do we have?
- What are the trade-offs for each option?
- What risks exist and how severe are they?
- Which assumptions should we challenge?

**Output checklist**:
- [ ] At least 2-3 options identified
- [ ] Each option has pros/cons/risks
- [ ] Trade-offs explicitly compared
- [ ] At least one assumption challenged
- [ ] Risks ranked by likelihood and impact

**Template**:
```markdown
## [Stage 3/5] ANALYSIS
Progress: [######____] 60%

**Tags**: #[domain] #[concern]
**Axioms Applied**: "[Relevant principle, e.g., 'KISS', 'YAGNI']"

**Patterns Observed**:
- [Pattern 1]: [What it suggests]
- [Pattern 2]: [What it suggests]

**Options Identified**:

| Option | Description | Pros | Cons | Risk Level |
|--------|-------------|------|------|------------|
| A | [Brief description] | [Advantages] | [Disadvantages] | Low/Med/High |
| B | [Brief description] | [Advantages] | [Disadvantages] | Low/Med/High |
| C | [Brief description] | [Advantages] | [Disadvantages] | Low/Med/High |

**Trade-off Analysis**:
- Option A vs B: [Key differentiator]
- Option B vs C: [Key differentiator]
- [Most important trade-off]: [Which option wins and why]

**Assumptions Challenged**:
| Original Assumption | Challenge | Revised Understanding |
|--------------------|-----------|----------------------|
| [From Stage 2] | [Why it might be wrong] | [Updated belief] |

**Risk Assessment**:
| Risk | Likelihood | Impact | Option(s) Affected |
|------|------------|--------|-------------------|
| [Risk 1] | High/Med/Low | High/Med/Low | A, B |
| [Risk 2] | High/Med/Low | High/Med/Low | C |

---
Next: Stage 4 (Synthesis)
```

**Common mistakes**:
- Only considering one option
- Not quantifying trade-offs
- Ignoring risks
- Analysis paralysis (too many options)

**Escalation trigger**: If you identify 3+ viable options with similar merit, consider escalating to Deep Mode for rigorous comparison.

---

### Stage 4: Synthesis

**Purpose**: Combine insights into a coherent recommendation.

**Time allocation**: ~20-25% of total effort

**Key questions**:
- Which option best meets success criteria?
- How do we address the identified risks?
- What's the implementation approach?
- What dependencies exist?
- How will stakeholders react?

**Output checklist**:
- [ ] Clear recommendation stated
- [ ] Rationale ties back to analysis
- [ ] Risks have mitigation plans
- [ ] Implementation steps outlined
- [ ] Stakeholder concerns addressed

**Template**:
```markdown
## [Stage 4/5] SYNTHESIS
Progress: [########__] 80%

**Recommended Approach**: [Option X]

**Rationale**:
- [Why this over Option Y]: [Specific reason from analysis]
- [Why this over Option Z]: [Specific reason from analysis]
- [How it meets success criteria]: [Tie back to Stage 1]

**Risk Mitigations**:
| Risk | Mitigation Strategy | Owner |
|------|---------------------|-------|
| [Risk 1] | [How to prevent/reduce] | [Who handles it] |
| [Risk 2] | [How to prevent/reduce] | [Who handles it] |

**Implementation Outline**:
1. [Phase 1]: [What and when]
   - Dependency: [What must happen first]
2. [Phase 2]: [What and when]
   - Dependency: [Phase 1 complete]
3. [Phase 3]: [What and when]

**Stakeholder Considerations**:
| Stakeholder | Likely Concern | Response |
|-------------|----------------|----------|
| [Stakeholder 1] | [What they'll ask] | [How to address] |

---
Next: Stage 5 (Conclusion)
```

**Common mistakes**:
- Recommendation doesn't follow from analysis
- Ignoring risks identified earlier
- No implementation path
- Forgetting stakeholder buy-in

**Escalation trigger**: If you can't commit to a single recommendation with confidence, escalate to Deep Mode for hypothesis verification.

---

### Stage 5: Conclusion

**Purpose**: Finalize with clear, actionable outcomes.

**Time allocation**: ~10-15% of total effort

**Key questions**:
- What is the final recommendation?
- What are the immediate next steps?
- What decisions need to be made?
- What would change this recommendation?
- How do we know if it's working?

**Output checklist**:
- [ ] Recommendation is one clear statement
- [ ] Key reasoning summarized (3-5 points)
- [ ] Next steps are concrete and assignable
- [ ] Decision points identified
- [ ] Conditions for revisiting stated

**Template**:
```markdown
## [Stage 5/5] CONCLUSION
Progress: [##########] 100%

**RECOMMENDATION**: 
[Clear, actionable one-sentence recommendation]

**Key Reasoning** (Summary):
1. [Most important point from analysis]
2. [Second most important point]
3. [Third point that clinched the decision]

**Immediate Next Steps**:
| Step | Owner | Deadline | Deliverable |
|------|-------|----------|-------------|
| [Action 1] | [Who] | [When] | [What they produce] |
| [Action 2] | [Who] | [When] | [What they produce] |

**Decision Points**:
- [Decision 1]: [When it needs to be made, by whom]
- [Decision 2]: [When and by whom]

**Revisit This Recommendation If**:
- [Condition 1]: [What would change, e.g., "Budget increases by 50%"]
- [Condition 2]: [What would change]

**Success Metrics**:
| Metric | Target | Measurement Method |
|--------|--------|-------------------|
| [From Stage 1 success criteria] | [Specific target] | [How to measure] |

---
COMPLETE
```

**Common mistakes**:
- Vague recommendations
- No next steps
- Missing ownership
- No way to measure success

---

## Adjusting Stage Count

### Condensed (3 Stages)

For simple problems:

```
Stage 1: Problem + Research (combined)
Stage 2: Analysis
Stage 3: Synthesis + Conclusion (combined)
```

Use when:
- Problem is well-understood
- Limited options (2-3 max)
- Time pressure is severe

### Expanded (6+ Stages)

For complex linear problems:

```
Stage 1: Problem Definition
Stage 2: Stakeholder Analysis (added)
Stage 3: Research
Stage 4: Analysis
Stage 5: Option Evaluation (added)
Stage 6: Synthesis
Stage 7: Conclusion
```

Use when:
- Multiple stakeholder groups
- Many options to evaluate
- High stakes require extra rigor

---

## Tags and Axioms

### Recommended Tags

Use tags to categorize and cross-reference thinking:

**Domain tags**: #architecture, #security, #performance, #ux, #data
**Concern tags**: #cost, #timeline, #risk, #scalability, #maintainability
**Status tags**: #blocked, #assumption, #verified, #uncertain

### Common Axioms

Reference established principles:

| Axiom | Meaning | Apply When |
|-------|---------|------------|
| KISS | Keep It Simple, Stupid | Complexity creeping in |
| YAGNI | You Aren't Gonna Need It | Premature optimization |
| DRY | Don't Repeat Yourself | Duplication emerging |
| Occam's Razor | Simplest explanation is best | Multiple theories |
| Pareto (80/20) | 80% results from 20% effort | Prioritizing work |

---

## Progress Visualization

### Standard Progress Bar

```
[##________] 20%  - Stage 1
[####______] 40%  - Stage 2
[######____] 60%  - Stage 3
[########__] 80%  - Stage 4
[##########] 100% - Stage 5
```

### Detailed Progress

```
Stages:  [1:DONE] [2:DONE] [3:ACTIVE] [4:TODO] [5:TODO]
Overall: [######____] 60%
Time:    ~15 min elapsed, ~10 min remaining (estimate)
```

---

## When to Escalate to Deep Mode

Escalation triggers during Light Mode:

| Trigger | Detection | Action |
|---------|-----------|--------|
| Can't choose between options | Stage 4 stalls | Convert options to hypotheses |
| Contradictory research | Stage 2 conflict | Create verification workflow |
| Assumption is critical | High-risk assumption | Decompose and verify |
| Stakeholders disagree | Stage 4 pushback | Model competing perspectives |
| Problem reveals sub-problems | Stage 3 complexity | Decompose into atoms |

See [mode-selection-guide.md](mode-selection-guide.md) for detailed escalation patterns.
