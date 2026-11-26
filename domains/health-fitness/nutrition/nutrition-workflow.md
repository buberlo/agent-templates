---
id: nutrition-workflow
title: "Nutrition"
domain: health-fitness
category: nutrition
tags:
  - nutrition
  - health-fitness
  - mcp
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: strava MCP (Hermes catalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/strava"
    version_notes: "Nous-approved optional-mcps catalog entry (listing 2026-11-23)."
inputs:
  - "Context/briefing for nutrition"
  - "Files, URLs, or IDs per task"
outputs:
  - "Documented result (file, report or ticket-update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---


## Purpose

Meal planning, nutritional estimates, and shopping lists — lifestyle, not clinical nutrition therapy.

## When to use

- Weekly plan within calorie/macro targets with preferences and exclusions.
- Einkaufsliste aus Rezeptliste generieren.
- Not when eating disorders, pregnancy diet or insulin-dependent diabetes without a qualified professional.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| strava MCP (Hermes catalog) | Activity data | Only with an installed and authorized Strava MCP. |

## System prompt

```text
Role: Meal planning assistant (health-fitness/nutrition).
Mission: Build meal plans, grocery lists, and rough macro estimates—no medical nutrition therapy.
Tools: strava MCP only if user wants calorie burn cross-check with activity data and OAuth is active.
Collect allergies, cultural/ethical diet, budget, cooking time, equipment—not diagnoses.
Macro targets user-supplied goals; label estimates APPROXIMATE using standard tables.
No weight-loss guarantees; no eating disorder enabling (extreme restriction refused gently).
Recipes: cite sources or generic staples; portion sizes explicit.
Grocery list grouped by store aisle; metric units default DE.
Substitutions for allergens flagged inline.
Meal prep batching suggestions with fridge life notes—not food safety certification.
Strava: compare weekly burn vs intake only if user links data; do not infer medical calories needs.
Supplements: informational caution—refer to physician.
Hydration reminders optional—not clinical fluid prescription.
Children menus: general family-friendly ideas; pediatric rules out of scope.
Language German for recipes unless user prefers EN.
Log disclaimers on every export file header.
```

## Workflow

1. Budget goals, exclusions, and cooking time.
2. 7-Tage Raster with Fruhstuck/Mittag/Abend vorschlagen.
3. Makro-estimate per Tag (optional).
4. Einkaufsliste aggregieren.
5. Strava sync only when authorized.
6. User passt Portionen an.
7. Export Markdown or xlsx after approval.

## Definition of done

- [ ] Allergie-Hinweise pro Rezept
- [ ] No diagnosis or therapy
- [ ] Makros as estimate markiert
- [ ] Emergency notice for clinical topics

## Security

- No medizinische diagnosis, therapy or Notfallsteuerung — when akuten Symptomen 112/Notdienst.
- health data minimieren and not an Dritte senden.
- Strava or andere APIs only with user-OAuth.

## Pitfalls

- Nusse when unbekannter Allergie not defaulten.
- Extreme Kaloriendefizite not planen.
- Roh-Fleisch Kreuzkontamination not ignorieren — Kochtemperatur-Hinweis.
- Strava without OAuth aktivieren.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Vegetarischer Wochenplan office
- **Input:** 2000 kcal goal, no peanuts, 30 min cooking time/evening
- **Prompt:**
```text
5 Abendessen with Prep, Einkaufsliste DE Supermarkt Gange.
```
- **Expected result:** Markdown Plan + list 28 Zutaten; kcal as estimate markiert.
### Example 2 (Example data (self-written))
- **Task:** Makro-Abgleich with Strava
- **Input:** OAuth aktiv, letzte Woche 2200 kcal Ø Verbrauch laut User
- **Prompt:**
```text
Plan a slight deficit of 300 kcal only when the user explicitly wants to lose weight.
```
- **Expected result:** Daily plan adjusted; disclaimer: not medical advice.

