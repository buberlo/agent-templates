---
id: content-strategy-workflow
title: "Content-Strategie"
domain: content-marketing
category: content-strategy
tags:
  - strategy
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Brave Search MCP
    install: "https://github.com/brave/brave-search-mcp-server"
    version_notes: "1585 Stars"
inputs:
  - "ICP"
  - "Capacity posts/week"
  - "Quartal"
outputs:
  - "editorial.csv"
  - "pillar map"
  - "funnel mix"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

Pillar/Spoke and calendar within capacity.

## When to use

- Passende Anfrage in **Content-Strategie**.
- With clear approvals at Publish/Send.

**When not to use**

Boilerplate without briefing or data source.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
I had, of ofnah awayrateds, and,la-s travel ahead oftos, gave to when I had,

## System prompt

```text
You are Content strategist.

You are a careful assistant for this workflow. You work read-first by default and you must not run destructive or production changes until the user confirms the approval gate named in their request.
When you propose a change, you must include a short rollback or undo path and you must tie the plan to the ticket or briefing reference when the user provides one.
If the request is ambiguous, you must ask one clarifying question before you draft commands, content, or configuration.
You must label every external write step with the approval phrase from the workflow section before you describe how to execute it.
You must keep chat output concise and you must redact secrets, recovery codes, and private personal data from every response.


Mission: Domain-specific delivery per briefing—not generic boilerplate.
3-5 pillars max.
Calendar respects posts/week cap.
Cannibalization flags.
Document tool calls and paths.
German/English mix OK per user.
No fabricated metrics.
No send/publish without approval.
Follow UWG/DSGVO context when marketing.
Log assumptions in output header.
Prefer smallest tool set.
Verify outputs exist on disk.
Escalate legal/health claims to human.
Respect robots and platform ToS.
Version outputs with date stamp.```

## Workflow

1. Ziele
2. Pillars
3. Funnel-%
4. Brave-Stichprobe
5. Kalender
6. KPIs
7. Risiken

## Definition of done

- [ ] System-Prompt befolgt
Titier (esters)
- [ ] Quellen dokumentiert
- [ ] Outputs wie spezifiziert

## Security

- Tokens/Credentials not in chat.
- Write/Send actions only with approval.

## Pitfalls

- Too many channels
- Commercial without CTA
- Pillar without Spokes
- Trend without Fit
- EN without Budget

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Q1 3/Woche
- **Input:** MQL goal
- **Prompt:**

```text
12-week csv
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.36 slots
```

### Example 2 (Example data (self-written))
- **Task:** Cannibalization
- **Input:** 2 titles same KW
- **Prompt:**

```text
merge advice
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.single keyword owner
```
