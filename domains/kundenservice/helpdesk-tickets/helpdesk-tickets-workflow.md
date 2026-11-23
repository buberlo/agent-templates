---
id: helpdesk-tickets-workflow
title: "Helpdesk und Tickets"
domain: kundenservice
category: helpdesk-tickets
tags:
  - helpdesk
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
  - name: awesome-mcp Support-Sektion
    install: "https://github.com/punkpeye/awesome-mcp-servers"
    version_notes: "Katalog."
inputs:
  - "Ticket-ID oder Suchfilter"
  - "Makro-Policy und Tonalität"
  - "Freigabe für öffentliche Antwort"
outputs:
  - "Priorisierte Ticketliste"
  - "Öffentliche Antwort-Entwurf und interne Notiz"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

Support-**Tickets lesen**, priorisieren und **Antworten/Notizen** als Entwurf erzeugen—Resolve/Close nur gemäß Policy, **PII-arm** in Logs.

## Wann nutzen

- Intercom (oder ähnlicher Helpdesk-MCP) verbunden.
- SLA- oder Prioritätsregeln bekannt.
- Agent unterstützt First Response, Mensch sendet oder gibt OK.

**Wann nicht**

- Rechtliche Beschwerden ohne Legal-Review-Workflow.
- Massen-Statusänderungen ohne Change-Fenster.
- Zendesk o. Ä. ohne passenden MCP (nur Katalog-Recherche).

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| intercom MCP | Ticket CRUD, Notizen | Hermes approved |
| awesome-mcp Katalog | Alternative ITSM | Eval vor Install |
| Interne KB | Makro-Quelle | Konsistente Antworten |

## System-Prompt / Instruktionen

```text
You process helpdesk tickets for kundenservice/helpdesk-tickets via Intercom MCP.

Inputs: view (open|snoozed|search query), sla_hours, tone (empathic DE), allowed_actions (draft_reply | internal_note | tag | resolve), macro_ids[].

Workflow:
1) List tickets matching view; sort by waiting_customer since longest.
2) For each ticket (max N per run): fetch thread, classify intent (billing|technical|howto|angry).
3) Draft public reply using approved macros when match; personalize with ticket facts only—no invented policies.
4) Add internal_note with next steps if escalation needed.
5) tag ticket only if user approved tags.
6) resolve or close ONLY if allowed_actions includes resolve AND user confirmed.

Redact card numbers, passwords from summaries.
If PII must appear in reply, keep minimal.

Output: ticket-run.md with ticket_id, actions taken, draft ids, nothing sent without send_approved flag.
```

## Arbeitsablauf

1. `hermes mcp install intercom` und Credentials prüfen.
2. Ticket-View laden: offene Tickets nach Wartezeit sortieren.
3. Top-5: Kontext lesen, Intent klassifizieren.
4. Öffentlichen Antwortentwurf aus Makro + Fakten bauen.
5. Interne Notiz bei Eskalationsrisiko.
6. Nutzer reviewt; bei OK: öffentliche Notiz senden (wenn erlaubt).
7. Run-Log `output/helpdesk-run.md` ohne unnötige PII.

## Qualitätskriterien / Definition of Done

- [ ] Keine erfundenen Rückerstattungs-/Policy-Versprechen
- [ ] Resolve nur mit expliziter Policy/Freigabe
- [ ] Antwort referenziert Ticket-Fakten
- [ ] Logs pseudonymisiert wo möglich

## Sicherheit & Freigaben

- Kundendaten nicht in öffentlichen Agent-Threads.
- OAuth-Token nicht loggen.
- DSGVO-Löschanfragen an Human eskalieren.

## Fallstricke

- Stilles Resolve → CSAT-Kollateralschaden.
- Makro passt nicht → falsche Produktversion genannt.
- Interne Notiz versehentlich öffentlich.
- Suche zu breit → falsches Ticket bearbeitet.
- Halluzinierte Ticket-ID.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Billing-Ticket First Response.
- **Input:** Ticket `#8821`, Kunde fragt Rechnungsduplikat.
- **Prompt:**

```text
Draft public reply in German, attach internal note if refund policy unclear, do not resolve.
```

- **Erwartetes Ergebnis:**

```text
Public draft: "Wir senden Ihnen die Rechnung #445… erneut zu…"
Internal note: verify payment gateway status before promise
Resolve: not executed
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Resolve ohne Freigabe.
- **Input:** User says only draft.
- **Prompt:**

```text
Close ticket 8821 as solved.
```

- **Erwartetes Ergebnis:**

```text
Abbruch: resolve not in allowed_actions.
Draft remains unsent; ticket state unchanged.
```