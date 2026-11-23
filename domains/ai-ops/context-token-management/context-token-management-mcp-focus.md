---
id: context-token-management-mcp-focus
title: "Context and Token Management: MCP/Skill Focus"
domain: ai-ops
category: context-token-management
tags:
  - context
  - ai-ops
  - mcp
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Hermes MCP settings
    install: "https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp"
    version_notes: "include/exclude"
inputs:
  - "Client (Hermes/OpenClaw/Cursor) and MCP count"
outputs:
  - "Konkrete include/exclude Konfiguration"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---
## Purpose

**Optimize MCP configuration for token costs**: include/exclude, tool policy, skills — before loading the first tool.

## When to use

- Setup of new agent machine with large MCP catalogue.
- Training: "Why is my context full?"

## Tool stack

| Tool | Role | Rationale |
|---------------------------------------------------------------------------------------------------------------------
| Hermes include/exclude | Filter | Official documentary |
| OpenClaw tool policy | Deny/allow | Skills separately |

## System prompt

```text
Role: MCP config specialist (ki-ops/context-token-management-mcp-focus).
Mission: Output exact config snippets for user's client—default deny heavy catalog entries.

Hermes pattern: include only task mcps in session yaml; exclude default bundle playwright if not needed.
Example include list comment: motherduck, github-readonly not github-write until approved.
OpenClaw: tool.policy deny playwright devtools until user tag #browser-task in message.
Cursor: dynamic servers list—toggle off unused integrations in settings before agent run.
Measure: recommend user count tools in first turn if product exposes tool count metric.
Skills catalog: install one skill not entire category from clawhub leaderboard.
Cross reference context-token-management-workflow for phased enablement plan.
Grok plugins oauth backend—trim X large tool namespaces if task unrelated social.
Never advise embedding full mcp catalog json in system prompt custom field.
Document restart requirement if client needs restart after config change.
Provide rollback: save previous include file copy path suggested.
```## Workflow

1. Client and estimated MCP number.
2. Prioritize task classes for next week.
3. include/exclude or write tool.policy snippet.
4. Name heavy servers identically as in catalog.
5. Test session with “list tools” if possible.
6. Refer to `context-token-management-workflow` for running sessions.

## Definition of done

- [ ] Copy-paste-capable Config
- [ ] Rollback note
-[ ] Heavy MCPs by default

## Security

- Config files no API keys.

## Pitfalls

- `include` without `exclude` → Rest still loaded depending on the client.
- Config not reloaded User thinks it works; Session restart is required.
Leave Playwright/browser MCPs active, although only reading was necessary — 5k vs 114k tokens per snapshot in community comparisons.
- Hermes/OpenClaw Tool-Policy and Skill-Ceiling are set independently of each other – check both.

## Basic examples

Example 1 (Example data)

- **Task:** Hermes data session
- **Input:** DuckDB report
- **Prompt:**

```text
mcp include exclude snippet.
```

- **Expected result:**

```text
include motherduck filesystem | exclude playwright firecrawl x
```

### Example 2 (Example data)

- **Task:** Alles an
- **Input:** power user 25 mcps
- **Prompt:**

```text
Keep all enabled for flexibility.
```

- **Expected result:**

```text
warn overhead | propose profile sets dev browser data
```

### Example 2 (Example data)

- **Task:** Second dry run
- **Input:** Example data only
- **Prompt:**
```text
Repeat workflow; no external writes.
```
- **Expected result:** Checklist only.
