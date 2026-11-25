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
  - name: MCP filtering (platform-specific)
    install: "https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp"
    version_notes: "Hermes include/exclude; pair with OpenClaw policy and Cursor toggles."
inputs:
  - "Model context limit and active MCP list"
  - "Task profile: read-heavy, write, browser, or documents"
outputs:
  - "Token budget plan with MCP phases"
  - "Recommended deactivations and file-handoff rules"
risk_level: low
example_count: 2
version: "1.2.0"
updated: "2026-11-24"
---

## Purpose

Plan **context budget** before long agent sessions: phased MCP enablement, rolling summaries, file handoffs for large payloads, and CLI fallbacks when MCP snapshots would dominate the window. Pair with the MCP-focus template for exact config snippets.

## When to use

- Before multi-hour research or large-repo refactors with many integrations enabled.
- After "context full" or truncated-answer errors.
- Handoffs from a research subagent must return executive summaries, not raw dumps.

### When not to use

- Short single-file edits with MCP already disabled.
- You cannot change MCP settings mid-session on a locked enterprise machine.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| MCP include/exclude | Phase 1 reads | Hermes and similar filters |
| Skill progressive disclosure | Text budget | Load SKILL.md sections on demand |
| Local CLI | Cheap IO | `gh`, `rg`, tests instead of fat MCP reads |
| File artifacts | Handoff | Write megabyte JSON to disk, reference path |

## System prompt

```text
You are a context budget engineer for ai-ops/context-token-management.
You inventory each enabled MCP and classify schema weight as high, medium, or low based on documented tool count, not invented token numbers.
You produce a phased plan: phase A read-only MCPs only, phase B add write MCP after user names the action class, phase C disable browser MCPs when the task returns to code.
You recommend at most one interactive browser MCP among playwright, devtools, or browserbase-style servers for a given phase.
You reserve roughly thirty percent of the stated model context limit for the model's reply and tool call overhead when the user supplies a limit such as 200k.
You instruct rolling summaries every N turns for long threads and a decisions table stored in a repo file outside chat.
You prefer writing large tool outputs to files under artifacts/ and referencing paths instead of pasting megabyte JSON inline.
You delegate long research subagents to return an executive summary capped near fifteen hundred tokens unless the user expands the cap.
You suggest CLI equivalents when they match MCP read behavior with lower overhead (git log vs full GitHub MCP history).
You cross-link context-token-management-mcp-focus when the user needs exact deny or exclude snippets.
You end with a one-page budget plan the user can pin at the top of the session.
```

## Workflow

1. Record model limit, MCP list, and task profile from the user.
2. Classify each MCP schema weight high/medium/low.
3. Draft phased enablement (read first, write later).
4. Identify browser MCP triplets to collapse to one server.
5. Set file-handoff rules for large JSON or log payloads.
6. Define rolling summary interval for chats expected to exceed twenty turns.
7. Apply MCP-focus snippets if config changes are required.
8. Revisit plan after first phase completes and trim unused MCPs.

## Definition of done

- [ ] Written budget plan with phases and MCP lists
- [ ] Browser MCP count ≤1 per active phase unless justified
- [ ] Large output strategy uses file paths, not inline paste
- [ ] Summary cap stated for subagent handoffs

## Security

- Deferring write MCPs to phase B reduces accidental posts during research.
- File artifacts with secrets must live in gitignored paths the plan names.

## Pitfalls

- Enabling fifteen MCPs "just in case" before the first user question leaves no room for code.
- Pasting full MCP tool JSON into chat to debug duplicates the schema cost.
- Subagent returns fifty-page scrape inline and collapses the parent session.
- Rolling summaries omitted and the model forgets early constraints.
- Treating community token overhead anecdotes as exact measurements for your stack.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Large repo refactor plan with GitHub MCP.
- **Input:** 200k context model; github, playwright, firecrawl enabled; code-only phase first.
- **Prompt:**

```text
Budget plan: phase A code and github read only. Disable browser MCPs until phase B labeled #ui-check.
```

- **Expected result:**

```text
Phase A: github read tools + local rg/git; playwright and firecrawl off
Reserve: ~60k for reply/tools (30% of 200k stated rule)
artifacts/decisions.md for locked choices
Phase B trigger: user sends #ui-check
Plan pinned for session start
```

### Example 2 (Example data (self-written))

- **Task:** Subagent handoff discipline.
- **Input:** Research worker asked to return full API scrape.
- **Prompt:**

```text
Research subagent on api.example.com — parent needs summary only under 1500 tokens.
```

- **Expected result:**

```text
Full scrape written to artifacts/api-scrape.json (path only in parent chat)
Executive summary: 8 bullets, auth scheme, rate limits, breaking changes
Parent message under 1500 tokens
Pointer to file for line-level detail
```