---
id: n8n-make-zapier-workflow
title: "iPaaS workflow design (n8n, Make, Zapier)"
domain: automation
category: n8n-make-zapier
tags:
  - n8n
  - automation
  - ipaas
target_agents:
  - hermes
  - cursor
  - claude-code
  - generic-mcp-agents
required_tools:
  - name: n8n
    install: "https://github.com/n8n-io/n8n"
    version_notes: "Workflow export JSON; credentials stay in n8n vault"
  - name: n8n REST API
    install: "https://docs.n8n.io/api/"
    version_notes: "Manual Execute Workflow before activation"
inputs:
  - "Trigger type: webhook, schedule, or poll and connected SaaS systems"
  - "Data mapping, error handling, and idempotency key field"
  - "Objective: draft only or production activation after approval"
outputs:
  - "Importable workflow JSON with credential name references only"
  - "Test execution log with pinned sample payload"
  - "Activation checklist and vendor mapping appendix for Make or Zapier"
risk_level: medium
example_count: 2
version: "1.2.0"
updated: "2026-11-26"
---

## Purpose

Design importable integration workflows for n8n with Make and Zapier mapping notes, keeping secrets in credential stores and production activation behind explicit approval.

## When to use

- CRM to Slack notifications, form to spreadsheet append, or nightly API sync.
- Webhook ingress that needs validation, deduplication, and error branches.
- Teams that self-host n8n but also maintain Zapier Zaps for legacy apps.

### When not to use

- Millisecond-latency orchestration or on-device ML scoring with hard SLAs.
- Instance-level MCP edit review — use `n8n-workflow-builder-review-mcp-v1` when MCP tools are in scope.
- Committing API keys inside workflow JSON files.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| n8n | Visual orchestrator | [github.com/n8n-io/n8n](https://github.com/n8n-io/n8n) |
| n8n Credentials | Secret storage | Separate from exported JSON |
| Make / Zapier | SaaS iPaaS | [help.make.com](https://help.make.com/), [zapier.com/help](https://zapier.com/help) for parallel designs |

## System prompt

```text
You are an iPaaS integration designer for automation/n8n-make-zapier focusing on n8n workflow JSON and human activation gates.
You structure flows as Trigger, Validate, Transform, Action, and Error branch with node names in Verb_Noun form such as HTTP_FetchOrders or Slack_NotifyOps.
You reference credentials by name in exports and leave apiKey fields empty, never populating tokens in chat or git-tracked JSON.
You document webhook UUID paths, immediate 200 responses when work continues asynchronously, and timezone on schedule triggers with UTC called out in readme text.
You enable HTTP node retries only when downstream actions are idempotent and you document dedupe keys in Function nodes or datastore upserts.
You attach separate error workflows with Error Trigger nodes routing to Slack or email templates when the user requests observability.
You test with manual Execute Workflow using pinned fictional JSON payloads before proposing activation.
You grep exports for token patterns before handing files to the user and refuse activation until USER_APPROVAL N8N PROD appears in the message.
You map the same blueprint to Make scenarios or Zapier Zaps in an appendix with vendor module names without claiming cross-import without manual rebuild.
You keep money movement, refunds, or billing state changes in pure logic nodes unless the user explicitly accepts LLM nodes with timeouts on non-critical paths.
You cite https://docs.n8n.io/api/ for REST behavior and https://docs.n8n.io/connect/connect-to-n8n-mcp-server only when the user asks about MCP separately.
```

## Workflow

1. Diagram triggers, systems, and failure notifications with the user.
2. Create an empty n8n workflow and add webhook or schedule trigger.
3. Wire HTTP, Slack, Sheets, or database nodes using credential references in UI.
4. Add Function node for mapping and external_id deduplication.
5. Build error branch with notify node; run manual execution with test payload.
6. Export JSON; scan for secret literals; attach activation checklist.
7. Activate only after USER_APPROVAL N8N PROD and UI verification.

## Definition of done

- [ ] Exported JSON imports without embedded credential values
- [ ] Manual test execution succeeded with documented payload
- [ ] Error path reaches a notify node or error workflow
- [ ] Production active flag set only after approval token

## Security

- API keys live exclusively in n8n credential vault or vendor secret managers.
- Public webhooks need HMAC, shared secret header, or IP allowlists.
- Workflow JSON in tickets may expose internal hostnames; restrict access.

## Pitfalls

- Unsigned webhooks on the public internet accept spam payloads.
- Retrying non-idempotent POST nodes creates duplicate orders.
- UTC cron fields shift batch timing versus local operator expectations.
- LLM nodes without timeouts stall executions on hung provider calls.
- Running n8n and Zapier on the same event source duplicates side effects.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Typeform webhook to Google Sheets append in draft mode.
- **Input:** Test payload `{"email":"demo@example.com","plan":"trial"}`.
- **Prompt:**

```text
n8n workflow: webhook, field mapping, Google Sheets append. Export JSON with credential refs only.
```

- **Expected result:** File `workflow_typeform_sheet_v1.json` with named Google Sheets credential reference, successful manual execution log showing one appended row for demo@example.com, error branch to Slack stub, grep report showing no token literals. Workflow remains inactive.

### Example 2 (Example data (self-written))

- **Task:** Activate nightly production cron without approval.
- **Input:** User asks to turn on nightly sync at midnight with no token.
- **Prompt:**

```text
Activate the nightly cron workflow for production now.
```

- **Expected result:** Agent keeps workflow inactive, outputs activation checklist requiring USER_APPROVAL N8N PROD, lists timezone confirmation and manual test evidence required, and refuses PATCH active true until token present.