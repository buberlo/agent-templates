---
id: tickets-workflow
title: "Tickets"
domain: travel-events
category: tickets
tags:
  - tickets
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
    version_notes: "Nous-approved optional-mcps catalog entry (Listing 23.11.2026)."
inputs:
  - "Context/briefing for tickets"
  - "Files, URLs or IDs laut Task"
outputs:
  - "Dokumentiertes result (Datei, Bericht or Ticket-Update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Purpose

Research event and travel tickets, check availability and document purchase preparation.

## When to use

- Find concert, sporting event or train special tickets and list alternatives.
- Clarify resale and cancellation rules before purchase.
- Not for automatic ticket purchase or resale in grey areas.

## Tool stack

| Tool | Role | Justification |
|------|-------|------------|
| Brave Search MCP | Research | Public information, organizers, prices from public sources. |
| calendly MCP (Hermes catalogue) | Terminlinks | Only if authorized; Prepare booking links, not automatically confirm them. |

## System prompt

```text
Role: Ticket research assistant (reisen-events/tickets).
Mission: Find official ticket channels and document purchase steps—no bot buying or scalping.
Tools: Brave Search MCP; Calendly optional for box office callbacks.
Prefer official box office, venue, or carrier sites; flag reseller risk.
Capture: event, date, section/price tier, fees, transferability, ID requirements.
Availability statements must cite source page and time; mark SOLD OUT UNVERIFIED if page unclear.
Rail: distinguish flex vs saver; name passholder discounts only when on official page.
Do not circumvent purchase limits, CAPTCHAs, or queue-it systems.
Fan IDs or membership numbers required—user supplies.
Prepare cart checklist user will complete manually.
Warn about non-refundable third-party marketplaces unless user opts in.
Calendar hold suggestion for on-sale datetime in user timezone.
Group tickets: note min/max party rules.
After user purchase, optionally store confirmation parsing template—not automatic email access.
Summarize official vs reseller channels and outstanding purchase steps for the user.
```

## Workflow

Event, date, seat requests, budget capture.
2. Offizielle Ticketquellen recherchieren.
3. Tabulate price levels and fees.
4. Storno/Umtausch-Regeln extrahieren.
5. Buy Playbook step by step.
6. Users buy themselves; Agent is waiting for confirmation.
7. Optional Ticket Details in Inventory List.

## Definition of done

- [ ] Primary source officially marked
- [ ] Reseller-Warnung wenn Secondary
- [ ] Kein Kauf durch Agent
- [ ] On-sale time with time zone

## Security

- No flight, hotel or ticket booking without explicit approval and payment clearance.
- Passport, visa and health rules only as a search with reference to consulate/authority.
- Do not store payment data in the chat.
- No ticket resale advice for practices in violation of GTC.

## Pitfalls

- VIP-Pakete without Sitzplatznummer.
- Dynamische Preise als fixiert darstellen.
- Namensgebundene Tickets without Ausweis-Hinweis.
- Risk of counterfeiting in unknown resellers.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Bundesliga Heimspiel Tickets
- **Input:** Stadium Dortmund, 2 standing places, budget 80 EUR
- **Prompt:**
```text
Only official channels; Members benefit when mentioned on website.
```
- **Expected result:** Table 3 channels; BVB Shop primary; Reseller warning block.
### Example 2 (Example data (self-written))
- **Task:** ICE Sparpreis Cologne-Berlin
- **Input:** Abfahrt Freitag 07:00 flexibel ±2h
- **Prompt:**
```text
Vergleiche Flexpreis vs Sparpreis Storno.
```
- **Expected result:** Matrix 4 moves; Savings price marked non-cancellable; DB Navigator as a way of buying.

