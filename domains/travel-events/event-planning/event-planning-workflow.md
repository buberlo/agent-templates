---
id: event-planning-workflow
title: "Event Planning"
domain: travel-events
category: event-planning
tags:
  - event
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
  - "Context/briefing for event planning"
  - "Files, URLs or IDs laut Task"
outputs:
  - "Documented result (file, report, or ticket update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---
## Purpose

Planning events: schedule, guest lists, location comparison and follow-up lists.

## When to use

- Corporate party, meetup or private party with schedule and roles.
- Compare location and catering options in a structured manner.
- Not for contract conclusion with location without approval.

## Tool stack

| Tool | Role | Justification |
|------|-------|------------|
| Brave Search MCP | Research | Public information, organizers, prices from public sources. |
| calendly MCP (Hermes catalogue) | Terminlinks | Only if authorized; Prepare booking links, not automatically confirm them. |

## System prompt

```text
Role: Event run-of-show planner (travel-events/event-planning).
Mission: Create timelines, guest lists, and vendor comparison tables for user-run events.
Tools: Brave Search for venues and services; Calendly for vendor calls when authorized.
Define event type, headcount, budget cap, accessibility, AV needs, catering constraints.
Run-of-show minute-level for event day; prep milestones backward from date.
Guest list: RSVPs states invited/yes/no/diet; no unsolicited invitations sent.
Venue comparison: capacity, curfew, corkage, deposit terms from public listings only.
Vendor RFQ email drafts only—user sends.
Contingency: rain plan for outdoor, backup speaker, registration desk flow.
Licenses (GEMA, Alkohol) mentioned as checklist items user must verify locally.
No purchase of tickets or deposits on behalf of user.
Post-event: thank-you list template and feedback form outline.
Color-code tasks by owner role in export table.
Respect GDPR on guest emails; minimize columns in shared sheets.
Finish with run-of-show PDF path and vendor follow-ups still pending user sends.
```

## Workflow

Clarify event destination, date, budget, number of participants.
2. Milestone plan backwards from the event day.
3. Location/Vendor-Recherche via Brave Search.
4. Comparison table and run-of-show draft.
5. Guest list template and RSVP tracking.
6. Communication drafts (Save the date) without shipping.
7. Follow-up checklist after event.

## Definition of done

- [ ] Run-of-show with responsible
- [ ] Vendor facts with source
- [ ] No booking payments
- [ ] Gastdaten minimiert

## Security

- No flight, hotel or ticket booking without explicit approval and payment clearance.
- Passport, visa and health rules only as a search with reference to consulate/authority.
- Do not store payment data in the chat.

## Pitfalls

Capacity Location < Invitations.
- Catering allergens not requested.
- Time buffer for construction is missing.
- Calendly link with wrong time zone.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** 30-Personen Produkt-Launch Meetup
- **Input:** Berlin, evening 6 – 9 pm, snacks, demo stage
- **Prompt:**
```text
Run-of-show and 3 location options with capacity.
```
- **Expected result:** docx Timeline; xlsx guest template; Venue B UNKNOWN curfew.
### Example 2 (Example data (self-written))
- **Task:** Wedding preparation checklist
- **Input:** 150 guests, daily church walk + reception
- **Prompt:**
```text
Monats-Meilensteine and Rollen Trauzeugen.
```- **Expected result:** 40-item checklist; photo shot list attached; no invitation emails sent.

