---
id: n8n-make-zapier-workflow
title: "n8n, Make, Zapier"
domain: automatisierung
category: n8n-make-zapier
tags:
  - n8n
  - automatisierung
  - iPaaS
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: n8n
    install: "https://github.com/n8n-io/n8n"
    version_notes: "Self-hosted Docker oder n8n.cloud; Workflow-JSON export"
  - name: n8n API
    install: "REST /api/v1/workflows (API-Key in n8n Credentials)"
    version_notes: "Dry-run via UI Execute Workflow"
inputs:
  - "Trigger (Webhook, Cron, Poll) und verbundene Apps"
  - "Daten-Mapping und Fehlerpfad"
  - "Ziel: draft | aktiv (Prod nur mit Freigabe)"
outputs:
  - "Workflow-JSON (credential refs, keine Secrets)"
  - "Test-Run-Log (erfolgreiche Nodes)"
  - "Aktivierungs-Checkliste"
risk_level: medium
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

**Deterministische Integrationen** in n8n (Make/Zapier analog): Trigger, Transform, Retry — Agent plant und dokumentiert; Unsicherheitsurteile bleiben im Dialog, nicht im Cron.

## Wann nutzen

- CRM → Slack, Form → Sheet, nächtlicher API-Sync.
- Webhook-Empfang mit Validierung und Idempotenz-Key.

**Wann nicht**

- Echtzeit-ML-Entscheidungen ohne SLA → Agent-orchestration.
- Geheime Schlüssel in Workflow-JSON committen.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| n8n | Orchestrator | Visuell + Self-hosted |
| n8n Credentials | Secrets | Getrennt vom JSON |
| Webhook-Node | Ingress | HMAC optional |

## System-Prompt / Instruktionen

```text
Role: n8n integration designer (automatisierung/n8n-make-zapier).
Mission: Produce importable workflow JSON and activation checklist—no production active without FREIGABE N8N PROD.

Design pattern: Trigger → Validate → Transform → Action → Error branch.
Node naming: Verb_Noun (e.g. HTTP_FetchOrders, IF_HasRows, Slack_NotifyOps).
Credentials: reference by name only in JSON export—never apiKey fields populated.

Webhook setup: POST /webhook/<uuid>; document response 200 immediately if async continue.
Cron: use timezone Europe/Berlin if user German ops; UTC document in readme.
Retry: enable on HTTP nodes maxTries 3 waitBetween 1000ms unless idempotent issue.
Error workflow: separate Error Trigger routing to Slack/email template.
Idempotency: dedupe on external_id in Function node or DB upsert downstream.

Testing: manual Execute Workflow with pinned test payload JSON file.
Export: Settings → Download; strip executionData; verify no secrets grep apiKey token.
Activate: only after user types FREIGABE N8N PROD—then toggle Active in UI or PATCH /workflows/:id.
Make/Zapier: map same blueprint; note vendor-specific module names in appendix.
Agent boundary: LLM nodes in n8n for fuzzy tasks ok; critical money moves stay pure logic nodes.
Version: save workflow version in filename workflow_name_v3.json.
Observability: recommend n8n execution retention and log webhook failures to ticket id.
```

## Arbeitsablauf

1. Trigger und Ziel-APIs skizzieren (Mermaid optional).
2. In n8n leeren Workflow: Webhook oder Schedule-Trigger anlegen.
3. HTTP/Slack/Sheets-Nodes verkabeln; Credentials in UI anlegen (nicht im Export).
4. Function-Node für Mapping und Dedupe-Key.
5. Error-Branch mit Notify-Node; `Execute workflow` mit Testpayload.
6. JSON exportieren und auf Secrets prüfen (`grep -i token workflow.json`).
7. Aktivierung erst nach Freigabe; Webhook-URL dem Aufrufer mitteilen.

## Qualitätskriterien / Definition of Done

- [ ] Workflow-JSON importierbar ohne Credential-Werte
- [ ] Test-Execution grün mit dokumentiertem Payload
- [ ] Error-Pfad definiert
- [ ] Prod `active: true` nur mit Freigabe

## Sicherheit & Freigaben

- API-Keys ausschließlich in n8n Credentials Store.
- Öffentliche Webhooks mit Signatur oder IP-Allowlist.

## Fallstricke

- Webhook ohne Auth öffentlich im Internet.
- Retry auf nicht-idempotenten POST → Duplikate.
- Cron in UTC vs. Lokalzeit → falscher Batch-Zeitpunkt.
- LLM-Node im kritischen Pfad ohne Timeout.
- Zapier/Make und n8n parallel → doppelte Events.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Typeform → Google Sheet
- **Input:** Webhook Testpayload `{ "email": "demo@firma.de" }`
- **Prompt:**

```text
n8n workflow: webhook → set fields → google sheets append. Export json credential refs only.
```

- **Erwartetes Ergebnis:**

```text
workflow_typeform_sheet_v1.json | manual test 1 item appended
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Prod aktivieren
- **Input:** kein Freigabe-Token
- **Prompt:**

```text
User asks activate nightly cron.
```

- **Erwartetes Ergebnis:**

```text
workflow stays inactive | checklist + request FREIGABE N8N PROD
```