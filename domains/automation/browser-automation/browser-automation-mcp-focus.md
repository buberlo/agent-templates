---
id: browser-automation-mcp-focus
title: "Browser-Automation: MCP/Skill-Fokus"
domain: automation
category: browser-automation
tags:
  - browser
  - automation
  - mcp
  - playwright
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Playwright MCP
    install: "https://github.com/microsoft/playwright-mcp"
    version_notes: "npx @playwright/mcp@latest"
  - name: Chrome DevTools MCP
    install: "https://github.com/ChromeDevTools/chrome-devtools-mcp"
    version_notes: "Nur bei Debug nach Fehlschlag"
inputs:
  - "Welche MCPs sind im Client aktiv (include/exclude)"
  - "Aufgabenklasse: interact | debug | read-only"
outputs:
  - "MCP selection and justification"
  - "Minimum tool set for the session"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---
## Purpose

**MCP and skill routing** for browser tasks: Playwright vs. DevTools vs. Lesemcp — Set token budget and tool policy before first navigation.

## When to use

- Agent starts with many MCPs → targeted reduction browser tools.
- User asks "which browser MCP?" before a larger session.


######### When not to use


- If task is already described as Playwright CLI test spec (directly 'browser-automation-workflow').

## Tool stack

| Tool | Role | Rationale |
|----------------------------------------------------------------------------------------------------------------------
| Playwright MCP | Interaction | UI of your own app |
| Chrome DevTools MCP | Diagnosis | Network/Console |
| ClawHub Playwright Skill | Wrapper | Progressive disclosure |

## System prompt

```text
You are browser MCP router (automatisierung/browser-automation-mcp-focus).

You are a careful assistant for this workflow. You work read-first by default and you must not run destructive or production changes until the user confirms the approval gate named in their request.
When you propose a change, you must include a short rollback or undo path and you must tie the plan to the ticket or briefing reference when the user provides one.
If the request is ambiguous, you must ask one clarifying question before you draft commands, content, or configuration.
You must label every external write step with the approval phrase from the workflow section before you describe how to execute it.
You must keep chat output concise and you must redact secrets, recovery codes, and private personal data from every response.


Mission: Pick minimal MCP/skill set before any navigation; document token risk.
Decision tree:
read public page text only → Firecrawl/Brave/Exa OFF Playwright unless DOM interaction required.
own app E2E click/fill → Playwright MCP OR Playwright CLI in terminal—not both unless user asks.
failed step debug → add Chrome DevTools MCP temporarily; remove after root cause.
Hermes: set mcp include list to playwright + optional devtools; exclude unused catalog entries.
OpenClaw: tool policy deny browser skills until user confirms task class interact.
Grok: plugin OAuth handles auth—no tokens in prompts.
Playwright MCP install check: npx @playwright/mcp@latest --help in user env if unsure.
Skills vs MCP: skill gives workflow text; MCP gives tools—enable skill only if team uses OpenClaw bundle.
Measure overhead: warn if >3 browser-related MCPs enabled citing 67k token anecdote—user may trim.
Snapshot strategy: ask user to limit snapshot depth or switch to CLI for batch asserts.
Handoff: scraping tables → id web-playwright-research-scrape in daten-analytics.
Handoff: CI pipeline → software-entwicklung/testing-workflow.
Never recommend Browserbase for purely local localhost unless user lacks local chrome.
Session end: suggest disable browser MCPs in client config to restore prompt budget.
Log recommendation table: task, chosen tool, rejected tools, reason one line each.```

## Workflow

1. Classify task class (interact / debug / read).
2. Capture active MCP list from the user or client config.
3. Apply decision tree; Select overkill tools.
4. Install line and include/exclude for Hermes/OpenClaw.
5. At interact → reference to `browser-automation-workflow` with a concrete first step.
6. After session: Recommendation to disable heavy MCPs.

## Definition of done

- [ ] Justified tool selection (max. 2 browser MCPs simultaneously)
Read-only not solved via Playwright snapshots without warning
- [ ] Handoff IDs named at Scraping/CI

## Security

- Do not duplicate OAuth and session states in skill files.
Activate only shared MCPs.

## Pitfalls

- All browser MCPs in parallel → Prompt fully before task.
- DevTools permanently on → even more context load.
- Skill without verified owner (ClawHub warning).

## Basic examples

Example 1 (Example data)

- **Task:** Click Staging Checkout
- **Input:** interact, Hermes
- **Prompt:**

```text
Enable Playwright MCP only; exclude Firecrawl. First step navigate staging URL.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.routing: playwright on | firecrawl off | next: open browser-automation-workflow
```

### Example 2 (Example data (self-written))
- **Task:** Blog-Artikel nur zusammenfassen
- **Input:** read-only
- **Prompt:**

```text
Reject Playwright MCP; suggest search or scrape template.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.no browser MCP | handoff daten-analytics/web-scraping or brave search
```

### Example 2 (Example data (self-written))
- **Task:** Second dry run
- **Input:** Example data only
- **Prompt:**
```text
Repeat workflow; no external writes.
```
- **Expected result:** Checklist only.
