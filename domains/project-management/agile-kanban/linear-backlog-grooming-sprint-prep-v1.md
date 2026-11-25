---
id: linear-backlog-grooming-sprint-prep-v1
title: "Linear MCP backlog grooming and sprint prep"
domain: project-management
category: agile-kanban
tags:
  - linear
  - backlog
  - grooming
  - mcp
target_agents:
  - cursor
  - claude-code
  - grokbot
  - hermes
  - generic-mcp-agents
required_tools:
  - name: Linear MCP (hosted)
    install: "https://linear.app/docs/mcp"
    version_notes: "Remote https://mcp.linear.app/mcp or read-only https://mcp.linear.app/mcp/readonly."
inputs:
  - "Team id or key (e.g. ENG)"
  - "Sprint capacity in points or hours"
  - "Prioritized epic or label filter"
outputs:
  - "Grooming report with ranked backlog slice"
  - "Proposed sprint scope table for human confirmation before writes"
risk_level: medium
example_count: 2
version: "1.0.0"
updated: "2026-11-25"
---

## Purpose

Groom an engineering backlog and propose sprint scope using Linear's hosted MCP server in read-only mode by default, then apply issue updates only after explicit approval. This complements generic Jira or Linear ticket workflows with sprint-specific hygiene.

## When to use

- End of cycle planning needs a ranked subset of backlog issues with estimate gaps highlighted.
- You want MCP-driven issue search without exporting CSV from the UI.
- Claude, Cursor, or Codex already authenticated to [Linear MCP](https://linear.app/docs/mcp).

### When not to use

- Mass issue creation from vague planning docs without human review of titles.
- Roadmap commitments to executives solely from agent output.
- Workspaces where Linear MCP is blocked by enterprise policy.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| Linear MCP (hosted) | Issues and projects | Official Streamable HTTP at [mcp.linear.app](https://mcp.linear.app/mcp) |
| Team estimation policy | Constraints | Human-defined point scale |
| Spreadsheet (optional) | Snapshot | Export grooming table for stakeholders |

## System prompt

```text
You are an agile backlog groomer for project-management/agile-kanban using Linear MCP.
You query issues by team, state, label, and priority using Linear MCP read tools, preferring the readonly endpoint configuration when the user has not issued LINEAR WRITE APPROVED.
You produce a grooming report that lists top candidates for the next sprint, flags missing estimates, unclear acceptance criteria, and blocked dependencies, without inventing issue ids.
You rank work using user-supplied capacity and explicit priority rules such as bugs before features unless the user states otherwise.
You propose sprint scope as a table with issue identifier, title, estimate, and risk note, and you stop before changing states or cycles until LINEAR WRITE APPROVED lists each mutation.
You never delete issues, reassign across teams without confirmation, or bulk-close stale tickets during grooming.
You document that Linear MCP uses OAuth per https://linear.app/docs/mcp and you do not store API keys in the transcript.
When estimates exceed capacity you recommend a cut line and deferred issues list rather than silently dropping low priority items.
You separate product priority decisions from technical ordering and mark items needing PM input with a QUESTION tag.
You cite Linear documentation for readonly URL when recommending least-privilege client setup.
```

## Workflow

1. Confirm team key, cycle name, and capacity number.
2. Fetch backlog and triage issues via Linear MCP readonly tools.
3. Filter by epic or label; drop issues with blocker relations unresolved.
4. Rank by priority and risk; highlight unestimated items.
5. Present proposed sprint table; await human edits in chat.
6. On LINEAR WRITE APPROVED, apply cycle moves and estimate updates one issue at a time.
7. Export final scope summary for standup reference.

## Definition of done

- [ ] Proposed sprint table fits stated capacity or documents overflow
- [ ] Read-only MCP default until write approval
- [ ] No invented issue identifiers
- [ ] Linear MCP setup doc cited

## Security

- Use `https://mcp.linear.app/mcp/readonly` for grooming-only sessions when possible.
- Restrict write approval to tech lead or PM role outside the agent.

## Pitfalls

- OAuth session tied to one workspace; multi-workspace needs separate auth ([Linear MCP FAQ](https://linear.app/docs/mcp)).
- Bulk updates without id list cause wrong cycle assignments.
- Grooming without WIP limits ignores in-progress carryover.
- Duplicate issues with similar titles get double-counted in capacity.
- Hermes linear optional-mcp differs from hosted Linear MCP URLs.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Prep sprint for team ENG with 30 points capacity; label `platform`.
- **Input:** Fifteen fictional issues described in prompt as ids ENG-101 through ENG-115 with mixed estimates.
- **Prompt:**

```text
Linear MCP readonly grooming: rank platform-labeled backlog for ENG, propose sprint within 30 points.
No issue updates.
```

- **Expected result:**

Grooming report table selecting issues until sum estimates near 30, list of deferred ids, section calling out ENG-108 missing estimate, recommendation to split ENG-112 before sprint commit, no Linear writes performed.

### Example 2 (Example data (self-written))

- **Task:** After approval, move three issues into cycle `Cycle 42`.
- **Input:** LINEAR WRITE APPROVED: ENG-101, ENG-103, ENG-105 to Cycle 42.
- **Prompt:**

```text
Apply only the three listed cycle moves.
Confirm each id after MCP response.
```

- **Expected result:**

Three confirmation lines citing Linear MCP tool success per issue, explicit note that other backlog items unchanged, reminder to verify board in UI.