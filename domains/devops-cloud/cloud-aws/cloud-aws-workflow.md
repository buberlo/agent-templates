---
id: cloud-aws-workflow
title: "Cloud: AWS"
domain: devops-cloud
category: cloud-aws
tags:
  - aws
  - cloud
  - cli
target_agents:
  - hermes
  - claude-code
  - cursor
  - generic-mcp-agents
required_tools:
  - name: aws-cli
    install: "AWS CLI v2"
    version_notes: "SSO: aws configure sso"
  - name: terraform
    install: "optional für IaC-Tasks"
    version_notes: "Siehe coding-terraform-aws-baseline"
inputs:
  - "Region, Account, Ressourcen-Typ"
  - "Read vs. Write Scope"
outputs:
  - "CLI-Protokoll und Empfehlung"
  - "Optional: Terraform-Modul-Entwurf"
risk_level: high
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

AWS-Ressourcen sicher **lesen**, kostensparend inventarisieren und Änderungen nur über genehmigte IaC- oder Runbook-Pfade vorschlagen.

## Wann nutzen

- Inventar, Kosten-Triage, IAM-Policy-Review (read-mostly).
- Vorbereitung Terraform-Module mit realistischen `aws`-Beispielen.

**Wann nicht:** Ad-hoc-Prod-Änderungen per Einzel-CLI ohne Change-Ticket.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| aws | API-CLI | STS, EC2, S3, IAM describe |
| terraform | IaC | Wenn Baseline gewünscht |
| aws-vault | optional | Kurzlebige Credentials |

## System-Prompt / Instruktionen

```text
AWS cloud workflow (devops-cloud/cloud-aws).

Start every session: aws sts get-caller-identity and confirm account/region.
Default read-only: describe*, list*, get*; no create/update/delete without approval.
Prefer --query and --output json for scripting; paginate with --page-size where needed.

Tag-based filters: filter tag:Environment=dev when user supplies environment.
Never output secret access keys or full ARNs of secrets in public tickets.
For cost: aws ce get-cost-and-usage with date range user provides (not guessed).
For S3 public exposure: s3api get-public-access-block and bucket-policy review read-only.

When change needed: output terraform snippet or change request, not silent aws ec2 run-instances.
Document region in every command (--region eu-central-1).
Respect SCP/permission boundaries; report AccessDenied verbatim.
Log command sequence for audit replay.
```

## Arbeitsablauf

1. `aws sts get-caller-identity` und Profil dokumentieren.
2. Scope klären: Service (EC2, RDS, Lambda) und Tags.
3. Inventar: z. B. `aws ec2 describe-instances --filters "Name=tag:Environment,Values=prod" --region eu-central-1`.
4. Policies: `aws iam get-user-policy` / `simulate-principal-policy` read-only.
5. Befund zusammenfassen; Kosten optional `aws ce get-cost-and-usage`.
6. Änderungsvorschlag als Terraform oder Ticket, nicht direkte Mutation.
7. Freigabe einholen vor jedem write-API-Aufruf.

## Qualitätskriterien / Definition of Done

- [ ] Account und Region in jeder Zusammenfassung
- [ ] Nur genehmigte Schreibaktionen
- [ ] Befehlsliste kopierfertig und redigiert

## Sicherheit & Freigaben

- Prod-Write nur mit Change-Fenster; `risk_level: high`.
- Keine langfristigen Keys im Chat; SSO bevorzugen.
- S3-/IAM-Exposition sofort eskalieren, nicht „schnell fixen“ ohne Review.

## Fallstricke

- Falsche Region — leere Listen statt Fehler.
- Paginierung vergessen — unvollständiges Inventar.
- `aws s3 ls` ohne Public-Block-Check — false sense of safety.
- Broad IAM `*` in Vorschlägen — immer least privilege formulieren.
- Datenübertragung aus Prod-Logs in KI-Thread — DSGVO beachten.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** EC2 in `prod` tag inventarisieren.
- **Input:** Region `eu-central-1`.
- **Prompt:**

```text
List running instances with tag Environment=prod; JSON table; read-only.
```

- **Erwartetes Ergebnis:**

```bash
aws ec2 describe-instances --region eu-central-1 \
  --filters "Name=tag:Environment,Values=prod" "Name=instance-state-name,Values=running" \
  --query 'Reservations[].Instances[].[InstanceId,InstanceType,Tags[?Key==`Name`].Value|[0]]' \
  --output table
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Verdächtige öffentliche S3-Bucket-Policy finden.
- **Input:** Bucket-Liste aus Audit.
- **Prompt:**

```text
Read-only check public access block and bucket policy for bucket logs-archive-prod.
```

- **Erwartetes Ergebnis:**

```bash
aws s3api get-public-access-block --bucket logs-archive-prod
aws s3api get-bucket-policy-status --bucket logs-archive-prod
# IsPublic: false, recommendation documented
```