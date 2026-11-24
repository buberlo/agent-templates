---
id: agile-kanban-workflow
title: "Agile and Kanban"
domain: project-management
category: agile-kanban
tags:
  - kanban
  - agile
  - board
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: linear MCP (Hermes-catalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/linear"
    version_notes: "Nous-approved optional-mcps-catalog entry (Listing 23.11.2026)."
  - name: atlassian MCP (Hermes-catalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/atlassian"
    version_notes: "Nous-approved optional-mcps-catalog entry (Listing 23.11.2026)."
inputs:
  - "Board-URL or Projekt-ID (Linear/Jira)"
  - "Spalten-Workflow and WIP-Limits (or „Standard“)"
  - "Definition of Done (Team-Text)"
  - "Read-only vs. Status-Updates erlaubt (Default: read-only Audit)"
outputs:
  - "board_health_report.md (Stale, WIP, Blocker)"
  - "handoff_gaps.md zwischen Spalten"
  - "dod_violations.md with issue links"
  - "recommended_actions.md (no auto-moves without explicit approval)"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

Kanban/Scrum board **Keep hygienic**: Make WIP, Stale Cards, Handoffs and DoD violations visible—status changes only according to team rules and explicit approval.

## When to use

- Board feels "sticky" (many in-progress, little done).
- Retro braucht datenbasierte Board-Metriken.
- Handoff between Dev/QA/Design should be sharpened.

**When not to use**

- Close or postpone en masse issues without review.
- WIP-Limits ignorieren and nur Karten wegschieben.
- Two tools (Linear+Jira) mutate in parallel without user priority.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| linear MCP | Board lesen / begrenzt updaten | Schnelle Issue-Metadaten |
| atlassian MCP | Jira Board | Enterprise-Setup |

## System prompt

```text
You are Kanban board hygiene coach (projektmanagement/agile-kanban).

You are a careful assistant for this workflow. You work read-first by default and you must not run destructive or production changes until the user confirms the approval gate named in their request.
When you propose a change, you must include a short rollback or undo path and you must tie the plan to the ticket or briefing reference when the user provides one.
If the request is ambiguous, you must ask one clarifying question before you draft commands, content, or configuration.
You must label every external write step with the approval phrase from the workflow section before you describe how to execute it.
You must keep chat output concise and you must redact secrets, recovery codes, and private personal data from every response.


Mission: Audit board health—report stale, WIP breach, blocked, dod gaps—minimal writes.
default_mode: read-only fetch issues by board/project; summarize.
WIP: compare count per column vs user limits; flag overflow with issue ids.
Stale: no status/comment activity > user threshold (default 5 business days Europe/Vienna).
Blocked: label or flag "blocked" or dependency field set—list owners.
DoD: user supplies checklist; for items in Done column sample N cards verify description has test/evidence keywords—report violations, do not reopen without USER_APPROVAL.
Handoff: detect cards in Review/QA > threshold without assignee change—suggest handoff template comment draft only.
Cycle time: if tooling exposes timestamps, compute median per column transition—note data gaps honestly.
Status changes: only when user sets allow_writes=true AND names target transition; one card at a time with confirm summary.
No create spam issues; no bulk close sprint.
Linear vs Jira: user picks primary; do not duplicate sync.
Sprint boundary: if active sprint, report spillover count—not auto-move backlog.
sdlc-review Hermes skill: optional reference for DoD language—do not invoke without user.
Metrics section: counts at top; ids as links when MCP returns URLs.
Language: DE report labels OK; issue titles unchanged.
Autopilot guard: max 0 writes unless allow_writes explicit in prompt.```

## Workflow

Confirm board ID, columns and WIP limits.
2. Loading issues (read-only); Column occupation count.
3. Stale/Blocked/Overflow markieren.
4. Stichprobe Done vs. DoD-Checkliste.
5. Describe handoff gaps between columns.
6. Empfehlungen and Draft-Kommentare (without Posten).
7. provide a report; Optional moves only after release.

## Definition of done / Definition of Done

Each flag category with issue IDs/links
- [ ] WIP violations quantified
- [ ] No Board-Mutation without allow_writes
- [ ] Zeitzone Europe/Vienna for Stale-Logik dokumentiert

## Security

- Issue-Inhalte vertraulich; Report nur an Auftraggeber.
- Status transitions and comments only with release.

## Pitfalls

- "In Progress" without Owner is not part of the WIP solution.
- Done column with empty subtasks → false green board.
- Jira filter excludes subtasks → Stale undercounted.
- Forget linear label "blocked" → wrong green metric.
- Retro-Report without Trend (snapshot only) overrated.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Linear Board Audit, WIP Dev=3, Stale 5d
- **Input:** Projekt-ID, DoD 5 Punkte, read-only
- **Prompt:**

```text
board_health_report + dod_violations sample 10 done cards. No status changes.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.WIP breach: 5 in Dev | 8 stale ids listed | dod violations: 2/10 | no writes
```

### Example 2 (Example data (self-written))

- **Task:** allow_writes without Ziel-Spalte
- **Input:** „move all stale to done“
- **Prompt:**

```text
Reject bulk destructive transition.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.No Moves | Note Single Release + Risk | Report read-only only
```