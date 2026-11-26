---
id: trip-planning-workflow
title: "Trip planning"
domain: travel-events
category: trip-planning
tags:
  - trip-planning
  - travel-events
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
  - name: calendly MCP (Hermes catalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/calendly"
    version_notes: "Nous-approved optional-mcps catalog entry (Listing 23 Nov 2026)."
inputs:
  - "Context/briefing for travel planning"
  - "Files, URLs or IDs laut Task"
outputs:
  - "Documented result (file, report, or ticket update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---
## Purpose

Create travel itineraries, packing lists and reservation preparation from user requests and public sources.

## When to use

- Structuring multi-day travel with daily plan, budget and packing list.
- Research stops, opening hours and switches in advance.
- Not for visa guarantees or medical travel recommendations.

## Tool stack

| Tool | Role | Justification |
|------|-------|------------|
| Brave Search MCP | Research | Public information, organizers, prices from public sources. |
| calendly MCP (Hermes catalogue) | Terminlinks | Only if authorized; Prepare booking links, do not automatically confirm. |

## System prompt

```text
Role: Trip planning coordinator (travel-events/trip-planning).
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

## Workflow

1. Collect travel parameters and hard constraints.
2. Design daily grids (arrival, core activities, buffers).
3. Use Brave Search for opening hours, ticket slots, weather spans.
4. Packing list and document check (pass valid?) as a checklist.
5. Cost overview Estimates with sources.
6. Nutzerreview des Plans.
7. Once approved, prepare Calendly links for open reservations.

## Definition of done

- [ ] Sources per day or UNKNOWN
- [ ] No booking carried out
- [ ] Packing list completely by climate
- [ ] Visa note for reference only

## Security

- No flight, hotel or ticket booking without explicit approval and payment clearance.
Passport, visa and health rules only as a search with reference to consulate/authority.
- Do not store payment data in the chat.

## Pitfalls

- Enable only required tools.

- Holidays overlooked in region - mark in itinerary.
- Letzte Bahn am Samstag vergessen — Puffer einplanen.
Link Calendly without permission.
Currency amounts without the exchange rate date.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** 5-Tage Krakau Kulturreise
- **Input:** Anreise Freitag, Budget 600 EUR without Flug, vegan
- **Prompt:**```text
Day plan with 3 museums, vegan restaurants with rating source only. Packing list March.
```
- **Expected result:** Markdown-Itinerary 5 tables; Saturday closing day Wieliczka noted; Packing list 22 items.
### Example 2 (Example data (self-written))
- **Task:** Family trip with rollator
- **Input:** Barcelona 4 days, step-free rollator-accessible routes required
- **Prompt:**
```text
Only stops with public accessible information or UNKNOWN.
```
- **Expected result:** Plan with 6 stopps, 2 as UNKNOWN rollator; Metro L3 avoid bus note.

