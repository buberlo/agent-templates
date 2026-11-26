---
id: cursor-subagent-governance-hooks-v1
title: "Cursor subagent governance with hooks"
domain: agent-platforms
category: cursor
tags:
  - cursor
  - subagents
  - task-tool
  - hooks
target_agents:
  - cursor
  - generic-mcp-agents
required_tools:
  - name: Cursor Agent hooks (subagentStart)
    install: "https://cursor.com/docs/agent/hooks"
    version_notes: "Matchers on subagent_type: explore, shell, generalPurpose, etc."
  - name: Cursor Task tool
    install: "https://cursor.com/docs/agent/hooks"
    version_notes: "subagentStop for audit and follow-up; loop_limit default 5."
inputs:
  - "Allowed subagent types for this repository (e.g. explore yes, shell no)"
  - "Max parallel explore workers and sensitive paths subagents must not read"
  - "Branch naming policy when subagents run on git_branch"
outputs:
  - "subagentStart/subagentStop hook pair with matcher rules"
  - "Audit log sample for one denied shell subagent and one allowed explore subagent"
risk_level: medium
example_count: 2
version: "1.0.0"
updated: "2026-11-26"
---

## Purpose

Govern **Cursor Task subagents** using `subagentStart` and `subagentStop` hooks so explore, shell, and `generalPurpose` workers cannot start outside policy ([Cursor hooks reference](https://cursor.com/docs/agent/hooks)). Matchers filter on `subagent_type` and optional task text.

## When to use

- A monorepo limits **shell** subagents on production release branches.
- Security wants explore subagents blocked from tasks mentioning `prod`, `payment`, or `customer-db` strings.
- Platform teams need structured audit lines when subagents complete or abort.

### When not to use

- The user runs only single-threaded Agent Chat with subagents disabled in settings.
- Hook maintenance cost exceeds benefit for a one-person hobby repo without cloud agents.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| `subagentStart` hook | Admission control | Returns `permission: deny` (ask treated as deny) |
| `subagentStop` hook | Audit / follow-up | Optional analytics; respects `loop_limit` |
| Git branch metadata | Scope | `git_branch` field in hook stdin when applicable |
| Repo rules / skills | Context | Complements hooks with static guidance |

## System prompt

```text
You govern Cursor Task subagents for agent-platforms/cursor using official hook events subagentStart and subagentStop documented at https://cursor.com/docs/agent/hooks.
You never spawn subagents yourself in this template run unless the user explicitly tests hooks; your deliverable is configuration and proof logs.
You map each allowed subagent_type (explore, generalPurpose, shell, ci-investigator, etc.) to an explicit allow or deny rule in the matcher table the user provides.
You deny shell subagents on protected branches when git_branch in hook input matches release/* or main if the user's policy says so, returning a clear user_message for the parent agent.
You scan subagent task strings for blocked keywords (credentials, prod database, PII export) and deny when matched, without logging full task text to shared CI artifacts when redaction is required.
You configure subagentStop hooks to append one JSON line per completion to a local audit file only when the user approves disk writes, redacting file paths that reveal home directories.
You set loop_limit in hooks.json consciously: null vs 5 changes stop-hook recursion behavior per Cursor docs; document the choice.
You explain that subagentStart on Cloud Agents is supported while sessionStart is not, so subagent policy is viable for cloud fleets.
You separate concerns: hooks gate spawning; .cursor/rules still tell the parent when to delegate versus work inline.
You finish with matcher JSON snippets, test transcripts for deny and allow, and a list of subagent types still permitted.
```

## Workflow

1. List subagent types the team uses today from Cursor settings and past Task tool calls.
2. Draft policy: which types are allowed on default branches, feature branches, and cloud runs.
3. Add `subagentStart` hook with matchers (e.g. only run `validate-explore.sh` when `subagent_type` is `explore` or `shell`).
4. Implement validators: parse stdin fields `subagent_id`, `task`, `subagent_model`, `is_parallel_worker`.
5. Add optional `subagentStop` hook for audit JSON lines or metrics export.
6. Test locally: parent agent requests a denied shell subagent and confirms block message.
7. Test allowed explore subagent on a safe codebase search task; capture stop hook output.
8. Document cloud agent behavior and link hook files in CONTRIBUTING or AGENTS.md.

## Definition of done

- [ ] subagentStart deny and allow paths demonstrated with hook JSON
- [ ] Policy table covers each subagent_type the repo uses
- [ ] Audit approach documented without leaking secrets in logs
- [ ] Parent agent instructions updated so humans know why spawn failed

## Security

- Subagents inherit repository access; denying shell type reduces arbitrary command risk but explore can still read files—pair with `beforeReadFile` hooks if needed.
- Parallel workers multiply cost and data exposure; cap with policy and billing alerts.
- Do not embed API keys in subagent task strings echoed to logs.

## Pitfalls

- Treating `permission: ask` as soft deny on subagentStart—Cursor docs say ask is unsupported and acts as deny.
- Forgetting plugin hook path differences (`CURSOR_PLUGIN_ROOT`) when hooks ship via marketplace plugins.
- Denying all subagents breaks large refactors that rely on explore agents; allow generalPurpose with narrower matchers instead.
- stop/subagentStop plugin hooks run from workspace root; script paths must be valid in cloud checkout layout.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Allow `explore` subagents; deny `shell` subagents on branch `main`.
- **Input:** Protected branches: `main`, `release/*`. Allowed types: `explore`, `generalPurpose`.
- **Prompt:**

```text
Configure subagentStart hook scripts/cursor-hooks/subagent-gate.sh with the branch and type rules above. Test deny on main + shell.
```

- **Expected result:**

```text
Hook input: subagent_type shell, git_branch main → permission deny, user_message "Shell subagents disabled on protected branches".
Hook input: subagent_type explore, git_branch main → permission allow.
subagentStop writes audit line: {"subagent_type":"explore","status":"completed","duration_s":42} (no secrets).
Policy table committed beside hooks.json.
```

### Example 2 (Example data (self-written))

- **Task:** Block subagents whose task text mentions production database refresh.
- **Input:** Deny substrings: `prod database`, `pg_dump production`, `customer PII export`.
- **Prompt:**

```text
Extend subagent-gate.sh to inspect task field. Allow explore for refactoring auth module only.
```

- **Expected result:**

```text
Task "run pg_dump production to /tmp" → deny before subagent spawns; parent sees user_message citing data-handling policy.
Task "refactor auth module JWT validation" → allow explore subagent; parent receives search summary cites paths under src/auth/.
No database commands run; audit log records deny reason keyword match only.
```