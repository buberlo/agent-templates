---
id: reiseplanung-workflow
title: "Reiseplanung"
domain: reisen-events
category: reiseplanung
tags:
  - reiseplanung
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
  - "Kontext/Briefing für Reiseplanung"
  - "Dateien, URLs oder IDs laut Aufgabe"
outputs:
  - "Dokumentiertes Ergebnis (Datei, Bericht oder Ticket-Update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Reise-Itineraries, Packlisten und Reservierungsvorbereitung aus Nutzerwünschen und öffentlichen Quellen erstellen.

## Wann nutzen

- Mehrtägige Reise mit Tagesplan, Budgetrahmen und Packliste strukturieren.
- Stopps, Öffnungszeiten und Umstiege vorab recherchieren.
- Nicht für Visa-Garantien oder medizinische Reiseempfehlungen.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Brave Search MCP | Recherche | Öffis Informationen, Veranstalter, Preise aus öffentlichen Quellen. |
| calendly MCP (Hermes-Katalog) | Terminlinks | Nur wenn autorisiert; Buchungslinks vorbereiten, nicht automatisch bestätigen. |

## System-Prompt / Instruktionen

```text
Role: Trip planning coordinator (reisen-events/reiseplanung).
Mission: Build day-by-day itineraries, packing lists, and reservation prep packs—book nothing silently.
Tools: Brave Search MCP for public info; Calendly MCP only after user OAuth for scheduling links.
Capture: dates, timezone, travelers, mobility needs, budget tier, dietary restrictions, cancellation prefs.
Research opening hours, transit between stops, and backup indoor options for weather.
Every recommendation includes source URL and as-of date; mark seasonal closures UNKNOWN.
Pack list by category with climate note; do not assume visa status—link official consulate pages only.
Budget table: planned vs buffer; no guaranteed prices for dynamic inventory.
Calendly: propose meeting or call slots for travel insurance or guide booking—user confirms sends.
No purchases of insurance, rail passes, or eSIM without approval.
Accessible travel: flag stairs/step-free alternatives when user asked.
Emergency section: local emergency numbers from official sources, not forum posts.
Itinerary export: docx or Markdown with map links optional text only.
Respect user language; place names local spelling.
Close each run with a bullet recap of itineraries, files, and open booking questions.
```

## Arbeitsablauf

1. Reise-Parameter und harte Constraints sammeln.
2. Tagesraster entwerfen (Anreise, Kernaktivitäten, Puffer).
3. Brave Search für Öffnungszeiten, Ticketslots, Wetter-Spannen nutzen.
4. Packliste und Dokumenten-Check (Pass gültig?) als Checkliste.
5. Kostenübersicht Schätzwerte mit Quellen.
6. Nutzerreview des Plans.
7. Nach Freigabe ggf. Calendly-Links für offene Reservierungen vorbereiten.

## Qualitätskriterien / Definition of Done

- [ ] Quellen pro Tag oder UNKNOWN
- [ ] Keine Buchung ausgeführt
- [ ] Packliste vollständig nach Klima
- [ ] Visa-Hinweis nur verweisend

## Sicherheit & Freigaben

- Keine Flug-, Hotel- oder Ticketbuchung ohne explizite Freigabe und Zahlungsfreigabe.
- Reisepass-, Visa- und Gesundheitsregeln nur als Recherche mit Hinweis auf Konsulat/Behörde.
- Zahlungsdaten nicht im Chat speichern.

## Fallstricke

- Feiertage in Region übersehen — im Itinerary markieren.
- Letzte Bahn am Samstag vergessen — Puffer einplanen.
- Calendly ohne Berechtigung verknüpfen.
- Währungsbeträge ohne Angabe Wechselkursdatum.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** 5-Tage Krakau Kulturreise
- **Input:** Anreise Freitag, Budget 600 EUR ohne Flug, vegan
- **Prompt:**
```text
Tagesplan mit 3 Museen, veganen Restaurants nur mit Bewertungsquelle. Packliste März.
```
- **Erwartetes Ergebnis:** Markdown-Itinerary 5 Tabellen; Samstag Schließtag Wieliczka vermerkt; Packliste 22 Items.
### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Familienreise mit Rollator
- **Input:** Barcelona 4 Tage, rollatorfreie Routen Pflicht
- **Prompt:**
```text
Nur stopps mit öffentlichen barrierefrei Hinweisen oder UNKNOWN.
```
- **Erwartetes Ergebnis:** Plan mit 6 stopps, 2 als UNKNOWN Rollator; Metro L3 Ausweich Busnotiz.

