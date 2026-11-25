---
id: pantry-weekly-meal-plan-usda-v1
title: "Pantry-based weekly meal plan with USDA nutrition lookup"
domain: health-fitness
category: nutrition
tags:
  - meal-planning
  - usda
  - pantry
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
required_tools:
  - name: USDA FoodData Central API
    install: "https://fdc.nal.usda.gov/api-guide/"
    version_notes: "GET /foods/search and /food/{fdcId} with data.gov API key in env; 1000 req/hour default limit."
  - name: curl or httpx
    install: "https://fdc.nal.usda.gov/api-key-signup/"
    version_notes: "CLI fallback when no nutrition MCP is installed."
inputs:
  - "Pantry inventory list with quantities (home use, not clinical)"
  - "Household size, excluded allergens, and calorie target range (optional)"
  - "USDA FDC API key in environment variable FDC_API_KEY"
outputs:
  - "Seven-day dinner plan using pantry-first ingredients and short shopping add-on list"
  - "Per-meal macro estimates from FDC nutrient IDs with disclaimer"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-25"
---

## Purpose

Build a seven-day meal plan that prioritizes ingredients already in the pantry, fills gaps with a minimal shopping list, and attaches approximate nutrition from USDA FoodData Central. This is wellness meal planning, not medical advice, diagnosis, or allergy testing.

## When to use

- Reducing food waste before grocery shopping.
- Agent can call FDC REST endpoints with a user-supplied API key.
- User disclosed allergens and accepts non-clinical macro estimates.

### When not to use

- Diabetes, eating disorders, pregnancy, or pediatric therapeutic diets without a clinician.
- Celiac or severe anaphylaxis rules without user-verified product labels.
- Replacing a registered dietitian for medical nutrition therapy.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| USDA FoodData Central API | Nutrient lookup | [API guide](https://fdc.nal.usda.gov/api-guide/) |
| Local pantry YAML | Inventory | Keeps lists out of model training logs when possible |
| Spreadsheet export optional | Shopping list | Human owns purchase decisions |

## System prompt

```text
You are a pantry-first meal planning assistant for health-fitness/nutrition using USDA FoodData Central read-only API calls.
You never diagnose conditions, prescribe diets for disease, or claim medical outcomes; you include a fixed disclaimer that the user must verify allergens on product labels.
You query /foods/search with pantry item names, select FDC IDs with clear descriptions, then fetch /food/{fdcId} with nutrients parameter for energy and macronutrients when available.
You block any recipe that contains user-declared allergens and substitute pantry-safe alternatives or mark Skip-Allergen-Risk when no safe swap exists.
You produce seven dinners plus optional lunch reuse notes, preferring ingredients consumed before pantry expiry dates the user listed.
You output a shopping add-on list separate from pantry use, with quantities in home units not clinical portions.
You cite https://fdc.nal.usda.gov/api-guide/ for rate limits and remind the user not to commit API keys to git repositories.
You flag when FDC returns branded foods with incomplete micronutrients and avoid inventing vitamin totals.
You end every plan with Not-Medical-Advice and Call-911-For-Emergency guidance for acute symptoms.
You refuse to remove allergen gates when the user asks to "ignore nuts" after declaring tree-nut allergy.
```

## Workflow

1. Confirm allergens, household size, optional calorie band, and FDC_API_KEY presence.
2. Parse pantry inventory; sort by expiry urgency.
3. Query FDC search for each staple protein, grain, and vegetable.
4. Draft seven meals mapping pantry items; note missing essentials.
5. Summarize approximate kcal and protein per serving from FDC fields returned.
6. Present shopping add-on list; no automatic ordering.
7. User reviews; agent does not log health conditions beyond allergens stated.

## Definition of done

- [ ] Each meal lists pantry items used and FDC IDs cited for nutrition rows
- [ ] Allergen gate enforced with no blocked ingredients
- [ ] Not-medical-advice disclaimer present
- [ ] No API key printed in output

## Security

- Store FDC_API_KEY in env; rotate if leaked per USDA key responsibility notice.
- Do not upload pantry photos with prescription pill bottles in frame.
- Grok Bot grocery connectors must not checkout without user payment approval.

## Pitfalls

- FDC branded item mismatch (wrong serving size) skews macros by 3x or more.
- "Pantry tomato" ambiguous between sauce, paste, and fresh; clarify with user.
- Rate limit 1000/hour blocks large batch lookups; cache FDC IDs in-session.
- International users may not find foods in FDC; label estimates unavailable honestly.
- Suggesting fasting or extreme deficit without clinician crosses medical boundary.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Plan week dinners for two adults; pantry has rice, black beans, frozen broccoli, olive oil; allergen: peanut.
- **Input:** FDC_API_KEY set in env; target ~600 kcal dinner ballpark optional.
- **Prompt:**

```text
Pantry meal plan 7 dinners.
USDA FDC for macros.
No medical advice.
```

- **Expected result:**

Seven dinners using beans and rice variations, broccoli thrice, peanut-free sauces only, shopping list for fresh citrus and eggs only, macro table with fictional FDC IDs like 173944 cited, disclaimer block, and note that labels must confirm allergen status.

### Example 2 (Example data (self-written))

- **Task:** Reject unsafe suggestion when user asks to use peanut sauce despite peanut allergy.
- **Input:** Allergen peanut declared; user prompt says use peanut garnish for crunch.
- **Prompt:**

```text
Add peanut garnish to meal 3.
```

- **Expected result:**

Refusal citing allergen gate, alternative seed-free crunch options from pantry like toasted oats if safe for user, unchanged meals 1-2 and 4-7, and reminder that agent does not override declared allergies.