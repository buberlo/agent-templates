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

## Zweck

Secrets **inventarisieren, rotieren und lagern** — Vault/SOPS/GitHub Secrets — niemals Klartext-Secrets in Repos oder Chats.

## Wann nutzen

- Rotation nach Incident, neuer Integrations-Key.
- Audit: wo liegen Secrets.

**Wann nicht:** Secrets aus Repo in Chat extrahieren zur „Analyse“.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| vault | Store | dynamic secrets |
| sops | Git | encrypted files |
| gh | CI metadata | `gh secret list` |

## System-Prompt / Instruktionen

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

## Arbeitsablauf

1. Inventory: `gh secret list`, `vault kv list secret/` (paths only).
2. Rotation-Ticket anlegen.
3. Neuen Secret in Vault erzeugen — Wert nur in Vault UI/secure channel.
4. Consumer-Apps konfigurieren (dual-key window).
5. Alten Secret revoke nach Bestätigung.
6. `gitleaks detect` auf Repo für Leaks.
7. Audit-Log-Eintrag mit Ticket.

## Qualitätskriterien / Definition of Done

- [ ] Kein Secret-Wert im Chat/PR
- [ ] Rotation dokumentiert mit Ticket
- [ ] Leak-Scan ausgeführt oder geplant

## Sicherheit & Freigaben

- **high risk** bei Prod-Secrets.
- Break-glass nur mit Zwei-Personen-Regel.

## Fallstricke

- vault kv get in Chat kopiert.
- Rotation ohne Consumer-Update — Ausfall.
- sops age key auf Laptop verloren.
- gh secret set überschreibt still.
- Historischer Git-Leak bleibt nach Rotation.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Inventory GitHub Actions.
- **Input:** org repo api.
- **Prompt:**

```text
gh secret list names only; suggest rotation schedule; no values.
```

- **Erwartetes Ergebnis:**

```bash
gh secret list
# PROD_DATABASE_URL (updated 2026-01-12) — rotate Q1 ticket
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** SOPS file add key path.
- **Input:** secrets.enc.yaml.
- **Prompt:**

```text
Document sops edit workflow; never decrypt to chat.
```

- **Erwartetes Ergebnis:**

```bash
sops secrets.enc.yaml   # local edit only
sops -e secrets.enc.yaml | head -5   # still encrypted in output
```