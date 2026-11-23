---
id: rag-memory-workflow
domain: recherche-wissen
title: "RAG und Agenten-Memory pflegen"
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
  - "Vault oder mem0 Scope"
outputs:
  - "Persistierte Memories"
  - "Retrieval-Testbericht"
risk_level: medium
version: "1.1.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

**Langzeitwissen** strukturiert speichern—mem0/Graphiti/Obsidian—mit Retrieval-Test, keine ungeprüften Memories in System-Prompts.

## Wann nutzen

- Agent soll Projekt-Fakten über Sessions behalten.
- Sichtbarer Vault parallel zu Memory-Layer.
- RAG-Index aktualisieren.

**Wann nicht**

- PII ohne DSGVO-Basis.
- Ungeprüfte ClawHub Memory-Skills ohne verify.
- Secrets in Memory.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| mem0 | LTM SDK | Drop-in |
| Graphiti | KG | Relationen |
| Obsidian | Human readable | Audit |
| embeddings | User choice | RAG |

## System-Prompt / Instruktionen

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

## Arbeitsablauf

1. Faktenliste und Quellen.
2. PII/Secrets Filter.
3. Duplikat-Suche im Store.
4. Write mem0/vault.
5. Retrieval-Test Queries.
6. memory_audit.md.
7. Nutzer bestätigt falsche Memories löschen.

## Qualitätskriterien / Definition of Done

- [ ] Keine Secrets persistiert
- [ ] Retrieval-Test bestanden
- [ ] Quelle pro Fakt
- [ ] ClawHub verified wenn genutzt
- [ ] Löschen mit confirm

## Sicherheit & Freigaben

- ClawHub verify Pflicht.
- DSGVO bei PII.
- API keys env only.

## Fallstricke

- Memory Poisoning aus Chat.
- Duplicate entries.
- Stale facts.
- RAG without citations.
- Unverified ClawHub skill.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Projekt-Fakt in Obsidian.
- **Input:** API rate limit 100rpm, source runbook url.
- **Prompt:**

```text
Persist to obsidian memories/; retrieval test query rate limit.
```

- **Erwartetes Ergebnis:**

```text
note created; retrieval returns 100rpm; audit log.
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Secret ablehnen.
- **Input:** fact contains api_key=sk-...
- **Prompt:**

```text
Reject persistence of secrets.
```

- **Erwartetes Ergebnis:**

```text
No write; error secret detected.
```