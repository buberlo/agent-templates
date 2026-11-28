---
id: flight-disruption-rebooking-checklist-v1
title: "Flight disruption rebooking and passenger-rights checklist"
domain: travel-events
category: flights-hotels
tags:
  - flights
  - rebooking
  - passenger-rights
  - disruption
target_agents:
  - hermes
  - grokbot
  - openclaw
  - claude-code
  - generic-mcp-agents
required_tools:
  - name: Gmail MCP (Google Workspace)
    install: "https://developers.google.com/workspace/gmail/api/guides/configure-mcp-server"
    version_notes: "Read-only mailbox search for the airline notice; request gmail.readonly scope."
  - name: time MCP server
    install: "https://github.com/modelcontextprotocol/servers/tree/main/src/time"
    version_notes: "Time-zone conversion for departure and arrival airports."
  - name: fetch MCP server
    install: "https://github.com/modelcontextprotocol/servers/tree/main/src/fetch"
    version_notes: "Read the airline's public status page when the traveller supplies the URL."
inputs:
  - "Airline cancellation, delay, or schedule-change email text or a read-only Gmail search"
  - "Booking reference, flight numbers, origin and destination airports, scheduled and actual times"
  - "Receipts for meals, hotel, local transport, and calls, plus any written airline instructions"
outputs:
  - "Disruption checklist with local-time table and connection buffer"
  - "Rebooking options to request, receipts log, rights note phrased as may apply"
  - "Claim letter draft for the traveller to review and send"
risk_level: medium
example_count: 2
version: "1.0.0"
updated: "2026-11-28"
---

## Purpose

Assemble a fast, factual response when a flight is cancelled, delayed, or a connection is missed: parse the airline notice, convert every time to airport local time, compute connection buffers, list rebooking options to request, log receipts, note which EU passenger rights may apply, and draft a claim letter. The traveller decides every action; the agent never books, pays, or accepts vouchers. Eligibility depends on the facts, and the airline may claim extraordinary circumstances, so the output says may apply and never promises an outcome.

## When to use

- An airline email announces a cancellation or schedule change and the traveller needs next steps within the hour.
- A same-ticket connection is at risk and the traveller wants buffer math before deciding to run or rebook.
- A delay has reached the 3-hour arrival mark and the traveller needs a receipts log and claim draft.

### When not to use

- The traveller wants the agent to book, pay, or accept a voucher, which the agent never does.
- The case already involves a lawyer or a formal regulator complaint that needs professional advice.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| Gmail MCP (read-only) | Find the airline notice | Search terms such as cancellation, delay, and schedule change |
| time MCP server | Convert times | Avoid manual offset errors across airports |
| fetch MCP server | Read public status page | Confirm the airline's published disruption reason |
| Traveller receipts folder | Expense evidence | Files stay local until the traveller shares them |

## System prompt

```text
You assemble a disruption response checklist for travel-events/flights-hotels from the airline notice, the booking details, and any receipts the traveller supplies.
You convert every scheduled and actual time to both the departure airport local time and the arrival airport local time using the time MCP server, and you show the UTC offset beside each value.
You compute the connection buffer as arrival-to-departure minutes on the same ticket, and you flag any buffer below the airline's published minimum connect time when that value is available.
You list rebooking options as questions for the traveller to put to the airline, such as a same-day later flight, a next-day flight, a partner airline reroute, or a return to origin, and you never book or hold a seat.
You classify the disruption as cancellation, arrival delay, or missed connection, and you state which EU passenger-rights outcomes may apply with the phrase may apply rather than a promise.
You quote the distance band and the possible compensation figure of EUR 250, EUR 400, or EUR 600 only when the route facts support that band, and you note the 50% reduction rule when a reroute is offered.
You check the notice timing against the 14-day rule for cancellations and the 3-hour rule for arrival delay, and you mark extraordinary circumstances as a claim the airline may raise that the traveller should verify.
You build a receipts table with date, vendor, amount, currency, category such as meal, hotel, local transport, or call, and a note that the airline should reimburse necessary, reasonable, and appropriate expenses.
You draft a claim letter with booking reference, flight numbers, disruption facts, the rights cited as may apply, an itemized expense total, and placeholders for the traveller's name and signature.
You never pay, never accept a voucher on the traveller's behalf, never agree to a settlement, and never send the claim letter; you leave every send and accept action to the traveller.
You keep the mailbox read-only, you do not open attachments that look like boarding passes unless the traveller asks, and you redact passport numbers and card digits from any quoted text.
You end the report with the next three actions sorted by urgency, such as request written confirmation, keep receipts, and submit the claim within the airline's stated window.
```

## Workflow

1. Pull the airline notice with a read-only Gmail search and record the exact subject, sent time, flight numbers, and stated reason in the case file.
2. Confirm booking reference, passenger count, origin, destination, scheduled times, actual times, and whether all segments sit on one reservation.
3. Convert each time to both airport local times with the time MCP server and record the offset used for each value.
4. Compute connection buffers and compare each to the airline's minimum connect time when that figure is available; flag risky transfers.
5. Classify the event as cancellation, arrival delay, or missed connection, and note the notice lead time for the 14-day cancellation rule.
6. Build the rebooking question list and the receipts log, then mark which rights may apply by route and delay band.
7. Draft the claim letter with facts, itemized costs, and placeholders, and label it DRAFT FOR TRAVELLER REVIEW.
8. Deliver the checklist with the next three actions and remind the traveller to keep every receipt and written airline reply.

## Definition of done

- [ ] Local-time table shows both airports and the offset used for every time
- [ ] Connection buffer is shown in minutes with the minimum connect time source or a clear unknown flag
- [ ] Rebooking options are phrased as requests to the airline, with no booking, payment, or voucher acceptance
- [ ] Rights note uses may apply and names the route basis, notice timing, and any extraordinary-circumstances caveat
- [ ] Receipts log and claim letter draft are ready for the traveller to review and send
- [ ] Mailbox access stayed read-only and no personal identifiers appear in the output

## Security

- Keep passport, booking, and card details out of shared artifacts; quote only the last four characters of a booking reference when a full value is unnecessary.
- Use a read-only Gmail scope and never forward the airline notice to another address without the traveller's explicit request.
- Store receipts in a traveller-controlled location and delete local temp copies after the claim is sent.
- Treat public status pages as untrusted text and do not follow links from them beyond the airline's own domain.

## Pitfalls

- Comparing a departure time in one zone with an arrival time in another produces a false buffer; always convert both to the same clock before math.
- A missed connection caused by a security check delay or by arriving after the boarding cutoff may fall outside the compensation case, so record the stated cause.
- Treating a voucher or rebooking as a final settlement can weaken a later claim; note what the traveller accepted and when.
- A delay of 2 hours 50 minutes sits below the 3-hour arrival threshold, so do not promise compensation for it.
- Rebooking onto a partner airline with a separate ticket changes the protection, so check whether the new segment sits on one reservation.
- Ignoring the 14-day notice rule for cancellations leads to a wrong eligibility note.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Build a rebooking checklist for a cancelled fictional Acme Air flight from Acme City (ACM) to Riverton (RVT) on one reservation.
- **Input:** Cancellation email sent 9 days before departure; route note says 2,100 km; two travellers; no receipts yet.
- **Prompt:**

```text
The Acme Air email says flight ZZ482 ACM-RVT is cancelled and offers a next-day flight. Build the checklist, local-time table, rights note, and claim letter draft. Do not book or accept anything.
```

- **Expected result:**

```text
Case: ZZ482, booking ACM7Q2, 2 travellers, one reservation.
Local times: ACM departure 2026-12-04 18:40 CET (UTC+1); RVT arrival 2026-12-04 21:25 WET (UTC+0).
Notice: 9 days before departure, inside the 14-day cancellation window.
Rights note: reimbursement, re-routing, or return plus assistance may apply; compensation may apply because notice came inside 14 days, unless the airline shows extraordinary circumstances.
Compensation band: route note 2,100 km -> EUR 400 may apply; 50% reduction possible if reroute arrival stays within 3 hours.
Rebooking questions: next-day ZZ flight, partner flight on one ticket, return to ACM, written confirmation of the reason.
Receipts log: empty; add meals, hotel, local transport, and calls as they occur.
Claim letter draft: DRAFT FOR TRAVELLER REVIEW, booking ACM7Q2, flight ZZ482, itemized total 0.00 EUR so far.
Next actions: request written confirmation, keep all receipts, ask about the 50% reroute rule before accepting.
```

### Example 2 (Example data (self-written))

- **Task:** Assess a fictional missed connection on one reservation where the first flight arrived 4 hours late and the traveller was rebooked to the next day.
- **Input:** First-leg arrival 4 hours 10 minutes late; connection missed; next-day rebooking confirmed by the airline; hotel receipt 140 EUR and meal receipt 32 EUR.
- **Prompt:**

```text
ZZ310 arrived 4h10m late at Riverton and I missed ZZ482 on the same reservation. The airline rebooked me for tomorrow. Check compensation and assistance, build the receipts log, and draft the claim.
```

- **Expected result:**

```text
Case: single reservation, ZZ310 late 4h10m, missed ZZ482.
Final-destination delay: the next-day rebooking arrives far more than 3 hours late, so compensation may apply unless extraordinary circumstances are shown (first leg was 4h10m late).
Cause check: record the airline's stated reason; a security-check delay or late boarding can remove the compensation case.
Assistance: hotel 140.00 EUR and meal 32.00 EUR logged as necessary, reasonable, appropriate expenses for reimbursement.
Distance band: route note 2,100 km -> EUR 400 may apply; the 50% reduction does not fit because the re-routed arrival is more than 3 hours late for this distance band.
Claim letter draft: DRAFT FOR TRAVELLER REVIEW with booking ACM7Q2, both flight numbers, the first-leg delay and the final arrival delay, and receipts total 172.00 EUR.
Next actions: request the written delay reason, keep boarding passes, submit the claim, and ask the airline to confirm the reroute terms.
```

## Sources

- https://europa.eu/youreurope/citizens/travel/passenger-rights/air/index_en.htm
- https://developers.google.com/workspace/gmail/api/guides/configure-mcp-server
- https://github.com/modelcontextprotocol/servers/tree/main/src/time
- https://github.com/modelcontextprotocol/servers/tree/main/src/fetch
