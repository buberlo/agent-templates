---
id: codex-workflow
title: "Codex"
domain: agent-platforms
category: codex
tags:
  - codex
  - agent-platforms
  - skill
target_agents:
  - codex
  - generic-mcp-agents
required_tools:
  - name: OpenAI Codex CLI
    install: "https://developers.openai.com/codex/cli/"
    version_notes: "`codex`, `codex exec`, `codex mcp`, `/permissions`, AGENTS.md."
  - name: Hermes codex skill (optional)
    install: "https://github.com/NousResearch/hermes-agent"
    version_notes: "Delegation from Hermes when Codex is the coding runtime."
  - name: OpenClaw MCP bridge (optional)
    install: "https://docs.openclaw.ai/cli/mcp/serve"
    version_notes: "`openclaw mcp serve` exposes gateway tools to external MCP clients."
inputs:
  - "Feature briefing, branch name, and acceptance criteria"
  - "Parent orchestrator thread ID when Codex is delegated"
outputs:
  - "Unified diff and test log from the Codex session"
  - "Handoff summary for the parent agent (Hermes, OpenClaw, or human)"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-24"
---

## Purpose

Use **OpenAI Codex CLI** as a terminal coding runtime: explore repos, edit files, run local commands, attach MCP servers with `codex mcp`, and enforce boundaries with `/permissions` and `AGENTS.md` ([Codex CLI docs](https://developers.openai.com/codex/cli/)). Parent platforms such as Hermes or OpenClaw delegate implementation here while retaining review and release.

## When to use

- Hermes or a human supervisor needs an isolated coding loop with diff and test output returned upstream.
- You run `codex exec` in CI for repeatable non-interactive tasks with pinned permissions.
- OpenClaw exposes gateway tools via `openclaw mcp serve` and Codex acts as the MCP client.

### When not to use

- Two agents write the same branch concurrently without a lock.
- You expect Office validate-and-render without handing that back to document skills on the parent.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| `codex` interactive | Implementation | Local repo, model and permissions picker |
| `codex exec` | Automation | Scriptable runs with defined prompts |
| `codex mcp` | Integrations | Add local or remote MCP servers |
| `AGENTS.md` | Project policy | `/init` seeds instructions for the repo |
| Parent orchestrator | Review | Hermes/OpenClaw thread holds approval |

## System prompt

```text
You run as OpenAI Codex in the delegated repository scope defined by the parent briefing or AGENTS.md.
You implement only the files and behaviors named in the charter; you refuse drive-by refactors outside the stated paths.
You use `codex mcp` to list enabled servers before the session and keep MCP count minimal to preserve context for code.
You run the project's test or build command after edits when AGENTS.md or the parent requires it and attach exit codes to the handoff.
You never `git push`, open pull requests, or call deploy MCP tools unless the parent thread records explicit PUSH_APPROVED.
You return a unified diff, test summary, and list of commands executed to the parent orchestrator before the session ends.
You serialize writes: one active Codex job per branch; you abort if another agent reports a conflicting lock on the same branch.
You store API keys in the environment or MCP config the platform provides, not in the delegation prompt or argv.
When bridged through OpenClaw MCP you respect gateway tool policy and do not bypass blocked write tools.
Document generation with layout requirements is escalated to the parent's document skills rather than improvised in Codex alone.
You label the handoff message with branch name, commit range (if any), and risk flags (schema migrations, auth changes).
```

## Workflow

1. Parent defines scope, branch, acceptance criteria, and approval tokens in the orchestrator thread.
2. Confirm single-writer lock on the branch; queue other jobs if contested.
3. Launch `codex` or `codex exec` in the repo; run `/permissions` or flags appropriate to risk.
4. Optional: configure `codex mcp` for GitHub read or other needed servers only.
5. Implement; run tests; capture diff and logs.
6. Post handoff payload (diff, tests, commands) to parent; do not push.
7. Parent reviews; user issues PUSH_APPROVED if satisfied.
8. Optional second Codex round only after review comments land.

## Definition of done

- [ ] One writer per branch during the Codex run
- [ ] Diff and test status documented in the parent thread
- [ ] No push or merge without documented parent approval
- [ ] MCP and permission settings match the briefing risk level

## Security

- Tighten `/permissions` for untrusted repos; widen only for known-safe sandboxes.
- OpenClaw bridge inherits gateway tool policy—verify writes stay blocked until release.
- Do not pass production database URLs in prompts; use read-only MCP where possible.

## Pitfalls

- Parallel Hermes agent and Codex editing `main` causes merge conflicts and lost work.
- Parent never reads the handoff diff and merges blind—always require review.
- Full MCP stack on both parent and child doubles schema overhead with little benefit.
- Confusing `openclaw mcp serve` with `openclaw acp` gives the client the wrong tool surface.
- Skipping tests because Codex "looks right" fails CI on the parent pipeline.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Hermes delegates a health endpoint.
- **Input:** "Add GET /health to Express in `src/routes/`"; branch `feat/health`.
- **Prompt:**

```text
(Hermes) Invoke codex skill scoped to src/routes/*. Implement GET /health, run npm test, no git push.
```

- **Expected result:**

```text
Diff: +14 lines in src/routes/health.js (or .ts)
npm test: 14 passed, 0 failed
Handoff to Hermes: diff attached, PUSH_APPROVED not set
Parent message: ready for human review on feat/health
```

### Example 2 (Example data (self-written))

- **Task:** Reject parallel writers.
- **Input:** Codex refactoring auth while Hermes updates README on `main`.
- **Prompt:**

```text
Speed up: Codex refactor auth and Hermes edit README on main at the same time.
```

- **Expected result:**

```text
Conflict detected or lock failure on main
Response: serialize jobs—one branch, one active writer
No force-push suggested
Queue second task after first completes or use separate branches
```