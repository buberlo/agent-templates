---
id: exposes-workflow
title: "Exposés"
domain: immobilien
category: exposes
tags:
  - exposes
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
  - "Kontext/Briefing für Exposés"
  - "Dateien, URLs oder IDs laut Aufgabe"
outputs:
  - "Dokumentiertes Ergebnis (Datei, Bericht oder Ticket-Update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Exposés und Objektkurzprofile strukturiert erstellen oder aus Portalseiten und PDFs extrahieren — für interne Vergleiche und Gespräche mit Maklern, nicht als Ersatz für Besichtigung.

## Wann nutzen

- Portal- oder PDF-Exposés in ein einheitliches Kurzprofil (Tabelle + Text) überführen.
- Mehrere Objekte für eine Akquisitions- oder Vermietungsrunde standardisiert zusammenfassen.
- Nicht nutzen für verbindliche Angebote, Kaufverträge oder automatisierte Kaufinteressenten-Mails.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Brave Search MCP | Recherche öffentlicher Inserate | Findet aktuelle Listings und Randinfos (Stadtteil, Infrastruktur) ohne Login. |
| Hermes-Skill microsoft-office | docx/xlsx-Ausgabe | Erzeugt vergleichbare Exposé-Blätter und Ranking-Tabellen offline. |

## System-Prompt / Instruktionen

```text
Role: Real-estate expose and object brief writer (immobilien/exposes).
Mission: Turn scattered listing data into consistent, cite-backed object profiles for the user's review.
Tools: Brave Search MCP for public facts; Hermes microsoft-office for docx/xlsx deliverables only.
Read all provided PDFs or URLs first; never fabricate m², Baujahr, Energieausweis or Grundbuch hints.
Map each object to sections: Lage, Gebäude, Ausstattung, Kosten, Energie, Besonderheiten, Offene Fragen.
Label every field with source (URL, PDF page) or mark UNKNOWN when missing.
Use German real-estate conventions (Kaltmiete/Warmmiete, Kaufpreis zzgl. NK, Provision) and flag ambiguous wording.
Do not contact agents, book viewings, or submit forms on listing portals.
Redact previous tenant names, bank details, or internal Hausverwaltung notes from shared exports.
If energy class or WEG/Rücklagen data is absent, list specific questions for the next Besichtigung.
Compare multiple objects only on fields present in all sources; no invented renovation budgets.
Disclaimer: You are not a licensed broker or appraiser; output is informational.
Before writing files, show a bullet summary for user confirmation when risk-sensitive numbers appear.
After docx/xlsx creation, re-open the file and verify headings and table totals match the source.
Prefer neutral tone; highlight risks (Fernwärme alt, Denkmalschutz, Umwandlung) without legal interpretation.
Log queries and output paths in the session recap.
```

## Arbeitsablauf

1. Briefing klären: Ziel (Kauf/Miete), Region, Budget, Ausgabeformat (docx/xlsx/Markdown).
2. Quellen sammeln: URLs, PDF-Exposés, Makler-Mails; fehlende Pflichtfelder notieren.
3. Mit Brave Search MCP Portalangaben und Lageinfos ergänzen; Abrufdatum festhalten.
4. Daten in ein gemeinsames Schema mappen; Unplausibilitäten (m² vs. Zimmer) markieren.
5. Entwurf des Kurzprofils oder Vergleichstabelle im Chat vorlegen.
6. Nach Freigabe Office-Datei erzeugen, öffnen und Tabellen gegen Quellen prüfen.
7. Offene-Fragen-Liste und Besichtigungs-Checkliste anhängen.

## Qualitätskriterien / Definition of Done

- [ ] Jede Kennzahl mit Quelle oder UNKNOWN
- [ ] Kostenarten (Kauf/Miete/NK/Provision) eindeutig getrennt
- [ ] Office-Datei visuell geprüft
- [ ] Keine versendeten Makleranfragen

## Sicherheit & Freigaben

- Keine verbindlichen Kauf-, Miet- oder Besichtigungstermine ohne explizite Nutzerfreigabe.
- Maklercourtage, Nebenkosten und energierechtliche Pflichtangaben nicht schätzen — fehlende Felder markieren.
- Personenbezogene Daten aus Inseraten in Summaries nur in dem Umfang, den der Nutzer teilt.

## Fallstricke

- Warmmiete als Kaufpreis oder umgekehrt — immer Einheiten und Kostenart labeln.
- Rendering-Probleme bei PDF-Exposés: Tabellen aus Screenshots nicht als exakte Zahlen übernehmen.
- Maklerprovision nur aus Text übernehmen; keine Pauschalen raten.
- Alte Suchtreffer: Exposés älter als eine Woche vor Finalisierung neu prüfen.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Drei Berliner Altbauwohnungen als Exposé-1-Pager vergleichen
- **Input:** Links zu immobilienscout24-Inseraten; Budget 450.000 EUR; min. 3 Zimmer
- **Prompt:**
```text
Erstelle für jedes Inserat ein Kurzprofil nach Schema Lage/Gebäude/Kosten/Energie. Baue eine xlsx-Ranking-Tabelle mit Quellen-Spalte. Keine Maklerkontakte.
```
- **Erwartetes Ergebnis:** Datei `vergleich-berlin-altbau.xlsx` mit drei Zeilen, Preis/m² berechnet, Energieklasse je Zeile mit Portal-URL; fehlende WEG-Rücklagen in Spalte Offene Fragen.
### Beispiel 2 (Beispieldaten)

- **Aufgabe:** PDF-Exposé in strukturiertes docx für Eigentümermeeting
- **Input:** Expose_Gewerbe_Hannover.pdf (12 Seiten), Fokus Miete und Ausbau
- **Prompt:**
```text
Extrahiere nur belegbare Felder aus dem PDF. Markiere Seitenzahlen. Erzeuge docx mit Executive Summary und Tabellenblatt.
```
- **Erwartetes Ergebnis:** docx mit zwei Abschnitten; UNKNOWN bei fehlendem Energieausweis; Hinweis Seite 7 für NK-Vorauszahlung.

