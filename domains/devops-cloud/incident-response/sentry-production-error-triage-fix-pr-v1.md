---
id: sentry-production-error-triage-fix-pr-v1
title: "Sentry MCP production error triage to fix PR plan"
domain: devops-cloud
category: incident-response
tags:
  - sentry
  - mcp
  - incident-response
  - debugging
target_agents:
  - cursor
  - claude-code
  - hermes
  - grokbot
  - generic-mcp-agents
required_tools:
  - name: Sentry MCP
    install: "https://github.com/getsentry/sentry-mcp"
    version_notes: "Remote hosted https://mcp.sentry.dev or stdio via Sentry CLI sentry mcp per README."
  - name: GitHub Official MCP
    install: "https://github.com/github/github-mcp-server"
    version_notes: "Read code and draft branch or PR after human approval."
inputs:
  - "Sentry issue ID or short error title and environment (prod/staging)"
  - "Release version or commit SHA associated with the spike"
  - "On-call severity label (SEV2 example)"
outputs:
  - "Triage brief with stack fingerprint, blast radius, and suspected module"
  - "Fix PR checklist and draft description (no merge without approval)"
risk_level: high
example_count: 2
version: "1.0.0"
updated: "2026-11-25"
---

## Purpose

Turn a rising Sentry issue into an evidence-backed triage brief and a fix pull request plan using Sentry MCP read tools, then hand off to a coding agent with explicit human gates before writes, deploys, or issue resolution in Sentry.

## When to use

- Error rate crosses alert threshold and on-call needs structured context fast.
- A coding agent should propose a patch but must not auto-resolve Sentry or deploy.
- You use the hosted server at [mcp.sentry.dev](https://mcp.sentry.dev) or stdio via [Sentry CLI MCP](https://cli.sentry.dev/commands/mcp/).

### When not to use

- Security incidents requiring credential rotation without code change.
- Self-hosted Sentry without MCP configured; follow [stdio auth docs](https://github.com/getsentry/sentry-mcp) first.
- Bulk backlog grooming across hundreds of muted issues.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| Sentry MCP | Issues, events, traces | Official middleware to Sentry API ([getsentry/sentry-mcp](https://github.com/getsentry/sentry-mcp)) |
| GitHub Official MCP | Code linkage | Map stack frames to repository paths |
| Local git | Patch | Human-owned branch after TRIAGE APPROVED |

## Example workflow diagram

Example data (self-written): see [assets/example-sentry-triage-flow.svg](assets/example-sentry-triage-flow.svg) for a fictional sequence from issue list to human merge.

## System prompt

```text
You are a production error triage lead using Sentry MCP under devops-cloud/incident-response.
You fetch the issue, recent events, and release metadata with read-only Sentry MCP tools, and you serialize tool calls one at a time when rate limit messages appear in the README guidance.
You summarize the user-visible symptom, the earliest failing frame in application code, and whether the spike correlates with a release or config flag change without guessing deploy times.
You distinguish client-side, edge, and backend ownership using tags and logger names present in the event payload, and you flag missing tags as data quality debt.
You never click resolve, assign, or mutate Sentry state unless the user types SENTRY_WRITE APPROVED with the exact action list.
You produce a fix plan that names files to edit, tests to add, and rollback steps, but you open or update pull requests only after PR DRAFT APPROVED.
You redact PII from stack arguments and breadcrumbs in the triage brief, replacing emails with user_id hashes when available.
You cite https://mcp.sentry.dev for hosted setup and https://github.com/getsentry/sentry-mcp for skill and scope limits.
When AI search tools are unavailable due to missing LLM provider keys, you state that limitation and fall back to structured issue queries only.
You end with an on-call handoff section listing open questions and whether customer comms is required.
```

## Workflow

1. Confirm org/project scope and time window for the spike.
2. Pull issue details and at least one representative event with stack trace.
3. Correlate `release` or `dist` with GitHub commits via GitHub MCP.
4. Draft root-cause hypothesis ranked by likelihood with disconfirming evidence.
5. List minimal code fix and monitoring follow-up (new Sentry alert rule proposal as text only).
6. On PR DRAFT APPROVED, create branch plan; human implements and runs tests.
7. Post-incident: document timeline; resolve Sentry only after deploy verified.

## Definition of done

- [ ] Triage brief cites Sentry issue id and environment without raw PII
- [ ] No Sentry or GitHub writes without explicit approval tokens
- [ ] Fix plan includes test strategy and rollback note
- [ ] Rate limits acknowledged if tools were throttled

## Security

- Use Sentry user tokens with least scope; hosted OAuth preferred over pasting tokens in chat.
- Do not export full event payloads into public tickets.
- Separate prod and staging MCP project scopes in client config (`sentry mcp acme/web`).

## Pitfalls

- Parallel Sentry MCP calls trip per-second rate limits ([sentry-mcp README](https://github.com/getsentry/sentry-mcp)).
- Resolving issues before deploy verification hides recurring regressions.
- AI-powered `search_*` tools require `EMBEDDED_AGENT_PROVIDER`; without keys, triage lacks NL search.
- Grouping unrelated errors under one fingerprint masks multiple root causes.
- Auto-generated PRs without reproduction steps waste reviewer time.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Triage spike in `TypeError: Cannot read properties of undefined (reading 'map')` in project `web` production.
- **Input:** Issue id `WEB-4821`, release `web@2.14.3`, SEV2.
- **Prompt:**

```text
Sentry MCP triage for WEB-4821 in acme/web production.
Output triage brief and fix plan only.
No resolve, no PR.
```

- **Expected result:**

A brief with event count trend placeholder, top frame in `src/components/CartList.tsx`, hypothesis that `lineItems` is undefined when API 204 returns, suggested guard and API contract test, and explicit note that Sentry resolve is blocked pending DEPLOY VERIFY. Includes reference to Sentry MCP hosted URL documentation.

### Example 2 (Example data (self-written))

- **Task:** Prepare PR description after human confirmed patch on branch `fix/web-4821-cart`.
- **Input:** Diff adds nullish coalescing and unit test; CI green locally.
- **Prompt:**

```text
PR DRAFT APPROVED: write GitHub PR body linking WEB-4821, test plan, rollback.
Do not merge.
```

- **Expected result:**

PR markdown with Summary, Sentry issue link pattern `https://acme.sentry.io/issues/WEB-4821/`, test commands, monitoring watch window of 30 minutes post-deploy, and rollback via redeploy `web@2.14.2` without claiming merge occurred.