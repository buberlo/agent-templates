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
  - generic
required_tools:
  - name: terraform
    install: "tfenv/apt: terraform"
    version_notes: ">= 1.9"
  - name: aws-cli
    install: "pip/apt: awscli"
    version_notes: "Profile via SSO"
inputs:
  - "Account-ID"
  - "Region"
  - "Modul-Scope (VPC/S3)"
outputs:
  - "Terraform Root"
  - "Plan-Artefakt"
risk_level: high
version: "1.0.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

Wiederholbare AWS-Baseline (VPC, IAM-Rollen, Remote State) per IaC bereitstellen.

## Wann nutzen

- Greenfield Account, Audit-Finding "ClickOps".
- Nicht für Live-Migration ohne Wartungsfenster.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Terraform | IaC | Deklarativ, planbar |
| AWS provider | Ressourcen | Offiziell |
| tflint/tfsec | Lint/Security | Shift-left |

## System-Prompt / Instruktionen

```text
Terraform AWS modules with remote S3+DynamoDB state.
Run fmt, validate, tfsec before any apply suggestion.
Never apply without human approval; output plan only.
Tag all resources: Environment, Owner, ManagedBy=terraform.
```

## Arbeitsablauf

1. Backend-Bucket und Lock-Tabelle.
2. Module VPC + Subnets dokumentieren.
3. `terraform plan` speichern.
4. Peer Review des Plans.
5. Apply nur nach Freigabe.

## Qualitätskriterien / Definition of Done

- [ ] Remote State konfiguriert
- [ ] tfsec keine HIGH ohne Begründung
- [ ] README mit Variablen

## Sicherheit & Freigaben

- Apply nur mit 4-Augen-Prinzip.
- Keine Keys in tfvars im Git.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

_Siehe vorheriger Abschnitt; bei Migration ergänzt._

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Validierung
- **Input:** n/a
- **Prompt:** `validate output`
- **Erwartetes Ergebnis:** OK

## Beispiele (Legacy)

**Eingabe:** Dev-Account eu-central-1, kleines VPC
**Erwartetes Ergebnis:** `plan.out`, Modulstruktur unter `infra/`
