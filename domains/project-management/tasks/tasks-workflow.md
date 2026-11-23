---
id: tasks-workflow
title: "Tasks"
domain: project-management
category: tasks
tags:
  - tasks
  - todoist
  - productivity
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: todoist MCP (Hermes catalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/todoist"
    version_notes: "Nous-approved optional-mcps catalog entry (Listing 23.11.2026)."
  - name: Hermes-Skills document-to-action-items, weekly-review-planning
    install: "https://hermes-agent.nousresearch.com/docs/reference/skills-catalog"
    version_notes: "Bundled."
inputs:
  - "Inbox source: meeting notes, email text, or document path"
  - "Todoist-Projekt/Label (optional)"
  - "Zeitzone Default Europe/Vienna"
  - "Erlaubt: create|complete (Default: create draft list, complete=false)"
outputs:
  - "task_candidates.md (action, owner, due, context)"
  - "todoist_import_review.md"
  - "inbox_zero_summary.md nach Verarbeitung"
  - "weekly plan draft.md (Mo–Fr blocks)"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

Aufgaben aus Inbox-Material extrahieren, in Todoist **strukturiert vorbereiten or anlegen**, Due Dates in Europe/Vienna—no stillen Completes, no invented Deadlines.

## When to use

- Meeting-Notes → Action Items.
Weekly review with prioritization.
- E-Mail-/Slack-Export als Task-Liste.

**When not**

- Fremde Tasks als erledigt markieren.
- Due Dates raten wenn User „offen“ will.
- Without release en masse Todoist.

## Tool stack

| Tool | Role | Justification |
|------|-------|------------|
| todoist MCP | Tasks lesen/anlegen | Zentrale Task-Liste |
| Hermes-Skills document-to-action-items | Extraktion |Aus Dokumenten|
| weekly-review-planning | Wochenstruktur | Planungsblock |

## System prompt

```text
Role: Personal/team task operator (project-management/tasks).
Mission: Extract actionable tasks, suggest dues responsibly, sync Todoist only with approval.
Extraction: imperative verb first; one outcome per task; split if compound "and".
Owner: default assignee user unless @name in source; unassigned → tag review.
Due: only if explicit date in source or user rule (e.g. "EOD" → today 17:00 Europe/Vienna); else no date field.
Priority: map urgent/important words to p1-p4 Todoist only if user glossary supplied.
Context: project @context from user labels; do not create new projects without USER_APPROVAL PROJECT.
Todoist create: batch max 10 per run unless user override; show preview in task_candidates.md first.
Complete: forbidden unless USER_APPROVAL COMPLETE and task id listed—never inbox sweep complete.
Duplicates: fuzzy match against open Todoist tasks if MCP read enabled—mark DUPLICATE skip.
Inbox zero: list processed sources, remaining ambiguous items as questions.
Weekly plan: bucket tasks into deep work / admin / meetings; respect user capacity hours/day.
document-to-action-items skill: use for long docs; cite paragraph for each task.
No silent deletes; reschedule proposes diff only.
Recurring: detect patterns but do not set recurrence without user confirm.
Language: task text in source language.
```

## Workflow

1. Read inbox source; confirm time zone.
2. Action Items extrahieren (Skill bei langen Docs).
3. Structuring candidates with owner/due/project.
4. Check open Todoist tasks for duplicates.
5. Preview; create at USER_APPROVAL CREATE in Todoist.
6. Unklare Items als Nachfragen listen.
7. Optional weekly_plan_draft aus offenen Tasks.

## Definition of done / Definition of Done

- [ ] Any task with source line or section
- [ ] No Due Date without Regel or Explizitheit
- [ ] Preview before Create (except User skip preview)
- [ ] No complete without FREEDOM COMPLETE

## Security

- Todoist Create/Complete/Delete only with release.
- No private content from Inbox to public logs.

## Pitfalls

- "Next week" without reference date incorrectly calculated.
- Meeting-Task an alle Teilnehmer statt Owner.
- 50 Micro-Tasks aus einem Satz generiert.
- DUPLICATE check out because Read is not allowed.
Complete on completing similarity without ID.

## Basic examples

### Example 1 (Example data)

- **Task:** Meeting Notes 1 Seite → Todoist Preview
- **Input:** 6 bullets, 2 with date “Fr 28.11.”, TZ Vienna
- **Prompt:**

```text
Task candidates and dedupe read open tasks. Please note that the information provided by the exporting producer is verified.
```

- **Expected result:**

```text
6 candidates | 2 with due | 0 todoist created | 1 duplicate flagged if match
```

### Example 2 (Example data)

- **Task:** FREEGABE COMPLETE all inbox
- **Input:** unspezifiziert
- **Prompt:**

```text
Reject bulk complete.
```

- **Expected result:**

```text
No completes | list ids required | inbox unchanged
```