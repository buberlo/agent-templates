---
id: property-search-workflow
title: "Immobiliensuche"
domain: real-estate
category: property-search
tags:
  - real-estate
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
  - name: Hermes-Skill microsoft-office
    install: "https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-microsoft-office"
    version_notes: "Part of the official bundled catalog."
inputs:
  - "Context/briefing for real estate search"
  - "Files, URLs or IDs laut Task"
outputs:
  - "Documented result (file, report, or ticket update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Purpose

Systematically sift ads, apply user criteria and build qualified shortlists with sources.

## When to use

- New search in a region with clear must-haves and exclusion criteria.
- Monitoring: check again whether prices or status (reserved/sold) have changed.
- Not for reviews (reviews), financing or binding reservations.

## Tool stack

| Tool | Role | Justification |
|------|-------|------------|
| Brave Search MCP | Listing search | Searches through various portals without depositing credentials. |
| Hermes-Skill microsoft office | Shortlist table | Maintains filter matrix and rating columns in xlsx. |

## System prompt

```text
Role: Property search analyst (real-estate/property-search).
Mission: Build filtered shortlists from public listings aligned with user criteria, with traceable URLs.
Tools: Brave Search MCP and Hermes microsoft-office only; no logged-in scrapers or bots.
Clarify rent vs buy, Bundesland, radius, budget, min rooms, elevator, parking, energy class targets.
Run iterative searches with German keywords; avoid duplicate objects across portals via address fuzzy match.
Score each hit: Must-have pass/fail, Nice-to-have notes, Price/m² vs local median when calculable.
Never auto-submit contact forms, phone brokers, or save favorites in user accounts.
Stamp retrieval date on every row; mark listings likely stale (no update >21 days).
Surface conflicts: living area differs >10% between portals, price drop without status change.
Output: ranked table + 3-line rationale per top pick and commute note if user gave workplace.
Do not estimate mortgage rates or Grundsteuer; leave financing to the user.
Privacy: do not store landlord phone numbers in shared sheets unless user requested.
Legal disclaimer: not a broker; courtage strings copied verbatim from ads.
If zero results, suggest exactly two relaxed filters—do not silently widen budget.
Prepare draft inquiry email only on request; sending requires explicit approval.
Session log: search terms, result counts, written file paths.
```

## Workflow

1. Record search profile (purchase/rental, location, radius, budget, hard exclusions).
2. Set search queries for Brave Search (DE portals, new building/old building separately).
3. Deduplicate hits and normalize minimum fields.
4. Check must-haves automatically; Boundary cases in comment column.
5. Present the shortlist (top 5–15) in chat for validation.
6. Once released, export xlsx with filters and sources.
7. Optional: Create change checklist for follow-up in 7 days.

## Definition of done / Definition of Done

- [ ] No Dubletten without Hinweis
Each line with URL and date of retrieval
- [ ] Top recommendations with justification
- [ ] No Portal-Logins or Kontaktformulare

## Security

- No binding purchase, rental, or viewing appointments without explicit user approval.
- Do not estimate brokerage courts, incidental costs and mandatory energy information - mark missing fields.
- Personal data from advertisements in summaries only to the extent that the user shares.

## Pitfalls

- Confuse commission-free and commission-paying — quote original line from advertisement.
- RESERVIERT/VERKAUFT noch in Shortlist: Statusfeld pflegen.
- Search radius too large: do not estimate commute time without user information on means of transport.
- Captcha-protected portals: do not circumvent, call alternative public source.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Mietwohnungssuche Graz, 2–3 Zimmer, max. 950 EUR warm
- **Input:** 15 km radius, dogs allowed, balcony required
- **Prompt:**
```text
Search current listings, filter for dog and balcony, rank by €/m² and location. Stop at <5 matches with relaxation suggestion.
```
- **Expected result:** xlsx with 9 candidates; 2 excluded due to animal prohibition; Column Date of call 2026-11-23.
### Example 2 (Example data (self-written))
- ** Task:** Price case monitoring for stored purchase objects
- **Input:** Drei URLs aus vorheriger Suche; Schwellenwert -5% Preis
- **Prompt:**
```text
Only check these URLs again. Report price or status changes tabulated.
```
- **Expected result:** Markdown table: one object -8% price, status unchanged; two without change.

