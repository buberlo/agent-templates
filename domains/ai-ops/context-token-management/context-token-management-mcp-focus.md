---
id: context-token-management-mcp-focus
title: "Context and token management: MCP/skill focus"
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
  - name: Hermes MCP user guide
    install: "https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp"
    version_notes: "include/exclude filters for optional MCPs."
  - name: OpenClaw MCP tools
    install: "https://docs.openclaw.ai/tools/mcp"
    version_notes: "Tool policy deny/allow per MCP tool."
  - name: Cursor MCP
    install: "https://cursor.com/docs/context/mcp"
    version_notes: "Toggle servers in Customize; Enterprise tool allowlists."
inputs:
  - "Client name (Hermes, OpenClaw, Cursor, Claude Code)"
  - "Current MCP inventory and task profile"
outputs:
  - "Exact include/exclude or policy snippets for the client"
  - "List of MCPs disabled for this session and why"
risk_level: low
example_count: 2
version: "1.2.0"
updated: "2026-11-24"
---

## Purpose

Produce **concrete MCP configuration trims** before a heavy session: Hermes include/exclude lists, OpenClaw tool policy denies, Cursor server toggles—so tool schemas do not consume the context window before user content ([Hermes MCP](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp), [Cursor MCP](https://cursor.com/docs/context/mcp)).

## When to use

- A new agent machine imports a large MCP catalogue defaults-on.
- Training: "Why is my context full before I ask the real question?"
- You prepare a focused run (e.g., SQL only) and must disable browser MCP triplets.

### When not to use

- The task genuinely needs many connectors and stakeholders accept a shorter answer budget.
- You have not listed which MCPs are currently enabled.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| Hermes include/exclude | Filter | Session-scoped MCP subsets |
| OpenClaw tool policy | Deny/allow | Block Playwright until tagged task |
| Cursor Customize toggles | Off switch | Disable unused integrations per run |
| `claude mcp list` | Audit | Claude Code footprint |

## System prompt

```text
You are an MCP configuration specialist for ai-ops/context-token-management-mcp-focus.
You ask which agent client is in use and you list every enabled MCP server before recommending changes.
You output copy-paste-ready snippets: Hermes include/exclude YAML comments, OpenClaw policy denies, or instructions to toggle Cursor servers off in Customize.
You recommend keeping at most one browser automation MCP and one read-only web search MCP for mixed tasks unless the user documents an exception.
You never advise pasting an entire MCP catalog JSON into a custom system prompt field.
You suggest measuring tool count on the first turn when the product exposes a tool inventory metric.
You tell the user when a client requires restart or reconnect after config change and you suggest saving a backup path for the previous include file.
You cross-reference context-token-management-workflow for phased enablement when the user has not started the task yet.
You label disabled servers with the task keyword that would re-enable them (for example #browser-task).
You finish with estimated high/medium/low schema weight per remaining MCP based on tool count, not unsupported token figures.
```

## Workflow

1. Capture client type, MCP list, and today's task profile (read, write, browser).
2. Mark MCPs unused for this profile for disable or exclude.
3. Draft client-specific snippet (Hermes exclude block, OpenClaw deny rules, or Cursor toggle list).
4. Consolidate duplicate browser or GitHub MCPs into one server.
5. Save backup of prior config path the user names.
6. Apply snippet; restart client if required.
7. Run a one-line user message smoke test and note tool count if visible.
8. Hand off to workflow template if phased enablement is still needed.

## Definition of done

- [ ] Snippet matches the stated client and is redacted of secrets
- [ ] Disabled MCPs listed with re-enable condition
- [ ] Backup path or rollback step documented
- [ ] No full catalog pasted into system prompt advice

## Security

- Disabling write MCPs via policy is preferred over trusting the model to refuse writes.
- Deny rules should not remove audit logging MCPs the security team requires.

## Pitfalls

- Excluding MCP in Hermes but leaving skills that call those tools causes confusing errors.
- OpenClaw deny on wrong tool name silently fails open—verify names in `openclaw mcp list`.
- Cursor Cloud Agents ignore local `~/.cursor/mcp.json`—trim team dashboard MCP instead.
- Re-enabling all servers after one task forgets the lesson—document per-task profiles.
- Estimating tokens from tool count alone is approximate; avoid presenting fake precision.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Hermes SQL session without browser MCP.
- **Input:** motherduck and github enabled; playwright enabled; task is DuckDB report only.
- **Prompt:**

```text
Hermes client. Trim MCP for SQL-only task. Provide include/exclude snippet.
```

- **Expected result:**

```text
exclude: playwright, browserbase (comment: enable with #browser-task)
include: motherduck, github-readonly subset
Backup: ~/.hermes/mcp-include.yaml.bak suggested
Smoke: user sends "list tables" — tool count drops in UI if shown
```

### Example 2 (Example data (self-written))

- **Task:** OpenClaw deny until browser tag.
- **Input:** Playwright MCP enabled; user message lacks browser scope.
- **Prompt:**

```text
OpenClaw: block playwright tools unless user message contains #browser-task.
```

- **Expected result:**

```text
tool.policy entry: deny playwright_* default
allow exception documented when message includes #browser-task
Test: linear read skill runs; playwright navigate blocked with log line
Rollback: prior policy file path noted
```