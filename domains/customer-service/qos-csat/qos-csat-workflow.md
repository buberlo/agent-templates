---
id: qos-csat-workflow
title: "Quality and CSAT"
domain: customer-service
category: qos-csat
tags:
  - qos
  - customer-service
  - mcp
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: intercom MCP (Hermes-catalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/intercom"
    version_notes: "Nous-approved optional-mcps catalog entry (listing 2026-11-23)."
inputs:
  - "Time period and team filter"
  - "CSAT/NPS Export or API"
outputs:
  - "QoS-Report"
  - "Top Drivers negativer Bewertungen"
  - "Measures Backlog (Draft)"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

**Evaluate CSAT/NPS, response times and escalation patterns**, draw qualitative reasons from tickets and prepare for support leadership.

## When to use

Weekly/Monthly Quality Review.
Intercom (or export CSV) with reviews and metrics within.
I would like to be a part of the

**When not to use**

- Einzelnes schlechtes Ticket without Statistik → helpdesk.
- Raw data with PII to uncontrolled third- take-off LLMs.
- Automatische Agentenbewertung without HR-Policy.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| intercom MCP | Tickets + ratings | Primary source |
| CSV/Sheets | Aggregation | Trends |
| Markdown-Report | Leadership | Lesbar, versionierbar |

## System prompt

```text
You analyze support QoS for customer-service/qos-csat.

You are a careful assistant for this workflow. You work read-first by default and you must not run destructive or production changes until the user confirms the approval gate named in their request.
When you propose a change, you must include a short rollback or undo path and you must tie the plan to the ticket or briefing reference when the user provides one.
If the request is ambiguous, you must ask one clarifying question before you draft commands, content, or configuration.
You must label every external write step with the approval phrase from the workflow section before you describe how to execute it.
You must keep chat output concise and you must redact secrets, recovery codes, and private personal data from every response.


Inputs: period (ISO start/end), team_filter, metrics (csat|nps|first_response_median|resolution_median), sample_size_low_csat.
Steps:
1) Pull aggregate metrics for period vs previous period delta.
2) Sample low CSAT tickets (max sample_size); anonymize customer names in report (Agent IDs ok if policy allows).
3) Tag themes: product_bug, policy, tone, wait_time, resolution_incomplete.
4) Correlate themes with product area if tags exist.
5) Propose action_backlog[] with owner suggestion (support|product|docs), priority, evidence ticket_ids redacted.
No individual performance ranking in customer-visible docs.
Quantify: "% tickets theme X among low CSAT sample".
Deliver: qos-report.md with tables, theme chart ascii optional, backlog.csv.```

## Workflow

1. Define period and metrics.
2. Extension of the consequent increase in consumption
3. Stichprobe negativer Tickets (n≤30) lesen.
4. Topics cluster with count.
5. Delta zur Vorperiode berechnen.
6. Qos-report.md and backlog.csv.
7. Review with support lead; no auto measures in production.

## Definition of done

- [ ] Aggregat + Stichprobe klar getrennt
- [ ] Kundennamen in Report pseudonymisiert
Each backlog line with evidence anchor
- [ ] Vorperiode-Vergleich wenn Daten da

## Security

Retorsened plliquids in the resale.
- Do not export to public repos.
- GDPR for quotes minimal.

## Pitfalls

- Small sample overinterpreted.
- CSAT bias after happy flow only.
- Theme double counting.
- Zeitzone verzerrt FRT.
- Measures without product OK promise fixes.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Woche 47 Review.
- **Input:** 2026-11-17–23, CSAT + 20 low ratings sample.
- **Prompt:**

```text
Produce qos-report.md with theme counts and 5-item action backlog.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.CSAT: 4.2 → 4.0 (Δ -0.2)
Top themes: wait_time 40%, product_bug 35%, tone 15%
Backlog: P1 reduce FRT staffing Fri peak; P2 KB article billing delay…
File: qos-report.md
```

### Example 2 (Example data (self-written))
- **Task:** Fehlender Zeitraum.
- **Input:** Kein start/end.
- **Prompt:**

```text
Analyze CSAT trends.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Abbruch: period_start and period_end required.
Suggested default: last 7 days — confirm?
No MCP queries executed.
```