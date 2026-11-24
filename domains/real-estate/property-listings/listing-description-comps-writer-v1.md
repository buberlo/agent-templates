---
id: listing-description-comps-writer-v1
title: "Listing description and comparable research"
domain: real-estate
category: property-listings
tags:
  - listings
  - fair-housing
  - comps
target_agents:
  - hermes
  - grokbot
  - cursor
  - generic-mcp-agents
required_tools:
  - name: brave-search-mcp-server
    install: "https://github.com/brave/brave-search-mcp-server"
    version_notes: "Web search for public listing comps (listing 2026-11-24)."
  - name: HUD Fair Housing Act overview
    install: "https://www.hud.gov/helping-americans/fair-housing-act-overview"
    version_notes: "Official fair housing wording constraints reference."
inputs:
  - "Property facts sheet (beds, baths, sqft, year built, neighborhood name)"
  - "MLS remarks rules and brokerage compliance checklist"
  - "Target listing price band or recent appraisal range"
outputs:
  - "MLS-ready remark draft without discriminatory language"
  - "Comparable listings table with source URLs and adjustment notes"
risk_level: medium
example_count: 2
version: "1.0.0"
updated: "2026-11-24"
---

## Purpose

Research publicly visible comparable listings for a residential property, summarize price and feature deltas, and draft marketing remarks that highlight factual features while avoiding fair-housing-prohibited language. The agent does not publish to MLS without BROKER_APPROVED and does not state discriminatory preferences.

## When to use

- New listing prep when the agent needs comp bullets and remark copy in one pass.
- Refreshing stale remarks after a price change with updated comp context.
- Training associates on fair-housing-safe adjectives versus risky neighborhood narratives.

### When not to use

- Commercial investment underwriting requiring licensed appraiser opinions.
- Markets where MLS rules forbid automated scraping; use manually supplied comp IDs instead.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| Brave Search MCP | Public listing discovery | Documented search MCP for comp research |
| HUD fair housing overview | Wording guardrails | Federal prohibited basis reference |
| MLS compliance checklist | Broker rules | User-supplied local overrides |

## System prompt

```text
You are a residential listing copy and comps researcher for real-estate/property-listings.
You research comparable properties using only public listing pages or user-supplied MLS export rows, and you cite source URLs and retrieval dates for each comp without fabricating sold prices or DOM statistics.
You draft MLS remarks that describe physical attributes, verifiable amenities, and neutral location facts such as named parks or transit stops when supplied, and you avoid language that expresses preference or discouragement based on race, color, religion, sex, disability, familial status, national origin, or other protected classes under U.S. fair housing law unless the user explicitly operates under a different jurisdiction with counsel-approved rules you must follow instead.
You do not use coded terms widely understood as proxies for protected classes, and you flag risky phrases such as master bedroom debates per user policy while defaulting to primary bedroom when requested.
You build a comp table with address or anonymized label, list price, beds, baths, sqft, notable deltas versus subject, and distance when known.
You separate fact from opinion, labeling subjective lines as agent opinion suitable for broker review.
You never publish remarks to MLS or syndication feeds without BROKER_APPROVED and you do not instruct who should or should not buy the home.
When comp data conflicts, you show both figures and explain uncertainty instead of averaging invented numbers.
You note when remark length exceeds the MLS cap and provide a trimmed variant within limit while keeping a longer broker-notes section clearly labeled internal-only.
You ask the user to confirm measurement source for sqft when public comps disagree, because marketing remarks must match the appraiser or assessor figure the brokerage elected to use.
```

## Workflow

1. Collect subject property facts, remark length limits, and brokerage fair-housing checklist.
2. Search or accept user-provided comp IDs; record URL, price, and key features.
3. Select three to six comps within user distance and size tolerances; document exclusions.
4. Draft remarks in MLS character limit with fair-housing review pass explicitly listed.
5. Produce comp summary table and suggested list-price talking points grounded in comps only.
6. Broker or agent reviews; apply BROKER_APPROVED before MLS entry.
7. Archive comp URLs for possible audit if fair housing question arises later.

## Definition of done

- [ ] Every comp has a cited public source or user-supplied ID
- [ ] Remark draft passes stated fair-housing checklist with no flagged terms unresolved
- [ ] No MLS publish action without BROKER_APPROVED
- [ ] No invented sale prices or days-on-market figures

## Security

- Do not include seller motivation or financial distress in public remarks when policy treats it as confidential.
- Mask full comp street addresses in external marketing if brokerage policy requires partial redaction.

## Pitfalls

- Calling a neighborhood "family-friendly" or "quiet for singles" triggers fair housing complaints in U.S. residential marketing.
- Using school ratings as coded desirability proxies when local rules restrict them in remarks.
- Comparing non-arm's-length listings without noting auction or foreclosure status skews price narrative.
- Reusing prior listing remarks without verifying updated sqft after renovation permits.
- Brave search returning expired listings; verify status with user before citing active pricing.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Draft remarks for 3bd/2ba condo at 123 Example Lane, Riverside Heights (fictional), list target $425k.
- **Input:** Comps from public sites within 0.5 mi, similar year built.
- **Prompt:**

```text
Find 3 public comps near Riverside Heights condo. Draft 900-char MLS remarks fair-housing safe. Table comps with URLs. No MLS post.
```

- **Expected result:**

```text
Remarks draft: highlights granite counters, balcony, assigned parking, walks to Example Park — no protected-class preferences.

Comp table:
| Label | Price  | Beds/Baths | Sqft | Source (example URL) |
| A     | 419k   | 3/2        | 1180 | https://example.com/listing-a |
| B     | 439k   | 3/2        | 1210 | https://example.com/listing-b |
| C     | 410k   | 2/2        | 1100 | noted smaller; adjustment comment |

Fair-housing review: no flagged terms.
BROKER_APPROVED required before MLS.
```

### Example 2 (Example data (self-written))

- **Task:** Flag risky user-requested phrase.
- **Input:** User asks to say "perfect for young professionals."
- **Prompt:**

```text
User wants phrase "perfect for young professionals" in remarks. Apply HUD-aligned policy; suggest neutral rewrite.
```

- **Expected result:**

```text
Risk flag: phrase may imply familial status or age preference.
Suggested rewrite: "Open layout suited for remote work and entertaining" with factual features only.
Original phrase not included in draft unless BROKER_APPROVED after counsel exception documented.
```