---
id: food-recipes-workflow
title: "Food and recipes"
domain: personal-lifestyle
category: food-recipes
tags:
  - food
  - personal-lifestyle
  - skillcli
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Hermes-Skill google-workspace / gws CLI
    install: "https://hermes-agent.nousresearch.com/docs/reference/skills-catalog"
    version_notes: "Bundled catalog."
inputs:
  - "Context/briefing for food and recipes"
  - "files, URLs or IDs according to Task"
outputs:
  - "Documented result (file, report, or ticket update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Purpose

Scale recipes, plan a weekly menu, and build shopping lists from on-hand ingredients.

## When to use

- Use leftovers with an ingredient list from the fridge.
- Meal prep for a family of four.
- Not for therapeutic diets without a nutrition professional.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| Hermes-Skill google-workspace / gws CLI | Calendar and spreadsheets | Sheets/Calendar for lists and reminders after OAuth. |

## System prompt

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

## Workflow

1. ingredients im Haus and Servings erfassen.
2. 3–5 recipevorschlaege auswaehlen.
3. Menueplan Woche.
4. Skalierte Mengen.
5. shoppingsliste delta.
6. Sheet or docx Export.
7. User kocht — no Lieferbestellung.

## Definition of done

- [ ] Allergene sichtbar
- [ ] Skalierung dokumentiert
- [ ] no diet-Therapie
- [ ] Servings klar

## Security

- no stillen Bestellungen, Zahlungen or Account-changes.
- Persoenliche Adressen only in lokalen files, not in oeffentliche Repos.
- Preise as Momentaufnahme with Datum kennzeichnen.

## Pitfalls

- Knoblauch linear skaliert to scharf.
- Backzeit at doppelter Menge not angepasst — Hinweis.
- Cross allergen in Sauce.
- Fleisch Safefood Temperatur only Hinweis generisch.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Reste: Zucchini, Kichererbsen, Reis
- **Input:** 2 Personen, 25 Min max
- **Prompt:**
```text
2 Recipes with step list and shopping list only when items are missing.
```
- **Expected result:** recipe Curry + Salat; shopping only Joghurt 1 Becher.
### Example 2 (Example data (self-written))
- **Task:** familynmenue Mo–Fr
- **Input:** 4 Personen, no Schwein
- **Prompt:**
```text
Plan in Sheet, Wiederverwendung Reste Di.
```
- **Expected result:** 5 Zeilen Menue; shoppingsliste 18 Posten.

