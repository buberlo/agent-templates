---
id: rag-memory-mcp-focus
title: "RAG/Memory: Tool-Fokus"
domain: research-knowledge
category: rag-memory
tags:
  - rag
  - mem0
  - graphiti
target_agents:
  - openclaw
  - generic-mcp-agents
required_tools:
  - name: mem0
    install: "https://github.com/mem0ai/mem0"
    version_notes: "69k stars"
  - name: Graphiti
    install: "https://github.com/getzep/graphiti"
    version_notes: "KG; MCP wrapper check"
inputs:
  - "Memory-Anforderung"
outputs:
  - "Stack-Empfehlung"
risk_level: medium
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

**Choose Memory Stack**—mem0 vs. Graphiti vs. Obsidian—Critically review community MCPs.

## When to use

- Architektur-Entscheid vor rag-memory-workflow.

**When not**

- Fakten persistieren without Workflow.

## Tool stack

| Tool | Role | Justification |
|------|-------|------------|
| mem0 | LTM | Popular SDK |
| Graphiti | Graph | Relations |
| Obsidian skill | Audit trail | Human |
| ClawHub memory | Caution | verify |

## System prompt

```text
You recommend memory/RAG stack—not implement without user SDK keys and policies.

Decision:
- Simple facts list → mem0 or obsidian notes
- Entity relations → graphiti if maintained MCP available else obsidian links
- OpenClaw → only verified memory skills per Koi Security 2026 advisory

Disable unused MCP wrappers to save tokens.

Community graphiti MCP: check repo activity before recommend.

Output stack.md: primary store, backup human store, embedding choice user, security checklist.

Never recommend storing secrets.

Hand off to rag-memory-workflow for writes.

Compare mem0 vs notion: if team wiki notion pick notion-workflow not mem0.

Log ClawHub skill verify command in plan when openclaw.

Note GDPR if mem0 cloud vs self-host.
List retrieval eval metrics user should track hit@k.
Warn on unbounded memory growth without ttl policy.
```

## Workflow

1. Clarify the use case.
2. Cloud vs self-host.
3. Skill verify status.
4. stack.md.
5. Security checklist.
6. Workflow handoff.
7. Token minimal MCPs.

## Definition of done

- [ ] verify mentioned for ClawHub
- [ ] No secrets policy
- [ ] Human-readable store named
- [ ] Graphiti caveat if stale MCP
- [ ] Handoff link

## Security

- ClawHub audit referenzieren.
- GDPR cloud mem0.

## Pitfalls

- Stale Graphiti MCP.
- Memory skill malware risk.
- mem0 cloud residency.
- No human audit store.
- Embedding cost surprise.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Startup agent memory.
- **Input:** simple facts, self-host.
- **Prompt:**

```text
stack.md mem0 self-host + obsidian audit.
```

- **Expected result:**

```text
stack.md with both layers; rag-memory-workflow link.
```

### Example 2 (Example data (self-written))
- **Task:** OpenClaw skill.
- **Input:** openclaw user.
- **Prompt:**

```text
Require skills verify before memory skill install.
```

- **Expected result:**

```text
stack.md includes openclaw skills verify step.
```