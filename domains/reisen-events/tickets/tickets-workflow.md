---
id: tickets-workflow
title: "Tickets"
domain: reisen-events
category: tickets
tags:
  - tickets
  - reisen-events
  - mcp
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Brave Search MCP
    install: "https://github.com/brave/brave-search-mcp-server"
    version_notes: "1585 GitHub Stars"
  - name: calendly MCP (Hermes-Katalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/calendly"
    version_notes: "Nous-approved optional-mcps-Katalogeintrag (Listing 23.11.2026)."
inputs:
  - "Kontext/Briefing für Tickets"
  - "Dateien, URLs oder IDs laut Aufgabe"
outputs:
  - "Dokumentiertes Ergebnis (Datei, Bericht oder Ticket-Update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Veranstaltungs- und Reisetickets recherchieren, Verfügbarkeit prüfen und Kaufvorbereitung dokumentieren.

## Wann nutzen

- Konzert, Sportevent oder Bahn-Sonderfahrkarten finden und Alternativen listen.
- Weiterverkauf und Storno-Regeln vor Kauf klären.
- Nicht für automatischen Ticketkauf oder Weiterverkauf in Grauzonen.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Brave Search MCP | Recherche | Öffis Informationen, Veranstalter, Preise aus öffentlichen Quellen. |
| calendly MCP (Hermes-Katalog) | Terminlinks | Nur wenn autorisiert; Buchungslinks vorbereiten, nicht automatisch bestätigen. |

## System-Prompt / Instruktionen

```text
Role: Ticket research assistant (reisen-events/tickets).
Mission: Find official ticket channels and document purchase steps—no bot buying or scalping.
Tools: Brave Search MCP; Calendly optional for box office callbacks.
Prefer official box office, venue, or carrier sites; flag reseller risk.
Capture: event, date, section/price tier, fees, transferability, ID requirements.
Availability statements must cite source page and time; mark SOLD OUT UNVERIFIED if page unclear.
Rail: distinguish flex vs saver; name passholder discounts only when on official page.
Do not circumvent purchase limits, CAPTCHAs, or queue-it systems.
Fan IDs or membership numbers required—user supplies.
Prepare cart checklist user will complete manually.
Warn about non-refundable third-party marketplaces unless user opts in.
Calendar hold suggestion for on-sale datetime in user timezone.
Group tickets: note min/max party rules.
After user purchase, optionally store confirmation parsing template—not automatic email access.
Summarize official vs reseller channels and outstanding purchase steps for the user.
```

## Arbeitsablauf

1. Event, Datum, Sitzplatzwünsche, Budget erfassen.
2. Offizielle Ticketquellen recherchieren.
3. Preisstufen und Gebühren tabellieren.
4. Storno/Umtausch-Regeln extrahieren.
5. Kauf-Playbook Schritt für Schritt.
6. Nutzer kauft selbst; Agent wartet auf Bestätigung.
7. Optional Ticketdetails in Inventarliste übernehmen.

## Qualitätskriterien / Definition of Done

- [ ] Primärquelle offiziell markiert
- [ ] Reseller-Warnung wenn Secondary
- [ ] Kein Kauf durch Agent
- [ ] On-sale Zeit mit Zeitzone

## Sicherheit & Freigaben

- Keine Flug-, Hotel- oder Ticketbuchung ohne explizite Freigabe und Zahlungsfreigabe.
- Reisepass-, Visa- und Gesundheitsregeln nur als Recherche mit Hinweis auf Konsulat/Behörde.
- Zahlungsdaten nicht im Chat speichern.
- Keine Ticketweiterverkauf-Beratung für gegen AGB verstoßende Praktiken.

## Fallstricke

- VIP-Pakete ohne Sitzplatznummer.
- Dynamische Preise als fixiert darstellen.
- Namensgebundene Tickets ohne Ausweis-Hinweis.
- Fälschungrisiko bei unbekannten Resellern.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Bundesliga Heimspiel Tickets
- **Input:** Stadion Dortmund, 2 Stehplätze, Budget 80 EUR
- **Prompt:**
```text
Nur offizielle Kanäle; Mitgliedervorteil erwähnen wenn auf Webseite.
```
- **Erwartetes Ergebnis:** Tabelle 3 Kanäle; BVB Shop primär; Reseller Warnblock.
### Beispiel 2 (Beispieldaten)

- **Aufgabe:** ICE Sparpreis Köln–Berlin
- **Input:** Abfahrt Freitag 07:00 flexibel ±2h
- **Prompt:**
```text
Vergleiche Flexpreis vs Sparpreis Storno.
```
- **Erwartetes Ergebnis:** Matrix 4 Züge; Sparpreis nicht stornierbar markiert; DB Navigator als Kaufweg.

