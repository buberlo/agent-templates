---
id: hermes-optional-mcp-sprint-onboarding-v1
title: "Hermes optional MCP sprint onboarding"
domain: agent-platforms
category: hermes
tags:
  - hermes
  - mcp
  - optional-mcps
  - onboarding
target_agents:
  - hermes
  - generic-mcp-agents
required_tools:
  - name: Hermes Agent
    install: "https://github.com/NousResearch/hermes-agent"
    version_notes: "Optional MCP catalogue under optional-mcps/; default off."
  - name: Hermes MCP user guide
    install: "https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp"
    version_notes: "`hermes mcp install`, include/exclude filters."
inputs:
  - "Sprint goal listing external systems (e.g. Linear, GitHub, Grafana)"
  - "Hermes host OS and whether skills declare platforms: [macos] only"
  - "Approval rules for write-capable MCP tools"
outputs:
  - "Minimal MCP set installed for the sprint with include/exclude snapshot"
  - "Thread checklist: tools used, approvals pending, deactivated MCPs after sprint"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-26"
---

## Purpose

Onboard a **Hermes** sprint by installing only the **Nous optional MCP** bundles the sprint needs, keeping default-off posture until each connector is justified ([Hermes repo](https://github.com/NousResearch/hermes-agent), [MCP user guide](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp)).

## When to use

- A new Hermes user wants Linear + GitHub read workflows without enabling the full catalogue.
- Security review demands an inventory before any write MCP is toggled on.
- Sprint ends and MCPs should be deactivated to reduce ambient credential scope.

### When not to use

- You need unaudited community MCPs outside `optional-mcps/`—use separate security review.
- All work happens on macOS-only skills while the host is Linux without checking `platforms` metadata.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| `hermes mcp` / install | Connector lifecycle | Catalogue paths in repo |
| optional-mcps/* | Curated servers | PR-merged integrations |
| Hermes skills | Procedure | Slash commands after MCP enable |
| Codex or Claude Code (optional) | Code delegation | Parent keeps review in Hermes thread |

## System prompt

```text
You onboard Hermes optional MCPs for agent-platforms/hermes using official docs at https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp and catalogue paths under https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps.
You list currently installed MCPs with Hermes CLI before adding any new connector and you install only servers mapped to the sprint systems the user named.
You apply include and exclude filters to trim tool schema noise after each install so the model sees fewer ambiguous tool names per Hermes guidance.
You obtain explicit human approval before enabling MCP tools that create issues, merge pull requests, send messages, or mutate cloud resources.
You verify skills declare platforms compatibility and warn when macOS-only skills are skipped on Linux hosts instead of failing silently.
You delegate coding-heavy tasks to Codex or Claude Code skills when configured, then review diffs in the Hermes parent thread before approving push.
You record one line per external tool call: server id, tool name, read or write, success or error, with tokens redacted.
You plan deactivation steps for MCPs that will not be needed after the sprint and you document credentials left in OS stores.
You never paste API tokens into skill markdown or chat transcripts.
You close with installed MCP inventory, filters applied, pending approvals, and links to each optional-mcp source directory used.
```

## Workflow

1. Run `hermes setup` or open desktop app; capture baseline `hermes mcp` status (expect off).
2. Map sprint artifacts to catalogue folders (linear, grafana, github, etc.).
3. Install one MCP at a time; run a read-only smoke tool (list issues, list repos).
4. Configure include/exclude lists; restart or refresh session if guide requires.
5. Attach the relevant Hermes skill or slash command for the recurring workflow.
6. Execute sprint tasks; log writes and block them until user approves each batch.
7. Before sprint end, export tool log and uninstall or disable MCPs not needed next sprint.
8. Archive checklist in team wiki with paths to optional-mcp source commits.

## Definition of done

- [ ] Installed MCP set matches sprint scope with no extra write connectors
- [ ] Include/exclude filters documented
- [ ] Tool log covers every write attempt with approval state
- [ ] Deactivation or uninstall steps recorded

## Security

- OAuth and PAT material stays in Hermes install cards and OS keychains, not git.
- Treat optional MCP source like dependency code—review diffs when upgrading.
- Shared Hermes hosts need per-user approval for write tools.

## Pitfalls

- Installing every catalogue MCP recreates token bloat and tool-selection errors.
- Skipping platform filters causes missing skills with no user-visible error.
- Leaving Grafana or cloud MCPs enabled after sprint expands blast radius.
- Assuming Hermes MCP paths match Cursor `.cursor/mcp.json` one-to-one—they differ.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Sprint needs Linear read + GitHub PR list only.
- **Input:** Host Linux; no writes this sprint.
- **Prompt:**

```text
hermes mcp install linear and github optional bundles. Read-only smoke tests. Document filters.
```

- **Expected result:**

```text
Installed optional-mcps/linear and github paths from Nous catalogue.
Smoke: linear list issues (limit 5) succeeds; github list pull_requests on org/repo succeeds.
Exclude applied to github merge and linear issue_create tools when supported by CLI filters.
Tool log shows 2 read calls, 0 writes. Pending approvals: none.
```

### Example 2 (Example data (self-written))

- **Task:** Mid-sprint request to enable Grafana for incident review; disable after.
- **Input:** Grafana optional MCP; read dashboards only; deactivate Friday.
- **Prompt:**

```text
Install grafana optional MCP, query one dashboard UID fictitious, schedule disable steps.
```

- **Expected result:**

```text
grafana optional-mcp installed; query_panel or equivalent read succeeds on UID demo-dashboard.
Write tools (if any) remain excluded by filter.
Friday checklist: hermes mcp disable grafana, revoke token in secret store, archive tool log with 14 read calls, 0 writes.
Parent thread notes Codex was not invoked; no repo diffs.
```