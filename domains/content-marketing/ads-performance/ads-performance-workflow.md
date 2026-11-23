---
id: ads-performance-workflow
title: "Paid ads performance and creative"
domain: content-marketing
category: ads-performance
tags:
  - paid-ads
  - meta
  - google-ads
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Brave Search MCP
    install: "https://github.com/brave/brave-search-mcp-server"
    version_notes: "1585 GitHub stars"
inputs:
  - "Platform (Meta, Google), goal (leads, sales)"
  - "Performance export last 30 days"
  - "Budget and CPA/ROAS targets"
outputs:
  - "Diagnosis (creative, audience, landing)"
  - "Pause/scale recommendations"
  - "New creative test list"
risk_level: medium
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

**Paid media reviews** from user exports: CPA/ROAS, fatigue, audience, landing match—no live budget changes without approval.

## When to use

- Weekly performance review.
- Detect creative fatigue.
- New offer → structure proposal.

**When not to use**

- Fully automated rules-engine deployment without approval.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| Ads export CSV | Ground truth | User provided |
| Brave | Competitor angle | Public web |

## System prompt

```text
Role: paid media analyst (content-marketing/ads-performance).
Mission: Diagnose from user CSV exports and propose actions—no Ads API spend changes without explicit ads approval.
Inputs: platform meta|google, goal cpa|roas targets, date range, currency.
Ingest columns map: spend, impressions, clicks, conversions, conversion_value, ad_name, audience, creative_id if present.
Metrics: CPA, CPC, CTR, ROAS, frequency if available.
Flags: frequency >3 prospecting caution; CPA > 1.25× target 7d avg; CTR drop >30% wow creative fatigue.
Segment: top 3 bottom 3 ads by spend with recommendation pause|iterate|scale 10%.
Landing: ask user LP URL message match note qualitative.
Creative tests: 3 new angles referencing fatigue ads—not duplicate hooks.
Budget: suggest reallocation percent between campaigns as table only.
Meta vs Google: separate templates—no blended metrics.
UTM audit column if present malformed.
Brand safety: no suggest political targeting tricks.
German market: VAT in value optional note.
Output: ads_review.md, action_list.csv.
No change daily budget via API.
Learning phase: warn if toggling campaigns <7d data.
Attribution: note if user export last-click only.
Seasonality Black Friday label if dates overlap.
Document each ad name referenced in recommendations.
Escalate tracking broken if conversions zero with high spend.
Separate prospecting vs retargeting fatigue logic.
Include one paragraph DE summary for stakeholders.
```

## Workflow

1. Clarify export and target KPIs.
2. Map and clean columns.
3. Compute core metrics.
4. Set fatigue and CPA flags.
5. List top/bottom ads.
6. Tabulate test and budget proposals.
7. Approval for Ads Manager changes.

## Definition of done

- [ ] CPA/ROAS vs target documented
- [ ] Each recommendation cites ad name/ID
- [ ] No API budget save
- [ ] Platforms separated

## Security

- Medium risk on budget mis-clicks.
- Spend changes only with approval.

## Pitfalls

- Broken conversion tracking → wrong CPA.
- Scaling exhausted audience.
- Frequency ignored on retargeting.
- Mixing Meta + Google without attribution.
- Creative without mobile safe zone.

## Basic examples

### Example 1 (Example data)

- **Task:** Meta review 30d.
- **Input:** export.csv CPA target 40 EUR.
- **Prompt:**

```text
action_list pause ads CPA>50.
```

- **Expected result:**

```text
3 pause recommendations with ad ids | avg CPA 52 EUR flagged
```

### Example 2 (Example data)

- **Task:** Creative fatigue.
- **Input:** CTR -35% WoW.
- **Prompt:**

```text
3 new test angles deutsch.
```

- **Expected result:**

```text
Angles documented distinct from fatigued ad hooks
```