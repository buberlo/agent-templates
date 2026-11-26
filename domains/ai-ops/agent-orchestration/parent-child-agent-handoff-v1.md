---
id: parent-child-agent-handoff-v1
title: "Parent-child agent handoff contract"
domain: ai-ops
category: agent-orchestration
tags:
  - orchestration
  - handoff
  - subagents
  - mcp
target_agents:
  - hermes
  - cursor
  - claude-code
  - codex
  - generic-mcp-agents
required_tools:
  - name: MCP specification
    install: "https://modelcontextprotocol.io"
    version_notes: "Tool boundaries between parent and child contexts."
  - name: Cursor Agent hooks (optional)
    install: "https://cursor.com/docs/agent/hooks"
    version_notes: "subagentStart governance when parent is Cursor."
inputs:
  - "Parent platform (Hermes, Cursor, Claude Code) and child delegate (Codex, explore subagent)"
  - "Artifact definition: PR, doc, triage table, etc."
  - "MCP and credential boundaries (which side may call which server)"
outputs:
  - "Handoff markdown contract: scope, forbidden actions, return payload schema"
  - "Example filled contract for one fictional feature task"
risk_level: medium
example_count: 2
version: "1.0.0"
updated: "2026-11-26"
---

## Purpose

Define a **parent-child agent handoff contract** so orchestrators (Hermes, Cursor Agent, Claude Code) delegate work to Codex or subagents with explicit **scope, MCP limits, approval tokens, and return schema** ([MCP specification](https://modelcontextprotocol.io), [Cursor subagent hooks](https://cursor.com/docs/agent/hooks)).

## When to use

- Hermes delegates coding to Codex while retaining merge approval.
- Cursor parent spawns explore or generalPurpose subagents for research then implements itself.
- Multiple MCP servers are enabled but only the parent may call write tools.

### When not to use

- Single-agent sessions with no delegation and no shared MCP credentials.
- Fully autonomous loops without human approval on any write—use stricter platform guardrails first.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| Handoff contract doc | Interface | Markdown or YAML in repo |
| Parent MCP allowlist | Control | Child lacks write connectors |
| Child runtime | Execution | Codex, subagent, or cloud worker |
| Hooks / permissions | Enforcement | subagentStart, PreToolUse optional |

## System prompt

```text
You author parent-child agent handoff contracts for ai-ops/agent-orchestration without executing undelegated production changes yourself.
You specify parent role: briefing, approval gates, MCP write access, and final user communication.
You specify child role: bounded filesystem paths, allowed commands, read-only MCP set, and required return payload fields.
You define SEND_APPROVED or equivalent tokens for each write class: git push, ticket update, email send, deploy, payment.
You map credentials so child processes never receive parent OAuth refresh tokens unless platform design requires it and the user accepts risk.
You include rollback instructions and maximum runtime or token budget for the child.
You align with MCP least privilege: child tool list is a subset of parent list unless child runs on isolated credentials.
You document observability: parent logs child session id, branch name, and diff summary paths.
You use plain English sections: Objective, Inputs, Forbidden, Outputs, Approvals, Done criteria.
You provide one filled example for a fictional repository task and one minimal template the user can copy.
You cite modelcontextprotocol.io for tool semantics and cursor.com/docs/agent/hooks when Cursor subagents are the child.
```

## Workflow

1. Identify parent and child platforms for the task; list MCP servers each side needs.
2. Draft contract sections: objective, repo paths, tests to run, forbidden paths (prod configs).
3. Assign MCP: parent keeps GitHub write; child gets read-only GitHub or none.
4. Define child return schema (diff stat, test log excerpt, open questions list).
5. Add approval table mapping actions to tokens and human owners.
6. Optionally wire Cursor subagentStart hook to deny child types that violate contract.
7. Parent runs child; validates return payload against schema before continuing.
8. Archive contract in `docs/agent-handoffs/` or ticket for audit.

## Definition of done

- [ ] Contract lists parent, child, MCP split, and return schema
- [ ] Approval tokens defined for every child write class
- [ ] Example contract filled for one fictional task
- [ ] Parent verification steps documented before merge or send

## Security

- Child agents must not inherit parent's payment or production MCP tools by default.
- Contracts stored in git should not embed secrets—reference vault names only.
- Subagents with shell type can bypass narrow MCP limits—deny shell when child should be read-only.

## Pitfalls

- Vague "implement feature" objectives cause child scope creep into unrelated dirs.
- Returning only chat prose without test logs forces parent to re-run everything.
- Parallel subagents without merge plan create conflicting branches.
- Hermes and Cursor delegation models differ—copy contracts per platform, not one-size-fits-all.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Hermes parent delegates bugfix to Codex child on fictional repo `acme/widget`.
- **Input:** Child may edit `src/widget/**`; must run `npm test`; no git push.
- **Prompt:**

```text
Write handoff contract markdown for Hermes→Codex. Include return schema.
```

- **Expected result:**

```text
Objective: fix null pointer in widget formatter issue #42.
Child inputs: branch fix/42, paths src/widget/** only.
Forbidden: .env, deploy/**, git push, GitHub issue close.
Child MCP: none; local shell only npm test.
Return schema: {diff_stat, test_exit_code, summary, open_questions[]}.
Approvals: parent reviews diff; PUSH_APPROVED required for push by parent or human.
Parent logs hermes session id and codex run id in ticket comment.
```

### Example 2 (Example data (self-written))

- **Task:** Cursor parent uses explore subagent then implements; hook denies shell child.
- **Input:** Research auth flow; child type explore only; contract stored in PR description.
- **Prompt:**

```text
Handoff contract for Cursor parent + explore child. Reference subagentStart hook denial for shell.
```

- **Expected result:**

```text
Child explore task: list files defining JWT validation under src/auth; no edits.
Return schema: {files[], call_graph_notes, risks[]}.
Parent implements after review; subagentStart denies shell subagent_type on main branch per hook policy.
MCP: neither side calls production database MCP.
Done when parent PR includes tests and explore notes linked in description.
```