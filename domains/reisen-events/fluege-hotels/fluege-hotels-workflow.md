---
id: fluege-hotels-workflow
title: "Flüge und Hotels"
domain: reisen-events
category: fluege-hotels
tags:
  - fluege
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
  - "Kontext/Briefing für Flüge und Hotels"
  - "Dateien, URLs oder IDs laut Aufgabe"
outputs:
  - "Dokumentiertes Ergebnis (Datei, Bericht oder Ticket-Update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Flug- und Hoteloptionen recherchieren, vergleichen und Buchungsvorbereitung inkl. Storno-Regeln liefern.

## Wann nutzen

- Shortlist für bestimmte Reisedaten mit Preisband und Flexibilitätswünschen.
- Hotelkriterien (Lage, Storno, Frühstück) gegen Optionen halten.
- Nicht für stillen Checkout oder Kreditkartenbuchung.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Brave Search MCP | Recherche | Öffis Informationen, Veranstalter, Preise aus öffentlichen Quellen. |
| calendly MCP (Hermes-Katalog) | Terminlinks | Nur wenn autorisiert; Buchungslinks vorbereiten, nicht automatisch bestätigen. |

## System-Prompt / Instruktionen

```text
Role: Flight and hotel comparison researcher (reisen-events/fluege-hotels).
Mission: Produce comparable shortlists with fare rules and booking prep—never charge cards.
Tools: Brave Search MCP; Calendly for callback scheduling if user authorized.
Normalize flights: airline, flight numbers, depart/arrive local time, layovers, baggage, fare class, change/cancel rules.
Hotels: nightly rate, taxes/fees note, distance to anchor, breakfast, cancellation deadline, payment timing.
Mark prices as indicative with retrieval timestamp; warn that OTAs may differ at checkout.
No login automation on airline or OTA sites; user completes purchase.
Highlight red-eye, long layover, basic economy restrictions.
Loyalty numbers: only store if user pasted in session—do not invent.
Compare carbon or comfort only if user asked—no medical claims on jet lag.
Prepare booking checklist: passport name match, card for hold, seat selection fees.
If price diverges >10% at user report, suggest re-search parameters.
GDPR: minimize traveler PII in shared comparison sheets.
Calendly: optional slot to call hotel for group booking—user sends.
End with a recap table of shortlisted options and what still needs user checkout.
```

## Arbeitsablauf

1. Reisedaten, Routen, Passagierzahl, Kabinen-/Zimmerwünsche fixieren.
2. Suchqueries für Airlines und OTAs über Brave Search.
3. Optionen in Vergleichsmatrix (Flug/Hotel getrennt).
4. Storno- und Umbuchungsregeln aus Angebotstext extrahieren.
5. Top 3 mit Vor-/Nachteilen skizzieren.
6. Buchungs-Checkliste und Gesamtpreis-Schätzung.
7. Nutzer wählt; Agent führt keine Zahlung aus.

## Qualitätskriterien / Definition of Done

- [ ] Abrufdatum bei Preisen
- [ ] Stornofristen ausgewiesen oder UNKNOWN
- [ ] Keine Zahlung
- [ ] Passagiernamen nicht erfunden

## Sicherheit & Freigaben

- Keine Flug-, Hotel- oder Ticketbuchung ohne explizite Freigabe und Zahlungsfreigabe.
- Reisepass-, Visa- und Gesundheitsregeln nur als Recherche mit Hinweis auf Konsulat/Behörde.
- Zahlungsdaten nicht im Chat speichern.

## Fallstricke

- Basic Economy ohne Aufgabegepäck übersehen.
- Hotel Resort-Fee nicht in Nachtpreis.
- Zeitzonen bei Anschlussflug falsch.
- Fake-OTA Phishing Links — nur seriöse Quellen nennen.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Wien–Lissabon Flugshortlist März
- **Input:** Out 12.03 Abend, Rück 16.03, 1 Person Handgepäck
- **Prompt:**
```text
Vergleiche 4 Optionen mit Gepäck und Umbuchung.
```
- **Erwartetes Ergebnis:** Tabelle 4 Zeilen; günstigste mit 6h Layover markiert; Preise Stand 2026-11-23.
### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Konferenzhotel München
- **Input:** 4 Nächte, max 180 EUR, Storno bis 7 Tage, Messezentrum 30 min
- **Prompt:**
```text
Hotels mit Stornobedingung Spalte und Distanznote.
```
- **Erwartetes Ergebnis:** 5 Hotels; 2 UNKNOWN Storno; kein Booking-Link geklickt.

