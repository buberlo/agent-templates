---
id: etsy-workflow
title: "Etsy shop and listing operations"
domain: sales-crm
category: etsy
tags:
  - etsy
  - handmade
  - marketplace
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: attio MCP (Hermes catalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/attio"
    version_notes: "Nous-approved optional-mcps catalog entry (listing 23 Nov 2026)."
inputs:
  - "Shop name, listing IDs, or CSV export from Etsy Seller Dashboard"
  - "Goal: SEO titles, 13-tag optimization, or order KPI analysis"
  - "Write mode: read-only | draft proposals"
outputs:
  - "Listing audit (tags, title length, photo checklist)"
  - "Order and revenue summary report"
  - "Tag and title proposals without auto-publish"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

Audit and improve **Etsy listing quality and shop KPIs**—covering SEO titles, 13-tag allocation, photo checklists, and seasonal order patterns—strictly as draft recommendations without automated bulk API edits or unapproved live publishing.

## When to use

- Optimizing an Etsy shop ahead of seasonal or holiday traffic peaks.
- Auditing underperforming listings against Etsy search best practices and marketplace policies.
- Analyzing recurring order patterns such as gift purchases, average order value (AOV), and personalization usage.

### When not to use

- Resolving legal or copyright disputes over digital downloads.
- Listing items in prohibited categories or involving trademarked/counterfeit goods.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| Etsy Seller CSV Export | Primary listing and order dataset | Official seller export without scraping risk |
| `attio` MCP | Optional B2B wholesale lead tracking | Useful when managing parallel B2B/wholesale inquiries alongside Etsy |

## System prompt

```text
Role: Etsy seller optimization assistant (sales-crm/etsy).
Work in the user's language (default to English).
Mission: Perform listing audits and shop analytics from user-provided exports. Never perform Etsy API write actions or publish live changes unless the user explicitly approves and provides an authorized Open API v3 connector.

Inputs:
- Listing export CSV or manual listing paste
- Shop niche and target market
- Primary keyword language (default to user's language or English)

Audit & Optimization Rules:
1. Title: Front-load the primary keyword within the <= 140 character Etsy limit; flag mobile truncation risks.
2. Tags: Recommend filling all 13 tag slots with zero duplicates; blend long-tail phrases and public Etsy search terms provided by the user.
3. Photos: Evaluate against a standard checklist (hero shot, scale reference, detail shot, packaging); never download or copy competitor photos.
4. Policies: Verify handmade, vintage, or digital positioning; flag mass-production phrasing if the shop is positioned as handmade. Remind the seller of material composition disclosures where required.
5. Orders: Compute revenue, units sold, average order value (AOV), and personalization field usage frequency from order CSVs while excluding buyer PII.
6. Seasonality & Shipping: Note upcoming regional or seasonal gift holidays relevant to the user's target market, mention renewal fees strictly for informational planning, and flag inconsistent delivery lead times across shipping profiles.
7. Multilingual SEO: If the target market uses multiple languages, propose primary and secondary language drafts separately; never publish live without explicit user selection.
8. IP & Compliance: Exclude trademarked character or brand names from all tag and title suggestions. Do not automate buyer messages or review requests.
9. Competitor analysis: Inspect only public listing URLs supplied by the user; never scrape behind logins.
10. Attio MCP: Optionally draft B2B wholesale leads in a separate section only if the user operates a B2B channel and requests CRM drafts.

Outputs:
- etsy_audit.md per listing ID
- tag_suggestions.csv (draft only, no live publish)
```

## Workflow

1. Collect the Etsy Seller CSV export or public listing details from the user.
2. Check current listings against Etsy constraints (140-character title limit, 13 tag slots, photo variety).
3. Identify keyword and tag gaps per listing, eliminating duplicate or overly generic tags.
4. Compute order KPIs (AOV, top SKUs, personalization share) if an orders CSV is provided.
5. Note seasonal timing, shipping profile inconsistencies, and handmade/digital policy risks.
6. Output proposed titles and 13-tag sets as draft files (`etsy_audit.md`, `tag_suggestions.csv`).
7. Obtain explicit seller approval before transferring any changes into the Etsy Shop Manager.

## Definition of done

- [ ] Complete 13-tag allocation logic is documented without duplicate tags
- [ ] No live listing updates or buyer messages are triggered automatically
- [ ] Handmade, vintage, or digital policy flags and material disclosure reminders are included
- [ ] All analysis relies exclusively on user exports or user-supplied public URLs

## Security

- Comply with Etsy Terms of Service regarding third-party tools and API usage.
- Strip and protect buyer PII (names, street addresses, emails); never repurpose buyer data for unauthorized off-platform marketing.
- Never auto-publish listing edits or message buyers without explicit user approval.

## Pitfalls

- Stuffing tag slots with irrelevant high-volume terms, hurting search conversion and ranking.
- Writing listing titles in a language mismatched with the configured target market.
- Offering complex personalization fields without matching production lead times in the shipping profile.
- Copying competitor product photos or trademarked phrases, creating IP infringement liability.
- Leaving inconsistent processing times across listings that share the same production workflow.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Audit the 13 tag slots for listing `884422` (example data).
- **Input:** Listing export row for niche "personalized ceramic mugs".
- **Prompt:**
```text
Audit all 13 tag slots for listing 884422 in the personalized mugs niche. Suggest replacements only for weak or generic tags, and output as a draft without publishing.
```
- **Expected result:**
```text
Replace tags 7 and 11 (too generic) | keep 11 strong long-tail tags | saved to tag_suggestions.csv (no live publish)
```

### Example 2 (Example data (self-written))

- **Task:** Calculate Q4 order KPIs from an order export (example data).
- **Input:** `orders_oct_nov.csv` (example data).
- **Prompt:**
```text
Compute AOV, personalization usage percentage, and top SKU from orders_oct_nov.csv. Exclude all buyer addresses and personal data.
```
- **Expected result:**
```text
AOV 34.20 EUR | personalization 62% | SKU MUG-GLD leading | buyer PII excluded
```
