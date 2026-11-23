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
    install: "https://www.terraform.io/downloads"
    version_notes: "See coding-terraform-aws-baseline"
inputs:
  - "Region, Account, resource type"
  - "Read vs. Write Scope"
outputs:
  - "CLI protocol and recommendation"
  - "Optional: Terraform-module draft"
risk_level: high
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---
## Purpose

AWS resources securely **read**, inventory cost-effectively, and suggest changes only through approved IaC or Runbook paths.

## When to use

- Inventory, cost triage, IAM-IAM policy review (read-mostly).
- Preparation of Terraform modules with realistic `aws` examples.

**When not:** Ad hoc Prod changes by single CLI without change ticket.

## Tool stack

| Tool | Role | Justification |
|------|-------|------------|
| aws | API-CLI | STS, EC2, S3, IAM describe |
| terraform | IaC | If baseline desired |
| aws-vault | optional | Kurzlebige Credentials |

## System prompt

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

## Workflow

1. `aws sts get-caller-identity` and document profile.
2. Scope clarification: Service (EC2, RDS, Lambda) and tags.
3. Inventory: z. B. `aws ec2 describe-instances --filters "Name=tag:Environment,Values=prod" --region eu-central-1`.
4. Policies: `aws iam get-user-policy` / `simulate-principal-policy` read-only.
5. Befund zusammenfassen; Kosten optional `aws ce get-cost-and-usage`.
6. Change proposal as terraform or ticket, not direct mutation.
7. Sharing before each write API call.

## Definition of done / Definition of Done

- [ ] Account and region in each summary
- [ ] Nur genehmigte Schreibaktionen
- [ ] command list ready to be copied and edited

## Security

Prod-Write only with change window; Risk level: high.
- No langfristigen Keys im Chat; SSO bevorzugen.
- S3/IAM exposure escalate immediately, not “fix quickly” without review.

## Pitfalls

- Falsche Region — leere Listen statt Fehler.
- Forget pagination - incomplete inventory.
- `aws s3 ls` without Public-Block-Check — false sense of safety.
- Broad IAM `*` in proposals - always formulate least privilege.
Data transmission from Prod logs in AI thread — observe GDPR.

## Basic examples

### Example 1 (Example data)

- **Task:** EC2 in `prod` tag inventarisieren.
- **Input:** Region `eu-central-1`.
- **Prompt:**

```text
List running instances with tag Environment=prod; JSON table; read-only.
```

- **Expected result:**

```bash
aws ec2 describe-instances --region eu-central-1 \
  --filters "Name=tag:Environment,Values=prod" "Name=instance-state-name,Values=running" \
  --query 'Reservations[].Instances[].[InstanceId,InstanceType,Tags[?Key==`Name`].Value|[0]]' \
  --output table
```

### Example 2 (Example data)

- **Task:** Find suspected public S3 bucket policy.
- **Input:** Bucket-Liste aus Audit.
- **Prompt:**

```text
Read-only check public access block and bucket policy for bucket logs-archive-prod.
```

- **Expected result:**

```bash
aws s3api get-public-access-block --bucket logs-archive-prod
aws s3api get-bucket-policy-status --bucket logs-archive-prod
# IsPublic: false, recommendation documented
```