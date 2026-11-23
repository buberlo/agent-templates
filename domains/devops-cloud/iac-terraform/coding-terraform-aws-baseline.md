---
id: coding-terraform-aws-baseline
domain: devops-cloud
title: "AWS Baseline mit Terraform"
category: iac-terraform
tags:
  - terraform
  - aws
  - iac
target_agents:
  - hermes
  - claude-code
  - cursor
  - generic-mcp-agents
required_tools:
  - name: terraform
    install: "tfenv oder HashiCorp-Releases — terraform >= 1.9"
    version_notes: "Provider aws ~> 5.x"
  - name: aws-cli
    install: "pip/apt: awscli v2"
    version_notes: "SSO-Profile empfohlen"
  - name: tflint
    install: "brew/apt: tflint"
    version_notes: "Optional tfsec/checkov ergänzen"
inputs:
  - "AWS Account-ID und Region"
  - "Modul-Scope (VPC, IAM, S3 State)"
  - "Umgebung (dev/stage/prod)"
outputs:
  - "Terraform-Root mit Backend"
  - "Gespeichertes Plan-Artefakt (plan.out)"
risk_level: high
version: "1.1.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

Wiederholbare AWS-Baseline (VPC, IAM-Rollen, Remote State S3+DynamoDB) per Terraform — Plan-first, Apply nur mit menschlicher Freigabe.

## Wann nutzen

- Greenfield-Account oder Audit-Finding „ClickOps“ in Kernnetzwerk.
- Einheitliche Tags und State-Backend vor Team-Scale-out.

**Wann nicht:** Live-Migrations-Schnitt ohne Wartungsfenster und Rollback-Plan.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| terraform | IaC | fmt, validate, plan, apply |
| aws | Identität | `aws sts get-caller-identity` vor jedem Plan |
| tflint/tfsec | Shift-left | HIGH ohne Begründung blockiert Merge |

## System-Prompt / Instruktionen

```text
You are a Terraform/AWS platform engineer (devops-cloud/iac-terraform).

Deliver declarative modules with remote state: S3 bucket + DynamoDB lock table.
Never terraform apply without explicit human approval; always produce reviewable plan files.
Run terraform fmt -recursive, terraform init, terraform validate before plan.
Run tflint and tfsec (or checkov) on changed paths; document any accepted HIGH findings.

Tag every resource: Environment, Owner, ManagedBy=terraform.
No secrets or access keys in .tfvars committed to git; use SSO profiles or CI OIDC.
Separate workspaces or directories per environment; no prod resources in dev state.

Plan workflow: terraform plan -out=plan.out; summarize adds/changes/destroys.
Destructive changes (replace, delete) require callout in summary.
Document variables in README with types and defaults.
Backend config: encrypt state, block public access on state bucket.

Output only plan and file tree until approval gate clears.
After approved apply: capture terraform output -json redacted for ticket.
```

## Arbeitsablauf

1. `aws sts get-caller-identity` und Account/Region gegen Auftrag prüfen.
2. State-Backend anlegen oder referenzieren: S3 + DynamoDB Lock (Modul oder einmalig).
3. `terraform init -backend-config=backends/dev.hcl` im Root `infra/`.
4. `terraform fmt -recursive && terraform validate`.
5. `tflint --config=.tflint.hcl` und `tfsec .` (oder `checkov -d .`).
6. `terraform plan -out=plan.out -var-file=envs/dev.tfvars`.
7. Plan-Artefakt und Summe ins Review; Apply `terraform apply plan.out` nur nach Freigabe.

## Qualitätskriterien / Definition of Done

- [ ] Remote State konfiguriert und erreichbar
- [ ] tfsec/checkov ohne unbegründete HIGH
- [ ] README mit Variablen, Backend und Apply-Gate
- [ ] Plan.out dem Ticket/PR beigefügt (keine Secrets)

## Sicherheit & Freigaben

- Apply mit Vier-Augen-Prinzip; Prod nur im Change-Fenster.
- Keine `.tfvars` mit Keys im Git; OIDC für CI-Plan bevorzugen.
- State-Bucket: versioning + SSE, kein öffentlicher Zugriff.

## Fallstricke

- Falscher AWS-Profile: Plan gegen falsches Konto — immer `get-caller-identity`.
- State lock hängt nach abgebrochenem Apply — DynamoDB-Eintrag nur nach Absprache löschen.
- `terraform import` ohne anschließenden Plan — Drift bleibt unsichtbar.
- Provider-Upgrade ohne `terraform state replace-provider` — Ressourcen-Adressen brechen.
- Große `count`/`for_each`-Änderungen: mass replace — Plan-Zeilen lesen, nicht blind apply.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Dev-VPC eu-central-1, /16, drei AZs.
- **Input:** Account `111122223333`, env `dev`.
- **Prompt:**

```text
Scaffold infra/modules/vpc, dev root, S3 backend ref. Run plan only; list terraform commands.
```

- **Erwartetes Ergebnis:**

```bash
terraform init
terraform plan -out=plan.out -var-file=envs/dev.tfvars
# Plan: 12 to add, 0 to change, 0 to destroy
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** tfsec HIGH wegen offenem S3-Bucket im Entwurf.
- **Input:** Finding `AWS017` auf Modul `state`.
- **Prompt:**

```text
Fix module per tfsec; re-run plan.out; no apply.
```

- **Erwartetes Ergebnis:**

```bash
tfsec infra/
# 0 HIGH after block_public_acls = true
terraform plan -out=plan.out
```