# Persistence Layer

Store, query, and learn from reasoning artifacts across sessions. Implements keyword-based auto-linking, SAFLA learning loops, and A-MEM memory evolution for adaptive knowledge management.

---

## Overview

The persistence layer eliminates the "lost reasoning" problem by storing:
- **Decisions**: Complete reasoning chains with conclusions
- **Premises**: Established facts that can be reused
- **Context**: Project-level information that persists

Enhanced capabilities:
- **Auto-Linking**: Keyword-based relationship discovery between memories
- **Learning Loop**: Outcome tracking with confidence propagation (SAFLA)
- **Memory Evolution**: Living memories that update with new context (A-MEM)
- **Usage Tracking**: Frequently-used memories decay slower

This enables:
- Querying past decisions ("Why did we choose X?")
- Reusing verified premises in new reasoning
- Tracking evidence staleness over time
- Learning from decision outcomes
- Discovering related decisions automatically
- Maintaining audit trails for review

---

## Directory Structure

```
.claude/
└── reasoning/
    ├── context.json              # Project-level context
    ├── decisions/                # Decision artifacts
    │   ├── 2025-01-16-api-arch.json
    │   └── 2025-01-18-cache-strategy.json
    └── premises/                 # Established facts by domain
        ├── api-premises.json
        ├── performance-premises.json
        └── requirements-premises.json
```

---

## Artifact Formats

### Decision Artifact

```json
{
  "id": "2025-01-16-api-architecture",
  "title": "API Architecture Decision",
  "timestamp": "2025-01-16T14:30:00Z",
  "problem": "Which API architecture for new service?",
  "mode": "deep",
  "type": "type-1",
  "atoms": [
    {
      "id": "P1",
      "type": "premise",
      "content": "Service must handle 10k req/s",
      "confidence": 0.95,
      "source": "Requirements doc v2.3",
      "established": "2025-01-10T09:00:00Z"
    },
    {
      "id": "H1",
      "type": "hypothesis",
      "content": "REST with horizontal scaling",
      "confidence": 0.75,
      "dependencies": ["P1", "R1"]
    },
    {
      "id": "H2",
      "type": "hypothesis",
      "content": "GraphQL with caching layer",
      "confidence": 0.70,
      "dependencies": ["P1", "R1"]
    },
    {
      "id": "BA1",
      "type": "bias_audit",
      "anchoring": true,
      "confirmation": true,
      "availability": true,
      "sunk_cost": true,
      "overall": "PASS"
    },
    {
      "id": "C1",
      "type": "conclusion",
      "content": "Use REST with horizontal scaling",
      "confidence": 0.87,
      "dependencies": ["V1", "H1", "BA1"]
    }
  ],
  "conclusion": {
    "recommendation": "REST API with 12-node horizontal scaling",
    "confidence": 0.87,
    "rationale": "Better tooling, team familiarity, proven at scale"
  },
  "evidence": [
    "Load test results: 11,200 req/s achieved",
    "Team survey: 80% REST experience"
  ],
  "tags": ["architecture", "api", "scaling"],
  "related": ["2025-01-10-scaling-decision", "2025-01-05-db-architecture"],
  "confidence": 0.87,
  "outcome": null,
  "outcome_date": null,
  "decay_days": 90,
  "times_used": 3,
  "last_used": "2025-01-16",
  "created": "2025-01-16",
  "context_updates": []
}
```

**New Fields Explained:**

| Field | Type | Purpose |
|-------|------|---------|
| `title` | string | Human-readable decision title |
| `related` | string[] | Auto-populated linked decision IDs |
| `confidence` | float | Top-level confidence (mirrors conclusion) |
| `outcome` | string\|null | `"success"`, `"partial"`, `"failure"`, or `null` |
| `outcome_date` | string\|null | ISO timestamp when outcome was recorded |
| `times_used` | integer | Count of references in other reasoning |
| `last_used` | string | Date of most recent reference |
| `context_updates` | array | A-MEM evolution history |

### Premise Collection

```json
{
  "domain": "api",
  "premises": [
    {
      "id": "api-rate-limit",
      "content": "API rate limit is 1000 req/min",
      "confidence": 0.95,
      "source": "API documentation v2.3",
      "established": "2025-01-16T14:30:00Z",
      "decay_days": 90,
      "times_used": 5,
      "last_used": "2025-01-20",
      "used_in": ["2025-01-16-api-architecture"],
      "outcome_history": [
        {"decision": "2025-01-16-api-architecture", "outcome": "success"}
      ]
    },
    {
      "id": "api-auth-method",
      "content": "API uses OAuth 2.0 with JWT tokens",
      "confidence": 0.98,
      "source": "Security spec v1.2",
      "established": "2025-01-10T09:00:00Z",
      "decay_days": 180,
      "times_used": 0,
      "last_used": null,
      "used_in": [],
      "outcome_history": []
    }
  ]
}
```

### Context File

```json
{
  "project": "acme-backend",
  "description": "Main backend service for Acme Corp",
  "created": "2025-01-01T00:00:00Z",
  "updated": "2025-01-16T14:30:00Z",
  "key_decisions": [
    "2025-01-16-api-architecture",
    "2025-01-18-cache-strategy"
  ],
  "hub_memories": ["2025-01-16-api-architecture"],
  "active_premises": 12,
  "stale_premises": 2,
  "tags_used": ["architecture", "api", "caching", "performance"],
  "learning_stats": {
    "total_outcomes": 8,
    "success_rate": 0.75,
    "last_learn_pass": "2025-01-20T10:00:00Z"
  }
}
```

---

## Auto-Linking

Decisions are automatically linked based on keyword similarity. No embeddings or semantic search required.

### Jaccard Similarity

The linking algorithm uses Jaccard similarity between keyword sets:

```
similarity = |keywords_A ∩ keywords_B| / |keywords_A ∪ keywords_B|
```

Where:
- `∩` = intersection (keywords in both sets)
- `∪` = union (keywords in either set)

### Keyword Extraction Process

1. **Content Processing**
   - Split content on whitespace
   - Remove stopwords (the, a, an, is, are, was, were, etc.)
   - Lowercase all terms
   - Include technical terms and identifiers

2. **Weighting**
   - Title words: **2x weight** (counted twice in set)
   - Explicit tags: **1x weight**
   - Content words: **1x weight**

3. **Linking Threshold**
   - On `/sr-save`, compare with all existing decisions
   - Auto-populate `related` array for items with **overlap > 0.3**
   - Maximum 5 related items per decision (highest similarity first)

### Example

```
Decision A keywords: {api, rest, scaling, architecture, horizontal}
Decision B keywords: {api, graphql, scaling, caching, performance}

Intersection: {api, scaling} = 2
Union: {api, rest, scaling, architecture, horizontal, graphql, caching, performance} = 8

Similarity = 2/8 = 0.25 → Below threshold, not linked

Decision C keywords: {api, rest, architecture, endpoints, versioning}

Intersection: {api, rest, architecture} = 3
Union: {api, rest, scaling, architecture, horizontal, endpoints, versioning} = 7

Similarity = 3/7 = 0.43 → Above threshold, linked!
```

### On Save Behavior

```
/sr-save

Saved decision: 2025-01-20-caching-strategy
  Mode: deep
  Atoms: P:3 R:2 H:2 V:2 BA:1 C:1
  Confidence: 0.85
  Tags: caching, redis, performance

Auto-linked to 2 related decisions:
  - 2025-01-18-cache-strategy (0.52 similarity)
  - 2025-01-16-api-architecture (0.35 similarity)
```

---

## Learning Loop

The SAFLA (Store-Analyze-Feedback-Learn-Apply) loop enables the knowledge base to improve from experience.

### SAFLA Cycle

```
STORE → LINK → QUERY → RANK → LEARN
  ↑                              ↓
  └──────── Confidence Update ←──┘
```

1. **STORE**: Save decision with initial confidence
2. **LINK**: Auto-link to related decisions
3. **QUERY**: Retrieve relevant memories on demand
4. **RANK**: Order by confidence × recency × keyword match
5. **LEARN**: Update confidence based on outcomes

### Outcome Tracking

Record outcomes for decisions to enable learning:

```
/sr-outcome 2025-01-16-api-architecture success

Recorded outcome: success
  Decision: 2025-01-16-api-architecture
  Previous confidence: 0.87
  New confidence: 0.90
  Outcome date: 2025-01-20T14:30:00Z

Propagating to 3 linked memories (decay factor: 0.5)
  - 2025-01-10-scaling-decision: 0.82 → 0.83
  - 2025-01-05-db-architecture: 0.78 → 0.79
  - api-rate-limit (premise): 0.95 → 0.96
```

**Outcome Values:**

| Outcome | Meaning | Effect |
|---------|---------|--------|
| `success` | Decision proved correct | Boost confidence |
| `partial` | Partially correct, needed adjustment | No change |
| `failure` | Decision was wrong | Reduce confidence |

### Confidence Propagation Formulas

**Primary Decision:**

```
Success:  new_confidence = old_confidence + 0.2 × (1 - old_confidence)
Failure:  new_confidence = old_confidence × 0.85
Partial:  new_confidence = old_confidence  (no change)
```

**Linked Memories (propagation with decay):**

```
linked_boost = primary_boost × 0.5
```

This means:
- A successful decision with confidence 0.80 becomes 0.84
- Its linked memories get half that boost (+0.02 instead of +0.04)
- Failure propagation: linked memories see 50% of confidence reduction

**Examples:**

| Scenario | Old | Outcome | New |
|----------|-----|---------|-----|
| High confidence success | 0.90 | success | 0.92 |
| Medium confidence success | 0.70 | success | 0.76 |
| Low confidence success | 0.50 | success | 0.60 |
| High confidence failure | 0.90 | failure | 0.77 |
| Medium confidence failure | 0.70 | failure | 0.60 |

### Learning-Weighted Retrieval

When using `/sr-query`, results are ranked by a composite score:

```
final_score = keyword_score × confidence × recency_factor

where:
  keyword_score = Jaccard similarity (0-1)
  confidence = current confidence (0-1)
  recency_factor = 1 / (1 + days_since_last_used / 30)
```

This means:
- Premises from successful decisions rank higher
- Recently-used memories surface first
- Strong keyword matches still matter most

---

## Memory Evolution

Based on the A-MEM (Agentic Memory) framework from NeurIPS 2025, memories are living documents that evolve as new knowledge is added.

### Evolution Process

```
New Memory Created
       ↓
Find Related Memories (keyword overlap > 0.3)
       ↓
For each related memory:
  - Add cross-reference note to context_updates
  - Update context_updates array with trigger info
  - Increment mutual link strength if co-referenced
       ↓
Related memories now reflect new knowledge
```

### Context Update Format

When a new decision relates to an existing one, both get updated:

```json
{
  "context_updates": [
    {
      "date": "2025-01-20",
      "trigger": "2025-01-20-caching-strategy",
      "note": "New caching decision builds on this API architecture"
    },
    {
      "date": "2025-01-22",
      "trigger": "2025-01-22-performance-audit",
      "note": "Performance audit validated 10k req/s premise"
    }
  ]
}
```

### Evolution Triggers

Memory evolution occurs on:
- `/sr-save` - New decision links to existing memories
- `/sr-outcome` - Outcome recording updates related memories
- `/sr-evolve` - Manual evolution pass for recent memories

### Hub Detection

Memories referenced by many others become "hub" concepts:

**Criteria:**
- Memory is referenced in `related` array of 5+ other decisions
- Hub status tracked via `link_count` (derived from incoming references)

**Hub Benefits:**
- Surfaced prominently in `/sr-context` output
- Higher weight in query results
- Flagged for review when staleness approaches

**Hub Display:**

```
/sr-hubs

Hub Memories (5+ references)
============================
1. 2025-01-16-api-architecture
   References: 8 | Confidence: 0.90 | Last used: 2025-01-22
   Tags: architecture, api, scaling

2. api-rate-limit (premise)
   References: 6 | Confidence: 0.96 | Domain: api
   Used in 6 decisions

These memories are central to project knowledge.
Consider extra care when updating or deprecating.
```

---

## Staleness Tracking

Memories decay over time, but usage slows decay.

### Enhanced Staleness Formula

```
staleness = (days_elapsed / decay_days) × (1 / sqrt(times_used + 1))
```

Where:
- `days_elapsed` = days since `established` or `created`
- `decay_days` = domain-specific threshold
- `times_used` = reference count

**Examples:**

| Days Elapsed | Decay Days | Times Used | Staleness |
|--------------|------------|------------|-----------|
| 90 | 90 | 0 | 1.00 (stale) |
| 90 | 90 | 3 | 0.50 (aging) |
| 90 | 90 | 8 | 0.33 (fresh) |
| 45 | 90 | 0 | 0.50 (aging) |
| 45 | 90 | 3 | 0.25 (fresh) |

Frequently-used memories stay fresh longer.

### Domain-Specific Decay Thresholds

| Premise Type | Decay Days | Rationale |
|--------------|------------|-----------|
| API documentation | 90 | APIs change quarterly |
| Product requirements | 30 | Requirements evolve fast |
| Performance measurements | 7 | Performance varies frequently |
| External facts | 180 | Third-party info relatively stable |
| Code behavior | 14 | Code changes often |
| Architectural decisions | 180 | Architecture changes slowly |
| Team knowledge | 60 | Team composition shifts |
| Security specs | 90 | Security requirements update regularly |

### Staleness Categories

| Staleness | Status | Action |
|-----------|--------|--------|
| < 0.5 | Fresh | Use freely |
| 0.5 - 1.0 | Aging | Consider verification |
| 1.0 - 2.0 | Stale | Verify before using |
| > 2.0 | Expired | Must re-establish |

---

## Commands

| Command | Action |
|---------|--------|
| `/sr-save` | Save current reasoning session to knowledge base |
| `/sr-query <term>` | Search past decisions by keyword or tag |
| `/sr-context` | Show or update project context |
| `/sr-load <id>` | Load a past decision for reference |
| `/sr-decay` | Check all premises for staleness |
| `/sr-premises [domain]` | List premises, optionally filtered by domain |
| `/sr-outcome <id> <result>` | Record decision outcome (success/partial/failure) |
| `/sr-learn` | Batch update confidences from recent outcomes |
| `/sr-confidence <id>` | Show confidence history and trajectory |
| `/sr-evolve` | Trigger evolution pass on recent memories |
| `/sr-hubs` | Show high-connectivity hub memories |

### Command Details

#### `/sr-save`

Saves the current reasoning session to the knowledge base.

**Prompts for:**
- Decision ID (auto-generated from date + slug)
- Title (human-readable)
- Tags for categorization
- Evidence sources

**Output:**
```
Saved decision: 2025-01-16-api-architecture
  Title: API Architecture Decision
  Mode: deep
  Atoms: P:4 R:3 H:2 V:2 BA:1 C:1
  Confidence: 0.87
  Tags: architecture, api, scaling

Auto-linked to 2 related decisions:
  - 2025-01-10-scaling-decision (0.45 similarity)
  - 2025-01-05-db-architecture (0.38 similarity)

Extracted 3 reusable premises to api-premises.json
```

#### `/sr-query <term>`

Search past decisions and premises with learning-weighted ranking.

**Examples:**
```
/sr-query architecture
→ Found 2 decisions (ranked by confidence × recency × keyword match):
  1. 2025-01-16-api-architecture (score: 0.82) - REST with horizontal scaling
     Confidence: 0.90 | Outcome: success | Used: 8 times
  2. 2025-01-05-db-architecture (score: 0.68) - PostgreSQL with read replicas
     Confidence: 0.78 | Outcome: partial | Used: 3 times

/sr-query #caching
→ Found 1 decision with tag 'caching':
  1. 2025-01-18-cache-strategy (score: 0.85) - Redis with write-through
     Confidence: 0.85 | Outcome: null | Used: 2 times
```

#### `/sr-outcome <id> <success|partial|failure>`

Record the outcome of a decision and trigger confidence updates.

**Output:**
```
/sr-outcome 2025-01-16-api-architecture success

Recorded outcome: success
  Decision: 2025-01-16-api-architecture
  Previous confidence: 0.87
  New confidence: 0.90
  Outcome date: 2025-01-20T14:30:00Z

Propagating to linked memories:
  - 2025-01-10-scaling-decision: 0.82 → 0.83
  - api-rate-limit (premise): 0.95 → 0.96

Updating 3 premises used in this decision:
  - api-rate-limit: outcome_history updated
  - api-auth-method: outcome_history updated
  - team-experience: outcome_history updated
```

#### `/sr-learn`

Batch process recent outcomes and update confidence scores.

**Output:**
```
/sr-learn

Learning Pass Results
=====================
Processed 5 decisions with outcomes since last pass

Confidence updates:
  ↑ 2025-01-16-api-architecture: 0.87 → 0.90 (success)
  ↓ 2025-01-12-auth-approach: 0.82 → 0.70 (failure)
  - 2025-01-18-cache-strategy: 0.85 → 0.85 (partial)
  ↑ 2025-01-19-logging-format: 0.75 → 0.80 (success)
  ↑ 2025-01-20-error-handling: 0.78 → 0.82 (success)

Propagated to 12 linked memories
Updated learning_stats in context.json
```

#### `/sr-confidence <id>`

Show confidence history and trajectory for a decision.

**Output:**
```
/sr-confidence 2025-01-16-api-architecture

Confidence History: 2025-01-16-api-architecture
===============================================
Title: API Architecture Decision
Current confidence: 0.90 (↑ trending)

Timeline:
  2025-01-16  0.87  Created (Deep Mode)
  2025-01-18  0.88  Propagation from related success
  2025-01-20  0.90  Outcome: success

Usage: 8 references | Last used: 2025-01-22
Outcome: success (recorded 2025-01-20)

Premises from this decision:
  - api-rate-limit: 0.96 (5 outcomes, 80% success)
  - api-auth-method: 0.98 (3 outcomes, 100% success)
```

#### `/sr-evolve`

Trigger manual evolution pass on recent memories.

**Output:**
```
/sr-evolve

Memory Evolution Pass
=====================
Scanning memories from last 7 days...

Updated 3 memories with new context:
  1. 2025-01-16-api-architecture
     + Context: New caching decision builds on this
     + Links: 2025-01-20-caching-strategy

  2. 2025-01-18-cache-strategy
     + Context: Performance audit validated assumptions
     + Links: 2025-01-22-performance-audit

  3. api-rate-limit (premise)
     + Context: Confirmed in production load test
     + Used by: 2025-01-22-performance-audit

Hub status changes:
  ↑ 2025-01-16-api-architecture now a hub (6 references)
```

#### `/sr-hubs`

Show high-connectivity hub memories.

**Output:**
```
/sr-hubs

Hub Memories (5+ references)
============================
1. 2025-01-16-api-architecture
   References: 8 | Confidence: 0.90 | Outcome: success
   Tags: architecture, api, scaling
   Last used: 2025-01-22

2. api-rate-limit (premise)
   References: 6 | Confidence: 0.96 | Domain: api
   Used in: 6 decisions | Success rate: 83%

3. 2025-01-05-db-architecture
   References: 5 | Confidence: 0.78 | Outcome: partial
   Tags: database, postgresql, replication
   Last used: 2025-01-20

These memories are central to project knowledge.
```

#### `/sr-decay`

Check all premises for staleness.

**Output:**
```
Premise Staleness Report
========================
Fresh (< 50%):     8 premises
Aging (50-100%):   3 premises
Stale (> 100%):    2 premises
Expired (> 200%):  0 premises

Stale premises requiring attention:
  - api-rate-limit (api): 95 days old, threshold 90 days
    Staleness: 1.05 (mitigated by 5 uses → effective: 0.47)
  - team-size (org): 45 days old, threshold 30 days
    Staleness: 1.50 (0 uses → no mitigation)

Run /sr-premises to see full list
```

#### `/sr-premises [domain]`

List premises, optionally filtered by domain.

**Output:**
```
/sr-premises api

API Premises (6 total)
======================
Fresh:
  [0.96] api-rate-limit - 1000 req/min (5 uses, 83% success)
  [0.98] api-auth-method - OAuth 2.0 with JWT (3 uses, 100% success)
  [0.92] api-versioning - Semantic versioning in URL (2 uses)

Aging:
  [0.85] api-timeout - 30s default timeout (1 use, last: 45 days ago)

Stale:
  [0.72] api-endpoints - 47 endpoints total (0 uses, 95 days old)

Run /sr-decay for full staleness report
```

#### `/sr-load <id>`

Load a past decision for reference in current reasoning.

**Output:**
```
Loaded: 2025-01-16-api-architecture
========================================
Title: API Architecture Decision
Problem: Which API architecture for new service?
Mode: Deep | Type: Type-1 | Confidence: 0.90

Conclusion: REST API with 12-node horizontal scaling
Rationale: Better tooling, team familiarity, proven at scale
Outcome: success (2025-01-20)

Key premises (reusable):
  [P1] Service must handle 10k req/s (0.96) - 5 uses
  [P2] Team has 80% REST experience (0.90) - 3 uses

Related decisions:
  - 2025-01-10-scaling-decision (0.83)
  - 2025-01-05-db-architecture (0.79)

Context updates:
  - 2025-01-20: New caching decision builds on this

Reference this decision as: @2025-01-16-api-architecture
```

---

## Integration with Reasoning Modes

### Deep Mode Integration

When in Deep Mode, premises can reference persisted facts with learning context:

```markdown
## [P1] PREMISE (confidence: 0.96)
@api-rate-limit (from api-premises.json)
The API rate limit is 1000 req/min.
Dependencies: none
Source: Persisted premise, last verified 2025-01-16
Usage: 5 decisions | Success rate: 83%
```

### Conclusion Persistence

When a Deep Mode session concludes with high confidence (>=0.85), prompt:

```
Reasoning complete with confidence 0.87
Would you like to save this decision? (/sr-save)
Extracted premises available for reuse: 3

Auto-linking preview:
  - 2025-01-10-scaling-decision (0.45 similarity)
  - 2025-01-05-db-architecture (0.38 similarity)
```

### Consensus Mode Integration

When consensus is reached, all participating perspectives contribute to outcome:

```
Consensus reached: REST with horizontal scaling
Contributing confidences merged from 3 personas
Final confidence: 0.88

Save with: /sr-save
Track outcome later with: /sr-outcome <id> <result>
```

---

## Best Practices

### Do

- Save decisions that might be referenced later
- Tag decisions for discoverability (3-5 tags)
- Extract reusable premises from conclusions
- Record outcomes when you know them
- Run `/sr-learn` periodically to update confidences
- Reference past decisions when relevant to current reasoning
- Check `/sr-hubs` before major decisions
- Run `/sr-decay` periodically on long-running projects
- Use `/sr-evolve` after adding related decisions

### Don't

- Save trivial decisions (Direct Mode outputs)
- Over-tag (3-5 tags is usually sufficient)
- Reference expired premises without re-verification
- Treat persisted decisions as unchangeable truth
- Ignore outcome recording (it powers learning)
- Skip the learning loop on active projects
- Manually edit `related` arrays (let auto-linking handle it)

### Learning Loop Habits

1. **After implementation**: Record outcome within 1-2 weeks
2. **After incidents**: Record failure outcomes immediately
3. **Weekly**: Run `/sr-learn` to batch process
4. **Monthly**: Run `/sr-evolve` and check `/sr-hubs`

---

## Initialization

Run `/sr-init` in a new project to create:
```
Created .claude/reasoning/
  ├── context.json (initialized with learning_stats)
  ├── decisions/ (empty)
  └── premises/ (empty)

Knowledge base ready. Use /sr-save after reasoning sessions.
Learning loop enabled. Use /sr-outcome to record results.
```

---

## Privacy & Security

- Knowledge base is local to the project directory
- No data is sent externally
- All learning and linking happens locally
- Add `.claude/reasoning/` to `.gitignore` if decisions contain sensitive information
- Or commit it for team knowledge sharing (recommended for most projects)

---

## Optional: Forgetful Backend Upgrade

For semantic search capabilities, entity management, and hybrid retrieval, see the optional Forgetful integration guide:

→ [Forgetful Backend](forgetful-backend.md) - SQLite/PostgreSQL storage, embedding-based search, entity relationships
