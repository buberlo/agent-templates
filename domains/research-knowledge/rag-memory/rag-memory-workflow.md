---
id: rag-memory-workflow
title: "Keep RAG and Agent Memory"
domain: research-knowledge
category: rag-memory
tags:
  - rag
  - memory
  - mem0
target_agents:
  - hermes
  - openclaw
  - generic
required_tools:
  - name: mem0
    install: "https://github.com/mem0ai/mem0"
    version_notes: "SDK optional"
  - name: Obsidian skill
    install: "Hermes bundled /obsidian"
    version_notes: "Visible store"
inputs:
  - "Fakten zum Persistieren"
  - "Vault or mem0 Scope"
outputs:
  - "Persistierte Memories"
  - "Retrieval-Testbericht"
risk_level: medium
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

**Long-term knowledge** structured storage—mem0/Graphiti/Obsidian—with retrieval testing, no untested memories in system prompts.

## When to use

- Agent should keep project facts about sessions.
- Sichtbarer Vault parallel zu Memory-Layer.
- RAG-Index aktualisieren.

**When not**

- PII without DSGVO-Basis.
- Unverified ClawHub memory skills without verify.
- Secrets in Memory.

## Tool stack

| Tool | Role | Justification |
|------|-------|------------|
| mem0 | LTM SDK | Drop-in |
| Graphiti | KG | Relationen |
| Obsidian | Human readable | Audit |
| embeddings | User choice | RAG |

## System prompt

```text
You manage agent long-term memory with explicit user-approved facts only.

Inputs: facts[] with source url or user attestation, store (obsidian|mem0|both), namespace/project_id, ttl optional, output memory_audit.md.

Rules:
- Never persist passwords, tokens, health data, or legal accusations.
- Each memory entry: text, source, created_at, confidence user|verified|inferred.
- inferred only when user allows; default user attested.

Before write: show diff of new vs existing search in vault/mem0.

After write: retrieval test—query must return new fact.

Obsidian path: memories/YYYY-MM-topic.md frontmatter tags memory.

mem0: use SDK user configures; agent does not embed API key in repo.

Graphiti only when user has MCP and wants relations—not default.

ClawHub memory skills: require openclaw skills verify per security advisory.

Approvals: delete memory bulk requires typed confirm.

Output: memory_audit.md, retrieval_test results.

Do not overwrite human notes in obsidian without merge strategy.

Periodic stale check: mark memories older than ttl REVIEW.

Reject contradictory new fact without user resolution note.

Chunk long docs for RAG with citation to source file path.
Log embedding model name when indexing.
```

## Workflow

1. Fact list and sources.
2. PII/Secrets Filter.
3. Duplikat-Suche im Store.
4. Write mem0/vault.
5. Retrieval-Test Queries.
6. memory_audit.md.
7. User confirms to delete false memories.

## Definition of done

- [ ] No Secrets persistiert
- [ ] Retrieval-Test bestanden
- [ ] Source per fact
- [ ] ClawHub verified wenn genutzt
- [ ] Delete with confirm

## Security

- ClawHub verify Pflicht.
- DSGVO bei PII.
- API keys env only.

## Pitfalls

- Memory Poisoning aus Chat.
- Duplicate entries.
- Stale facts.
- RAG without citations.
- Unverified ClawHub skill.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Projekt-Fakt in Obsidian.
- **Input:** API rate limit 100rpm, source runbook url.
- **Prompt:**

```text
Persist to obsidian memories/; retrieval test query rate limit.
```

- **Expected result:**

```text
note created; retrieval returns 100rpm; audit log.
```

### Example 2 (Example data (self-written))
- **Task:** Secret ablehnen.
- **Input:** fact contains api_key=sk-...
- **Prompt:**

```text
Reject persistence of secrets.
```

- **Expected result:**

```text
No write; error secret detected.
```