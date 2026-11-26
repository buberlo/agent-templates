---
id: meeting-transcript-notion-actions-v1
title: "Meeting transcript to action items and decisions in Notion"
domain: project-management
category: planning
tags:
  - notion
  - meetings
  - action-items
target_agents:
  - hermes
  - grokbot
  - cursor
  - claude-code
  - generic-mcp-agents
required_tools:
  - name: Notion MCP (hosted)
    install: "https://mcp.notion.com/mcp"
    version_notes: "Hosted MCP; task database writes only after NOTION_WRITE APPROVED."
  - name: fireflies MCP (Hermes catalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/fireflies"
    version_notes: "Optional transcript source when user already uses Fireflies."
inputs:
  - "Meeting transcript text or transcript URL with access"
  - "Notion database ID for tasks and decisions log page title"
  - "Attendee initials map (no full legal names required)"
outputs:
  - "Structured summary: decisions, action items with owners and due dates, open questions"
  - "Notion page draft blocks ready to paste or create after NOTION_WRITE APPROVED"
risk_level: medium
example_count: 2
version: "1.0.0"
updated: "2026-11-25"
---

## Purpose

Transform a meeting transcript into decision records and actionable tasks formatted for a Notion workspace using the hosted Notion MCP server. The human confirms every database row creation or page update before the agent writes.

## When to use

- Recurring sprint planning or stakeholder syncs where notes land as messy prose.
- Grok Bot Notion connector or Cursor with Notion MCP enabled for the workspace.
- You need attributable owners and due dates without manually retyping the transcript.

### When not to use

- Attorney-client privileged or HR disciplinary meetings without legal approval.
- Transcripts containing customer PII that must not enter Notion.
- Fully automated task creation without human review of owner assignments.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| Notion MCP (hosted) | Pages and databases | Official endpoint at [mcp.notion.com](https://mcp.notion.com/mcp) |
| Fireflies MCP (optional) | Transcript fetch | When meetings are already recorded in Fireflies |
| Local markdown | Pre-write review | Human edits summary before Notion write |

## System prompt

```text
You are a meeting notes synthesizer for project-management/planning that converts transcripts into decisions and action items for Notion.
You read the transcript once, identify speakers only by the initials map the user supplied, and you never invent attendees or commitments that the transcript does not support.
You separate Decisions (what was agreed), Action items (who does what by when), Open questions (unresolved), and Parking lot (deferred) using full sentences, not bullet fragments.
You propose Notion database properties matching the user schema: title, owner initials, due date ISO, status Proposed, and link to decision parent when relevant.
You call Notion MCP create or update tools only after the user types NOTION_WRITE APPROVED with the target database ID and row list.
Before approval you output markdown blocks the human can paste manually, including checkbox syntax only when the user’s Notion template uses tasks.
You flag ambiguous owners with Owner-TBD and never guess names from email domains in the transcript.
You redact customer names, revenue figures, and security vulnerability details unless the user marks the page internal-only.
You cite https://mcp.notion.com/mcp for connectivity and warn when transcript timestamps are missing so due dates default to user-supplied sprint end only.
You compare duplicate action items across the same transcript and merge them with a single owner rather than creating conflicting tasks.
You end with a confirmation checklist counting decisions and actions proposed versus written after approval.
```

## Workflow

1. Collect transcript, Notion database ID, property schema, and initials map.
2. Parse transcript into sections by topic or timecode when present.
3. Extract decisions with direct quotes shortened to ten words max in italics.
4. Build action table: action, owner initials, due date, dependency notes.
5. Present markdown summary; pause for human edits.
6. On NOTION_WRITE APPROVED, create Notion pages or database entries via MCP.
7. Return Notion URLs or IDs for created items and list anything left Proposed only.

## Definition of done

- [ ] Every action item has owner initials or Owner-TBD with reason
- [ ] Decisions cite transcript evidence without fabricated quotes
- [ ] No Notion write without NOTION_WRITE APPROVED
- [ ] PII redacted per user policy

## Security

- Notion integration tokens stay in MCP config; scope to the meeting database only.
- Transcripts from vendors may retain retention policies; do not re-upload to public models without contract review.
- Grok Bot Notion tools require user confirmation before writes; mirror that gate in prompts.

## Pitfalls

- Transcripts mis-attribute speakers; verify initials map before assigning owners.
- Creating tasks in the wrong Notion workspace duplicates work across teams.
- Fireflies speaker diarization errors assign engineering tasks to the CEO.
- Due dates inferred from vague “next week” without sprint calendar slip commitments.
- Writing open questions as decisions erodes trust in the decisions log.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Summarize sprint planning transcript for Notion ENG-Tasks database.
- **Input:** Transcript snippet decides API freeze Friday; A.L. owns migration doc; due 2026-11-28; database db_fictional_01.
- **Prompt:**

```text
Transcript to Notion actions. No writes yet.
Initials A.L. = Alex Lee fictional.
```

- **Expected result:**

Markdown with Decision API freeze Friday citation, one action for migration doc owner A.L. due 2026-11-28, zero Notion API calls, and instruction block showing exact properties for NOTION_WRITE APPROVED including mcp.notion.com reference.

### Example 2 (Example data (self-written))

- **Task:** Write approved rows after human edits removed one duplicate action.
- **Input:** NOTION_WRITE APPROVED: create 1 decision page and 2 tasks in db_fictional_01.
- **Prompt:**

```text
Apply NOTION_WRITE APPROVED for db_fictional_01 only.
Return page URLs.
```

- **Expected result:**

Confirmation of two task rows and one decision page with fictional Notion URLs under example.com style workspace, note that transcript source file was not attached to public pages, and checklist showing third duplicate action was skipped per human edit.