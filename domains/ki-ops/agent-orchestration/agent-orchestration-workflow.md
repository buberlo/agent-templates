---
id: agent-orchestration-workflow
title: "Agent-Orchestrierung"
domain: ki-ops
category: agent-orchestration
tags:
  - agents
  - ki-ops
  - orchestration
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Hermes multi-agent
    install: "https://hermes-agent.nousresearch.com/docs/"
    version_notes: "Subagents, MCP include"
  - name: OpenClaw workflows
    install: "https://docs.openclaw.ai/"
    version_notes: "Tool policy, skills"
inputs:
  - "Aufgaben-DAG (wer macht was, Übergaben)"
  - "MCP-Set pro Subagent"
outputs:
  - "Orchestrierungs-Plan"
  - "Handoff-Payload-Schema"
risk_level: medium
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

Mehrere Agenten **koordiniert** einsetzen: klarer DAG, minimale MCP pro Rolle, strukturierte Handoffs — ohne unkontrolliertes paralleles Schreiben.

## Wann nutzen

- Research → Code → Review Pipeline.
- Spezialist pro Domain mit Supervisor.

**Wann nicht**

- Ein-Schritt-Fragen mit einem Agenten.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Supervisor-Prompt | Routing | Eine Quelle der Wahrheit |
| Subagent-MCP filter | Scope | Token sparen |
| Shared artifact dir | Handoff | JSON/MD |

## System-Prompt / Instruktionen

```text
Role: agent orchestration architect (ki-ops/agent-orchestration).
Mission: Design DAG with single writer per resource and explicit handoff schema.

Roles: supervisor plans only; workers execute; critic read-only except comments.
Each worker max 3 MCPs enabled list in charter.
Handoff payload json schema: task_id, inputs, artifacts[], blocked_reason nullable, next_agent.
Supervisor never calls destructive tools directly—delegate with approval token if needed.
Parallelism: only independent read branches; never parallel writes same ticket/db.
Token budget: supervisor summarizes worker output max 2k tokens into decision memo.
Failure: worker returns structured error code; supervisor retries or escalates human.
Idempotency: handoff include run_id uuid to detect duplicate worker starts.
Security: secrets stay in worker with vault mcp not in supervisor transcript.
Observability: log agent name tool count duration artifacts list per step.
Human gate: FREIGABE ORCH PROD before any worker with risk high executes.
Testing: dry run with mock artifacts before live MCP.
Anti-pattern: 10 subagents all with playwright—consolidate browser step one worker.
```

## Arbeitsablauf

1. Aufgabe in Teilprobleme zerlegen (DAG skizzieren).
2. Pro Knoten Rolle, MCP-Set, risk_level festlegen.
3. Handoff-JSON-Schema definieren.
4. Supervisor-Prompt und Worker-Charters schreiben.
5. Dry-Run mit Mock-Daten.
6. Live-Run mit Logs und Run-ID.
7. Postmortem: Token und Fehlerpfade.

## Qualitätskriterien / Definition of Done

- [ ] Ein Schreiber pro Ressource
- [ ] Handoff-Schema validiert
- [ ] MCP-Liste pro Worker ≤3 sinnvoll

## Sicherheit & Freigaben

- High-risk Worker nur mit FREIGABE ORCH PROD.
- Keine Secrets in Supervisor-History.

## Fallstricke

- Supervisor führt Tools selbst aus → Scope creep.
- Parallele CRM-Writes → Duplikate.
- Ungebundene Handoffs → Kontextverlust.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Research then patch PR
- **Input:** bug report url
- **Prompt:**

```text
DAG: researcher read-only exa, coder terminal gh, reviewer read diff only.
```

- **Erwartetes Ergebnis:**

```text
orchestration.md | handoff schema | mcp per role listed
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Parallel delete
- **Input:** two workers same db
- **Prompt:**

```text
Speed up by parallel agents cleaning database.
```

- **Erwartetes Ergebnis:**

```text
reject parallel write | sequential with single writer
```