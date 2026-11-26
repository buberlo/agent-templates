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

- Rotation after incident, new integration key.
- Audit: where secrets are stored.

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

Never print secret values; only names, paths, rotation dates, and metadata.
vault kv metadata get secret/path — not kv get unless user in secure break-glass with approval.
sops: edit encrypted files; verify with sops -d only in secure session, never paste decrypted output to chat.
gh secret list — names only; gh secret set only after ROTATION_APPROVE.
Rotation: generate new, dual-run consumers, revoke old, audit log entry.
Detect secrets in git history: recommend trufflehog/gitleaks scan commands, do not paste findings tokens.
Prefer workload identity over long-lived keys.
Emergency revoke checklist: cloud provider key disable, vault lease revoke, session invalidate.
Document who approved rotation with ticket id.
No secret values in commit messages or PR titles.
```

## Workflow

1. Inventory: `gh secret list`, `vault kv list secret/` (paths only).
2. Create rotation ticket.
3. Create new secret in Vault — value only in Vault UI/secure channel.
4. Consumer-Apps konfigurieren (dual-key window).
5. Old Secret revoke after confirmation.
6. `gitleaks detect` on repo for leaks.
7. Audit log entry with ticket.

## Definition of done

- [ ] No secret value in chat/PR
-[ ] Rotation documented with ticket
- [ ] Leak scan executed or planned

## Security

- **high risk** for prod secrets.
- Break-glass only with two-person rule.

## Pitfalls

- vault kv get in Chat kopiert.
- Rotation without Consumer-Update — Ausfall.
- sops age key auf Laptop verloren.
- GH Secret Set silently overwrites.
- Historical Git leak remains after rotation.

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
gh secret list
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
sops secrets.enc.yaml   # local edit only
sops -e secrets.enc.yaml | head -5   # still encrypted in output
```