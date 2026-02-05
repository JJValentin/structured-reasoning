# Forgetful Backend (Optional Upgrade)

> **Note:** This document describes an optional upgrade to the Structured Reasoning persistence layer. The default JSON + keyword system works without any installation. Add Forgetful when you want semantic search capabilities.

---

## Detection & Fallback Logic

The persistence layer auto-detects which backend to use:

```
if (forgetful_mcp_available):
    use Forgetful backend (semantic search, entity management)
else:
    use JSON + keyword backend (default)
```

**All extensions work with EITHER backend:**
- SAFLA learning cycles
- A-MEM memory evolution
- Staleness decay and refresh
- Confidence scoring and ranking

The switch is transparent—your workflow remains identical.

---

## Installation

**Option 1: Direct install**
```bash
uvx forgetful-ai
```

**Option 2: Claude Code MCP configuration**

Add to your MCP settings:
```json
{
  "mcpServers": {
    "forgetful": {
      "command": "uvx",
      "args": ["forgetful-ai"]
    }
  }
}
```

Restart Claude Code after configuration. The system will auto-detect Forgetful on next `/sr-save` or `/sr-query`.

---

## Benefits Comparison

| Capability | Without Forgetful | With Forgetful |
|------------|-------------------|----------------|
| **Search** | Keyword matching | Semantic + hybrid retrieval |
| **Linking** | Jaccard similarity | Embedding-based auto-linking (0.7 threshold) |
| **Storage** | JSON files | SQLite (ACID-compliant, upgradeable to PostgreSQL) |
| **Entities** | Not supported | First-class entities (people, projects, clients) |
| **Context** | Manual assembly | Token budget management (8K default) |
| **Graph** | Keyword co-occurrence | 1-hop traversal with typed relationships |

---

## Command Behavior Mapping

Commands adapt automatically based on detected backend:

| Command | JSON Backend | Forgetful Backend |
|---------|--------------|-------------------|
| `/sr-save` | JSON file + keyword extraction | `create_memory` + embedding generation |
| `/sr-query` | Keyword + confidence ranking | Hybrid retrieval (Dense + BM25 + RRF + cross-encoder) |
| `/sr-load` | JSON read + related lookup | `get_memory` + 1-hop graph traversal |
| `/sr-context` | context.json read | `get_project` with entity context |

---

## Additional Commands (Forgetful Only)

These commands require Forgetful and will error gracefully if unavailable:

| Command | Action |
|---------|--------|
| `/sr-entity <type> <name>` | Create/link entities (types: `person`, `project`, `client`, `organization`) |
| `/sr-relate <entity1> <entity2> <type>` | Create typed relationships (e.g., `works_on`, `depends_on`, `supersedes`) |
| `/sr-graph <id>` | Visualize 1-hop memory network from specified memory |
| `/sr-budget [tokens]` | View or set token budget for context retrieval (default: 8192) |

### Entity Examples

```
/sr-entity person "Sarah Chen"
/sr-entity project "Q1 Launch"
/sr-entity client "Acme Corp"

/sr-relate "Sarah Chen" "Q1 Launch" works_on
/sr-relate "Q1 Launch" "Acme Corp" deliverable_for
```

---

## Architecture Reference

```
┌─────────────────────────────────────────────────────────────┐
│                    MCP Transport Layer                       │
│                  (stdio or HTTP protocol)                    │
├─────────────────────────────────────────────────────────────┤
│                     Service Layer                            │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐           │
│  │Memories │ │Entities │ │Projects │ │Documents│           │
│  │(atomic) │ │(people, │ │(scoped  │ │(long-   │           │
│  │300-400w │ │ orgs)   │ │ context)│ │  form)  │           │
│  └─────────┘ └─────────┘ └─────────┘ └─────────┘           │
├─────────────────────────────────────────────────────────────┤
│                    Storage Layer                             │
│           SQLite (default) / PostgreSQL (production)         │
├─────────────────────────────────────────────────────────────┤
│                   Retrieval Layer                            │
│  Dense Vector → BM25 Sparse → RRF Fusion → Cross-Encoder    │
│                    + 1-hop linked memories                   │
└─────────────────────────────────────────────────────────────┘
```

---

## Retrieval Pipeline

1. **Dense Vector** — Semantic similarity via embeddings
2. **BM25 Sparse** — Keyword relevance scoring
3. **RRF Fusion** — Reciprocal Rank Fusion combines both signals
4. **Cross-Encoder** — Re-ranks top candidates for precision
5. **1-hop Expansion** — Includes directly linked memories

---

## When to Upgrade

### Stay with JSON backend when:
- Memory count < 50
- Keyword search sufficient
- Minimal entity relationships
- Simplicity preferred

### Upgrade to Forgetful when:
- Memory count > 50
- Semantic search needed ("find memories about X concept")
- Entity relationships matter (people, projects, clients)
- Cross-session context retrieval critical
- Production deployment planned (PostgreSQL path)

The default system is production-ready. Forgetful is an enhancement, not a requirement.

---

## Resources

| Resource | Link |
|----------|------|
| GitHub Repository | https://github.com/ScottRBK/forgetful |
| Claude Code Plugin | https://github.com/ScottRBK/forgetful-plugin |
| Introduction Article | https://dev.to/scott_raisbeck_24ea5fbc1e/introducing-forgetful-shared-knowledge-and-memory-across-agents-40o6 |
