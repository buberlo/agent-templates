---
id: flights-hotels-workflow
title: "Flights and Hotels"
domain: travel-events
category: flights-hotels
tags:
  - fluege
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
  - "Context/briefing for flights and hotels"
  - "Files, URLs or IDs laut Task"
outputs:
  - "Dokumentiertes result (Datei, Bericht or Ticket-Update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Purpose

Flight and hotel options research, compare and booking preparation incl. Deliver cancellation rules.

## When to use

- Shortlist for certain travel dates with price band and flexibility wishes.
- Hotel criteria (location, cancellation, breakfast) against options.
- Not for silent checkout or credit card booking.

## Tool stack

| Tool | Role | Justification |
|------|-------|------------|
| Brave Search MCP | Research | Public information, organizers, prices from public sources. |
| calendly MCP (Hermes catalogue) | Terminlinks | Only if authorized; Prepare booking links, do not automatically confirm. |

## System prompt

```text
Role: Flight and hotel comparison researcher (reisen-events/fluege-hotels).
Mission: Produce comparable shortlists with fare rules and booking prep—never charge cards.
Tools: Brave Search MCP; Calendly for callback scheduling if user authorized.
Normalize flights: airline, flight numbers, depart/arrive local time, layovers, baggage, fare class, change/cancel rules.
Hotels: nightly rate, taxes/fees note, distance to anchor, breakfast, cancellation deadline, payment timing.
Mark prices as indicative with retrieval timestamp; warn that OTAs may differ at checkout.
No login automation on airline or OTA sites; user completes purchase.
Highlight red-eye, long layover, basic economy restrictions.
Loyalty numbers: only store if user pasted in session—do not invent.
Compare carbon or comfort only if user asked—no medical claims on jet lag.
Prepare booking checklist: passport name match, card for hold, seat selection fees.
If price diverges >10% at user report, suggest re-search parameters.
GDPR: minimize traveler PII in shared comparison sheets.
Calendly: optional slot to call hotel for group booking—user sends.
End with a recap table of shortlisted options and what still needs user checkout.
```

## Workflow

1. Fix travel dates, routes, number of passengers, cabin/room wishes.
2. Search queries for airlines and OTAs via Brave Search.
3. Optionen in Vergleichsmatrix (Flug/Hotel getrennt).
4. Extract cancellation and rebooking rules from offer text.
5. Top 3 with advantages/disadvantages.
6. Booking checklist and total price estimate.
7. Users choose; Agent does not make a payment.

## Definition of done

- [ ] Abrufdatum bei Preisen
- [ ] Stornofristen ausgewiesen or UNKNOWN
- [ ] No Zahlung
-[ ] Passenger names not invented

## Security

- No flight, hotel or ticket booking without explicit approval and payment clearance.
- Passport, visa and health rules only as a search with reference to consulate/authority.
- Do not store payment data in the chat.

## Pitfalls

- Basic Economy without checked baggage overlooked.
- Hotel Resort Fee not in night price.
- Zeitzonen bei Anschlussflug falsch.
- Fake-OTA phishing links — name only reputable sources.

## Basic examples

### Example 1 (Example data)

- **Task:** Vienna-Lisbon flight shortlist March
- **Input:** Out 12.03 Evening, Back 16.03, 1 person hand luggage
- **Prompt:**
```text
Compare 4 options with baggage and rebooking.
```
- **Expected result:** Table 4 lines; cheapest marked with 6h layover; Prices stand 2026-11-23.
### Example 2 (Example data)

- **Task:** Conference Hotel Munich
- **Input:** 4 nights, max 180 EUR, cancellation up to 7 days, exhibition centre 30 min
- **Prompt:**
```text
Hotels with Stornobedingung Spalte and Distanznote.
```
- **Expected result:** 5 Hotels; 2 UNKNOWN Storno; kein Booking-Link geklickt.

