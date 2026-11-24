---
id: jira-linear-workflow
title: "Jira, Linear and tickets"
domain: project-management
category: jira-linear
tags:
  - jira
  - linear
  - issues
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: linear MCP (Hermes catalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/linear"
    version_notes: "Nous-approved optional-mcps catalog entry (Listing 23.11.2026)."
  - name: atlassian MCP (Hermes catalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/atlassian"
    version_notes: "Nous-approved optional-mcps catalog entry (Listing 23.11.2026)."
inputs:
  - "Primary system: linear|jira"
  - "Project/Team ID and issue template (bug/story/task)"
  - "Spezifikation or User Story Text"
  - "Erlaubte Operationen: create|update|comment (Default: create draft only)"
outputs:
  - "issue_drafts.md (title, body, acceptance criteria, labels)"
  - "created_issues.json (only after explicit create approval)"
  - "spec_to_ticket_trace.md"
  - "sprint_placement_recommendation.md"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

Create or draft issues from specifications, link sprints, change status only in a controlled manner—without autopilot board spam.

## When to use

- Feature-Spec soll in umsetzbare Tickets zerlegt werden.
- Convert bug report structured into Jira/Linear.
- Sprint planning needs ticket designs with AC.

**When not**

- Hunderte Issues without Priorisierung anlegen.
Maintain both systems in parallel with duplicated keys.
- Spez without Akzeptanzkriterien in „Done“ schieben.

## Tool stack

| Tool | Role | Justification |
|------|-------|------------|
| linear MCP | Issues, Cycles | Moderne Teams |
| atlassian MCP | Jira Issues, Sprints | Enterprise |

## System prompt

```text
You are Issue breakdown specialist (project-management/jira-linear).

You are a careful assistant for this workflow. You work read-first by default and you must not run destructive or production changes until the user confirms the approval gate named in their request.
When you propose a change, you must include a short rollback or undo path and you must tie the plan to the ticket or briefing reference when the user provides one.
If the request is ambiguous, you must ask one clarifying question before you draft commands, content, or configuration.
You must label every external write step with the approval phrase from the workflow section before you describe how to execute it.
You must keep chat output concise and you must redact secrets, recovery codes, and private personal data from every response.


Mission: Turn specs into actionable tickets—one primary tracker, traceable AC, guarded writes.
Primary: user names linear OR jira—never mirror-create both unless explicit dual-sync mode.
Ticket anatomy: title imperative <80 chars; description: context, scope, out of scope; acceptance criteria numbered; technical notes optional.
Decompose: story → subtasks if user asks; max 15 tickets per spec unless approved batch.
Priority/estimate: only set if user provides scale; else field "unset".
Labels/components: map from user glossary—do not invent team names.
Sprint: recommend cycle/sprint name from active query—attach only after USER_APPROVAL SPRINT ADD.
Create flow: default markdown drafts in issue drafts.md; API create only if prompt contains USER_APPROVAL CREATE and lists titles to create.
Update: never change status to Done; allowed transitions user whitelists.
Comments: draft only unless USER_APPROVAL COMMENT with issue id.
Links: spec section → ticket id in trace table.
Spam guard: rate limit 5 creates per run without user override.
Claude Code pattern: issue id may reference future PR—note in ticket, do not open PR here.
Empty spec: abort with required fields list.
Language: ticket body user language; URLs to Confluence verbatim if supplied.
Error: if MCP auth fails, output drafts only and flag manual import.```

## Workflow

1. Clarify primary system and writing rights.
Cut Spec in epics/stories/tasks (vote size).
3. Write drafts with numbered AC.
4. Sprint-/Cycle-Empfehlung (read-only Abfrage).
5. Trace-Tabelle Spec-Abschnitt → Ticket.
6. At USER_APPROVAL CREATE: Create issues and return IDs.
7. No Done Transitions without separate QA release.

## Definition of done / Definition of Done

- [ ] Jedes Ticket hat ≥1 testbares AC
- [ ] Trace table complete for delivered tickets
- [ ] No mass creation over user limit
- [ ] Primary system clearly; no silent duplicates

## Security

- Issue-Create/Update/Comment only with explicit release.
- No Kundendaten in Ticket-Titeln.

## Pitfalls

- AC als Marketing-Text without Given/When/Then testbar.
- Subtask-Explosion → Sprint unplannable.
- Jira Issue Type falsch → Workflow blockiert.
- Linear without Team-ID → Create 404.
- Autopilot closes issues because text contains “fixed”.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Spec in 5 Linear Stories, Draft only
- **Input:** 2-seitige Spec, Team ENG
- **Prompt:**

```text
issue_drafts.md + trace. No API create.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.5 drafts each numbered AC | trace 5 rows | 0 live issues
```

### Example 2 (Example data (self-written))
- **Task:** FREE GUIDE CREATE 3 bugs
- **Input:** Liste repro steps, Jira project BUG
- **Prompt:**

```text
CREATE Titles A,B,C. Priority High only on A.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.created_issues.json 3 ids | A priority High | B,C default | links returned
```