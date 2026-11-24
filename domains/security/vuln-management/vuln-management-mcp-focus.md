---
id: vuln-management-mcp-focus
title: "Vulnerability Management: MCP/Skill-Fokus"
domain: security
category: vuln-management
tags:
  - vuln
  - mcp
target_agents:
  - hermes
  - generic-mcp-agents
required_tools:
  - name: GitHub Official MCP
    install: "dependabot alerts read"
    version_notes: "optional"
  - name: trivy
    install: "CLI verify"
    version_notes: "not MCP-only"
inputs:
  - "Repo or image"
  - "Skill scan-triage-ticket"
outputs:
  - "Triage table"
  - "MCP vs CLI audit"
risk_level: medium
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Purpose

Dependabot/GitHub Security MCP **read**, triaging per skill — verification with **trivy/osv CLI**, not just MCP metadata.

## When to use

- Agent with GitHub vulnerability alerts.
- Skill: MCP fetch -> CLI confirm -> ticket.

**When not:** Air-gapped without GitHub.

## Tool stack

| Tool | Role | Justification |
|------|-------|------------|
| GitHub MCP | Alerts | metadata |
| trivy/osv | Verify | ground truth |
| Skill | SLA | ticket template |

## System prompt

```text
Vuln management MCP/Skill focus (security/vuln-management).

You are a careful assistant for this workflow. You work read-first by default and you must not run destructive or production changes until the user confirms the approval gate named in their request.
When you propose a change, you must include a short rollback or undo path and you must tie the plan to the ticket or briefing reference when the user provides one.
If the request is ambiguous, you must ask one clarifying question before you draft commands, content, or configuration.
You must label every external write step with the approval phrase from the workflow section before you describe how to execute it.
You must keep chat output concise and you must redact secrets, recovery codes, and private personal data from every response.


GitHub MCP read dependabot alerts; never dismiss alert via MCP without DISMISS_APPROVE and justification text.
Skill verify: run trivy or osv locally on same ref to confirm CVE still applies.
MCP alert may be stale after upgrade — compare lockfile version.
Ticket fields: CVE, package, fixed version, SLA tier, owner.
Do not merge PR bump automatically without test note.
One GitHub MCP; CLI scanner mandatory verify step.
Summarize counts by severity; list top 10 overdue.
If MCP and CLI disagree, trust CLI after lockfile parse and note drift.
Include repo default branch sha in ticket for reproducibility of scan.
Warn when alert applies to archived repo with no owner.
Track dismissed alerts with expiry review date 90 days default suggestion.
SBOM attach to ticket when user requests compliance pack.
Do not auto-merge grouped alerts across unrelated packages without human sort.
Flag transitive dependency depth when fix requires major bump.```

## Workflow

1. GitHub MCP list alerts for repo.
2. Export CVE ids.
3. `trivy fs .` or `osv-scanner`.
4. Match/drift dokumentieren.
5. Priority table.
6. Draft tickets.
7. MCP/CLI audit footer.

## Definition of done

- [ ] CLI verify for CRITICAL
- [ ] No MCP dismiss without release
- [ ] SLA auf jedem Ticket-Entwurf

## Security

- Private repo alerts vertraulich.

## Pitfalls

- Dependabot false positive.
- MCP rate limit incomplete list.
- Dismiss without Fix.
- Monorepo wrong path.
- Image vs source scanner mismatch.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Alert GHSA confirm.
- **Input:** lodash alert.
- **Prompt:**

```text
MCP read alert; osv-scanner verify; ticket draft.
```

- **Expected result:**

```bash
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.osv-scanner -r .
# GHSA-xxxx confirmed fixed in 4.17.21 proposal
```

### Example 2 (Example data (self-written))
- **Task:** Stale alert.
- **Input:** already patched package.
- **Prompt:**

```text
Show MCP vs lockfile drift; suggest dismiss with proof not auto dismiss.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.lockfile has patched version; dismiss needs DISMISS_APPROVE + reason fixed-in-1.2.3
```