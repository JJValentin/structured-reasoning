# Structured Reasoning

A unified framework for systematic problem-solving with adaptive mode selection, designed as a Claude Code skill.

## Overview

Structured Reasoning provides multiple reasoning modes that adapt to your problem's complexity:

- **Decision Router**: First determines Type 1 (irreversible) vs Type 2 (reversible) decisions
- **Direct Mode**: Skip reasoning for trivial tasks
- **Light Mode**: Fast, linear, stage-based sequential thinking
- **Deep Mode**: Rigorous, networked reasoning with explicit dependencies and verification
- **Consensus Mode**: Parallel advisors for open-ended problems with multiple viable paths
- **Hybrid Mode**: Start light, escalate to deep when complexity demands

## Quick Start

Simply describe your problem to Claude, and the Decision Router will automatically select the appropriate reasoning mode.

```
User: Should I take this client project?

Claude: [Decision Router: Type 1 (irreversible) -> Deep Mode with EA reminder]
```

```
User: What content should I create this week?

Claude: [Decision Router: Type 2 (reversible) + multiple viable paths -> Consensus Mode]
```

## Installation

### Quick Install (Recommended)

Copy and paste this prompt into Claude Code:

```
Install the structured-reasoning skill from GitHub: https://github.com/JJValentin/structured-reasoning
```

Claude Code will clone the repository into your skills folder and make it available immediately.

### Manual Installation

1. Copy the entire directory to your Claude Code skills folder:
   - Windows: `C:\Users\<username>\.claude\skills\structured-reasoning\`
   - macOS/Linux: `~/.claude/skills/structured-reasoning/`

2. The skill will be automatically available in Claude Code sessions

### Standalone Usage

You can also reference the SKILL.md file directly in your prompts to any Claude instance.

## Features

### Type 1/Type 2 Decision Framework

The router first categorizes decisions:

| Type 1 (Irreversible) | Type 2 (Reversible) |
|-----------------------|---------------------|
| Hard to undo | Easy to undo |
| Taking clients | Content topics |
| Signing contracts | Offer tweaks |
| Major partnerships | Task order |
| **-> Always Deep Mode** | **-> Route by characteristics** |

### Reasoning Modes

#### Direct Mode
For trivial questions - just answer without reasoning overhead.

**Use when:**
- Simple lookups ("What is X?")
- Facts you know
- No decision required

#### Light Mode (Sequential Thinking)
Progress through 5 stages linearly:

1. Problem Definition
2. Research
3. Analysis
4. Synthesis
5. Conclusion

**Use when:**
- Clear linear path
- Time-constrained
- Standard verification needs

#### Deep Mode (Atom of Thoughts)
Build a network of interconnected thought atoms with explicit dependencies:

- **Premise (P)**: Given facts, constraints
- **Reasoning (R)**: Logical deductions
- **Hypothesis (H)**: Proposed solutions
- **Verification (V)**: Tests and validates
- **Bias Audit (BA)**: Checks for reasoning errors
- **Conclusion (C)**: Final recommendations

**Use when:**
- Type 1 (irreversible) decisions
- High stakes requiring certainty
- Complex dependencies
- Need explicit confidence tracking

#### Consensus Mode (Parallel Advisors)
Run multiple parallel "advisors" with different perspectives:

- **Enumerator**: List all options
- **Pattern Matcher**: Match to known solutions
- **First Principles**: Build from fundamentals
- **Contrarian**: Challenge assumptions
- **Pragmatist**: Focus on execution speed

**Use when:**
- Open-ended Type 2 decisions
- Multiple viable paths
- Need to compare trade-offs

#### Hybrid Mode
Start with Light Mode for efficiency, automatically escalate to Deep Mode when complexity warrants.

**Escalation triggers:**
- Confidence drop during synthesis
- Multiple viable paths discovered
- Contradictory information found
- User requests deeper analysis

### Persistence Layer (v2.2+)

Store and query reasoning artifacts across sessions:

- **Decisions**: Complete reasoning chains with conclusions
- **Premises**: Established facts that can be reused
- **Context**: Project-level information that persists
- **Learning**: Outcome tracking with confidence propagation

### Learning Loop (v2.3+)

Improve from experience with SAFLA integration:

- **Outcome Tracking**: Record success/partial/failure for decisions
- **Confidence Propagation**: Update linked memories based on outcomes
- **Memory Evolution**: Living memories that update with new context
- **Hub Detection**: Identify central knowledge nodes

## Documentation

- **[SKILL.md](SKILL.md)**: Complete skill specification
- **[references/light-mode.md](references/light-mode.md)**: Detailed Light Mode guidance
- **[references/deep-mode.md](references/deep-mode.md)**: Atom mechanics and patterns
- **[references/consensus-mode.md](references/consensus-mode.md)**: Parallel advisor patterns
- **[references/mode-selection-guide.md](references/mode-selection-guide.md)**: Decision framework
- **[references/persistence.md](references/persistence.md)**: Knowledge base and learning
- **[references/forgetful-backend.md](references/forgetful-backend.md)**: Optional semantic search upgrade
- **[references/worked-examples.md](references/worked-examples.md)**: Complete walkthroughs

## Examples

### Software Architecture (Deep Mode)

```
Problem: Design a caching layer for a high-traffic e-commerce API

[P1] API handles 50,000 requests per minute (confidence: 0.95)
[P2] Target response time < 50ms (confidence: 0.95)
[R1] 80% read operations would benefit from caching (confidence: 0.88)
[H1] AWS ElastiCache will meet requirements (confidence: 0.70)
[V1] Testing shows all criteria pass (confidence: 0.88)
[BA1] Bias audit: PASS (2 hypotheses, disconfirming evidence sought)
[C1] Deploy ElastiCache cluster (confidence: 0.88)
```

### Content Decision (Consensus Mode)

```
Problem: What content should I create this week?

Enumerator: Tutorial video (0.72)
Pattern Matcher: Twitter thread (0.78) - proven format
First Principles: Blog + Loom walkthrough (0.68)
Contrarian: Skip content, direct outreach (0.55)
Pragmatist: Repurpose existing recording (0.83) <- WINNER

Recommendation: Repurpose recording into thread + carousel
```

## Triggers

Force a specific mode with explicit phrases:

| Trigger | Mode |
|---------|------|
| `think through this` | Auto (Router) |
| `just answer` | Direct |
| `sequential thinking` | Light |
| `get consensus` | Consensus |
| `atom of thoughts` | Deep |
| `Type 1 decision` | Deep + EA reminder |

## Commands

Control sessions with inline commands:

- `/reset` - Clear and start fresh
- `/status` - Show current progress
- `/route` - Show Decision Router output
- `/switch <mode>` - Force mode change
- `/escalate` - Trigger hybrid escalation
- `/ice` - Run ICE scoring on options
- `/sr-save` - Save reasoning to knowledge base
- `/sr-query` - Search past decisions
- `/sr-outcome <id> <result>` - Record decision outcome
- `/sr-learn` - Batch update confidences
- `/sr-hubs` - Show hub memories

## Version

**v2.3.0**

### Changelog

- **v2.3.0**: SAFLA Learning Loop, A-MEM Memory Evolution, Keyword Auto-Linking, Hub Detection, Usage-Weighted Staleness, Optional Forgetful Backend
- **v2.2.0**: Persistence Layer, Competing Hypotheses, Bias Audit, Premise Staleness
- **v2.1.0**: Optimized SKILL.md, Extension Points, Enhanced description
- **v2.0.0**: Decision Router, Direct Mode, Consensus Mode, ICE Integration, EA Integration
- **v1.0.0**: Initial release with Light, Deep, and Hybrid modes

## Sources

Based on research and frameworks from:

- Sequential Thinking MCP (arben-adm)
- Atom of Thoughts for Markov LLM Test-Time Scaling (Teng et al., 2025)
- TerminaI Cognitive Architecture (Prof-Harita, 2025)
- Joshua's Type 1/Type 2 Decision Framework
- Quint Code First Principles Framework (m0n0x41d)
- SAFLA Learning Loop (ruvnet/SAFLA)
- A-MEM Agentic Memory (agiresearch/A-mem, NeurIPS 2025)

## License

MIT License

## Contributing

This skill was developed for Claude Code. To contribute:

1. Fork the repository
2. Create a feature branch
3. Test changes with Claude Code
4. Submit a pull request

## Support

For issues or questions:
- Open an issue on GitHub
- Reference the documentation in the `references/` folder
- Test with the worked examples

---

**Note**: This is a Claude Code skill designed for AI-assisted reasoning. The framework adapts to problem characteristics automatically while remaining transparent and explainable.
