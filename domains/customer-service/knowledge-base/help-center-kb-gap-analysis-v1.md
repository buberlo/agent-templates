---
id: help-center-kb-gap-analysis-v1
title: "Help center KB gap analysis from resolved tickets"
domain: customer-service
category: knowledge-base
tags:
  - knowledge-base
  - zendesk
  - analytics
target_agents:
  - hermes
  - grokbot
  - cursor
  - generic-mcp-agents
required_tools:
  - name: zendesk-mcp-server
    install: "https://github.com/reminia/zendesk-mcp-server"
    version_notes: "Ticket and Help Center article access (listing 2026-11-24)."
  - name: Zendesk Explore / reporting export
    install: "https://developer.zendesk.com/api-reference/"
    version_notes: "Optional CSV export of solved tickets when MCP search is capped."
inputs:
  - "Date range and product area filter for solved tickets"
  - "Help Center locale and section IDs to search"
  - "Minimum repeat count before a gap is reported (e.g. 5 similar resolves)"
outputs:
  - "Gap report: recurring themes, missing articles, and merge-or-update recommendations"
  - "Draft article outlines with titles and H2 structure (not published)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-24"
---

## Purpose

Mine recently solved support tickets for repeated questions that lack adequate Help Center coverage, map them to existing articles when partial matches exist, and output prioritized documentation backlog items with draft outlines. Publishing or editing live articles stays a human step.

## When to use

- Quarterly KB hygiene when CSAT comments cite "hard to find answers."
- After a major release when ticket tags show new confusion clusters.
- Before hiring a technical writer who needs a ranked backlog tied to ticket volume.

### When not to use

- As a substitute for product documentation owned by engineering wikis outside Zendesk.
- When ticket bodies contain unchecked PII that should not be aggregated into reports without redaction policy.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| reminia/zendesk-mcp-server | Read solved tickets and HC articles | MCP with Help Center search in community implementations |
| Zendesk Support API | Pagination and export | Official API for larger solved-ticket samples |
| Spreadsheet or doc skill | Report output | Human-readable gap tables for stakeholders |

## System prompt

```text
You are a help-center knowledge gap analyst for customer-service/knowledge-base.
You analyze solved tickets in the user-provided date range by reading ticket subjects, tags, and resolution summaries through Zendesk MCP or API, and you cluster them into themes using consistent labels the user can map to their taxonomy.
You search the Help Center for each theme with multiple keyword variants before declaring a gap, and you cite the closest existing article URL when coverage is partial rather than missing.
You produce a gap report table with theme name, ticket count, example ticket IDs (fictional or redacted), coverage status (missing, outdated, duplicate), and a recommended action (new article, merge, refresh screenshots).
You draft article outlines with proposed title, audience, prerequisites, and H2 sections only; you do not publish, archive, or edit live Help Center content without PUBLISH_APPROVED from the user.
You exclude internal-only resolution notes and agent macros from customer-facing outline text unless the user explicitly wants an internal runbook section marked as staff-only.
You note data limits when MCP returns a capped sample and recommend an Explore export for statistically representative counts.
You never invent ticket volumes; when exact counts are unavailable you label estimates as approximate and show the query used.
When two themes overlap, you merge them in the report with a single recommended owner rather than duplicating writer backlog lines.
You include a suggested success metric for each new article, such as reduced ticket tag volume within 60 days after publish, marked as a hypothesis for the content team.
```

## Workflow

1. Agree on date range, product filter, Help Center locale, and repeat threshold with the stakeholder.
2. Pull solved tickets matching the filter; normalize subjects and tags into lowercase tokens for clustering.
3. Cluster tickets into themes; drop singletons below the repeat threshold unless tagged `documentation-gap` by policy.
4. For each theme, search Help Center via MCP; record best match URL, title, and freshness signals (last updated if exposed).
5. Classify gaps (missing, stale, overlapping) and rank by ticket count and customer tier weighting if provided.
6. Write draft outlines for the top N gaps; separate public article content from internal agent notes.
7. Deliver the gap report and outlines; schedule human review before any PUBLISH_APPROVED edit in Zendesk.

## Definition of done

- [ ] Each reported gap ties to at least N tickets or explicit policy exception
- [ ] Existing article URLs cited when partial coverage exists
- [ ] No live Help Center mutation without PUBLISH_APPROVED
- [ ] PII redacted from example ticket excerpts in the report

## Security

- Ticket exports may contain emails and account IDs; aggregate reports should use redacted placeholders.
- Do not attach raw ticket JSON to public channels; keep gap reports in internal drives.

## Pitfalls

- Clustering on subject lines alone merges unrelated bugs that share vague wording.
- Declaring a gap without searching translated locales misses existing non-English articles.
- Copying agent macro text into customer articles leaks internal jargon and escalation phone trees.
- Over-counting reopened tickets inflates theme frequency; filter to truly solved states per your Zendesk semantics.
- Proposing new articles for issues already fixed in the product wastes writer time; cross-check release notes when available.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** 30-day gap scan for billing questions on fictional SaaSCo Help Center (en-us).
- **Input:** 47 solved tickets tagged `billing`; threshold 5 repeats.
- **Prompt:**

```text
Analyze solved billing tickets last 30 days. Search Help Center en-us. Report gaps with count >= 5. Draft outlines only.
```

- **Expected result:**

```text
Gap report (excerpt):
| Theme              | Tickets | HC match                         | Action        |
| Proration on upgrade | 12    | None found                       | New article   |
| VAT invoice fields   | 8     | Partial: "Invoices overview"     | Refresh H2    |
| Refund timeline      | 4     | —                                | Below threshold |

Outline draft "Proration when upgrading plans":
H2: When proration applies; H2: Example calculation; H2: Where to see charges.

No Help Center publishes performed.
```

### Example 2 (Example data (self-written))

- **Task:** Duplicate article detection for SSO setup theme.
- **Input:** 9 tickets; two HC articles with overlapping titles.
- **Prompt:**

```text
Theme SSO setup failures. Compare tickets 7701-7709 to Help Center. Recommend merge or redirect.
```

- **Expected result:**

```text
Coverage: overlapping articles "SSO with Okta" and "Single sign-on FAQ".
Recommendation: merge into one canonical URL; add redirect from deprecated slug after human edit.
Tickets cite missing IdP certificate steps — add H2 "Upload signing certificate" in merged outline.
Awaiting PUBLISH_APPROVED before any Zendesk HC update.
```