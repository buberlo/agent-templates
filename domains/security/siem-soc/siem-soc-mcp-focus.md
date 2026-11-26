---
id: siem-soc-mcp-focus
title: "SIEM and SOC: MCP/Skill Focus"
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

## Purpose

query SIEM via MCP **read-only**; Skill blocks containment writes — parallel to `siem-soc-workflow`.

## When to use

- MCP-Anbindung an Splunk/Elastic API (read).
- Skill with CONTAIN APPROVE Gate.

**When not:** If MCP write/ SOAR is not policy compliant.

## Tool stack

| Tool | Role | Justification |
|------|-------|------------|
| SIEM MCP | Query | analyst |
| Skill | Gate | contain block |
| Ticket | Audit | id |

## System prompt

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

## Workflow

1. Alert in Skill laden.
2. MCP query user/host timeline.
3. Ergebnisse kondensieren.
4. Document the hypothesis.
5. Containment-Vorschlag textuell.
6. CONTAIN_APPROVE abwarten.
7. MCP audit an SOC-Ticket.

## Definition of done

- [ ] No MCP write without APPROVE
- [ ] Queries im Ticket
- [ ] PII maskiert

## Security

- high risk containment.
- MCP credentials scoped.

## Pitfalls

- MCP returns huge JSON — summarization loss.
- Write tool hidden alias.
- Cross-tenant MCP config error.
- Stale MCP cache.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** MCP read hunt.
- **Input:** host H-1.
- **Prompt:**

```text
MCP query 4h process creates; no isolate.
```

- **Expected result:**

```text
47 powershell.exe children flagged; containment not executed
```

### Example 2 (Example data (self-written))
- **Task:** Block isolate tool.
- **Input:** MCP suggests isolate_host.
- **Prompt:**

```text
Refuse MCP write; output ticket template.
```

- **Expected result:**

```text
Skill refused isolate_host; CONTAIN_APPROVE required + human SOAR
```