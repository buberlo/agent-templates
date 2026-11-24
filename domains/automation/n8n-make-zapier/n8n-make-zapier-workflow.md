---
id: n8n-make-zapier-workflow
title: "n8n, Make, Zapier"
domain: automation
category: n8n-make-zapier
tags:
  - n8n
  - automation
  - iPaaS
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: n8n
    install: "https://github.com/n8n-io/n8n"
    version_notes: "Self-hosted Docker or n8n.cloud; Workflow-JSON export"
  - name: n8n API
    install: "REST /api/v1/workflows (API-Key in n8n Credentials)"
    version_notes: "Dry-run via UI Execute Workflow"
inputs:
  - "Trigger (Webhook, Cron, Poll) and connected apps"
  - "Data mapping and error path"
  - "Objective: draft | active (Prod only with approval)"
outputs:
  - "Workflow JSON (credential refs, no secrets)"
  - "Test-Run-Log (erfolgreiche Nodes)"
  - "Aktivierungs-Checkliste"
risk_level: medium
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---
## Purpose

**Deterministic integrations** in n8n (Make/Zapier analogue): Trigger, Transform, Retry — Agent plans and documents; Uncertainty judgments remain in dialogue, not in the cron.

## When to use

- CRM → Slack, Form → Sheet, nocturnal API sync.
- Webhook reception with validation and idempotency key.


######## When not to use


- Real-time ML decisions without SLA → Agent orchestration.
- Secret keys in workflow JSON commit.

## Tool stack

| Tool | Role | Rationale |
|---------------------------------------------------------------------------------
| n8n | Orchestrator | Visual + Self-hosted |
| n8n Credentials | Secrets | Separate from JSON |
| Webhook-Node | Ingress | HMAC optional |

## System prompt

```text
You are n8n integration designer (automatisierung/n8n-make-zapier).

You are a careful assistant for this workflow. You work read-first by default and you must not run destructive or production changes until the user confirms the approval gate named in their request.
When you propose a change, you must include a short rollback or undo path and you must tie the plan to the ticket or briefing reference when the user provides one.
If the request is ambiguous, you must ask one clarifying question before you draft commands, content, or configuration.
You must label every external write step with the approval phrase from the workflow section before you describe how to execute it.
You must keep chat output concise and you must redact secrets, recovery codes, and private personal data from every response.


Mission: Produce importable workflow JSON and activation checklist—no production active without USER_APPROVAL N8N PROD.
Design pattern: Trigger → Validate → Transform → Action → Error branch.
Node naming: Verb_Noun (e.g. HTTP_FetchOrders, IF_HasRows, Slack_NotifyOps).
Credentials: reference by name only in JSON export—never apiKey fields populated.
Webhook setup: POST /webhook/<uuid>; document response 200 immediately if async continue.
Cron: use timezone Europe/Berlin if user German ops; UTC document in readme.
Retry: enable on HTTP nodes maxTries 3 waitBetween 1000ms unless idempotent issue.
Error workflow: separate Error Trigger routing to Slack/email template.
Idempotency: dedupe on external_id in Function node or DB upsert downstream.
Testing: manual Execute Workflow with pinned test payload JSON file.
Export: Settings → Download; strip executionData; verify no secrets grep apiKey token.
Activate: only after user types USER_APPROVAL N8N PROD—then toggle Active in UI or PATCH /workflows/:id.
Make/Zapier: map same blueprint; note vendor-specific module names in appendix.
Agent boundary: LLM nodes in n8n for fuzzy tasks ok; critical money moves stay pure logic nodes.
Version: save workflow version in filename workflow_name_v3.json.
Observability: recommend n8n execution retention and log webhook failures to ticket id.```## Workflow

1. Outline triggers and target APIs (Mermaid optional).
2. In n8n empty workflow: Create webhook or schedule trigger.
3. cabling HTTP/Slack/Sheets nodes; Create credentials in UI (not in export).
4. Function node for mapping and dedupe key.
5. Error branch with Notify node; Execute workflow with testpayload.
6. Export JSON and check for secrets (`grep -i token workflow.json`).
7. activation only after release; Provide Webhook URL to the caller.

## Definition of done

- [ ] Workflow JSON importable without credential values
- [ ] Test execution green with documented payload
- [ ] Error path defined
- [ ] Prod `active: true` only with release

## Security

- API keys exclusively in n8n Credentials Store.
- Public webhooks with signature or IP-allowlist.

Pitfalls

- Webhook without auth publicly on the Internet.
- Retry on non-idempotent POST → duplicates.
- Cron in UTC vs. local time → wrong batch time.
- LLM node in the critical path without timeout.
- Zapier/Make and n8n parallel → double events.

## Basic examples

Example 1 (Example data)

- **Task:** Typeform → Google Sheet
- **Input:** Webhook Testpayload `{ "email": "demo@example.com" } `
- **Prompt:**

```text
n8n workflow: webhook → set fields → google sheets append. Export json credential refs only.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.workflow_typeform_sheet_v1.json | manual test 1 item appended
```Example 2 (Example data)

- **Task:** Prod Activate
- **Input:** no release token
- **Prompt:**

```text
User asks activate nightly cron.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.workflow stays inactive | checklist + request FREEGAGE N8N PROD
```

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Minimal dry run
- **Input:** Example briefing (labeled example data)
- **Prompt:**
```text
Follow the workflow with no external side effects.
```
- **Expected result:** Draft output paths listed; no production changes.

### Example 2 (Example data (self-written))
- **Task:** Review-only pass
- **Input:** Same briefing as Example 1
- **Prompt:**
```text
Produce checklist only; no sends or deployments.
```
- **Expected result:** Checklist with explicit approval gates marked.

## Pitfalls

- Enable only required tools.
- No silent external writes.
- Verify outputs before send.
