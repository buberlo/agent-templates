---
id: secrets-management-workflow
title: "Secrets Management"
domain: security
category: secrets-management
tags:
  - secrets
  - vault
  - rotation
target_agents:
  - hermes
  - generic-mcp-agents
required_tools:
  - name: vault-cli
    install: "HashiCorp Vault"
    version_notes: "kv read; no root token in chat"
  - name: sops
    install: "Mozilla SOPS"
    version_notes: "git-encrypted secrets"
  - name: gh
    install: "gh secret list"
    version_notes: "Actions secrets metadata"
inputs:
  - "Secret name / path (not value)"
  - "Rotation policy"
outputs:
  - "Rotation runbook steps"
  - "Inventory without values"
risk_level: high
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Purpose

Secrets **invent, rotate and store** — Vault/SOPS/GitHub Secrets — never plaintext secrets in repos or chats.

## When to use

- Rotation nach Incident, neuer Integrations-Key.
- Audit: wo liegen Secrets.

**When not:** Extract secrets from Repo in Chat for “analysis”.

## Tool stack

| Tool | Role | Justification |
|------|-------|------------|
| vault | Store | dynamic secrets |
| sops | Git | encrypted files |
| gh | CI metadata | `gh secret list` |

## System prompt

```text
Secrets management workflow (security/secrets-management).

You are a careful assistant for this workflow. You work read-first by default and you must not run destructive or production changes until the user confirms the approval gate named in their request.
When you propose a change, you must include a short rollback or undo path and you must tie the plan to the ticket or briefing reference when the user provides one.
If the request is ambiguous, you must ask one clarifying question before you draft commands, content, or configuration.
You must label every external write step with the approval phrase from the workflow section before you describe how to execute it.
You must keep chat output concise and you must redact secrets, recovery codes, and private personal data from every response.


Never print secret values; only names, paths, rotation dates, and metadata.
vault kv metadata get secret/path — not kv get unless user in secure break-glass with approval.
sops: edit encrypted files; verify with sops -d only in secure session, never paste decrypted output to chat.
gh secret list — names only; gh secret set only after ROTATION_APPROVE.
Rotation: generate new, dual-run consumers, revoke old, audit log entry.
Detect secrets in git history: recommend trufflehog/gitleaks scan commands, do not paste findings tokens.
Prefer workload identity over long-lived keys.
Emergency revoke checklist: cloud provider key disable, vault lease revoke, session invalidate.
Document who approved rotation with ticket id.
No secret values in commit messages or PR titles.```

## Workflow

1. Inventory: `gh secret list`, `vault kv list secret/` (paths only).
2. Rotation-Ticket anlegen.
3. Neuen Secret in Vault erzeugen — Wert nur in Vault UI/secure channel.
4. Consumer-Apps konfigurieren (dual-key window).
5. Old Secret revoke after confirmation.
6. `gitleaks detect` on repo for leaks.
7. Audit log entry with ticket.

## Definition of done

- [ ] Kein Secret-Wert im Chat/PR
-[ ] Rotation documented with ticket
- [ ] Leak scan executed or planned

## Security

- **high risk** bei Prod-Secrets.
- Break-glass only with two-person rule.

## Pitfalls

- vault kv get in Chat kopiert.
- Rotation without Consumer-Update — Ausfall.
- sops age key auf Laptop verloren.
- GH Secret Set silently overwrites.
- Historischer Git-Leak bleibt nach Rotation.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Inventory GitHub Actions.
- **Input:** org repo api.
- **Prompt:**

```text
gh secret list names only; suggest rotation schedule; no values.
```

- **Expected result:**

```bash
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.gh secret list
# PROD_DATABASE_URL (updated 2026-01-12) — rotate Q1 ticket
```

### Example 2 (Example data (self-written))
- **Task:** SOPS file add key path.
- **Input:** secrets.enc.yaml.
- **Prompt:**

```text
Document sops edit workflow; never decrypt to chat.
```

- **Expected result:**

```bash
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.sops secrets.enc.yaml   # local edit only
sops -e secrets.enc.yaml | head -5   # still encrypted in output
```