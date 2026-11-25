---
id: incident-response-mcp-focus
title: "Incident response: MCP focus"
domain: devops-cloud
category: incident-response
tags:
  - incident
  - mcp
  - observability
target_agents:
  - hermes
  - cursor
  - claude-code
  - grokbot
  - generic-mcp-agents
required_tools:
  - name: GitHub Official MCP
    install: "https://github.com/github/github-mcp-server"
    version_notes: "Workflow runs read during incident"
  - name: Sentry MCP
    install: "https://github.com/getsentry/sentry-mcp"
    version_notes: "Error spikes by release"
  - name: kubernetes-mcp-server
    install: "https://github.com/containers/kubernetes-mcp-server"
    version_notes: "readonly default"
inputs:
  - "Incident bridge context and severity"
  - "Skill step to MCP tool mapping"
outputs:
  - "Minimized MCP set for the incident"
  - "Deploy and error correlation notes"
risk_level: high
example_count: 2
version: "1.2.0"
updated: "2026-11-25"
---

## Purpose

During incidents activate only **necessary MCP servers**: GitHub runs, Sentry spikes, Kubernetes read-only — while the skill owns approval gates for any write tools.

## When to use

- An agent supports an incident commander with correlation reads.
- The team maintains an incident skill with an MCP matrix.

### When not to use

- First-line triage without a skill — start with incident-response-workflow.
- Incidents where CLI-only is faster than MCP auth setup.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| Sentry MCP | Errors | Release and fingerprint correlation |
| GitHub MCP | Deploys | Run id to commit mapping |
| kubernetes-mcp-server | Pods | Read-only workload status |

## System prompt

```text
You are an incident MCP focus assistant for devops-cloud/incident-response.
You keep at most three MCP servers active during an active incident bridge.
You map skill steps to correlate read-only, propose mitigation, await APPROVE, then execute kubectl or gh writes.
You use Sentry MCP to fetch issue stats for the release version the user names and avoid pasting PII.
You use GitHub MCP to list workflow runs around the incident start timestamp in UTC.
You configure Kubernetes MCP at readonly access level and never request admin without incident commander sign-off.
You disable unrelated MCPs such as Notion or email send for the session duration.
You document tool provenance in timeline bullets with server name and tool id.
You keep MCP write tools off by default in Cursor and Hermes tool policy during incidents.
You fall back to gh and kubectl CLI when MCP auth fails without abandoning the bridge.
You restore the normal MCP profile after post-incident handoff.
```

## Workflow

1. Load incident skill; apply MCP whitelist of three servers.
2. Build matrix: correlate deploy, correlate errors, pod status.
3. Run Sentry and GitHub MCP reads in parallel for the UTC window.
4. Kubernetes MCP describe failing workload and events.
5. Insert proposals into bridge doc; no automatic mitigation.
6. After APPROVE, run skill mitigation via CLI unless write MCP is pre-approved.
7. Post-incident: reset MCP list and document matrix for the retro.

## Definition of done

- [ ] At most three MCPs active during incident
- [ ] Deploy to error correlation documented with timestamps
- [ ] Writes only after explicit APPROVE token

## Security

- **High risk** in production; incident commander approval for writes.
- Sentry and Kubernetes payloads may include PII — redact in summaries.
- Admin Kubernetes MCP is forbidden in default incident skills.

## Pitfalls

- Leaving all MCPs enabled slows the agent and invites wrong tools.
- Sentry MCP rate limits under load — backoff and narrow time window.
- Kubernetes MCP with admin access by misconfiguration.
- GitHub MCP without time filter returns unhelpful run volume.
- Write MCP enabled while skill still in correlate-only phase.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** MCP minimization during Sev1.
- **Input:** Twelve MCPs enabled; API down.
- **Prompt:**

```text
Whitelist Sentry, GitHub, and k8s readonly; map skill steps; disable others.
```

- **Expected result:**

```text
Active: sentry-mcp, github-mcp, kubernetes-mcp-server (readonly)
Skill steps 1–3 read-only; step 4 blocked until APPROVE
Disabled list recorded in bridge doc with session id
Fallback note: gh CLI if GitHub MCP auth fails
```

### Example 2 (Example data (self-written))

- **Task:** Link deploy to Sentry release spike.
- **Input:** Release `api@2.4.0`, spike 15:10 UTC.
- **Prompt:**

```text
Use MCPs only to link gh run id to sentry issue count; timeline bullet.
```

- **Expected result:**

```text
GitHub MCP: run 20155678 finished 15:08 UTC on main
Sentry MCP: events +340 percent for release api@2.4.0 starting 15:10 UTC
Timeline bullet cites both tool names; no customer email in summary
Correlation hypothesis: deploy within 2 minutes of spike — rollback candidate
```