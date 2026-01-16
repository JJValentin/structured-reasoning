# Worked Examples

Complete walkthroughs demonstrating each mode in different domains.

---

## Example 1: Software Architecture (Deep Mode)

**Problem**: Design a caching layer for a high-traffic e-commerce API.

**Why Deep Mode**: High stakes architectural decision with multiple viable options requiring rigorous comparison.

---

### Deep Mode Execution

#### Premises

```markdown
## [P1] PREMISE (confidence: 0.95)
API handles 50,000 requests per minute at peak (Black Friday).
Dependencies: none
Source: Production metrics from last year

## [P2] PREMISE (confidence: 0.95)
Current database response time averages 150ms, target is <50ms.
Dependencies: none
Source: Performance requirements document

## [P3] PREMISE (confidence: 0.90)
80% of API calls are read operations on product catalog.
Dependencies: none
Source: Request analytics

## [P4] PREMISE (confidence: 0.85)
Team has 3 months to implement before next Black Friday.
Dependencies: none
Source: Project timeline

## [P5] PREMISE (confidence: 0.88)
Budget allows for ~$3,000/month additional infrastructure.
Dependencies: none
Source: Finance approval
```

#### Reasoning

```markdown
## [R1] REASONING (confidence: 0.88)
Given 80% read operations (P3) and the need to reduce latency by 100ms (P2), 
a read-through cache would eliminate most database calls for hot data.
Dependencies: P2, P3
Logic: Cache hit rate of 80%+ would reduce average response to ~30ms

## [R2] REASONING (confidence: 0.85)
With 50k req/min (P1) and 80% cache-eligible (P3), we need a cache 
supporting ~40k reads/min = ~667 ops/sec minimum.
Dependencies: P1, P3
Logic: 50,000 * 0.80 = 40,000 cacheable requests

## [R3] REASONING (confidence: 0.82)
3-month timeline (P4) favors managed services over self-hosted 
to reduce operational complexity.
Dependencies: P4
Logic: Self-hosted adds 4-6 weeks setup and learning curve
```

#### Hypotheses

```markdown
## [H1] HYPOTHESIS (confidence: 0.70)
AWS ElastiCache (Redis) as managed cache will meet performance 
and timeline requirements.
Dependencies: R1, R2, R3
Testable by: 
- Verify ops/sec capacity
- Confirm setup time <2 weeks
- Check cost within budget

## [H2] HYPOTHESIS (confidence: 0.65)
Self-hosted Redis cluster on existing infrastructure will meet 
requirements at lower cost.
Dependencies: R1, R2
Testable by:
- Verify existing server capacity
- Estimate setup time
- Compare TCO

## [H3] HYPOTHESIS (confidence: 0.55)
Application-level caching (in-memory per instance) could suffice 
without infrastructure changes.
Dependencies: R1
Testable by:
- Verify memory availability per instance
- Test cache consistency across instances
- Measure hit rates with distributed invalidation
```

#### Verification

```markdown
## [V1] VERIFICATION (confidence: 0.88)
Testing H1 (AWS ElastiCache):

| Test | Criterion | Result | Notes |
|------|-----------|--------|-------|
| Throughput | >667 ops/sec | PASS | r6g.large: 100k ops/sec |
| Latency | <5ms cache read | PASS | Sub-millisecond typical |
| Setup time | <2 weeks | PASS | ~3 days with Terraform |
| Cost | <$3k/month | PASS | r6g.large ~$200/month |
| Team experience | Some familiarity | PASS | 2 devs have used Redis |

Overall: 5 PASS, 0 FAIL
Dependencies: H1
Effect: H1 confidence increased from 0.70 to 0.88

## [V2] VERIFICATION (confidence: 0.72)
Testing H2 (Self-hosted Redis):

| Test | Criterion | Result | Notes |
|------|-----------|--------|-------|
| Server capacity | Available resources | WARN | Would need new instance |
| Setup time | <4 weeks | FAIL | Estimated 6-8 weeks |
| Ops burden | Acceptable | WARN | No Redis ops experience |
| Cost | Lower than managed | PASS | ~$100/month compute |

Overall: 1 PASS, 2 WARN, 1 FAIL
Dependencies: H2
Effect: H2 confidence decreased from 0.65 to 0.50

## [V3] VERIFICATION (confidence: 0.45)
Testing H3 (Application-level cache):

| Test | Criterion | Result | Notes |
|------|-----------|--------|-------|
| Memory | <2GB per instance | WARN | Catalog is 1.5GB, tight |
| Consistency | Acceptable staleness | FAIL | Product prices must sync |
| Hit rate | >70% | FAIL | Distributed invalidation complex |
| Complexity | Low | FAIL | Significant app changes needed |

Overall: 0 PASS, 1 WARN, 3 FAIL
Dependencies: H3
Effect: H3 confidence decreased from 0.55 to 0.25 (rejected)
```

#### Conclusion

```markdown
## [C1] CONCLUSION (confidence: 0.88)
Implement AWS ElastiCache (Redis) r6g.large cluster for API caching.

**Recommendation**: 
Deploy 2-node ElastiCache Redis cluster with automatic failover.

**Based on**:
- V1: All verification criteria passed
- H1: Best balance of performance, cost, and timeline
- H2, H3: Rejected due to timeline (H2) and consistency (H3) concerns

**Confidence breakdown**:
- Performance: 0.95 (exceeds requirements by 100x)
- Cost: 0.90 (well under budget at ~$400/month with redundancy)
- Timeline: 0.85 (3 days setup, 2 weeks integration)
- Risk: 0.80 (managed service reduces operational risk)

**Implementation steps**:
1. Week 1: Provision ElastiCache via Terraform
2. Week 2-3: Implement cache-aside pattern in API
3. Week 4: Load testing with production-like traffic
4. Week 5-6: Staged rollout with monitoring
5. Week 7+: Performance tuning based on metrics

**Remaining uncertainties**:
- Cache invalidation strategy needs design
- Cold start behavior on deployment untested
- Cost at 2x traffic (growth scenario) not verified

Dependencies: V1, H1
```

#### Final Status

```
Atoms: P:5 R:3 H:3 V:3 C:1
Depth: 3/5
Best confidence: 0.88 (C1)
Status: TERMINATED - High-confidence conclusion reached
```

---

## Example 2: Debugging (Hybrid Mode)

**Problem**: Users report intermittent 500 errors on the checkout API.

**Why Hybrid**: Starts as simple investigation, escalates when multiple root causes are possible.

---

### Light Mode Start

```markdown
## [Stage 1/5] PROBLEM DEFINITION
Progress: [##________] 20%

**Problem Statement**: 
Checkout API returns HTTP 500 errors intermittently, affecting ~2% of transactions.

**Stakeholders**:
- Users: Lost transactions, frustration
- Business: Revenue loss (~$5k/day estimated)
- Engineering: On-call burden, reputation

**Constraints**:
- Time: Need resolution within 24-48 hours (revenue impact)
- Access: Production logs available, can't reproduce locally
- Risk: Can't deploy breaking changes during peak hours

**Success Criteria**:
- [ ] Error rate < 0.1%
- [ ] Root cause identified and documented
- [ ] Monitoring in place for recurrence

**Out of Scope**:
- General API performance optimization
- Refactoring checkout flow

---
Next: Stage 2 (Research)
```

```markdown
## [Stage 2/5] RESEARCH
Progress: [####______] 40%

**Tags**: #debugging #production #checkout

**Known Facts**:
| Fact | Source | Confidence |
|------|--------|------------|
| Errors started 3 days ago | Logs | High |
| Deployment occurred 4 days ago | CI/CD | High |
| Errors correlate with traffic spikes | Metrics | Medium |
| Database connections spike during errors | APM | Medium |
| Memory usage normal | Monitoring | High |

**Knowledge Gaps**:
| Gap | Impact | Resolution |
|-----|--------|------------|
| Exact query causing timeout | Critical | Enable slow query log |
| Connection pool configuration | High | Check recent config changes |
| Retry behavior of client | Medium | Review client code |

**Assumptions**:
| Assumption | Risk if Wrong |
|------------|---------------|
| Related to recent deployment | May look in wrong place |
| Database is the bottleneck | May miss actual cause |

---
Next: Stage 3 (Analysis)
```

```markdown
## [Stage 3/5] ANALYSIS
Progress: [######____] 60%

**Patterns Observed**:
- Errors cluster at :00 and :30 minutes (cron jobs?)
- 90% of errors are on `/checkout/complete` endpoint
- Stack traces show connection timeout to payment service

**Options Identified**:
| Root Cause | Evidence | Confidence |
|------------|----------|------------|
| A: Database connection exhaustion | Pool metrics spike | Medium |
| B: Payment service timeout | Stack traces | Medium |
| C: Cron job resource contention | Timing pattern | Low-Medium |

**ESCALATION TRIGGER DETECTED**:
Multiple viable root causes identified. Evidence is mixed.
Cannot differentiate without rigorous hypothesis testing.

-> Escalating to Deep Mode for verification
```

### Escalation to Deep Mode

```markdown
## ESCALATION: Light -> Deep Mode

**Trigger**: Multiple viable root causes with overlapping evidence
**Preserving**: Problem definition and research findings

### Converted Atoms:

## [P1] PREMISE (confidence: 0.95)
Errors started 3 days ago, deployment was 4 days ago.
Dependencies: none

## [P2] PREMISE (confidence: 0.85)
Stack traces show "Connection timeout" to payment service.
Dependencies: none

## [P3] PREMISE (confidence: 0.80)
Errors correlate with traffic spikes at :00 and :30.
Dependencies: none

## [R1] REASONING (confidence: 0.78)
Timing correlation (P3) suggests scheduled job interference,
but stack traces (P2) point to payment service.
These could be related: cron job causes resource contention
affecting payment service calls.
Dependencies: P2, P3

### New Hypotheses:

## [H1] HYPOTHESIS (confidence: 0.60)
Database connection pool exhaustion during traffic spikes
causes cascading timeouts to payment service.
Dependencies: R1, P1
Testable by: Check connection pool metrics during error windows

## [H2] HYPOTHESIS (confidence: 0.55)
Payment service itself is degraded, unrelated to our deployment.
Dependencies: P2
Testable by: Check payment service status page, contact provider

## [H3] HYPOTHESIS (confidence: 0.50)
Cron job at :00/:30 competes for same resources as checkout.
Dependencies: P3
Testable by: Correlate cron execution with error timestamps
```

### Deep Mode Verification

```markdown
## [V1] VERIFICATION (confidence: 0.85)
Testing H1 (Connection pool exhaustion):

| Test | Result | Notes |
|------|--------|-------|
| Pool metrics at error time | PASS | Max connections hit |
| Pool size vs traffic | PASS | Pool=20, need=35 at peak |
| Recent config change | PASS | Pool reduced in deployment |
| Timeout matches pool wait | PASS | 30s timeout = pool wait time |

Conclusion: H1 verified. Connection pool was reduced from 50 to 20
in recent deployment (config file change, likely unintentional).

Effect: H1 confidence 0.60 -> 0.92

## [V2] VERIFICATION (confidence: 0.70)
Testing H2 (Payment service degraded):

| Test | Result | Notes |
|------|--------|-------|
| Status page | FAIL | No reported issues |
| Direct API test | FAIL | Response time normal |
| Other clients affected | FAIL | Only us seeing errors |

Conclusion: H2 rejected. Payment service is healthy.

Effect: H2 confidence 0.55 -> 0.20 (rejected)

## [V3] VERIFICATION (confidence: 0.65)
Testing H3 (Cron job contention):

| Test | Result | Notes |
|------|--------|-------|
| Cron timing correlation | PARTIAL | Some overlap but not all errors |
| Cron resource usage | FAIL | CPU/memory normal during cron |

Conclusion: H3 is secondary factor at best, not root cause.

Effect: H3 confidence 0.50 -> 0.35
```

### Conclusion

```markdown
## [C1] CONCLUSION (confidence: 0.92)
Root cause: Database connection pool misconfiguration in recent deployment.

**The Fix**:
1. Restore connection pool from 20 to 50 (immediate)
2. Add connection pool monitoring alert
3. Add config validation to CI/CD pipeline

**Evidence chain**:
P1 (deployment timing) -> H1 (pool exhaustion) -> V1 (verified)
Pool was reduced from 50->20, causing exhaustion at 35+ concurrent requests.

**Verification of fix**:
- Deploy config change: 5 minutes
- Monitor error rate: Should drop to <0.1% within 1 hour
- Confirm pool metrics show headroom

Dependencies: V1, H1
```

---

## Example 3: Business Decision (Deep Mode)

**Problem**: Should we build a custom analytics dashboard or buy a SaaS solution?

**Why Deep Mode**: Major investment decision requiring explicit trade-off analysis and confidence tracking.

---

### Deep Mode Execution

```markdown
## [P1] PREMISE (confidence: 0.95)
We need analytics dashboard within 6 months for board reporting.
Dependencies: none

## [P2] PREMISE (confidence: 0.90)
Engineering team has 2 available developers for 3 months max.
Dependencies: none

## [P3] PREMISE (confidence: 0.88)
Budget is $50k one-time or $2k/month ongoing.
Dependencies: none

## [P4] PREMISE (confidence: 0.85)
Required features: real-time metrics, custom reports, API access.
Dependencies: none

## [P5] PREMISE (confidence: 0.80)
Data is sensitive (PII), must meet SOC2 requirements.
Dependencies: none
```

```markdown
## [R1] REASONING (confidence: 0.85)
2 developers for 3 months (P2) = 6 person-months capacity.
Industry benchmark for custom dashboard: 4-8 person-months.
This is achievable but leaves no buffer for issues.
Dependencies: P2

## [R2] REASONING (confidence: 0.82)
$50k one-time (P3) vs $2k/month = break-even at 25 months.
If build takes 6 person-months at $15k/month loaded cost = $90k.
Build is more expensive unless used 4+ years.
Dependencies: P3

## [R3] REASONING (confidence: 0.80)
SOC2 requirement (P5) adds complexity to build (audit, documentation).
Most established SaaS vendors already have SOC2 certification.
Dependencies: P5
```

```markdown
## [H1] HYPOTHESIS (confidence: 0.65)
Buy SaaS solution (e.g., Metabase Cloud, Looker, Tableau) 
is the better choice for our situation.
Dependencies: R1, R2, R3
Testable by: Evaluate specific vendors against requirements

## [H2] HYPOTHESIS (confidence: 0.55)
Build custom dashboard using open-source tools (Metabase self-hosted)
provides better long-term value and control.
Dependencies: R1
Testable by: Estimate true cost and timeline with buffer
```

```markdown
## [V1] VERIFICATION (confidence: 0.82)
Testing H1 (Buy SaaS):

| Criterion | Metabase Cloud | Looker | Tableau |
|-----------|---------------|--------|---------|
| Real-time metrics | PASS | PASS | PASS |
| Custom reports | PASS | PASS | PASS |
| API access | PASS | PASS | PASS |
| SOC2 certified | PASS | PASS | PASS |
| Cost/month | $500 | $3000 | $1500 |
| Setup time | 1 week | 4 weeks | 2 weeks |
| Within budget | PASS | FAIL | PASS |

Best option: Metabase Cloud at $500/month
- All features met
- 1 week setup (vs 6 month deadline)
- $500/month << $2k budget
- SOC2 compliant

Effect: H1 confidence 0.65 -> 0.88

## [V2] VERIFICATION (confidence: 0.60)
Testing H2 (Build with self-hosted):

| Criterion | Result | Notes |
|-----------|--------|-------|
| Timeline achievable | WARN | 6mo is tight, no buffer |
| Cost competitive | FAIL | $90k build > $30k (5yr SaaS) |
| SOC2 compliance | WARN | 2+ months additional work |
| Team capacity | WARN | Blocks other priorities |
| Maintenance burden | FAIL | Ongoing ops not budgeted |

Build option has significant risks and hidden costs.

Effect: H2 confidence 0.55 -> 0.35
```

```markdown
## [C1] CONCLUSION (confidence: 0.88)
**Recommendation**: Buy Metabase Cloud at $500/month.

**Rationale**:
1. Meets all functional requirements (P4) 
2. SOC2 compliant out-of-box (P5)
3. 1-week setup vs 6-month timeline (P1) - massive buffer
4. $500/month well under $2k budget (P3)
5. Frees engineering capacity for core product (P2)

**5-year TCO comparison**:
- Metabase Cloud: $500 x 60 = $30,000
- Build: $90k build + $10k/yr maintenance = $140,000

**Decision confidence**: 0.88
- Strong on: cost, timeline, compliance
- Moderate on: long-term flexibility (vendor lock-in risk)

**Recommended next steps**:
1. Start Metabase Cloud trial this week
2. Validate data connection to our warehouse
3. Build first dashboard as POC
4. Present to board for sign-off
5. Full rollout within 1 month

Dependencies: V1, H1
```

---

## Example 4: General Problem-Solving (Light Mode)

**Problem**: Plan a team offsite event for 25 people.

**Why Light Mode**: Clear goal, straightforward planning, no competing hypotheses to verify.

---

### Light Mode Execution

```markdown
## [Stage 1/5] PROBLEM DEFINITION
Progress: [##________] 20%

**Problem Statement**: 
Plan a 2-day team offsite for 25 people within 6 weeks and $15k budget.

**Stakeholders**:
- Team members: Want valuable, enjoyable experience
- Leadership: Want team bonding and strategic alignment
- Finance: Want cost control and proper expense tracking

**Constraints**:
- Time: 6 weeks to plan, event is 2 days
- Budget: $15,000 total ($600/person)
- Logistics: Mix of remote and local team members (travel needed for 10)
- Dates: Must avoid Q4 close (accounting) and product launch

**Success Criteria**:
- [ ] 90%+ attendance
- [ ] Post-event survey satisfaction > 4/5
- [ ] Within budget
- [ ] Mix of work sessions and team bonding

**Out of Scope**:
- Regular team meetings (this is special event)
- Individual travel reimbursement (handled separately)

---
Next: Stage 2 (Research)
```

```markdown
## [Stage 2/5] RESEARCH
Progress: [####______] 40%

**Tags**: #event-planning #team-building #offsite

**Known Facts**:
| Fact | Source |
|------|--------|
| 25 attendees (15 local, 10 remote) | HR roster |
| Available dates: Oct 15-16 or Oct 22-23 | Calendar check |
| Dietary restrictions: 3 vegetarian, 1 gluten-free | Team survey |
| Previous offsite was 18 months ago | Records |
| Most requested: outdoor activities | Survey |

**Knowledge Gaps**:
| Gap | Resolution |
|-----|------------|
| Venue availability | Send RFPs this week |
| Flight costs for remote | Get quotes |
| Team preferences on location | Quick poll |

**Prior Art**:
- Last offsite: Conference room + dinner, rated 3.5/5
- Feedback: "Too many meetings, not enough bonding"

**Assumptions**:
| Assumption | Risk |
|------------|------|
| Oct dates work for everyone | May have conflicts |
| $600/person is sufficient | Venue costs vary |

---
Next: Stage 3 (Analysis)
```

```markdown
## [Stage 3/5] ANALYSIS
Progress: [######____] 60%

**Tags**: #venue #activities #budget

**Patterns from research**:
- Team wants more bonding, less meetings
- Previous event too formal, low engagement
- Outdoor activities highly requested

**Venue Options**:
| Option | Pros | Cons | Est. Cost |
|--------|------|------|-----------|
| A: Mountain retreat | Outdoor, scenic, bonding | Remote, limited WiFi | $8k |
| B: Urban hotel | Convenient, WiFi, restaurants | Less unique, "work-like" | $10k |
| C: Beach resort | Fun, relaxed, outdoor | Further travel, distracting | $12k |

**Budget Breakdown Analysis**:
| Category | Estimate | Notes |
|----------|----------|-------|
| Venue (2 days) | $6-10k | Depends on choice |
| Travel (10 remote) | $3-5k | Flights + ground |
| Food/beverage | $2-3k | All meals included |
| Activities | $1-2k | Team building, supplies |
| Buffer | $1k | Unexpected costs |
| **Total** | **$13-21k** | Option A fits, B/C tight |

**Assumptions Challenged**:
- "Need WiFi for work sessions" -> Can we go WiFi-free for bonding focus?

---
Next: Stage 4 (Synthesis)
```

```markdown
## [Stage 4/5] SYNTHESIS
Progress: [########__] 80%

**Recommended Approach**: Option A - Mountain Retreat

**Rationale**:
- Addresses feedback: More bonding, less formal
- Fits budget: $8k venue + $4k travel + $2k food + $1k buffer = $15k
- Unique experience: Different from office/hotel
- Outdoor activities: Top team request

**Risk Mitigations**:
| Risk | Mitigation |
|------|------------|
| Limited WiFi | Embrace it - 1 focused work session only |
| Weather | Indoor backup activities, Oct is mild |
| Travel logistics | Arrange group transport from airport |
| Dietary needs | Confirm with venue in advance |

**Proposed Agenda**:
| Day 1 | Day 2 |
|-------|-------|
| 10am: Arrivals, settle in | 8am: Breakfast |
| 12pm: Lunch | 9am: Strategic planning (2hr) |
| 1pm: Team building activity (outdoor) | 11am: Outdoor hike |
| 5pm: Free time | 1pm: Lunch & departures |
| 7pm: Group dinner |  |
| 9pm: Bonfire/social |  |

**Stakeholder Considerations**:
| Stakeholder | Concern | Response |
|-------------|---------|----------|
| Leadership | Enough work content? | 2-hour focused session |
| Team | Too remote? | Group transport, phone signal OK |
| Finance | Budget tracking? | All-inclusive venue simplifies |

---
Next: Stage 5 (Conclusion)
```

```markdown
## [Stage 5/5] CONCLUSION
Progress: [##########] 100%

**RECOMMENDATION**: 
Book Mountain Retreat for Oct 22-23, emphasizing team bonding with one focused work session.

**Key Reasoning**:
1. Directly addresses "too many meetings" feedback from last event
2. Within budget at $15k including buffer
3. Outdoor/unique setting matches team survey preferences
4. 2-hour work session satisfies leadership alignment goals

**Immediate Next Steps**:
| Step | Owner | Deadline | Deliverable |
|------|-------|----------|-------------|
| Confirm venue availability | Event lead | This Friday | Signed contract |
| Book group flights | Admin | Next Monday | Itineraries |
| Send calendar invites | Event lead | Next Tuesday | 90%+ RSVPs |
| Confirm dietary needs | Admin | 2 weeks out | Final count to venue |
| Prepare work session agenda | Leadership | 1 week out | Session outline |

**Decision Points**:
- Oct 22-23 vs Oct 15-16: Confirm with leadership by Friday
- Activity choice: Finalize after venue walkthrough

**Revisit If**:
- More than 3 people can't make either date
- Venue cost exceeds $9k (need to cut elsewhere)
- Weather forecast is severe

**Success Metrics**:
| Metric | Target | Measurement |
|--------|--------|-------------|
| Attendance | >90% (23+) | Headcount |
| Satisfaction | >4/5 | Post-event survey |
| Budget | <$15k | Expense report |

---
COMPLETE
```

---

## Summary: Mode Selection by Example

| Example | Domain | Mode Used | Why |
|---------|--------|-----------|-----|
| Caching layer | Software Architecture | Deep | High stakes, multiple options |
| 500 errors | Debugging | Hybrid | Started simple, escalated on complexity |
| Build vs Buy | Business Decision | Deep | Major investment, needed confidence |
| Team offsite | General | Light | Clear goal, straightforward planning |
