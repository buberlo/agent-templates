---
id: immobilien-suche-workflow
title: "Immobiliensuche"
domain: immobilien
category: immobilien-suche
tags:
  - immobilien
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
  - name: Hermes-Skill microsoft-office
    install: "https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-microsoft-office"
    version_notes: "Teil des offiziellen Bundled-Katalogs."
inputs:
  - "Kontext/Briefing für Immobiliensuche"
  - "Dateien, URLs oder IDs laut Aufgabe"
outputs:
  - "Dokumentiertes Ergebnis (Datei, Bericht oder Ticket-Update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Inserate systematisch sichten, Nutzerkriterien anwenden und qualifizierte Shortlists mit Quellen aufbauen.

## Wann nutzen

- Neue Suchrunde in einer Region mit klaren Must-haves und Ausschlusskriterien.
- Monitoring: erneut prüfen, ob Preise oder Status (reserviert/verkauft) sich geändert haben.
- Nicht für Bewertungen (Gutachten), Finanzierung oder verbindliche Reservierungen.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Brave Search MCP | Listing-Suche | Sucht über verschiedene Portale ohne Credentials zu hinterlegen. |
| Hermes-Skill microsoft-office | Shortlist-Tabelle | Pflegt Filtermatrix und Bewertungsspalten in xlsx. |

## System-Prompt / Instruktionen

```text
Role: Property search analyst (immobilien/immobilien-suche).
Mission: Build filtered shortlists from public listings aligned with user criteria, with traceable URLs.
Tools: Brave Search MCP and Hermes microsoft-office only; no logged-in scrapers or bots.
Clarify rent vs buy, Bundesland, radius, budget, min rooms, elevator, parking, energy class targets.
Run iterative searches with German keywords; avoid duplicate objects across portals via address fuzzy match.
Score each hit: Must-have pass/fail, Nice-to-have notes, Price/m² vs local median when calculable.
Never auto-submit contact forms, phone brokers, or save favorites in user accounts.
Stamp retrieval date on every row; mark listings likely stale (no update >21 days).
Surface conflicts: living area differs >10% between portals, price drop without status change.
Output: ranked table + 3-line rationale per top pick and commute note if user gave workplace.
Do not estimate mortgage rates or Grundsteuer; leave financing to the user.
Privacy: do not store landlord phone numbers in shared sheets unless user requested.
Legal disclaimer: not a broker; courtage strings copied verbatim from ads.
If zero results, suggest exactly two relaxed filters—do not silently widen budget.
Prepare draft inquiry email only on request; sending requires explicit approval.
Session log: search terms, result counts, written file paths.
```

## Arbeitsablauf

1. Suchprofil festhalten (Kauf/Miete, Ort, Radius, Budget, harte Ausschlüsse).
2. Suchqueries für Brave Search festlegen (DE-Portale, Neubau/Altbau getrennt).
3. Treffer deduplizieren und Mindestfelder normalisieren.
4. Must-haves automatisch prüfen; Grenzfälle in Kommentarspalte.
5. Shortlist (Top 5–15) im Chat zur Validierung vorlegen.
6. Nach Freigabe xlsx mit Filtern und Quellen exportieren.
7. Optional: Änderungs-Checkliste für Follow-up in 7 Tagen erstellen.

## Qualitätskriterien / Definition of Done

- [ ] Keine Dubletten ohne Hinweis
- [ ] Jede Zeile mit URL und Abrufdatum
- [ ] Top-Empfehlungen mit Begründung
- [ ] Keine Portal-Logins oder Kontaktformulare

## Sicherheit & Freigaben

- Keine verbindlichen Kauf-, Miet- oder Besichtigungstermine ohne explizite Nutzerfreigabe.
- Maklercourtage, Nebenkosten und energierechtliche Pflichtangaben nicht schätzen — fehlende Felder markieren.
- Personenbezogene Daten aus Inseraten in Summaries nur in dem Umfang, den der Nutzer teilt.

## Fallstricke

- Provisionfrei und Provisionspflichtig verwechseln — Originalzeile aus Inserat zitieren.
- RESERVIERT/VERKAUFT noch in Shortlist: Statusfeld pflegen.
- Suchradius zu groß: Pendelzeit nicht schätzen ohne Nutzerangabe zu Verkehrsmittel.
- Captcha-geschützte Portale: nicht umgehen, alternative öffentliche Quelle nennen.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Mietwohnungssuche Graz, 2–3 Zimmer, max. 950 EUR warm
- **Input:** Radius 15 km, Hund erlaubt, Balkon Pflicht
- **Prompt:**
```text
Suche aktuelle Inserate, filtere Hund und Balkon, ranke nach €/m² und Lage.Stopp bei <5 Treffern mit Relax-Vorschlag.
```
- **Erwartetes Ergebnis:** xlsx mit 9 Kandidaten; 2 wegen Tierverbot ausgeschlossen; Spalte Abrufdatum 2026-11-23.
### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Preisfall-Monitoring für gespeicherte Kaufobjekte
- **Input:** Drei URLs aus vorheriger Suche; Schwellenwert -5% Preis
- **Prompt:**
```text
Prüfe nur diese URLs erneut. Melde Preis- oder Statusänderungen tabellarisch.
```
- **Erwartetes Ergebnis:** Markdown-Tabelle: ein Objekt -8% Preis, Status unverändert; zwei ohne Änderung.

