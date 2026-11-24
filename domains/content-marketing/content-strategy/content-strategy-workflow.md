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
Role: Content strategist.
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
Version outputs with date stamp.
```

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
36 slots
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
single keyword owner
```
