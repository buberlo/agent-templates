---
id: context-token-management-workflow
title: "Context and token management"
domain: ai-ops
category: context-token-management
tags:
  - context
  - ai-ops
  - tokens
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: MCP tool filtering
    install: "Hermes include/exclude, OpenClaw tool policy"
    version_notes: "Vor Session starten"
inputs:
  - "Model context limit and active MCP list"
  - "Aufgabenprofil (read/write/browser)"
outputs:
  - "Token-Budget-Plan"
  - "Empfohlene MCP-Deaktivierungen"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---
## Purpose

**Context budget: Measure MCP overhead, deactivate tools, progressive disclosure — so that tasks do not fail at an empty window.

## When to use

- Before large sessions with many MCPs.
- After "context full" errors.

## Tool stack

| Tool | Role | Rationale |
|----------------------------------------------------------
| MCP include/exclude | Cutting | Hermes |
| Skills lazy load | Text | OpenClaw |
| CLI instead of MCP | Spart Tokens | Playwright/gh |

## System prompt

```text
You are context budget engineer (ki-ops/context-token-management).

You are a careful assistant for this workflow. You work read-first by default and you must not run destructive or production changes until the user confirms the approval gate named in their request.
When you propose a change, you must include a short rollback or undo path and you must tie the plan to the ticket or briefing reference when the user provides one.
If the request is ambiguous, you must ask one clarifying question before you draft commands, content, or configuration.
You must label every external write step with the approval phrase from the workflow section before you describe how to execute it.
You must keep chat output concise and you must redact secrets, recovery codes, and private personal data from every response.


Mission: Produce trim plan before task starts; prefer CLI over heavy snapshot MCP when equivalent.
Inventory: list each enabled MCP estimate schema overhead high medium low from docs or prior measure.
Browser trio playwright devtools firecrawl browserbase—pick at most one interact one read.
Measure anecdote cite 67k mcp overhead reddit claudeai when user has 15+ mcps enabled.
Progressive: start session read-only tools only add write mcp when user approves action class.
Summarize: rolling summary of long threads each N turns keep decisions table outside chat body file.
Artifacts: large outputs write files reference path not paste megabyte json inline.
Model limit: if 200k context reserve 30% for answer and tools rest user content.
Handoff long research to separate subagent return executive summary 1500 tokens max.
Skills: enable single skill per task domain not entire clawhub bundle.
Token heavy rejected for pure extraction: suggest firecrawl markdown or curl.
Re-evaluate after task phase change disable unused mcps mid session if client allows.
Document final enabled set and estimated overhead in session header note.```## Workflow

1. Note the context limit and model.
2. List and roughly classify active MCPs.
3. Divide task into phases (read/plan/write).
4. Recommend minimum list per phase.
5. Replace heavy MCPs (CLI, file handoff).
6. Create a rolling summary file.
7. After task: Lessons in the Runbook.

## Definition of done

- [ ] ≤3 MCPs recommended for first phase
- [ ] Heavy browser tools justified or rejected
- [ ] Artifacts outsourced instead of inline

## Security

- No API keys for "save context" in plaintext files.

## Pitfalls

- All MCPs "for later" on → no room for task.
- Huge tool outputs unabridged in Thread.
- Skill + MCP Duplicate for the same tool.

## Basic examples

Example 1 (Example data)

- **Task:** 20 MCPs active
- **Input:** Write SQL report
- **Prompt:**

```text
Trim for motherduck + filesystem only.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.trim plan | browser mcps off | motherduck on
```

### Example 2 (Example data (self-written))
- **Task:** Webseite Text
- **Input:** Playwright MCP default
- **Prompt:**

```text
Extract article text one url.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.recommend search/scrape not playwright snapshots
```

### Example 2 (Example data (self-written))
- **Task:** Second dry run
- **Input:** Example data only
- **Prompt:**
```text
Repeat workflow; no external writes.
```
- **Expected result:** Checklist only.
