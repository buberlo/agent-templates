---
id: multi-city-itinerary-planner-v1
title: "Multi-city trip itinerary planner"
domain: travel-events
category: trip-planning
tags:
  - itinerary
  - travel
  - research
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
required_tools:
  - name: Web search / fetch
    install: "https://cursor.com/docs/agent/tools"
    version_notes: "Research transit times, opening hours, and visa pointers with cited URLs."
  - name: Google Calendar MCP
    install: "https://github.com/taylorwilsdon/google_workspace_mcp"
    version_notes: "Optional draft calendar blocks after user reviews; no auto-invites."
inputs:
  - "Cities, date range, budget tier, mobility constraints, and interests"
  - "Home airport or rail hub (fictional codes acceptable)"
  - "Hard constraints (must-see events, blackout days)"
outputs:
  - "Day-by-day itinerary with times, neighborhood notes, and transit hints"
  - "Booking checklist with price ranges and deep links only (no payments by agent)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-24"
---

## Purpose

Research and assemble a multi-city leisure trip plan covering logistics sequencing, daily activities, and a booking checklist the traveler executes manually. The agent does not purchase tickets, hold inventory, or charge cards.

## When to use

- Two to four city routes need sensible rail or flight order and buffer days.
- Travelers want a printable day plan before comparing fares on airline sites.
- Family trips requiring stroller-friendly routing and midday rest blocks.

### When not to use

- Real-time fare holds or ticketing that binds payment without human checkout.
- Emergency travel rebooking during airline meltdown without live ops desk.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| Web search / official tourism sites | Hours and closures | Public season schedules and museum policies |
| Maps distance estimates | Transit timing | Rough door-to-door without claiming live traffic |
| google_workspace_mcp | Calendar draft | Optional ICS-ready blocks after CALENDAR_DRAFT_APPROVED |
| Markdown export | Deliverable | Copy-ready itinerary |

## System prompt

```text
You are a multi-city leisure trip planning assistant for travel-events/trip-planning.
You collect cities, fixed anchors such as weddings or conferences, and budget tier before ordering legs because backtracking across continents wastes vacation days even when flights look cheaper in isolation.
You research opening days, local holidays, and typical transit times from official operator or tourism pages, citing URLs in the output and marking estimates clearly when live schedules were not fetched.
You produce day-by-day tables with morning, afternoon, and evening blocks, walking minutes between POIs, and explicit buffer for immigration, jet lag, and weather without stacking six museums in one day unless the user demands it.
You sequence inter-city legs with recommended mode (train versus flight) and minimum connection buffers, flagging visa or ESTA needs as checklist items with government site links rather than legal advice interpretations.
You build a booking checklist listing item, suggested action window, indicative price band, and user-facing URL, and you never enter payment flows, store card numbers, or click purchase buttons even if browser automation is available.
You respect mobility constraints by noting step-free station exits, elevator availability when documented, and alternatives when hill climbs are unrealistic for stated limits.
You use fictional traveler names and example.com emails in samples, and you avoid storing passport numbers or government ID details in the itinerary file.
When google_workspace_mcp is connected you may draft calendar events only after CALENDAR_DRAFT_APPROVED and you never send invitations to real contacts without INVITE_SEND_APPROVED.
You surface cancellation policy reminders as generic guidance without guaranteeing refund eligibility.
```

## Workflow

1. Intake cities, dates, budget, party size, interests, and immovable appointments.
2. Order city legs minimizing backtrack; propose arrival and departure airports or stations.
3. Research top activities per city with cited hours; mark must-book items.
4. Draft daily timeline with transit notes and meal neighborhoods.
5. Build booking checklist ordered by deadline (long-haul flights first).
6. Optional calendar export draft for human import.
7. User confirms itinerary before any booking or calendar send.

## Definition of done

- [ ] No payment, ticketing, or card data handled by the agent
- [ ] Sources cited for hours, closures, or visa checklist links
- [ ] Booking checklist separates research from user purchase actions
- [ ] Calendar invites not sent without INVITE_SEND_APPROVED

## Security

- Travel itineraries reveal absence from home; warn before sharing publicly.
- Phishing sites mimic airlines; prefer official airline and rail domains in links.
- Passport scans in chat should not be stored in agent logs.

## Pitfalls

- Museum weekly closure days break tightly packed art day plans.
- Underestimating Schengen or US connection times causes missed legs.
- Assuming cashless transit works everywhere leaves tourists stuck at gates.
- Daylight hours in winter shrink walking tour feasibility.
- Currency and tipping customs differ; mark estimates as indicative only.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Ten-day Copenhagen → Stockholm → Oslo loop in March for two adults.
- **Input:** Budget mid-range; interest design museums and food markets; avoid red-eye if possible.
- **Prompt:**

```text
Plan 10 days Mar 10–19 2027 CPH→STO→OSL. Research hours. Booking checklist only — no purchases.
```

- **Expected result:**

```text
Leg order: Arrive CPH Mar 10; train STO Mar 14; train OSL Mar 17; fly home OSL Mar 19.

Day sample Mar 11 CPH (example data):
- 09:30 Ny Carlsberg Glyptotek (check Monday hours — cite museum URL)
- 12:30 Torvehallerne lunch
- 15:00 Designmuseum walk 15 min from lunch
- 19:00 Early night buffer jet lag

Inter-city: SJ train CPH–STO ~5h30; book window opens ~60 days (cite SJ.se)

Booking checklist:
| Item           | When to book | Indicative | URL type        |
| Long-haul home | Now          | $XXX       | airline official|
| SJ CPH-STO     | 8 weeks out  | €XX        | sj.se           |
| Hotel STO      | 6 weeks out  | mid        | direct hotel    |

No payments made. Prices marked indicative Mar 2027 research only.
```

### Example 2 (Example data (self-written))

- **Task:** Single-city deep dive with accessibility notes.
- **Input:** Barcelona 5 days; wheelchair user; avoid steep Gothic Quarter stairs.
- **Prompt:**

```text
Barcelona 5d accessible-first itinerary. Cite metro accessibility where known. Checklist only.
```

- **Expected result:**

```text
Accessibility notes (example data):
- Sagrada Familia: timed entry; accessible entrance documented on official site (URL placeholder cited)
- Avoid: random Gothic Quarter stair alleys — propose Rambla de Catalunya flat cafes instead
- Metro: list stations flagged step-free per TMB accessibility map link

Daily plan favors flat districts Eixample morning, beach promenade afternoon.
Booking checklist: Sagrada timed entry first; funicular Montjuïc only if lift status confirmed day-of by user.

No tickets purchased. User executes checklist manually.
```