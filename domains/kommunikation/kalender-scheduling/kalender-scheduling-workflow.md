---
id: kalender-scheduling-workflow
title: "Kalender und Scheduling"
domain: kommunikation
category: kalender-scheduling
tags:
  - kalender
  - kommunikation
  - skillcli
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Hermes-Skill google-workspace / gws CLI
    install: "https://hermes-agent.nousresearch.com/docs/reference/skills-catalog"
    version_notes: "Bundled-Katalog."
  - name: calendly MCP (Hermes-Katalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/calendly"
    version_notes: "Nous-approved optional-mcps-Katalogeintrag (Listing 23.11.2026)."
  - name: Grok Bot Google Calendar
    install: "https://x.ai/bot/guides/grok-bot-101"
    version_notes: "Produktdoku."
inputs:
  - "Zeitzone und Suchfenster"
  - "Teilnehmer und Dauer"
  - "Titel/Agenda-Entwurf"
outputs:
  - "Slot-Vorschläge"
  - "Kalendereinladung (nach Freigabe)"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

**Freie Termine finden**, Vorschläge formulieren und **Einladungen erstellen** (Google Calendar, Calendly)—mit fester Zeitzone und ohne Doppelbuchungen über Kalender hinweg.

## Wann nutzen

- Meeting mit 2–8 Teilnehmern innerhalb der nächsten 2 Wochen.
- gws, Calendly MCP oder Grok Calendar verbunden.
- Text der Einladung und Teilnehmerliste vom Nutzer freigegeben.

**Wann nicht**

- Recurring-Regeln für ganze Organisation neu designen.
- Räume/Ressourcen ohne gebundenen Ressourcen-Kalender.
- Termine in Zeitzonen ohne explizite IANA-Angabe.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| gws calendar | Free/busy, events.insert | Workspace-nativ |
| Calendly MCP | Booking-Links, availability | Externe Buchung |
| Grok Google Calendar | Chat-OAuth | Schnelle Slot-Suche |

## System-Prompt / Instruktionen

```text
You schedule meetings for kommunikation/kalender-scheduling using gws, Calendly MCP, or Grok Calendar.

Inputs: timezone (default Europe/Vienna), window start/end ISO, duration minutes, attendee emails, title, agenda bullets, location (meet link or room), calendars_to_check[], create_event (yes only after approval).

Process:
1) Query freebusy for all attendees; intersect availability.
2) Propose 3 slots in local timezone with weekday names in German if user locale DE.
3) Show draft invitation body (HTML/plain) including agenda and conferencing link placeholder.
4) On "CREATE EVENT", call events.insert with sendUpdates=none unless user requests email invites.
5) Detect conflicts on organizer calendar; flag if hard conflict exists.

Never delete events without confirmation.
Use IANA timezone in API calls, not abbreviations like CET.
Log event_id after create.
```

## Arbeitsablauf

1. Zeitzone `Europe/Vienna` und Fenster (z. B. nächste 5 Werktage) festlegen.
2. `gws calendar freebusy` für alle Teilnehmer-Emails.
3. Drei gemeinsame Slots berechnen und tabellarisch ausgeben.
4. Nutzer wählt Slot; Titel/Agenda finalisieren.
5. Entwurf der Einladung zeigen (Teilnehmer, Zoom/Meet-Link).
6. Nach `CREATE`: `events.insert` mit gewähltem Slot.
7. `event_id` und ICS-Link in `output/scheduling.md` speichern.

## Qualitätskriterien / Definition of Done

- [ ] Alle Zeiten mit Offset/IANA angegeben
- [ ] Keine Einladung ohne bestätigten Slot und Teilnehmerliste
- [ ] Konflikte auf Organisator-Kalender geprüft
- [ ] event_id dokumentiert

## Sicherheit & Freigaben

- Teilnehmer-E-Mails nicht in öffentliche Logs.
- Calendly-Links nur teilen, wenn Buchungspolicy das erlaubt.
- Löschen/Verschieben nur nach explizitem Auftrag.

## Fallstricke

- Sommerzeit-Umstellung falsch berechnet.
- Mehrere Kalender des Organisators nicht abgefragt → Doppelbuchung.
- `sendUpdates=all` ohne Review → falsche Einladung raus.
- Calendly vs. Google: zwei parallele Buchungen für denselben Slot.
- Nur UTC intern gerechnet → Nutzer sieht falsche lokale Uhrzeit.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** 30-Min-Sync mit zwei Kolleg:innen.
- **Input:** `alice@firma.example`, `bob@firma.example`, Mo–Fr 09–17 Europe/Vienna.
- **Prompt:**

```text
Find 3 free 30-min slots next week, draft invite title "API Review", do not create until I pick.
```

- **Erwartetes Ergebnis:**

```text
1) Di 25.11. 10:00–10:30 CET
2) Mi 26.11. 14:00–14:30 CET
3) Do 27.11. 11:30–12:00 CET
Draft title: API Review | Attendees: alice, bob
Create: pending
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Hard Conflict.
- **Input:** Organisator hat 14:00–15:00 blockiert, gewünschter Slot 14:30.
- **Prompt:**

```text
Create event at 14:30 Tuesday.
```

- **Erwartetes Ergebnis:**

```text
Konflikt: bestehendes Event "Board prep" 14:00–15:00.
Kein events.insert ausgeführt.
Vorschlag: alternativer Slot 15:00 oder Nutzer-Override explizit bestätigen.
```