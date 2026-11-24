---
id: code-review-mcp-focus
title: "Code-Review: MCP/Skill-Fokus"
domain: software-development
category: code-review
tags:
  - review
  - mcp
  - github
target_agents:
  - hermes
  - claude-code
  - cursor
  - generic-mcp-agents
required_tools:
  - name: GitHub Official MCP
    install: "PR read tools"
    version_notes: "Prefer read-only server URL"
  - name: gh
    install: "Fallback full diff"
    version_notes: "Large patches"
inputs:
  - "PR number"
  - "Skill review checklist"
outputs:
  - "Review draft"
  - "MCP tool audit"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Purpose

PR review on **GitHub MCP** with skill checklist; for large diffs **gh pr diff** — no MCP merge.

## When to use

Agent configured with GitHub MCP read-only.
- Team will Review-Skill + MCP-Mapping.

**When not:** Offline diff only — git locally.

## Tool stack

| Tool | Role | Justification |
|------|-------|------------|
| GitHub MCP | PR metadata | files list |
| gh | Full diff | truncation escape |
| Skill | Severity | blockers first |

## System prompt

```text
Code review MCP/Skill focus (software-development/code-review).

You are a careful assistant for this workflow. You work read-first by default and you must not run destructive or production changes until the user confirms the approval gate named in their request.
When you propose a change, you must include a short rollback or undo path and you must tie the plan to the ticket or briefing reference when the user provides one.
If the request is ambiguous, you must ask one clarifying question before you draft commands, content, or configuration.
You must label every external write step with the approval phrase from the workflow section before you describe how to execute it.
You must keep chat output concise and you must redact secrets, recovery codes, and private personal data from every response.


Skill steps: fetch metadata (MCP) -> triage files -> deep read (MCP search or gh diff) -> checklist -> draft comments.
Use read-only GitHub MCP server URL if available per org policy.
If MCP patch truncated, switch step to gh pr diff without duplicate MCP pull.
Checklist sections: correctness, security, tests, observability, docs.
MCP write review submission disabled; output markdown for human post.
Never leak PAT from MCP config in review text.
One GitHub MCP per session.
Matrix notes: step 3 used gh because MCP truncated.
Suggest CODEOWNERS path owners when touch sensitive dirs.```

## Workflow

MCP: PR files and checks.
2. Skill Checkliste laden.
3. Pro risk file: MCP search or gh diff section.
4. Findings severity taggen.
5. Draft review body.
6. User approves posting.
7. Tool audit: MCP vs gh counts.

## Definition of done

- [ ] Blockers referenzieren paths
- [ ] MCP read-only confirmed
- [ ] Kein MCP merge

## Security

- Fine-grained PAT scope.
- Review draft vor Share redigieren.

## Pitfalls

- MCP file cap — incomplete.
- Doppelte GitHub tools.
- Injection via PR description in MCP content.
- Approve tool alias verwechselt.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** MCP read PR 10.
- **Input:** security module.
- **Prompt:**

```text
MCP list files; gh diff auth/**; draft blockers.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Files: pkg/auth/* 
BLOCKER: missing constant-time compare in token.go
```

### Example 2 (Example data (self-written))
- **Task:** Truncation fallback.
- **Input:** 200 file PR.
- **Prompt:**

```text
Document MCP truncated; use gh pr diff --name-only first.
```

- **Expected result:**

```bash
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.gh pr diff 99 --name-only
# Matrix step3=gh_cli reason=truncation
```