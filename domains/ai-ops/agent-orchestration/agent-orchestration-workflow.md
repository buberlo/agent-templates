---
id: agent-orchestration-workflow
title: "Agent orchestration"
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
  - name: Hermes Agent
    install: "https://github.com/NousResearch/hermes-agent"
    version_notes: "Subagents and MCP filters for worker roles."
  - name: OpenClaw gateway
    install: "https://docs.openclaw.ai/"
    version_notes: "Tool policy and channel routing for supervised workers."
inputs:
  - "Task DAG (roles, dependencies, handovers)"
  - "Per-worker MCP allow list and risk class"
outputs:
  - "Orchestration charter (supervisor + worker prompts)"
  - "Handoff JSON schema and artifact directory layout"
risk_level: medium
example_count: 2
version: "1.2.0"
updated: "2026-11-24"
---

## Purpose

Coordinate **multiple agents** with a clear DAG: one writer per shared resource, bounded MCP per worker, and structured handoffs so supervisors do not become shadow executors. Applies to Hermes subagents, OpenClaw-supervised workers, or any host that spawns child runs.

## When to use

- Pipelines such as research → implementation → review across separate tool sets.
- Specialists need different MCP exposure (browser vs terminal vs CRM read).
- You must prove approval gates and artifact paths for audit.

### When not to use

- Single-step questions one agent can answer without delegation overhead.
- Two workers would write the same database or ticket queue in parallel.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| Supervisor prompt | Routing | Plans and summarizes; avoids destructive tools |
| Worker charters | Scope | Max MCP count and allowed tools per role |
| Shared artifact directory | Handoff | JSON or markdown payloads between steps |
| Human approval token | Gate | `ORCH_PROD` or per-worker write release |

## System prompt

```text
You are an agent orchestration architect for ai-ops/agent-orchestration.
You decompose the user goal into a directed acyclic graph where each node has one owner role and explicit inputs and outputs.
You assign at most three MCP servers per worker and you document tool names allowed for that worker in the charter.
You enforce single-writer semantics: only one worker may mutate a given git branch, ticket queue, or database table per run.
You define a handoff JSON schema with fields task_id, run_id, inputs, artifacts, blocked_reason, and next_agent.
You instruct the supervisor to plan and delegate only; destructive tools run in workers after approval tokens, not from the supervisor session.
You cap supervisor summaries of worker output to a concise decision memo so token budget stays for implementation detail in artifacts.
You require idempotent run_id values so duplicate worker launches are detectable and aborted.
You keep secrets in worker environments with vault or MCP env wiring, not in supervisor chat history.
You mandate a dry-run with mock artifacts before live MCP when risk is medium or high.
You reject designs that assign Playwright or browser MCP to every worker; consolidate browsing in one read-only worker.
```

## Workflow

1. Sketch the DAG on paper: nodes, edges, and which artifacts cross each edge.
2. Assign role, risk level, and MCP allow list per node.
3. Write the handoff JSON schema and example payload.
4. Draft supervisor system prompt and one charter per worker.
5. Dry-run with mock artifacts and no live writes.
6. Obtain `ORCH_PROD` or equivalent before high-risk workers start.
7. Execute live run; supervisor collects artifacts and logs durations.
8. Postmortem: token use, errors, and whether MCP counts should shrink.

## Definition of done

- [ ] Single writer per shared resource documented in the charter
- [ ] Handoff schema validated with at least one example payload
- [ ] Each worker lists ≤3 MCPs with justified tools
- [ ] Dry-run completed before live destructive paths

## Security

- Supervisors must not hold production credentials when workers can use scoped MCP.
- Parallel CRM or ticket writes are forbidden without transactional design reviewed by a human.
- High-risk workers require explicit approval naming worker ID and target systems.

## Pitfalls

- Supervisor runs GitHub merge tools "to save time" and bypasses review charter.
- Handoffs without `run_id` spawn duplicate workers that double-post comments.
- Unbounded worker prose pasted into supervisor chat consumes the planning window.
- Ten subagents each with browser MCP multiply flaky UI steps.
- Mock dry-run skipped and production CRM writes duplicate records.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Research then patch from a bug report URL.
- **Input:** `https://bugs.example.com/8841` on branch `fix/8841`.
- **Prompt:**

```text
DAG: researcher read-only (Exa MCP), coder terminal+git on fix/8841, reviewer read diff only. Handoff schema required.
```

- **Expected result:**

```text
orchestration.md with 3 nodes and edges
handoff-schema.json: task_id, run_id, artifacts[], next_agent
Researcher: brief.md artifact, 1 MCP (exa)
Coder: diff.patch, no push without CODER_PUSH_APPROVED
Reviewer: findings.md, no write tools enabled
```

### Example 2 (Example data (self-written))

- **Task:** Reject parallel database cleaners.
- **Input:** Two workers asked to purge stale rows concurrently.
- **Prompt:**

```text
Speed up DB cleanup with two agents deleting in parallel on the same table.
```

- **Expected result:**

```text
Design rejected: single writer on table users_staging
Proposed sequential DAG or partitioned table scope with human review
No ORCH_PROD token issued
Explanation cites duplicate delete and lock risk
```