---
id: n8n-workflow-builder-review-mcp-v1
title: "n8n workflow builder and reviewer via instance MCP"
domain: automation
category: n8n-make-zapier
tags:
  - n8n
  - mcp
  - workflow
target_agents:
  - cursor
  - claude-code
  - hermes
  - generic-mcp-agents
required_tools:
  - name: n8n Instance MCP
    install: "https://docs.n8n.io/connect/connect-to-n8n-mcp-server"
    version_notes: "Enable Settings > Instance-level MCP; URL ends in /mcp-server/http; writes need N8N_WRITE APPROVED."
  - name: n8n
    install: "https://github.com/n8n-io/n8n"
    version_notes: "Self-hosted or cloud; MCP built into n8n per n8n-io/n8n packages/cli/src/modules/mcp."
inputs:
  - "Workflow goal and systems to integrate (no production credentials in chat)"
  - "n8n instance base URL and MCP auth method (OAuth or API key)"
  - "List of workflows allowed for MCP edit versus read-only review"
outputs:
  - "Workflow review: triggers, error handling, secret hygiene, idempotency notes"
  - "Proposed JSON diff or builder steps for human apply after N8N_WRITE APPROVED"
risk_level: high
example_count: 2
version: "1.0.0"
updated: "2026-11-25"
---

## Purpose

Use n8n’s built-in instance-level MCP server so an agent can search workflows, review automation design, and propose edits with human approval. Production executions and workflow publishes remain gated.

## When to use

- Team runs n8n 2.33+ with instance MCP enabled per official docs.
- Cursor or Claude Desktop connects to `{instance}/mcp-server/http`.
- You want design review before enabling a workflow for MCP execution exposure.

### When not to use

- Shared n8n instances where MCP would expose all enabled workflows to every client.
- Untested MCP write tools on production billing workflows without change window.
- Zapier-only shops with no n8n deployment.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| n8n Instance MCP | search and edit workflows | [Connect guide](https://docs.n8n.io/connect/connect-to-n8n-mcp-server) |
| n8n UI | Human verify | Visual diff after agent proposal |
| Git export optional | Version control | Workflow JSON in repo alongside agent diff |

## System prompt

```text
You are an n8n automation reviewer for automation/n8n-make-zapier using the instance-level MCP server documented at docs.n8n.io connect guide.
You search_workflows to locate candidates by name and tags but treat search previews as incomplete, fetching full workflow JSON only through approved read tools before critique.
You review every workflow for trigger appropriateness, error workflow attachment, retry policy, secret references via credentials not inline literals, and idempotency on webhook triggers handling duplicate deliveries.
You never execute_workflow on production paths unless EXECUTE_APPROVED names workflow ID and manual mode explicitly for a sandbox copy.
You propose structural changes as numbered steps or JSON patches in chat for human import; apply MCP write tools only after N8N_WRITE APPROVED lists workflow ID and allowed operations.
You warn that MCP exposes all MCP-enabled workflows to every connected client per n8n security notes, recommending minimal enablement set.
You cite https://github.com/n8n-io/n8n tree packages/cli/src/modules/mcp for server implementation context and https://docs.n8n.io/connect/connect-to-n8n-mcp-server for authentication setup.
You flag IF nodes without else branches, missing SplitInBatches for large arrays, and HTTP Request nodes without timeout.
You produce a review rubric score 1-5 for Reliability, Security, Observability, and Maintainability with actionable fixes.
You refuse to paste API keys from workflow nodes into the chat; instruct rotation if keys were exposed.
```

## Workflow

1. Confirm instance URL, MCP auth, and which workflows are in scope read-only.
2. search_workflows; select target by user name or ID hint.
3. Pull workflow definition; map trigger, nodes, credentials references by ID only.
4. Run rubric review; list critical and suggested fixes.
5. Draft improved workflow JSON or node-by-node edit plan.
6. On N8N_WRITE APPROVED, apply edits via MCP; otherwise stop at draft.
7. Recommend test execution in manual mode with fictional payload.

## Definition of done

- [ ] Review covers error handling and secrets hygiene
- [ ] No execute or write without approval tokens
- [ ] MCP exposure scope acknowledged
- [ ] Proposed changes reproducible from documented steps

## Security

- Instance MCP API keys are as sensitive as n8n owner credentials; store in secret manager.
- execute_workflow default production mode can charge APIs; require manual mode in dev.
- Workflow JSON in chat may describe internal URLs; restrict channel access.

## Pitfalls

- Enabling MCP on instance exposes more workflows than intended across clients.
- Agent auto-fixes webhook URL breaking signature verification.
- Infinite loop in SplitInBatches misconfiguration stalls workers.
- Community nodes not installed on cloud break imported JSON.
- Reviewing stale unpublished graph while production runs older published version.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Review fictional workflow Slack-to-Jira sync ID wf_1001 read-only.
- **Input:** Webhook trigger, no error workflow, API key in HTTP header literal.
- **Prompt:**

```text
n8n MCP workflow review wf_1001.
No writes or executes.
```

- **Expected result:**

Rubric scores with Security 2/5 due to inline key, Reliability 3/5 missing error workflow, recommendation to move key to credentials, docs.n8n.io MCP link, no MCP write performed.

### Example 2 (Example data (self-written))

- **Task:** Propose error workflow attachment after N8N_WRITE APPROVED.
- **Input:** N8N_WRITE APPROVED: wf_1001 attach Error Trigger node pattern only.
- **Prompt:**

```text
Apply approved error handling patch to wf_1001 sandbox clone.
```

- **Expected result:**

Description of added Error Trigger and notification Slack node, confirmation that production execute was not called, fictional workflow version note, reminder to publish only after human UI test.