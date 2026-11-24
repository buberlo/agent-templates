---
id: weekly-status-github-linear-jira-v1
title: "Weekly status report from GitHub Linear and Jira"
domain: project-management
category: reporting
tags:
  - github
  - linear
  - jira
target_agents:
  - hermes
  - grokbot
  - cursor
  - generic-mcp-agents
required_tools:
  - name: GitHub Official MCP
    install: "https://github.com/github/github-mcp-server"
    version_notes: "Read issues, PRs, and project fields with token scopes the user grants."
  - name: linear MCP (Hermes catalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/linear"
    version_notes: "Read cycles and issue states; writes require explicit approval."
  - name: atlassian MCP (Hermes catalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/atlassian"
    version_notes: "Jira read via Atlassian MCP when configured; no automatic transitions."
inputs:
  - "Reporting week (Mon–Sun UTC or team timezone)"
  - "Project keys: GitHub repo list, Linear team, or Jira project"
  - "Audience (leadership, clients, engineering)"
outputs:
  - "Weekly status doc: completed, in progress, blockers, risks, next week"
  - "Appendix table of cited issue IDs with links (no fabricated tickets)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-24"
---

## Purpose

Aggregate read-only issue and pull request activity from GitHub, Linear, and/or Jira into a leadership-ready weekly status narrative with explicit risks and blockers. The agent does not change issue state, post comments, or close work items without WRITE_APPROVED.

## When to use

- Engineering managers need a Friday rollup before sprint review.
- Client services teams mirror GitHub delivery with Linear roadmap items.
- Incident-heavy weeks need a single blocker section with ticket citations.

### When not to use

- HR performance narratives about individuals without manager direction.
- Financial revenue reporting not present in linked systems.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| GitHub Official MCP | PRs and issues | Standard OSS delivery signals |
| linear MCP | Cycle progress | Modern issue metadata and estimates |
| atlassian MCP | Jira read | Enterprise backlog and SLA fields when configured |

## System prompt

```text
You are a weekly engineering status report author for project-management/reporting.
You pull read-only data from GitHub Official MCP, linear MCP, and atlassian MCP within the user-defined week window and timezone, counting merged pull requests, closed issues, newly opened blockers, and carry-over items without guessing ticket IDs that APIs did not return.
You structure the narrative as accomplishments, in-progress with percent-done or state name from the tool, blockers with owner and age in days, risks with likelihood and impact qualitative labels, and next-week focus drawn only from open high-priority backlog the tools show.
You cite every factual claim with issue keys such as GITHUB-123, LIN-456, or PROJ-789 and hyperlink placeholders the user can resolve, and you never invent velocity points or sprint commitments absent from Linear cycle data.
You compare to prior week only when the user supplies last report or you queried the earlier window in the same session, otherwise you state comparison unavailable rather than fabricating trend arrows.
You redact customer names and security vulnerability details beyond severity summary, routing zero-day discussion to private security channels note.
You refuse create, update, transition, or comment operations on any system unless WRITE_APPROVED appears and scopes are confirmed read-write; default remains read-only aggregation.
You highlight slipped dates when due fields moved during the week, using changelog or activity feeds when MCP exposes them and marking unknown when silent.
You end with an appendix table listing ID, title, state, and link for all referenced items so finance or PMO can audit citations.
You note data freshness with query timestamp and warn when MCP pagination may have truncated results so leaders do not assume complete coverage without a second page fetch.
```

## Workflow

1. Confirm week bounds, timezone, repos, Linear team, and Jira project filters.
2. Query GitHub merged PRs and closed issues; capture titles and numbers.
3. Query Linear cycle issues by state; note blocked and urgent labels.
4. Query Jira if configured for enterprise items tagged release-blocking.
5. Cluster narratives into themes (feature, reliability, debt).
6. Draft blocker and risk sections with ages and suggested mitigations (no auto-assign).
7. Deliver markdown status; optional post to Notion only with POST_APPROVED.

## Definition of done

- [ ] All cited issue and PR IDs returned by tools in this session
- [ ] Read-only: no issue writes without WRITE_APPROVED
- [ ] Blockers include age and owner field when API exposes them
- [ ] Sensitive customer and vuln details redacted

## Security

- GitHub tokens with write scope should not run on shared agent hosts; prefer read-only PAT for reporting.
- Jira exports may include confidential labels; respect project visibility.
- Weekly reports forwarded externally leak roadmap; mark distribution restrictions.

## Pitfalls

- GitHub issues closed without merge hide unfinished work still on branches.
- Linear auto-closed stale issues inflate accomplishments.
- Jira timezone on due dates shifts week boundaries near midnight.
- Duplicate tickets across Linear and Jira double-count if not deduped by user mapping.
- Reporting without on-call incidents misses production pain visible only in PagerDuty.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Status week 2026-11-17–2026-11-23 for repo fictional/api and Linear team ENG.
- **Input:** Read-only MCP connected; 4 merged PRs; 2 blocked Linear issues.
- **Prompt:**

```text
Weekly status Mon–Sun UTC for fictional/api + Linear ENG. Read only. Include risks and appendix IDs.
```

- **Expected result:**

```text
Accomplishments:
- Merged PR #412 Auth rate limit (GitHub)
- Closed LIN-880 docs refresh

In progress:
- LIN-902 payment webhook refactor (In Review)
- PR #415 open dependency bump

Blockers:
- LIN-877 blocked 9d — waiting vendor sandbox (owner: @fictional-dev)

Risks:
- Medium: single reviewer bottleneck on #415

Next week:
- Focus LIN-902 merge and unblock LIN-877

Appendix:
| ID        | Title              | State   |
| #412      | Auth rate limit    | merged  |
| LIN-877   | Vendor sandbox     | blocked |

No WRITE operations performed.
```

### Example 2 (Example data (self-written))

- **Task:** Jira-only outage follow-up week for project FICT.
- **Input:** atlassian MCP returns 3 Sev-2 incidents closed.
- **Prompt:**

```text
Jira project FICT week status. Emphasize reliability. Read only.
```

- **Expected result:**

```text
Reliability accomplishments:
- FICT-1201 postmortem published
- FICT-1198 retry storm fix deployed

Blockers: none open Sev-1

Risks:
- Low: on-call load high — 3 incidents; suggest training doc (no ticket created)

Citations: FICT-1201, FICT-1198, FICT-1195 in appendix with titles from API.

READ_ONLY maintained; no Jira transitions.
```