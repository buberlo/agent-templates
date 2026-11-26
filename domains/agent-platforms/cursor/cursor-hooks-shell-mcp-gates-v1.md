---
id: cursor-hooks-shell-mcp-gates-v1
title: "Cursor Agent hooks: shell and MCP gates"
domain: agent-platforms
category: cursor
tags:
  - cursor
  - hooks
  - security
  - cloud-agents
target_agents:
  - cursor
  - generic-mcp-agents
required_tools:
  - name: Cursor Agent hooks
    install: "https://cursor.com/docs/agent/hooks"
    version_notes: "Project `.cursor/hooks.json`, JSON stdio handlers, cloud agent subset."
  - name: Cursor MCP
    install: "https://cursor.com/docs/context/mcp"
    version_notes: "beforeMCPExecution / afterMCPExecution on local IDE; limited on cloud."
inputs:
  - "Repository with `.cursor/hooks.json` scaffold or permission policy table"
  - "List of blocked shell patterns and MCP tool prefixes (e.g. payments, deploy)"
  - "Whether runs target Cloud Agents, IDE Agent, or both"
outputs:
  - "Versioned hook scripts plus documented deny/allow matrix"
  - "Sample hook JSON output proving a risky command is blocked"
risk_level: medium
example_count: 2
version: "1.0.0"
updated: "2026-11-26"
---

## Purpose

Configure **Cursor Agent hooks** to observe and block risky **shell** and **MCP** tool calls before they run. Hooks are JSON-speaking scripts referenced from `.cursor/hooks.json` ([Cursor hooks docs](https://cursor.com/docs/agent/hooks)). Cloud Agents load **project** hooks from the repository root, not `~/.cursor/hooks.json`.

See also: `domains/agent-platforms/cursor/assets/example-hooks-gate-flow.svg` (example data).

## When to use

- A team wants deny-by-default rules for `DROP DATABASE`, `rm -rf`, production deploy CLIs, or payment MCP tools.
- Enterprise Cloud Agents need the same hook policy as local IDE agents via committed `.cursor/hooks.json`.
- You need audit logs after shell or MCP execution (`afterShellExecution`, `afterMCPExecution` on supported surfaces).

### When not to use

- You expect **prompt-based** hooks to run on Cloud Agents (command hooks only on cloud).
- You rely on **user-level** `~/.cursor/hooks.json` for Cloud Agent policy (not loaded on cloud VMs).

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| `.cursor/hooks.json` | Policy config | Declares matchers and hook commands per event |
| Shell hook scripts | Enforcement | Exit `0` with JSON `permission: deny` to block |
| Git | Version control | Hooks and scripts ship with the repo |
| Cursor MCP docs | MCP hook limits | Cloud HTTP MCP uses `preToolUse` with redacted post output |

## System prompt

```text
You are configuring Cursor Agent hooks for agent-platforms/cursor, not executing unrestricted production changes yourself.
You read https://cursor.com/docs/agent/hooks and implement command-based hooks in .cursor/hooks.json at the repository root so Cloud Agents inherit the same policy as local Agent Chat where supported.
You prioritize beforeShellExecution and subagentStart gates first, then beforeMCPExecution where the runtime supports it, and document which hook events are unavailable on Cloud Agents per the official support table.
You write hook handlers that read JSON from stdin, respond on stdout with valid JSON, and use exit code 0 even when denying an action so the agent receives a structured permission block.
You block destructive shell prefixes the user listed (rm -rf, DROP, kubectl delete, stripe charges) and require allow patterns for routine dev commands such as npm test or pytest when the user wants a tight default.
You log denied attempts with command text redacted when it may contain secrets, and never print environment variables from hook child processes.
You test hooks locally in Agent Chat with a harmless command before asking the user to merge hook changes that could block CI Cloud Agents.
You document matcher fields for preToolUse when denying MCP:<tool_name> patterns on cloud HTTP MCP servers, noting that updated_input and full MCP output are not returned on cloud in some cases.
You remind the user that Tab hooks and workspaceOpen are IDE-only and must not be the only control for cloud safety.
You deliver a deny/allow matrix table, file paths for each hook script, and reproduction steps showing one blocked and one allowed invocation.
```

## Workflow

1. Inventory risky commands and MCP tools from incident history or platform docs; draft a deny/allow matrix with owners.
2. Add `.cursor/hooks.json` at the repo root with `beforeShellExecution` (and optional `preToolUse` / `subagentStart`) command entries.
3. Implement small idempotent shell scripts (e.g. `scripts/cursor-hooks/before-shell.sh`) that parse stdin JSON and emit `{"permission":"deny","user_message":"..."}` on matches.
4. Run Agent Chat locally: trigger a blocked pattern and confirm the agent surfaces the hook `user_message`.
5. Commit hooks and scripts; open a Cloud Agent test task that only edits files in-repo to confirm project hooks load.
6. Document cloud vs IDE differences (`beforeMCPExecution` deferred on cloud per docs; use `preToolUse` for MCP on cloud).
7. Add a short RUNBOOK section in the PR describing how to update matchers when new MCP servers are enabled.

## Definition of done

- [ ] `.cursor/hooks.json` and hook scripts are committed and referenced in the PR
- [ ] At least one blocked and one allowed shell path demonstrated with captured hook JSON
- [ ] Cloud vs local hook availability documented for this repo's run mode
- [ ] No secrets or tokens embedded in hook scripts or logs

## Security

- Hook scripts run with the agent's privileges; keep them minimal and auditable.
- Deny rules should default for destructive SQL, secret exfiltration paths (`~/.ssh`, cloud cred files), and unapproved deploy targets.
- Review third-party hook snippets like third-party Claude Code hook imports before enabling.

## Pitfalls

- Invalid JSON from a permission hook with exit `0` blocks the action on Cursor; test schemas against the docs table.
- Over-broad matchers (`*`) break legitimate `git` or `docker` workflows and frustrate developers.
- Assuming `sessionStart` runs on Cloud Agents causes missing context injection; use `beforeSubmitPrompt` or repo rules instead.
- HTTP MCP on cloud ignores some `preToolUse` mutation fields; blocking still works, rewriting inputs may not.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Block `rm -rf /` and allow `npm test` in a Node monorepo.
- **Input:** Deny regex list: `\brm\s+-rf\b`, `\bkubectl\s+delete\b`. Allow: `^npm test$`, `^pnpm test$`.
- **Prompt:**

```text
Add .cursor/hooks.json with beforeShellExecution calling scripts/cursor-hooks/before-shell.sh. Implement the deny/allow table above. Show one test deny output.
```

- **Expected result:**

```text
Created .cursor/hooks.json with matcher "*" → before-shell.sh.
Test: agent proposes `rm -rf ./tmp`; hook returns permission deny with user_message "Blocked: recursive force delete".
Test: `npm test` returns permission allow; command runs and afterShellExecution logs exit 0.
Cloud note: project hooks path confirmed in PR description per cursor.com/docs/agent/hooks.
```

### Example 2 (Example data (self-written))

- **Task:** Gate MCP tools that start with payment namespaces on cloud.
- **Input:** Deny `MCP:stripe_*` and `MCP:create_payment` via preToolUse matcher.
- **Prompt:**

```text
Add preToolUse hook scripts/cursor-hooks/deny-payments.sh for Cloud Agent runs. Document cloud HTTP MCP redaction limits.
```

- **Expected result:**

```text
hooks.json preToolUse entry with matcher tool_name prefix stripe.
Simulated stdin: tool_name Mcp:create_payment_intent → JSON deny, user_message asks human to use dashboard.
Docs cited: cloud postToolUse receives {"redacted":true} for HTTP MCP; blocking happens in preToolUse only.
No payment MCP calls executed during the test run.
```