---
id: hermes-workflow
title: "Hermes Agent (Nous Research)"
domain: agent-platforms
category: hermes
tags:
  - hermes
  - agent-platforms
  - agent-platform
target_agents:
  - hermes
  - generic-mcp-agents
required_tools:
  - name: Hermes Agent
    install: "https://github.com/NousResearch/hermes-agent"
    version_notes: "CLI and desktop; skills, memory, optional MCP catalogue."
  - name: Hermes MCP user guide
    install: "https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp"
    version_notes: "Optional MCPs off by default; `hermes mcp install`."
inputs:
  - "Task briefing with desired artifact and risk level"
  - "Optional repo path, ticket URLs, or document templates"
outputs:
  - "Artifact path or structured summary"
  - "Tool log listing MCPs and skills activated during the run"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-24"
---

## Purpose

Run **Hermes** as a self-hosted agent platform where **Skills** define procedure and **Nous-approved optional MCPs** supply data. Install MCPs deliberately with `hermes mcp install`; delegate heavy coding to Codex or Claude Code when appropriate ([Hermes repo](https://github.com/NousResearch/hermes-agent), [MCP guide](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp)).

## When to use

- You want a least-privilege start with MCPs disabled until the task needs them.
- Slash commands and bundled skills cover GitHub triage, research, or document flows.
- You orchestrate a coding sub-agent and keep review in the Hermes thread.

### When not to use

- You require unreviewed community registry skills without local audit—prefer verified sources.
- The skill lists `platforms: [macos]` but you run on Linux (skill may be skipped silently).

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| Hermes CLI / app | Orchestrator | Skills, cron, tool gateway |
| Nous optional MCP catalogue | Curated connectors | PR-merged `optional-mcps/` paths |
| `~/.hermes/skills` | Procedure | Progressive disclosure |
| Codex or Claude Code (optional) | Delegation | Coding loop with parent review |

## System prompt

```text
You operate on Hermes (Nous Research) and treat skills as the source of procedure while MCPs provide external data and actions.
You list installed MCPs with Hermes CLI before enabling new ones and install only catalogue entries the task requires.
You honor skills' `platforms` filters and warn the user when a macOS-only skill cannot run on Linux instead of failing silently.
You obtain explicit approval before MCP or built-in tools send email, post comments, deploy, charge payments, or delete data.
You follow document skills' validate and render steps when producing Office or PDF artifacts and re-read the output file.
You delegate large coding tasks to Codex or Claude Code skills when configured, then review diffs in this Hermes thread before merge.
You never place API tokens in chat, skill markdown, or MCP launch argv; use Hermes install cards and OS secret stores.
You log each external tool call in one line: tool name, purpose, success or error code.
You use include/exclude filters to limit MCP and skill exposure when the session context feels crowded.
You close with the artifact location, approvals pending, and a list of MCPs that remained active.
```

## Workflow

1. Run `hermes setup` or open the app; check MCP status (`hermes mcp`—default off).
2. Decompose briefing into artifact, risk, and required external systems.
3. Install skills from the catalogue only when steps demand them.
4. `hermes mcp install` for each needed optional MCP; apply include/exclude to trim tools.
5. Start the thread with a slash command or skill trigger matching the task.
6. Verify outputs; run document validate and render when applicable.
7. Delegate coding if needed; review sub-agent diff before any push approval.
8. Save tool log and artifact pointers for reproducibility.

## Definition of done

- [ ] Only required MCPs and skills were active (listed in the log)
- [ ] No write/send without documented approval
- [ ] Office/PDF outputs passed validate or visual check when relevant
- [ ] Delegation results reviewed in the Hermes thread, not only in the sub-agent

## Security

- Prefer Nous catalogue MCPs; custom servers need maintainer review.
- Write paths require explicit human approval each session unless policy says otherwise.
- Redact PII from logs shared outside the privacy team.

## Pitfalls

- macOS-only skills skip on Linux without a clear error—check `platforms` in SKILL.md first.
- Installing every optional MCP at once inflates tool schemas and slows responses.
- Delegating to Codex without reading the returned diff merges broken auth changes.
- Skill sync deletes local edits unexpectedly—use documented reset flags carefully.
- Assuming skill activation replaces MCP for GitHub writes—both may need coordinated gates.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** GitHub issue triage with minimal MCP.
- **Input:** `https://github.com/org/example/issues/42`; labels and draft comment only.
- **Prompt:**

```text
Install github MCP from Nous catalogue only. Summarize issue #42, propose labels, draft comment. Do not post without approval.
```

- **Expected result:**

```text
Summary: 3 sentences on reproduction steps
Suggested labels: bug, needs-triage
Draft comment in markdown (not posted)
Tool log: get_issue OK, list_labels OK (2 MCP calls)
Awaiting POST_APPROVED
```

### Example 2 (Example data (self-written))

- **Task:** macOS-only skill on Linux.
- **Input:** Calendar export skill with `platforms: [macos]`.
- **Prompt:**

```text
Run the macOS calendar export skill for this week's events.
```

- **Expected result:**

```text
Skill not loaded for platform linux
User message: no compatible skill—suggest manual export or a Linux-capable alternative
No MCP calls made
No partial calendar file claimed as success
```