# Consensus Mode: Parallel Advisor Patterns

Deep dive into the multi-advisor architecture for open-ended Type 2 decisions.

---

## Core Architecture

Consensus Mode runs multiple "advisors" in parallel, each bringing a different perspective to the problem. This is inspired by TerminaI's cognitive architecture, which uses parallel expert evaluation with early return on high confidence.

```
                         PROBLEM
                            |
                   [ADVISOR DISPATCH]
                            |
      +----------+----------+----------+----------+
      |          |          |          |          |
      v          v          v          v          v
  Enumerator  Pattern   FirstPrin  Contrarian  Pragmatist
      |          |          |          |          |
      v          v          v          v          v
  [Proposal]  [Proposal]  [Proposal]  [Proposal]  [Proposal]
      |          |          |          |          |
      +----------+----------+----------+----------+
                            |
                    [CONSENSUS MATRIX]
                            |
                    [SELECT WINNER]
                    (confidence or ICE)
```

---

## The Five Advisors

### 1. Enumerator Advisor

**Perspective**: Comprehensive option generation
**Question**: "What are ALL the ways we could approach this?"
**Strength**: Ensures no obvious options are missed
**Weakness**: Can overwhelm with too many options

**Process**:
1. Brainstorm all possible approaches (no filtering)
2. Group into categories
3. Select 2-3 most promising for proposal
4. Assign confidence based on how exhaustive the search was

**Output Template**:
```markdown
### Enumerator Analysis

**Options Identified**: 7 total
- Category A (Content): Video, blog, thread, carousel
- Category B (Direct): DM, email, cold call
- Category C (Other): Partnership, paid ads

**Top Proposal**: Video series
**Confidence**: 0.75
**Rationale**: Highest reach potential in Category A, which aligns with stated goal
```

### 2. Pattern Matcher Advisor

**Perspective**: Historical precedent and proven solutions
**Question**: "What worked before in similar situations?"
**Strength**: Grounds recommendations in evidence
**Weakness**: May miss novel solutions

**Process**:
1. Search for similar past problems (internal knowledge or tools)
2. Identify patterns that led to success
3. Map those patterns to current situation
4. Assign confidence based on pattern match strength

**Output Template**:
```markdown
### Pattern Matcher Analysis

**Similar Situations Found**: 3
1. [85% match] Twitter thread on AI tools went viral (Feb 2025)
2. [70% match] Blog post on productivity got 10k views (Jan 2025)
3. [60% match] Video series on workflows, moderate engagement

**Top Proposal**: Twitter thread
**Confidence**: 0.80
**Rationale**: Strongest pattern match; thread format proven for similar topic
```

### 3. First Principles Advisor

**Perspective**: Fundamental reasoning from core truths
**Question**: "If we started from scratch, ignoring convention, what would we do?"
**Strength**: Can discover non-obvious optimal paths
**Weakness**: May ignore practical constraints

**Process**:
1. Identify the core goal (strip away surface requirements)
2. List fundamental constraints that cannot be changed
3. Build up solution from those foundations
4. Assign confidence based on logical soundness

**Output Template**:
```markdown
### First Principles Analysis

**Core Goal**: Reach audience with high-value insight
**Fundamental Constraints**:
- Limited time (must ship this week)
- Audience is busy professionals
- Message has depth that requires explanation

**Derived Solution**: Long-form blog with embedded video snippet
**Confidence**: 0.70
**Rationale**: Depth requires long-form; video snippet aids discovery
```

### 4. Contrarian Advisor

**Perspective**: Challenge assumptions and find blind spots
**Question**: "What if the opposite is true? What are we missing?"
**Strength**: Prevents groupthink and reveals risks
**Weakness**: Can be dismissed as "just negative"

**Process**:
1. Identify implicit assumptions in the problem framing
2. Invert each assumption and explore consequences
3. Find the most dangerous assumption if wrong
4. Propose alternative or highlight risk

**Output Template**:
```markdown
### Contrarian Analysis

**Assumptions Challenged**:
1. "Content is the right approach" → What if direct outreach works better?
2. "Audience wants this topic" → What if they're oversaturated?
3. "Viral reach matters" → What if 10 right people beats 10k random?

**Counter-Proposal**: Skip content, DM 20 ideal prospects directly
**Confidence**: 0.60
**Rationale**: Content assumes reach = results; direct outreach tests faster
```

### 5. Pragmatist Advisor

**Perspective**: Execution speed and practical constraints
**Question**: "What's the fastest path to a working solution?"
**Strength**: Optimizes for shipping over perfection
**Weakness**: May miss strategic opportunities

**Process**:
1. Inventory existing assets (skills, content, tools, relationships)
2. Identify path with least friction
3. Estimate time-to-ship for each option
4. Select fastest viable option

**Output Template**:
```markdown
### Pragmatist Analysis

**Existing Assets**:
- Video recording setup ready
- 3 draft scripts already written
- Editing software familiar

**Friction Analysis**:
| Option | Time to Ship | Friction Points |
|--------|--------------|-----------------|
| Video | 2 days | None - setup ready |
| Blog | 3 days | Need images, SEO |
| Thread | 4 hours | Need to distill |

**Top Proposal**: Twitter thread (then repurpose to video)
**Confidence**: 0.85
**Rationale**: Ship in 4 hours, learn, then expand if works
```

---

## Consensus Matrix

After all advisors complete, build the comparison matrix:

```markdown
| Advisor | Proposal | Confidence | Time | ICE |
|---------|----------|------------|------|-----|
| Enumerator | Video series | 0.75 | 2d | 21 |
| Pattern Matcher | Twitter thread | 0.80 | 4h | 23 |
| First Principles | Blog + video | 0.70 | 3d | 19 |
| Contrarian | Direct DM | 0.60 | 1h | 18 |
| Pragmatist | Thread→video | 0.85 | 4h | 24 |
```

### Selection Criteria

1. **Confidence-based**: If one advisor has significantly higher confidence (0.15+ delta), prefer it
2. **Convergent signal**: If 2+ advisors recommend same approach, weight it higher
3. **ICE tie-breaker**: If confidence is close, use ICE score
4. **Contrarian check**: If Contrarian raised valid concern, address it in final recommendation

---

## Early Return

To optimize for speed, implement early return:

```python
EARLY_RETURN_CONFIDENCE = 0.80

def run_advisors(problem):
    for advisor in advisors:
        proposal = advisor.propose(problem)
        if proposal.confidence >= EARLY_RETURN_CONFIDENCE:
            return proposal  # Early return
    
    # If no early return, compare all proposals
    return select_best(all_proposals)
```

**Early return signals**:
- Pattern Matcher finds exact precedent (0.85+)
- Pragmatist identifies zero-friction path (0.85+)
- First Principles derives logically necessary solution (0.90+)

---

## MCP Tool Integration

When MCP tools are available, advisors can query external data:

| Advisor | Tool | Query |
|---------|------|-------|
| Pattern Matcher | `linkup-search` | "content that went viral on [topic]" |
| Pattern Matcher | `reddit-search` | "what posts got upvotes on [topic]" |
| Enumerator | `youtube-search` | "popular videos on [topic]" |
| Contrarian | `dataforseo-trends` | "is [topic] trending up or down" |
| Pragmatist | `todoist-get-tasks` | "what related tasks are already planned" |

### Tool Query Format

```markdown
### [Advisor Name] External Data

**Tool**: linkup-search
**Query**: "viral content AI agents 2025"
**Results**: [summary of top 3 results]

**Impact on Proposal**: Adjusted confidence from 0.70 to 0.82 based on external validation
```

---

## Worked Example: Content Strategy Decision

**Problem**: "What content should I create this week to grow my AI consulting brand?"

### [ROUTER] Type 2 (reversible) | Open-ended, multiple viable paths | → Consensus Mode

### Advisor Outputs

**Enumerator** (0.72):
- Options: Tutorial video, case study blog, Twitter thread, LinkedIn carousel, podcast guest, YouTube Short
- Proposal: Tutorial video showing real client workflow
- Rationale: Most comprehensive option that showcases expertise

**Pattern Matcher** (0.78):
- Patterns: "Before/after" threads get 3x engagement; video tutorials with specific numbers perform well
- Proposal: Twitter thread with before/after transformation story
- Rationale: Proven format matches current audience preference

**First Principles** (0.68):
- Core goal: Build trust with potential clients
- Proposal: Deep blog post with embedded Loom walkthrough
- Rationale: Trust requires depth; video adds personality

**Contrarian** (0.55):
- Challenge: "Creating more content assumes content is the bottleneck"
- Counter-proposal: Spend week on direct outreach instead
- Warning: May be over-indexing on content when conversion is the issue

**Pragmatist** (0.83):
- Assets: Have unused client recording, thread drafts, 2 hours available
- Proposal: Repurpose recording into thread + LinkedIn carousel
- Rationale: Fastest path; tests two platforms with same content

### Consensus Matrix

| Advisor | Proposal | Conf | ICE |
|---------|----------|------|-----|
| Enumerator | Tutorial video | 0.72 | 20 |
| Pattern Matcher | Before/after thread | 0.78 | 22 |
| First Principles | Blog + Loom | 0.68 | 18 |
| Contrarian | Direct outreach | 0.55 | 15 |
| Pragmatist | Repurpose→thread+carousel | 0.83 | 24 |

### Consensus Analysis

**Convergent Signal**: Enumerator, Pattern Matcher, and Pragmatist all favor content (not outreach)
**Highest Confidence**: Pragmatist (0.83) with clear execution path
**ICE Winner**: Pragmatist (24) - Impact 8, Confidence 8, Ease 8

**Contrarian Note**: Valid point about content vs conversion. If this week's content doesn't generate leads, revisit outreach strategy next week.

### Final Recommendation

**Winner**: Repurpose existing recording into Twitter thread + LinkedIn carousel
**Next Action**: Block 2 hours tomorrow for editing and scheduling
**Success Metric**: Track replies/DMs from each platform
**Contingency**: If no engagement by Friday, pivot to Contrarian's direct outreach

---

## Anti-Patterns

| Avoid | Why | Instead |
|-------|-----|---------|
| Ignoring Contrarian | Miss blind spots | Always address the challenge, even if rejecting |
| Over-weighting Pattern Matcher | Past ≠ future | Balance with First Principles |
| Skipping low-confidence advisors | Lose perspective | Include all in matrix |
| Analysis paralysis | Defeats purpose | ICE score and ship |
| Using Consensus for Type 1 | Needs verification | Use Deep Mode instead |

---

## When to Escalate to Deep Mode

Consensus Mode is for fast, good-enough decisions. Escalate to Deep Mode if:

- Advisors fundamentally disagree on premises (not just solutions)
- Contrarian raises concern that can't be dismissed
- Stakes turn out higher than initially thought
- Need explicit confidence scores for each assumption

```
[ESCALATION] Pattern Matcher and First Principles have conflicting premises
→ Converting proposals to hypotheses for Deep Mode verification
```
