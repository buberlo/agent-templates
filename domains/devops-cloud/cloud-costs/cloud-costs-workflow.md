---
id: cloud-costs-workflow
title: "Cloud costs"
domain: devops-cloud
category: cloud-costs
tags:
  - finops
  - cost
  - cloud
target_agents:
  - hermes
  - claude-code
  - cursor
  - generic-mcp-agents
required_tools:
  - name: aws-cli
    install: "AWS CE API via aws ce"
    version_notes: "Cost Explorer Berechtigung"
  - name: az
    install: "Azure Cost Management REST/az costmanagement"
    version_notes: "Reader auf Subscription"
  - name: infracost
    install: "https://www.infracost.io/docs/"
    version_notes: "Estimate Terraform plan cost"
inputs:
  - "Cloud account(s), time range, tag filters"
  - "Threshold for anomaly"
outputs:
  - "Cost report (CSV/table)"
  - "Top 10 resources plus recommendations"
risk_level: medium
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Purpose

Analyze cloud spend, highlight anomalies and **rightsizing**/reserve recommendations without deleting resources.

## When to use

- Monthly FinOps review, sudden increase in costs.
- Before Terraform apply: Infracost on plan.

**When not:** Contract negotiation without CFO clearance.

## Tool stack

| Tool | Role | Justification |
|------|-------|------------|
| aws ce | AWS Kosten | get-cost-and-usage |
| infracost | IaC estimation | PR commentable |
| kubecost | optional GKE/EKS | Allocation |

## System prompt

```text
FinOps workflow (devops-cloud/cloud-kosten).

Read-only cost APIs only unless user explicitly approves resource stop/delete recommendations as tickets.
AWS: aws ce get-cost-and-usage with Granularity=MONTHLY and GroupBy SERVICE or TAG.
Date range always ISO from user; never invent future months.
Azure: az costmanagement query or REST with scope /subscriptions/<id>.

Summarize: total, delta vs prior period, top 5 services, top 5 untagged resources.
Flag idle resources from metrics (CPU<5% 14d) as candidates, not auto-actions.
Infracost: infracost breakdown --path=. --format=json on terraform plan output when provided.
No dollar amounts fabricated; if API denied, state missing IAM permission.
Recommendations: RI/Savings Plan, S3 lifecycle, rightsizing — each with risk note.
Do not expose full account billing IDs in public channels.
```

## Workflow

Confirm cloud and period ('2026-10-01' to '2026-10-31').
2. AWS: `aws ce get-cost-and-usage --time-period Start=...,End=... --granularity MONTHLY --metrics BlendedCost --group-by Type=DIMENSION,Key=SERVICE`.
3. Comparison previous month: same command with adjusted period.
4. Tags: GroupBy `TAG:Environment` wo Tagging existiert.
5. Terraform-PR optional: `infracost breakdown --path=infra/`.
6. Top-Anomalien textuell; Idle-Liste aus Compute-Metriken (read).
7. Measures as tickets, no `terminate-instances` without approval.

## Definition of done / Definition of Done

- [ ] Period and currency called
- [ ] Top services with amount from API (not estimated)
- [ ] Recommendations with risk level

## Security

- Billing data confidential; Not in public repos.
- Stop/delete resources only after owner release.

## Pitfalls

- CE API 24h delay - "today" incomplete.
- Untagged Ressourcen verzerren Service-Gruppen.
Infracost without a current provider plan — false estimate.
- Reserved Instance Recommendation without workload stability — loss of money.
- Only compute considered — NAT Gateway, egress, logs forgotten.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** AWS October by service.
- **Input:** Account with CE access.
- **Prompt:**

```text
get-cost-and-usage grouped by SERVICE for Oct 2026; table output.
```

- **Expected result:**

```bash
aws ce get-cost-and-usage --time-period Start=2026-10-01,End=2026-11-01 \
  --granularity MONTHLY --metrics BlendedCost \
  --group-by Type=DIMENSION,Key=SERVICE --output table
```

### Example 2 (Example data (self-written))
- **Task:** Terraform plan costs for new module.
- **Input:** `infra/modules/rds` PR.
- **Prompt:**

```text
infracost breakdown on infra/; highlight monthly delta > 200 USD.
```

- **Expected result:**

```bash
infracost breakdown --path=infra/ --format table
# +$312/mo RDS db.r6g.large called out
```