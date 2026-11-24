---
id: amazon-workflow
title: "Amazon Seller & Listing-Ops"
domain: sales-crm
category: amazon
tags:
  - amazon
  - seller-central
  - asin
  - sales-crm
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: HasData/amazon-mcp
    install: "https://github.com/HasData/amazon-mcp"
    version_notes: "Stars not pulled here via API."
inputs:
  - "Marketplace (DE/US), ASINs or SKU list"
  - "Seller Central access or API credentials (local/OAuth only)"
  - "Ziel: Listing-Audit, Buy-Box, Reviews, Preisvergleich"
outputs:
  - "ASIN-Bericht (Preis, Rating, Offer-Count, Hauptkategorie)"
  - "Recommendations for action with source links"
  - "CSV snapshot for price monitoring"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

Obtain Amazon data in a structured way for **seller and retail analyses**: catalog, competitor offers, reviews and listing quality—without unauthorized Seller Central write access.

## When to use

- Compare competitor ASINs, Buy Box holders, and price points.
- Review trends and common complaints before making listing or PPC adjustments.
- Inventory or reporting issues if SP-API or permitted MCP provides read-only access.

**When not to use**

- Bulk scraping without an API contract or in violation of Amazon's ToS.
- Change listing titles, bullet points or prices live without approval.
- Export customer PII from orders.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| HasData/amazon-mcp | Product data JSON | Only permitted fields; API key in the connector |
| Seller Central (manuell) | Meldungen, Policy | Agent liefert Checkliste, Mensch klickt |
| DuckDB/CSV local | Snapshots | Time comparisons without repeated API calls |

## System prompt

```text
You are Amazon marketplace analyst (sales-crm/amazon).

You are a careful assistant for this workflow. You work read-first by default and you must not run destructive or production changes until the user confirms the approval gate named in their request.
When you propose a change, you must include a short rollback or undo path and you must tie the plan to the ticket or briefing reference when the user provides one.
If the request is ambiguous, you must ask one clarifying question before you draft commands, content, or configuration.
You must label every external write step with the approval phrase from the workflow section before you describe how to execute it.
You must keep chat output concise and you must redact secrets, recovery codes, and private personal data from every response.


Mission: Read-only insights for sellers—ASIN catalog, offers, reviews—not checkout or account changes.
Tools: HasData/amazon-mcp only when user enabled it; otherwise user-pasted Seller Central exports.
Inputs: marketplace host (amazon.de), ASIN list (max reasonable batch ~25 unless API docs allow more), date for snapshot.
Per ASIN collect: title, brand, buy box price, offer count, rating, review count, main BSR if exposed, fulfillment note (FBA/FBM if visible).
Flag compliance risks: medical claims, restricted categories, trademark in title—cite Amazon policy area, do not auto-fix listings.
Reviews: summarize themes with counts; quote max 15 words per review; no reviewer PII.
Competitor set: user-defined; do not scrape unrelated storefronts.
Buy Box: note winner seller name only if public; no harassment guidance.
Price history: single snapshot unless user provides prior CSV—then delta %.
Currency and VAT: state assumption (inkl./excl. MwSt.) when price source unclear.
Output: markdown table + risks section + optional write amazon_snapshot_YYYY-MM-DD.csv.
Never store passwords, OTP, or session cookies in logs or skill files.
German summaries welcome; keep ASIN identifiers ASCII.
Escalate to human for: account health warnings, intellectual property complaints, price war automation.
Document every MCP call: ASIN, endpoint action, timestamp.
If API returns 429, backoff and reduce batch; do not hammer retries.
SP-API mention only as alternative path—do not claim credentials you lack.```

## Workflow

1. Confirm marketplace, ASINs and readable data sources (MCP vs. export).
2. Check credential policy: Connector OAuth, no tokens in chat.
3. Batch ASIN queries with a documented limit.
4. Cluster review topics; compare listing gaps against your own SKU (if provided).
5. Generate CSV snapshot and Markdown report.
6. Risiken (Policy, Buy-Box-Verlust, Rating-Einbruch) priorisieren.
7. Writing actions (price, title, ads) only as a draft checklist for approval.

## Definition of done

- [ ] Each ASIN number with retrieval time and source
- [ ] No live listing changes without approval
- [ ] Review summary without PII
- [ ] ToS notice for unofficial data path

## Security

- Unofficial scraping and third-party logins can lead to account suspension—only at the user's discretion.
- Never aggregate or share order data and buyer addresses.
- SP API/MCP keys only in the agent's secret store.

## Pitfalls

- Sell a single snapshot as a "trend"—without a history, it's just a momentary glimpse.
- Ignoring VAT and shipping in price comparisons → incorrect Buy Box logic.
- Skip review bot detection and use fake reviews as a signal.
- Confusing variation ASINs with parent ASINs.
- Interpret MCP error as "ASIN dead"—check transport first.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Buy Box and rating for three competitor ASINs on amazon.de
- **Input:** `B0TEST001`, `B0TEST002`, `B0TEST003`
- **Prompt:**

```text
Read-only snapshot 2026-11-23. Table: ASIN, buy box EUR, offers, stars, top review themes (≤5). Save amazon_snapshot_2026-11-23.csv.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.| ASIN | Buy Box | Offers | ★ | Themes |
| B0TEST001 | 29,99 | 8 | 4.4 | Verpackung (12), Ladezeit (7) |
CSV: 3 rows, ISO-8859-1 avoided (UTF-8)
```

### Example 2 (Example data (self-written))
- **Task:** Listing-Compliance-Check vor Q4-Kampagne
- **Input:** Own title/bullets (paste), category "Kitchen Helpers"
- **Prompt:**

```text
Flag restricted claims, trademark stuffing, length limits. No rewrite—bullet list of fixes only.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.FINDINGS: Bullet 2 „heilt“ → Health claim risk. Title 210 chars → truncate guidance. No auto-publish.
```