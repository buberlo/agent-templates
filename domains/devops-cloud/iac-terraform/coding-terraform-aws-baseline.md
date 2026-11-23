---
id: coding-terraform-aws-baseline
title: "AWS Baseline with Terraform"
domain: devops-cloud
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
    install: "tfenv or HashiCorp-Releases — terraform >= 1.9"
    version_notes: "Provider aws ~> 5.x"
  - name: aws-cli
    install: "pip/apt: awscli v2"
    version_notes: "SSO-Profile empfohlen"
  - name: tflint
    install: "brew/apt: tflint"
    version_notes: "Optionally add tfsec/checkov"
inputs:
  - "AWS Account ID and Region"
  - "Modul-Scope (VPC, IAM, S3 State)"
  - "Umgebung (dev/stage/prod)"
outputs:
  - "Terraform root with backend"
  - "Gespeichertes Plan-Artefakt (plan.out)"
risk_level: high
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

Repeatable AWS baseline (VPC, IAM roles, Remote State S3+DynamoDB) per Terraform — Plan-first, Apply only with human approval.

## When to use

- Greenfield-Account or Audit-Finding „ClickOps“ in Kernnetzwerk.
- Uniform tags and state backend before team scale-out.

When, not to use: Live migration cut without maintenance window and rollback plan.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| terraform | IaC | fmt, validate, plan, apply |
| aws | identity | `aws sts get-caller-identity` before any plan |
| tflint/tfsec | Shift-left | HIGH without justification blocks Merge |

## System prompt

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

## Workflow

1. `aws sts get-caller-identity` and check account/region against order.
2. State-Backend anlegen or referenzieren: S3 + DynamoDB Lock (Modul or einmalig).
3. `terraform init -backend-config=backends/dev.hcl` im Root `infra/`.
4. `terraform fmt -recursive && terraform validate`.
5. `tflint --config=.tflint.hcl` and `tfsec .` (or `checkov -d .`).
6. `terraform plan -out=plan.out -var-file=envs/dev.tfvars`.
7. Plan artifact and sum in the review; Apply `terraform apply plan.out` only after approval.

## Definition of done

- [ ] Remote State configured and accessible
- [ ] tfsec/ item checkov without unfounded HIGH
- [ ] README with variables, backend and apply gate
- [ ] Plan.out attached to the ticket/PR (no secrets)

## Security

- Apply with four-eyes principle; Prod only in the change window.
- No `.tfvars` with keys in the git; prefer OIDC for CI plan.
- State-Bucket: versioning + SSE, no public access.

## Pitfalls

- Falscher AWS-Profile: Plan gegen falsches Konto — immer `get-caller-identity`.
- State lock depends on canceled Apply - only delete DynamoDB entry by appointment.
- `terraform import` without subsequent plan — drift remains invisible.
- Provider-Upgrade without `terraform state replace-provider` — Ressourcen-Adressen brechen.
- Great 'count'/'for'each': mass re-read — plan, not blindly apply.

## Basic examples

### Example 1 (Example data)

- **Task:** Dev-VPC eu-central-1, /16, drei AZs.
- **Input:** Account `111122223333`, env `dev`.
- **Prompt:**

```text
Scaffold infra/modules/vpc, dev root, S3 backend ref. Run plan only; list terraform commands.
```

- **Expected result:**

```bash
terraform init
terraform plan -out=plan.out -var-file=envs/dev.tfvars
# Plan: 12 to add, 0 to change, 0 to destroy
```

### Example 2 (Example data)

- **Task:** tfsec HIGH wegen offenem S3-Bucket im Entwurf.
- **Input:** Finding `AWS017` auf Modul `state`.
- **Prompt:**

```text
Fix module per tfsec; re-run plan.out; no apply.
```

- **Expected result:**

```bash
tfsec infra/
# 0 HIGH after block_public_acls = true
terraform plan -out=plan.out
```