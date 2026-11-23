---
id: cloud-kosten-workflow
title: "Cloud-Kosten"
domain: devops-cloud
category: cloud-kosten
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
    version_notes: "Terraform-Plan-Kosten schätzen"
inputs:
  - "Cloud(s), Zeitraum, Tag-Filter"
  - "Schwellenwert für Anomalie"
outputs:
  - "Kostenbericht (CSV/Table)"
  - "Top-10 Ressourcen + Empfehlungen"
risk_level: medium
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Cloud-Ausgaben analysieren, Anomalien markieren und **rightsizing**/Reserve-Empfehlungen ohne Ressourcen zu löschen.

## Wann nutzen

- Monatliche FinOps-Review, plötzlicher Kostenanstieg.
- Vor Terraform-Apply: Infracost auf Plan.

**Wann nicht:** Vertragsverhandlung ohne CFO-Freigabe.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| aws ce | AWS Kosten | get-cost-and-usage |
| infracost | IaC-Schätzung | PR-Kommentar-tauglich |
| kubecost | optional GKE/EKS | Allocation |

## System-Prompt / Instruktionen

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

## Arbeitsablauf

1. Cloud und Zeitraum bestätigen (`2026-10-01` bis `2026-10-31`).
2. AWS: `aws ce get-cost-and-usage --time-period Start=...,End=... --granularity MONTHLY --metrics BlendedCost --group-by Type=DIMENSION,Key=SERVICE`.
3. Vergleich Vormonat: gleicher Befehl mit angepasstem Zeitraum.
4. Tags: GroupBy `TAG:Environment` wo Tagging existiert.
5. Terraform-PR optional: `infracost breakdown --path=infra/`.
6. Top-Anomalien textuell; Idle-Liste aus Compute-Metriken (read).
7. Maßnahmen als Tickets, keine `terminate-instances` ohne Freigabe.

## Qualitätskriterien / Definition of Done

- [ ] Zeitraum und Währung genannt
- [ ] Top-Services mit Betrag aus API (nicht geschätzt)
- [ ] Empfehlungen mit Risiko-Stufe

## Sicherheit & Freigaben

- Billing-Daten vertraulich; nicht in öffentliche Repos.
- Ressourcen stoppen/löschen nur nach Owner-Freigabe.

## Fallstricke

- CE API 24h Verzögerung — „heute“ unvollständig.
- Untagged Ressourcen verzerren Service-Gruppen.
- Infracost ohne aktuellen Provider-Plan — falsche Schätzung.
- Reserved Instance Empfehlung ohne Workload-Stabilität — Geldverlust.
- Nur Compute betrachtet — NAT Gateway, Egress, Logs vergessen.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** AWS Oktober nach Service.
- **Input:** Account mit CE-Zugriff.
- **Prompt:**

```text
get-cost-and-usage grouped by SERVICE for Oct 2026; table output.
```

- **Erwartetes Ergebnis:**

```bash
aws ce get-cost-and-usage --time-period Start=2026-10-01,End=2026-11-01 \
  --granularity MONTHLY --metrics BlendedCost \
  --group-by Type=DIMENSION,Key=SERVICE --output table
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Terraform-Plan-Kosten für neues Modul.
- **Input:** `infra/modules/rds` PR.
- **Prompt:**

```text
infracost breakdown on infra/; highlight monthly delta > 200 USD.
```

- **Erwartetes Ergebnis:**

```bash
infracost breakdown --path=infra/ --format table
# +$312/mo RDS db.r6g.large called out
```