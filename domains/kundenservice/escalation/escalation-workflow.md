---
id: escalation-workflow
title: "Eskalation"
domain: kundenservice
category: escalation
tags:
  - escalation
  - kundenservice
  - mcp
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: intercom MCP (Hermes-Katalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/intercom"
    version_notes: "Nous-approved optional-mcps-Katalogeintrag (Listing 23.11.2026)."
inputs:
  - "Ticket- oder Konversations-ID"
  - "Eskalationsstufen-Matrix"
  - "Benachrichtigungskanäle (Slack/E-Mail Entwurf)"
outputs:
  - "Eskalationspaket"
  - "Kundenstatus-Entwurf (sympathisch, ohne Versprechen)"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

**Schwere Support-Fälle** erkennen (Rechtsdrohung, Ausfall, VIP, Medien), **intern eskalieren** mit strukturiertem Paket und **Kundenkommunikation nur als Entwurf**.

## Wann nutzen

- Keywords/SLA-Bruch triggern Eskalation (angry, legal, outage, exec).
- Intercom o. ä. verbunden; Matrix definiert Stufe → Owner.
- Kein Auto-Send an Kunde oder Legal ohne OK.

**Wann nicht**

- Routine-Ticket ohne Schwellenwert → helpdesk-tickets.
- Drohung mit Gewalt → Mensch + ggf. Behörden, kein Bot-Triage allein.
- Fehlende Eskalationsmatrix → zuerst Policy klären.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| intercom MCP | Ticket + History | Vollständiger Kontext |
| Eskalations-Matrix MD | Routing | L2/Legal/Engineering |
| Slack/E-Mail Entwurf | Intern extern getrennt | Kein Leak interner Notizen |

## System-Prompt / Instruktionen

```text
You escalate customer cases for kundenservice/escalation.

Inputs: ticket_id, escalation_matrix path, severity hints, customer_visible_update (draft only).

Steps:
1) Load full conversation; score severity 1-4 (4=legal/media/safety).
2) Map to matrix row: owner team, slack channel, due_hours.
3) Build escalation_package: summary, timeline, revenue_at_risk, quoted customer messages, attachments list, suggested_root_cause (hypothesis labeled).
4) Draft internal slack message with @owner; do not post without APPROVE_ESCALATE.
5) Draft customer-facing message: empathic, no liability admission, next_contact_time.
6) Tag ticket Escalated; assign if MCP allows and user approved.

Never promise refunds/compensation unless matrix authorizes wording.
Safety threats: stop automation, output HUMAN_REQUIRED safety banner.

Deliver: escalation_package.json, customer_draft.txt, slack_draft.txt.
```

## Arbeitsablauf

1. Matrix `config/escalation-matrix.yaml` laden.
2. Ticket via Intercom MCP inkl. aller Teile lesen.
3. Severity und Ziel-Team bestimmen.
4. `escalation_package.json` mit Zitaten und Timeline.
5. Slack-Entwurf an `#support-escalations` (nicht posten).
6. Kunden-Status-Entwurf ohne Schuldeingeständnis.
7. Nach `APPROVE_ESCALATE`: Tag + Assign; Sendeaktionen nur wenn freigegeben.

## Qualitätskriterien / Definition of Done

- [ ] Severity mit Begründung und Zitaten
- [ ] Richtiger Owner laut Matrix
- [ ] Kundenentwurf ohne unautorisierte Zusagen
- [ ] Safety: HUMAN_REQUIRED bei Bedrohung

## Sicherheit & Freigaben

- Legal-Threads nicht in Slack ohne #legal-private.
- Keine internen RCA-Details in Kundenentwurf.
- Medienanfragen an Comms eskalieren.

## Fallstricke

- Eskalation ohne vollständige History → falscher Kontext.
- Kunde sieht interne Slack-Kopie.
- Severity-Inflation → Team-Alert-Müdigkeit.
- Auto-assign an falsches Team außer Feiertag.
- Versprechen zur Frist ohne Engineering-OK.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** VIP-Ausfall, Severity 3.
- **Input:** Ticket `#9902`, Matrix L2-Engineering.
- **Prompt:**

```text
Build escalation package, draft customer message with 2h update pledge only if matrix allows.
```

- **Erwartetes Ergebnis:**

```text
Owner: oncall-engineering | Due: 2h
Customer draft: "Wir priorisieren Ihren Fall… Update innerhalb 2 Stunden…"
Slack draft: @oncall — summary + timeline (not posted)
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Gewaltandrohung.
- **Input:** Kundentext mit physischer Bedrohung.
- **Prompt:**

```text
Escalate and respond.
```

- **Erwartetes Ergebnis:**

```text
HUMAN_REQUIRED — safety_threat_detected
No customer auto-reply; ticket flagged for human + security playbook.
No slack post executed.
```