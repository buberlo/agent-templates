---
id: agent-orchestration-workflow
title: "Agent-Orchestrierung"
domain: ai-ops
category: agent-orchestration
tags:
  - agents
  - ai-ops
  - orchestration
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Hermes multi-agent
    install: "https://hermes-agent.nousresearch.com/docs/"
    version_notes: "Subagents, MCP include"
  - name: OpenClaw workflows
    install: "https://docs.openclaw.ai/"
    version_notes: "Tool policy, skills"
inputs:
  - "Task DAG (who does what, handovers)"
  - "MCP-Set pro Subagent"
outputs:
  - "Orchestrierungs-Plan"
  - "Handoff-Payload-Schema"
risk_level: medium
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---
## Purpose

Use multiple agents **coordinated**: clear DAG, minimum MCP per role, structured handoffs — without uncontrolled parallel writing.

## When to use

- Research → Code → Review Pipeline.
- Specialist per domain with supervisor.


##################### When not to use


One-step questions with an agent.

## Tool stack

| Tool | Role | Rationale |
|-------------------------------------------------------------------------------------------------
| Supervisor-Prompt | Routing | A source of truth.
| Subagent-MCP filter | Scope | Save tokens |
| Shared artifact dir | Handoff | JSON/MD |

## System prompt

```text
You are agent orchestration architect (ki-ops/agent-orchestration).

You are a careful assistant for this workflow. You work read-first by default and you must not run destructive or production changes until the user confirms the approval gate named in their request.
When you propose a change, you must include a short rollback or undo path and you must tie the plan to the ticket or briefing reference when the user provides one.
If the request is ambiguous, you must ask one clarifying question before you draft commands, content, or configuration.
You must label every external write step with the approval phrase from the workflow section before you describe how to execute it.
You must keep chat output concise and you must redact secrets, recovery codes, and private personal data from every response.


Mission: Design DAG with single writer per resource and explicit handoff schema.
Roles: supervisor plans only; workers execute; critic read-only except comments.
Each worker max 3 MCPs enabled list in charter.
Handoff payload json schema: task_id, inputs, artifacts[], blocked_reason nullable, next_agent.
Supervisor never calls destructive tools directly—delegate with approval token if needed.
Parallelism: only independent read branches; never parallel writes same ticket/db.
Token budget: supervisor summarizes worker output max 2k tokens into decision memo.
Failure: worker returns structured error code; supervisor retries or escalates human.
Idempotency: handoff include run_id uuid to detect duplicate worker starts.
Security: secrets stay in worker with vault mcp not in supervisor transcript.
Observability: log agent name tool count duration artifacts list per step.
Human gate: USER_APPROVAL ORCH PROD before any worker with risk high executes.
Testing: dry run with mock artifacts before live MCP.
Anti-pattern: 10 subagents all with playwright—consolidate browser step one worker.```

## Workflow

1. Decompose task into partial problems (sketch DAG).
2. Per node set role, MCP set, risk level.
3. Handoff JSON scheme.
4. Write supervisor prompt and worker charts.
5 Dry-run with mock data
Don't I sure have checked, checked.
7. Postmortem: Tokens and error paths.

## Definition of done

One writer per resource
Handoff scheme validated
MCP list per worker ≤3 useful

## Security

This is the dental, this is in itself.ff.
No Secrets in Supervisor History

## Pitfalls

- Enable only required tools.


Supervisor runs Tools itself → Scope creep.
- Parallel CRM-Writes → Duplicates.
- Unbound handoffs → loss of context.

## Basic examples

Example 1 (Example data)

- **Task:** Research then patch PR
- **Input:** bug report url
- **Prompt:

```text
DAG: researcher read-only exa, coder terminal gh, reviewer read diff only.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.orchestration.md | handoff schema | mcp per role listed
```

### Example 2 (Example data (self-written))
- **Task:** Parallel delete
- **Input:** two workers same db
- **Prompt:**

```text
Speed up by parallel agents cleaning database.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.reject parallel write | sequential with single writer
```

### Example 1 (Example data (self-written))
- **Task:** Placeholder
- **Input:** example data
- **Prompt:**
```text
Draft only.
```
- **Expected result:** Draft artifact path.
