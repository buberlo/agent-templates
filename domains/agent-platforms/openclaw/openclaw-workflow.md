---
id: openclaw-workflow
title: "OpenClaw"
domain: agent-platforms
category: openclaw
tags:
  - openclaw
  - agent-platforms
  - agent-platform
target_agents:
  - openclaw
  - generic-mcp-agents
required_tools:
  - name: OpenClaw
    install: "https://github.com/openclaw/openclaw"
    version_notes: "Gateway CLI: skills, mcp, plugins, channels."
  - name: ClawHub
    install: "https://docs.openclaw.ai/clawhub"
    version_notes: "Registry install; verify before production."
  - name: OpenClaw skills
    install: "https://docs.openclaw.ai/skills/"
    version_notes: "Workspace skills, workshop, `.clawhub` metadata."
inputs:
  - "Running gateway or fresh install path"
  - "Skill IDs and MCP definitions for the task"
outputs:
  - "Gateway configured with documented tool policy"
  - "Verify log for each ClawHub skill used"
risk_level: high
example_count: 2
version: "1.1.0"
updated: "2026-11-24"
---

## Purpose

Operate **OpenClaw** as a self-hosted **gateway** for skills, plugins, MCP, and channels. Use ClawHub for community skills only after **`openclaw skills verify`**, keep workspace skills auditable, and align MCP with tool policy ([OpenClaw docs](https://docs.openclaw.ai/), [skills](https://docs.openclaw.ai/skills/)).

## When to use

- You need local control of channels, Android companion pairing, and tool restrictions.
- Team procedures live in workspace skills with semver and optional skill workshop review.
- External coding clients connect through `openclaw mcp serve` under a strict policy.

### When not to use

- You intend to mass-install leaderboard skills without verify or security review.
- You rely on the Android companion as the gateway host instead of pairing to a server.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| OpenClaw gateway | Host | Skills, MCP, plugins, messaging channels |
| ClawHub registry | Skill distribution | `openclaw skills install @owner/skill` |
| Skill Workshop | New procedures | Proposal flow before publish |
| Tool policy + `mcp.servers` | Least privilege | Restrict risky MCP tools |
| Android companion | Client | QR pairing to existing gateway |

## System prompt

```text
You configure and operate an OpenClaw gateway for the team described in the briefing.
You run `openclaw skills verify` on every ClawHub skill before install and you store the verify output with the deployment record.
You prefer workspace-authored skills for critical workflows and treat ClawHub installs as optional accelerators after review.
You register MCP servers in `mcp.servers` and align tool policy so send, pay, deploy, and delete tools need human release.
You respect skill loading order where workspace definitions override bundled skills with the same name and you document which version won.
You keep secrets out of skill install arguments, chat transcripts, and committed gateway exports.
You pair the Android companion only to an already-secured gateway host via QR; you do not treat the phone app as the authoritative gateway process.
You monitor `maxSkillsPromptChars` and shorten skill summaries when prompt budget truncates core steps.
You verify document outputs by re-reading files and rendering PDF or PNG when the skill chain requires it.
You produce a production readiness checklist covering verify logs, MCP list, policy, and approval gates before go-live tasks.
```

## Workflow

1. Start gateway; record workspace path and CLI version.
2. Collect ClawHub skill IDs; verify each; archive results.
3. Install only verified skills; reject or fork on WARN per security policy.
4. Configure MCP via CLI or settings; tighten write tools.
5. Use Skill Workshop when creating new team procedures.
6. Pair Android companion to the live gateway (not as host replacement).
7. Pilot task with minimal skill set; check prompt length.
8. Production traffic only after write/send approvals are documented.

## Definition of done

- [ ] Every ClawHub skill has verify output before activation
- [ ] Tool policy matches briefing and active MCP list
- [ ] Metadata uses `.clawhub` conventions documented in current docs
- [ ] Write or send actions occurred only with approval

## Security

- Registry skills carry higher risk—verify and prefer workspace forks for sensitive flows.
- Workspace overrides can silently change behavior—audit name collisions.
- Destructive gateway tools require named human approval in the channel policy.

## Pitfalls

- Blind ClawHub install from leaderboard hype bypasses verify and invites malicious skill code.
- Legacy `.clawdhub` metadata is ignored—migrations fail quietly.
- Truncated skill prompts drop approval steps when `maxSkillsPromptChars` is too low.
- Companion app confusion leads to exposing gateway admin on an unmanaged device.
- Too many MCP servers on the gateway mirrors context pressure seen on other agent clients.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Production triage skill with no auto-write.
- **Input:** `clawhub:@team/linear-triage`; linear MCP in `mcp.servers`.
- **Prompt:**

```text
Verify triage skill, list open issues, draft summary. Block comment and create tools.
```

- **Expected result:**

```text
verify: PASS
8 issues listed in markdown table
create_comment blocked by policy (log entry)
No POST to Linear executed
Checklist: reads only ✓
```

### Example 2 (Example data (self-written))

- **Task:** Workspace overrides bundled skill name.
- **Input:** Same skill name in workspace and bundled with different instructions.
- **Prompt:**

```text
Run github PR summary skill for org/example PR #12.
```

- **Expected result:**

```text
Workspace skill instructions used (loading order documented)
Bundled variant not referenced in execution log
PR summary follows workspace template (3 sections)
DoD note: document override in team runbook
```