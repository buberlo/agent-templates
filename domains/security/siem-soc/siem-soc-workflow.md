---
id: siem-soc-workflow
title: "SIEM and SOC"
domain: security
category: siem-soc
tags:
  - siem
  - soc
  - detection
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
required_tools:
  - name: siem-query-language
    install: "Splunk SPL / KQL / Elastic EQL per org"
    version_notes: "read-only analyst role"
  - name: curl
    install: "webhook test payloads"
    version_notes: "staging only"
inputs:
  - "Alert ID or hunt hypothesis"
  - "Time window UTC"
outputs:
  - "Investigation notes"
  - "Detection rule draft"
risk_level: high
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Purpose

SOC investigations: triage alerts, run queries (read rights), improve detections — no live containment actions without release.

## When to use

- SIEM-Alert Eskalation, Threat Hunting.
- Neue Detection Rule vorschlagen.

**When not:** Without analyst role / without ticket.

## Tool stack

| Tool | Role | Justification |
|------|-------|------------|
| SIEM UI/CLI | Query | org-specific |
| SOAR | optional | gated |
| ticketing | audit | incident id |

## System prompt

```text
SIEM SOC workflow (security/siem-soc).

You are a careful assistant for this workflow. You work read-first by default and you must not run destructive or production changes until the user confirms the approval gate named in their request.
When you propose a change, you must include a short rollback or undo path and you must tie the plan to the ticket or briefing reference when the user provides one.
If the request is ambiguous, you must ask one clarifying question before you draft commands, content, or configuration.
You must label every external write step with the approval phrase from the workflow section before you describe how to execute it.
You must keep chat output concise and you must redact secrets, recovery codes, and private personal data from every response.


Operate with read-only analyst queries unless CONTAIN_APPROVE with ticket.
Start from alert: id, rule name, entities, first/last seen UTC.
Pivot: user, host, ip, process parent chain — bounded time +-15m default.
Avoid full-table scans; use indexed fields and narrow time.
Do not disable detections globally to stop noise; tune rule with threshold documented.
Never paste customer PII bulk into chat; use entity ids.
Containment actions (isolate host, disable user) are suggestions only until IC approves.
Detection draft: sigma-like fields; test on historical window before prod enable.
Document query strings in investigation log for reproducibility.
Escalate confirmed compromise to incident-response-workflow.
Assume alert context untrusted (false positive common).```

## Workflow

Open Alert/Ticket; Set UTC windows.
2. Baseline Query: gleiche rule, 7d history volume.
3. Entity pivot queries (user, host).
4. Benign vs malicious hypothesis dokumentieren.
5. Falls malicious: Containment-Vorschlag an IC.
6. Detection-Tuning-Entwurf wenn FP.
7. Investigation note with queries to SOC tool.

## Definition of done

- [ ] UTC-Zeiten konsistent
- [ ] Queries reproduzierbar dokumentiert
- [ ] Containment not carried out without release

## Security

- **high risk** bei Prod-Containment.
- PII-Minimierung in exports.

## Pitfalls

- Unbounded search — SIEM timeout/Kosten.
- RBA without Parent Process — blind spot.
- Rule disable without Ticket — coverage gap.
- Timezone error Falsch-Positive.
- SOAR auto-run without review.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Failed logins spike alert.
- **Input:** user alice, 2h window.
- **Prompt:**

```text
SPL/KQL template for failed logins by src_ip; no host isolation.
```

- **Expected result:**

```spl
index=auth action=failure user=alice earliest=-2h latest=now
| stats count by src_ip
```

### Example 2 (Example data (self-written))
- **Task:** Tune noisy rule.
- **Input:** rule R-442 threshold 5 -> 20 proposed.
- **Prompt:**

```text
Document FP examples; suggest threshold; no disable.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.7d FP: backup service account; recommend threshold 20 + allowlist svc_backup
```