---
id: siem-soc-mcp-focus
title: "SIEM und SOC: MCP/Skill-Fokus"
domain: security
category: siem-soc
tags:
  - siem
  - mcp
  - soc
target_agents:
  - hermes
  - generic-mcp-agents
required_tools:
  - name: SIEM MCP
    install: "org-specific if available"
    version_notes: "read-only role"
  - name: Sentry/security MCP
    install: "app errors optional"
    version_notes: "correlation"
inputs:
  - "Alert context"
  - "Skill contain gate"
outputs:
  - "Investigation summary"
  - "MCP tool audit"
risk_level: high
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

SIEM über MCP **read-only** abfragen; Skill blockiert Containment-Writes — Parallel zu `siem-soc-workflow`.

## Wann nutzen

- MCP-Anbindung an Splunk/Elastic API (read).
- Skill mit CONTAIN_APPROVE Gate.

**Wann nicht:** Wenn MCP write/ SOAR nicht policy-konform.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| SIEM MCP | Query | analyst |
| Skill | Gate | contain block |
| Ticket | Audit | id |

## System-Prompt / Instruktionen

```text
SIEM SOC MCP/Skill focus (security/siem-soc).

MCP tools whitelist: search/query only; ban isolate, delete_index, update_notable.
Skill steps: ingest alert -> MCP query entities -> correlate -> document -> containment suggestion awaiting CONTAIN_APPROVE.
If MCP offers write action, skill must refuse and use ticket template instead.
Log query strings and result counts not raw log bulk.
Cross MCP Sentry only for app errors with same trace id when provided.
Session time bound enforced in MCP parameters.
Disable unrelated MCPs during active incident triage.
PII fields masked in summary.
Handoff to human analyst if MCP auth fails mid-investigation.
```

## Arbeitsablauf

1. Alert in Skill laden.
2. MCP query user/host timeline.
3. Ergebnisse kondensieren.
4. Hypothese dokumentieren.
5. Containment-Vorschlag textuell.
6. CONTAIN_APPROVE abwarten.
7. MCP audit an SOC-Ticket.

## Qualitätskriterien / Definition of Done

- [ ] Kein MCP write ohne APPROVE
- [ ] Queries im Ticket
- [ ] PII maskiert

## Sicherheit & Freigaben

- high risk containment.
- MCP credentials scoped.

## Fallstricke

- MCP returns huge JSON — summarization loss.
- Write tool hidden alias.
- Cross-tenant MCP config error.
- Stale MCP cache.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** MCP read hunt.
- **Input:** host H-1.
- **Prompt:**

```text
MCP query 4h process creates; no isolate.
```

- **Erwartetes Ergebnis:**

```text
47 powershell.exe children flagged; containment not executed
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Block isolate tool.
- **Input:** MCP suggests isolate_host.
- **Prompt:**

```text
Refuse MCP write; output ticket template.
```

- **Erwartetes Ergebnis:**

```text
Skill refused isolate_host; CONTAIN_APPROVE required + human SOAR
```