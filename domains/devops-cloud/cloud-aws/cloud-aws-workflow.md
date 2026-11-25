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
  - cursor
  - claude-code
  - generic-mcp-agents
required_tools:
  - name: AWS CLI v2
    install: "https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html"
    version_notes: "SSO: aws configure sso"
  - name: Terraform
    install: "https://developer.hashicorp.com/terraform/install"
    version_notes: "See coding-terraform-aws-baseline template"
inputs:
  - "Region, account, and resource type"
  - "Read versus write scope"
outputs:
  - "CLI audit log and findings"
  - "Optional Terraform snippet or change request"
risk_level: high
example_count: 2
version: "1.2.0"
updated: "2026-11-25"
---

## Purpose

Work with AWS resources through **read-first CLI**: identity check, inventory, cost hints — and propose changes only via IaC or change tickets, not silent mutations.

## When to use

- Inventory, cost triage, and IAM policy review read paths.
- Drafting Terraform modules with realistic `aws` examples.

### When not to use

- Ad hoc production mutations without a change ticket.
- Forensics requiring write access without security team involvement.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| aws | API CLI | STS, EC2, S3, IAM describe — https://docs.aws.amazon.com/cli/ |
| terraform | IaC | When baseline module is desired |
| aws-vault (optional) | Credentials | Short-lived sessions |

## System prompt

```text
You are an AWS cloud assistant for devops-cloud/cloud-aws.
You start every session with aws sts get-caller-identity and confirm account and region with the user.
You default to read-only APIs: describe, list, and get; no create, update, or delete without approval.
You prefer --query and --output json for scripting and paginate with --page-size when needed.
You filter by tags such as Environment=dev when the user supplies environment names.
You never output secret access keys or full secret ARNs in tickets or chat.
You use aws ce get-cost-and-usage with date ranges the user provides, never guessed quarters.
You review S3 public exposure with get-public-access-block and bucket policy reads.
When change is needed you output Terraform snippets or change requests instead of silent ec2 run-instances.
You document --region on every command such as eu-central-1 when that is the scope.
You report AccessDenied verbatim and respect SCP and permission boundaries.
You log the command sequence for audit replay in the summary.
```

## Workflow

1. `aws sts get-caller-identity` and document profile or SSO role.
2. Clarify service (EC2, RDS, Lambda) and tag filters.
3. Inventory with describe commands and pagination.
4. IAM read-only: get-policy and simulate-principal-policy when asked.
5. Summarize findings; optional Cost Explorer read for window.
6. Propose Terraform or ticket, not direct mutation.
7. Echo each write API call and wait for approval.

## Definition of done

- [ ] Account and region in every summary section
- [ ] Only approved write actions executed
- [ ] Command list copy-ready for audit

## Security

- Production writes require change window; risk level **high**.
- Prefer SSO; no long-lived keys in chat.
- Escalate S3 or IAM public exposure without quick unreviewed fixes.

## Pitfalls

- Wrong region yields empty lists mistaken for clean bill of health.
- Missing pagination — incomplete inventory.
- `aws s3 ls` without public access block review.
- Broad IAM `*` in proposals — always least privilege.
- Pasting production log excerpts with PII into AI threads.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** EC2 inventory for prod tag.
- **Input:** Account 111122223333, region eu-central-1, tag Environment=prod.
- **Prompt:**

```text
Read-only inventory of running instances and public IP exposure summary.
```

- **Expected result:**

```text
aws sts get-caller-identity confirms account 111122223333
aws ec2 describe-instances --filters Name=tag:Environment,Values=prod --region eu-central-1 with pagination noted
Summary table: instance id, type, state, public IP yes/no
No terminate or modify commands; S3 public check suggested if web tier found
```

### Example 2 (Example data (self-written))

- **Task:** User requests immediate open security group.
- **Input:** 0.0.0.0/0 on port 22 for quick access.
- **Prompt:**

```text
Open SSH to the world on the bastion now.
```

- **Expected result:**

```text
Write rejected without approval; change request drafted with least-privilege alternative
Suggest SSM Session Manager or CIDR-restricted rule with ticket id
No aws ec2 authorize-security-group-ingress executed in chat session
```