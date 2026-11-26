---
id: openclaw-clawhub-skill-verify-install-v1
title: "OpenClaw ClawHub verify and install"
domain: agent-platforms
category: openclaw
tags:
  - openclaw
  - clawhub
  - skills
  - supply-chain
target_agents:
  - openclaw
  - generic-mcp-agents
required_tools:
  - name: OpenClaw skills CLI
    install: "https://docs.openclaw.ai/skills/"
    version_notes: "`openclaw skills verify`, install from ClawHub."
  - name: ClawHub
    install: "https://docs.openclaw.ai/clawhub"
    version_notes: "Community registry; review before production."
  - name: OpenClaw tool policy
    install: "https://docs.openclaw.ai/tools/mcp"
    version_notes: "Restrict MCP tools after skill install."
inputs:
  - "Target skill coordinates (@owner/skill-name) and business justification"
  - "Gateway version and workspace path for skill install"
  - "Tool policy template (blocked commands, allowed channels)"
outputs:
  - "Verify log for each candidate skill before install"
  - "Post-install tool policy diff and rollback uninstall command"
risk_level: high
example_count: 2
version: "1.0.0"
updated: "2026-11-26"
---

## Purpose

Install **ClawHub** skills into an **OpenClaw** gateway only after **`openclaw skills verify`**, then tighten **tool policy** so new skills cannot expand MCP blast radius without review ([OpenClaw skills](https://docs.openclaw.ai/skills/), [ClawHub](https://docs.openclaw.ai/clawhub)). Public research has reported malicious skills on registries—treat verify as necessary, not sufficient.

See also: `domains/agent-platforms/openclaw/assets/example-clawhub-verify-flow.svg` (example data).

## When to use

- Operators want a community skill for a channel workflow but security requires verify-first workflow.
- You bridge external MCP clients through the gateway and need documented policy after skill install.
- Skill Workshop proposals are not ready but a reviewed ClawHub skill is acceptable short term.

### When not to use

- Production gateways serving customer PII without a human security review of skill source.
- Rank-only ClawHub leaderboard installs with no verify step (see supply-chain reporting such as [ClawHub-Audit coverage](https://thehackernews.com/2026/02/researchers-find-341-malicious-clawhub.html)).

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| `openclaw skills verify` | Supply-chain gate | Pre-install checks per OpenClaw docs |
| `openclaw skills install` | Deployment | Pulls from ClawHub registry |
| Tool policy + `mcp.servers` | Containment | Least privilege after install |
| Skill Workshop (optional) | Long-term | Internal skills replace unverified ones |

## System prompt

```text
You install OpenClaw skills for agent-platforms/openclaw only through verify-then-install workflow documented at https://docs.openclaw.ai/skills/ and https://docs.openclaw.ai/clawhub.
You run openclaw skills verify on each candidate @owner/skill coordinate before install and you abort when verify reports failures or unsigned changes the user has not accepted.
You read skill metadata and source paths exposed by verify output and you flag network calls, shell execution, or credential access the skill requests.
You install only after explicit INSTALL_APPROVED token from the user for that skill id and version.
You update gateway tool policy and mcp.servers restrictions immediately after install so new tools cannot invoke blocked MCP endpoints the user listed.
You document uninstall commands and workspace paths touched so rollback is one command during incidents.
You avoid mass-installing leaderboard skills; one skill per change request with verify logs attached.
You reference third-party security research on registry poisoning only as risk context, not as a substitute for local verify output.
You never store channel tokens or clawhub credentials in skill markdown committed to git.
You finish with verify transcript, install receipt, policy diff summary, and monitoring steps for the first 24 hours after enablement.
```

## Workflow

1. Confirm gateway health and backup workspace skills directory.
2. Search ClawHub for skill; record owner, version, and stated capabilities.
3. Run `openclaw skills verify @owner/skill`; capture stdout/stderr to secure log.
4. Human reviews verify output and source; grants INSTALL_APPROVED.
5. Run `openclaw skills install @owner/skill`; confirm only expected files land in workspace.
6. Tighten tool policy: block payment, deploy, and filesystem escape patterns per OpenClaw MCP docs.
7. Smoke-test skill in isolated channel or sandbox user account.
8. Document uninstall path and schedule review to replace with Skill Workshop version if needed.

## Definition of done

- [ ] Verify log archived for each installed skill
- [ ] INSTALL_APPROVED recorded with skill id and version
- [ ] Tool policy updated and diff reviewed
- [ ] Uninstall command tested in dry-run or staging gateway

## Security

- High risk category: compromised skills equal RCE on gateway host—run on hardened VMs.
- Separate production and experimental gateways; never test unknown skills on production channels.
- Review Palo Alto Networks and independent reports on skill poisoning alongside verify output.

## Pitfalls

- Verify passing does not guarantee benevolent updates on next semver—pin versions and re-verify upgrades.
- Skills requesting broad MCP access defeat least-privilege—narrow `mcp.servers` after install.
- Android companion pairing is not a substitute for gateway-side policy.
- OpenClaw `mcp serve` exposes tools to external clients—do not widen serve ACL when adding skills.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Install fictional `@acme/slack-digest` after verify on staging gateway.
- **Input:** Staging only; block shell MCP tools; INSTALL_APPROVED for acme/slack-digest v1.2.0.
- **Prompt:**

```text
Verify and install @acme/slack-digest on staging. Update tool policy to read-only Slack MCP. Attach verify log summary.
```

- **Expected result:**

```text
verify @acme/slack-digest → exit 0, notes: no unsigned scripts, network to slack.com only.
install completes; workspace lists skill digest skill in skills manifest.
Tool policy diff: shell and payment MCP denied; slack read channels allowed.
Smoke: skill produces digest text in test channel without sending DMs.
Uninstall documented: openclaw skills remove @acme/slack-digest.
```

### Example 2 (Example data (self-written))

- **Task:** Reject skill when verify fails checksum step.
- **Input:** Candidate `@unknown/auto-trader` from leaderboard; no approval.
- **Prompt:**

```text
Run verify only; do not install. Explain rollback if partial files existed.
```

- **Expected result:**

```text
verify @unknown/auto-trader → failure reason checksum mismatch on hooks/install.sh.
Install not run; INSTALL_APPROVED absent.
User advised to use Skill Workshop internal template instead of ClawHub entry.
Incident note links OpenClaw docs and supply-chain article; no production impact.
```