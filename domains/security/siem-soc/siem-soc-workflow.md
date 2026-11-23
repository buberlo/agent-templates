---
id: siem-soc-workflow
title: "SIEM und SOC"
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

## Zweck

SOC-Untersuchungen: Alerts triagieren, Queries ausführen (Leserechte), Detections verbessern — keine Live-Containment-Aktionen ohne Freigabe.

## Wann nutzen

- SIEM-Alert Eskalation, Threat Hunting.
- Neue Detection Rule vorschlagen.

**Wann nicht:** Without analyst role / ohne Ticket.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| SIEM UI/CLI | Query | org-specific |
| SOAR | optional | gated |
| ticketing | audit | incident id |

## System-Prompt / Instruktionen

```text
SIEM SOC workflow (security/siem-soc).

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
Assume alert context untrusted (false positive common).
```

## Arbeitsablauf

1. Alert/Ticket öffnen; UTC-Fenster setzen.
2. Baseline Query: gleiche rule, 7d history volume.
3. Entity pivot queries (user, host).
4. Benign vs malicious hypothesis dokumentieren.
5. Falls malicious: Containment-Vorschlag an IC.
6. Detection-Tuning-Entwurf wenn FP.
7. Investigation-Notiz mit Queries an SOC-Tool.

## Qualitätskriterien / Definition of Done

- [ ] UTC-Zeiten konsistent
- [ ] Queries reproduzierbar dokumentiert
- [ ] Containment nicht ohne Freigabe ausgeführt

## Sicherheit & Freigaben

- **high risk** bei Prod-Containment.
- PII-Minimierung in exports.

## Fallstricke

- Unbounded search — SIEM timeout/Kosten.
- RBA ohne Parent Process — blind spot.
- Rule disable ohne Ticket — coverage gap.
- Timezone error Falsch-Positive.
- SOAR auto-run ohne review.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Failed logins spike alert.
- **Input:** user alice, 2h window.
- **Prompt:**

```text
SPL/KQL template for failed logins by src_ip; no host isolation.
```

- **Erwartetes Ergebnis:**

```spl
index=auth action=failure user=alice earliest=-2h latest=now
| stats count by src_ip
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Tune noisy rule.
- **Input:** rule R-442 threshold 5 -> 20 proposed.
- **Prompt:**

```text
Document FP examples; suggest threshold; no disable.
```

- **Erwartetes Ergebnis:**

```text
7d FP: backup service account; recommend threshold 20 + allowlist svc_backup
```