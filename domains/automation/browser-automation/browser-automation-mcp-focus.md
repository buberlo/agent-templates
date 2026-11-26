---
id: browser-automation-mcp-focus
title: "Browser automation: MCP tool selection"
domain: automation
category: browser-automation
tags:
  - browser
  - automation
  - mcp
  - playwright
target_agents:
  - hermes
  - cursor
  - claude-code
  - openclaw
  - generic-mcp-agents
required_tools:
  - name: Playwright MCP
    install: "https://github.com/microsoft/playwright-mcp"
    version_notes: "Introduction: https://playwright.dev/mcp/introduction — accessibility snapshots cost context tokens."
  - name: Chrome DevTools MCP
    install: "https://github.com/ChromeDevTools/chrome-devtools-mcp"
    version_notes: "Attach only after a failed interaction step."
  - name: Browserbase MCP
    install: "https://github.com/browserbase/mcp-server-browserbase"
    version_notes: "Optional remote browser when local Chrome is unavailable."
inputs:
  - "Task class: read-only | interact | debug"
  - "Client active MCP list and include/exclude settings"
  - "Target host: localhost, staging, or public third-party"
outputs:
  - "Chosen primary browser tool and disabled tools with reasons"
  - "Client-specific MCP include list for the session"
  - "Handoff template ID when task is scraping or CI testing"
risk_level: low
example_count: 2
version: "1.2.0"
updated: "2026-11-26"
---

## Purpose

Pick the smallest browser automation surface before the first navigation so MCP clients do not load redundant accessibility trees and token-heavy tools.

## When to use

- The agent session starts with many MCP servers enabled and the user wants a browser task.
- A prior run failed and you need to decide whether to add Chrome DevTools MCP or switch to Playwright CLI.
- OpenClaw or Hermes needs an explicit include list before enabling browser skills.

### When not to use

- The user already pinned Playwright CLI with a repo and wants only `npx playwright test`.
- The goal is bulk public-page extraction without login — use `data-analytics/web-scraping/web-playwright-research-scrape` instead.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| [Playwright MCP](https://github.com/microsoft/playwright-mcp) | Interactive UI control | Documented at [playwright.dev/mcp/introduction](https://playwright.dev/mcp/introduction) |
| [Chrome DevTools MCP](https://github.com/ChromeDevTools/chrome-devtools-mcp) | Network and console diagnosis | Short-lived debug adjunct |
| [Browserbase MCP](https://github.com/browserbase/mcp-server-browserbase) | Hosted browser | When local install is blocked |
| Playwright CLI | Repeatable scripts | [playwright.dev/docs/intro](https://playwright.dev/docs/intro); often lower token cost than MCP snapshots |

## System prompt

```text
You are a browser automation tooling advisor for automation/browser-automation-mcp-focus.
Your job is completed before any page loads: you classify the task, pick one primary control plane, and name tools to disable for the rest of the session.
When the user only needs article text from a public page, recommend search or scrape templates and keep Playwright MCP off unless DOM interaction is required.
When the user tests their own app with clicks and form fills, choose Playwright MCP for exploratory steps or Playwright CLI when they already maintain a test repo.
If a step failed, you may recommend Chrome DevTools MCP temporarily, then remove it after the root cause is identified so console and HAR data do not flood context.
You warn when more than two browser-related MCP servers stay enabled, citing that large accessibility snapshots can dominate prompt budget per community guidance at https://www.reddit.com/r/mcp/comments/1spvkrz/microsoft_recommends_cli_over_mcp_for_playwright/.
For Hermes and OpenClaw, you output an explicit include/exclude list instead of assuming all catalog browser tools are active.
You never recommend Browserbase for pure localhost work unless the user cannot run local Chromium.
You document handoffs: table scraping to web-playwright-research-scrape, CI pipelines to software-development/testing-workflow.
You end with a one-line table: task class, chosen tool, rejected tools, and reason.
You refuse to store OAuth tokens or session cookies in skill text; session state belongs in env or storageState paths outside git.
```

## Workflow

1. Ask whether the task is read-only, interactive UI, or post-failure debug.
2. List the client’s active MCP servers; mark browser-related entries.
3. If read-only public content, branch to scrape or search templates unless login or shadow DOM forces Playwright.
4. If interact on owned app, pick Playwright MCP or CLI; disable parallel browser MCPs.
5. If debug, add Chrome DevTools MCP with a stated removal step after diagnosis.
6. Emit include/exclude guidance for Hermes, Cursor, Claude Code, or OpenClaw configs.
7. Point to `browser-automation-workflow` for the first concrete navigation step when interact was chosen.

## Definition of done

- [ ] At most two browser MCP servers recommended simultaneously
- [ ] Read-only tasks do not default to full accessibility snapshots without warning
- [ ] Handoff template IDs named when task is scraping or CI
- [ ] DevTools MCP has an explicit detach step when used

## Security

- Shared MCP OAuth sessions must not be copied into prompts or committed skill files.
- Remote browser vendors receive page content; confirm data residency before Browserbase.
- Third-party sites get read-only routing unless the user supplies legal test accounts.

## Pitfalls

- Enabling Playwright MCP, Browserbase, and DevTools together leaves little room for task instructions.
- Leaving DevTools attached inflates every later turn with network logs.
- OpenClaw ClawHub skills without `skills verify` may be stale or unrelated to Playwright MCP.
- Choosing MCP for a one-line text fetch triggers unnecessary snapshot cost.
- Forgetting to disable browser tools after the session slows unrelated coding tasks.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Route staging checkout clicks for Cursor with Hermes also enabled.
- **Input:** Task class `interact`, staging `https://staging.example.com/checkout`, Playwright MCP and Firecrawl both on.
- **Prompt:**

```text
Before navigation: which browser tools stay enabled for a staging checkout flow?
```

- **Expected result:** Primary tool is Playwright MCP with Firecrawl disabled for this session. Include list names `playwright` only among browser tools. Next step references `browser-automation-workflow` with navigate to staging checkout URL. Warn that accessibility snapshots should be limited to checkout steps, not entire catalog pages.

### Example 2 (Example data (self-written))

- **Task:** Summarize a public blog post without login.
- **Input:** Task class `read-only`, URL `https://blog.example.com/posts/release-notes`.
- **Prompt:**

```text
User wants a summary of a public blog post. Should Playwright MCP be enabled?
```

- **Expected result:** Recommendation rejects Playwright MCP for this session and points to `data-analytics/web-scraping/web-playwright-research-scrape` or search MCP. Handoff row lists rejected tools (Playwright MCP, Browserbase) with reason “no DOM interaction required.” Cites [playwright.dev/mcp/introduction](https://playwright.dev/mcp/introduction) only as contrast, not as the chosen path.