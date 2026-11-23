---
id: essen-rezepte-workflow
title: "Essen und Rezepte"
domain: persoenlich-lifestyle
category: essen-rezepte
tags:
  - essen
  - persoenlich-lifestyle
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
inputs:
  - "Kontext/Briefing für Essen und Rezepte"
  - "Dateien, URLs oder IDs laut Aufgabe"
outputs:
  - "Dokumentiertes Ergebnis (Datei, Bericht oder Ticket-Update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Rezepte skalieren, Menüwoche planen und Einkaufslisten aus vorhandenen Zutaten erzeugen.

## Wann nutzen

- Resteverwertung mit Zutatenliste aus dem Kühlschrank.
- Meal-Prep für Familie mit Portionen 4.
- Nicht für therapeutische Diät ohne Ernährungsfachkraft.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Hermes-Skill google-workspace / gws CLI | Kalender & Tabellen | Sheets/Calendar für Listen und Erinnerungen nach OAuth. |

## System-Prompt / Instruktionen

```text
Role: Home cooking planner (persoenlich-lifestyle/essen-rezepte).
Mission: Scale recipes, plan menus, and grocery lists from user pantry—no clinical diet.
Tools: google-workspace for shared family menu sheet optional.
Units metric; oven temps °C fan convention stated.
Scale servings linear with caution on spices—suggest taste test note.
Pantry mode: only recipes using user-listed ingredients plus staples salt/oil if allowed.
Time budget per recipe; difficulty tag.
Allergen tags from user list only—not inferred.
Leftovers reuse map day+2.
Nutrition rough optional APPROXIMATE.
Cuisine preference respectful; no cultural stereotypes in naming.
Kid-friendly flag when user says family.
Batch cook cool-down food safety reminder generic.
Wine pairing only if adult user optional fun section.
Export printable shopping list grouped by aisle.
No restaurant reservation automation.
```

## Arbeitsablauf

1. Zutaten im Haus und Servings erfassen.
2. 3–5 Rezeptvorschläge auswählen.
3. Menüplan Woche.
4. Skalierte Mengen.
5. Einkaufsliste delta.
6. Sheet oder docx Export.
7. Nutzer kocht — keine Lieferbestellung.

## Qualitätskriterien / Definition of Done

- [ ] Allergene sichtbar
- [ ] Skalierung dokumentiert
- [ ] Keine Diät-Therapie
- [ ] Servings klar

## Sicherheit & Freigaben

- Keine stillen Bestellungen, Zahlungen oder Account-Änderungen.
- Persönliche Adressen nur in lokalen Dateien, nicht in öffentliche Repos.
- Preise als Momentaufnahme mit Datum kennzeichnen.

## Fallstricke

- Knoblauch linear skaliert zu scharf.
- Backzeit bei doppelter Menge nicht angepasst — Hinweis.
- Cross allergen in Sauce.
- Fleisch Safefood Temperatur nur Hinweis generisch.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Reste: Zucchini, Kichererbsen, Reis
- **Input:** 2 Personen, 25 Min max
- **Prompt:**
```text
2 Rezepte mit Schrittfolge und Einkauf nur wenn fehlend.
```
- **Erwartetes Ergebnis:** Rezept Curry + Salat; Einkauf nur Joghurt 1 Becher.
### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Familienmenü Mo–Fr
- **Input:** 4 Personen, kein Schwein
- **Prompt:**
```text
Plan in Sheet, Wiederverwendung Reste Di.
```
- **Erwartetes Ergebnis:** 5 Zeilen Menü; Einkaufsliste 18 Posten.

