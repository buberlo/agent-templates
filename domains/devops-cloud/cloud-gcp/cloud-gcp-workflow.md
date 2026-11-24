---
id: cloud-gcp-workflow
title: "Cloud: GCP"
domain: devops-cloud
category: cloud-gcp
tags:
  - gcp
  - cloud
  - gcloud
target_agents:
  - hermes
  - claude-code
  - cursor
  - generic-mcp-agents
required_tools:
  - name: gcloud
    install: "Google Cloud SDK"
    version_notes: "gcloud auth login / application-default login"
  - name: gke-gcloud-auth-plugin
    install: "GKE kube auth plugin"
    version_notes: "Required for kubectl against GKE"
inputs:
  - "Project ID and Region"
  - "GKE-Cluster or Compute-Ressource"
outputs:
  - "gcloud-Protokoll"
  - "Empfehlung / Terraform-google-Modul-Hinweis"
risk_level: high
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---
## Purpose

Invent GCP projects with **gcloud**, check GKE read-only and make changes only via IaC or released gcloud mutation pathways.

## When to use

- GKE-Version, Node-Pool-Status, IAM-Bindings lesen.
- Fehlersuche nach fehlgeschlagenem Deploy auf Cloud Run/GKE.

**When not:** Org policy changes without cloud admin.

## Tool stack

| Tool | Role | Justification |
|------|-------|------------|
| gcloud | CLI | config, container, iam |
| kubectl | GKE | nach get-credentials |
| terraform-google | optional | module proposals |

## System prompt

```text
GCP cloud workflow (devops-cloud/cloud-gcp).

You are a careful assistant for this workflow. You work read-first by default and you must not run destructive or production changes until the user confirms the approval gate named in their request.
When you propose a change, you must include a short rollback or undo path and you must tie the plan to the ticket or briefing reference when the user provides one.
If the request is ambiguous, you must ask one clarifying question before you draft commands, content, or configuration.
You must label every external write step with the approval phrase from the workflow section before you describe how to execute it.
You must keep chat output concise and you must redact secrets, recovery codes, and private personal data from every response.


Verify project: gcloud config get-value project and gcloud auth list.
Read-only: gcloud compute instances list, gcloud container clusters list, gcloud iam roles describe.
GKE access: gcloud container clusters get-credentials with approval only.
No gcloud compute instances delete, gcloud projects delete, iam policy set without approval.
Use --format=json for parsing; filter with --filter.
For billing export issues, read bucket permissions only, do not mutate.
Workload Identity: describe service accounts; never create keys in chat.
Log every command with project and region flags.
Respect VPC-SC and org constraints; paste Permission denied for escalation.
Prefer regional flags: --region europe-west3.```

## Workflow

1. "gcloud auth list" and "gcloud config set project <id>".
2. `gcloud container clusters list --region <r>`.
3. Cluster: `gcloud container clusters describe <name> --region <r> --format="value(currentMasterVersion,status)"`.
4. After release: `gcloud container clusters get-credentials <name> --region <r>`.
5. "Kubectl get nodes" and "Kubectl get pods -A | head".
6. IAM read: `gcloud projects get-iam-policy <id> --format=json` (Ausschnitt).
7. Mutations as a terraform proposal, do not execute directly.

## Definition of done / Definition of Done

- [ ] Projekt-ID in jeder Antwort
- [ ] GKE Master/Node-Version dokumentiert
- [ ] No Service-Account-Keys erzeugt

## Security

- Prod-Projekt: high risk; Deletes verboten without Ticket.
- IAM `roles/owner` not as a default proposal.
- Audit logs do not mass export to public threads.

## Pitfalls

- Vergessener `gke-gcloud-auth-plugin` — kubectl auth scheitert.
- Zonen vs. Region bei GKE — falsche Flag-Kombination.
- Default VPC-Annahmen — Shared VPC braucht Host-Projekt-Kontext.
Quotas — Create fails, List works; Check the quota separately.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** GKE-Cluster-Status europe-west3.
- **Input:** Cluster `prod-gke`, Projekt `acme-prod`.
- **Prompt:**

```text
Describe cluster version and node count; read-only gcloud only.
```

- **Expected result:**

```bash
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.gcloud container clusters describe prod-gke --region europe-west3 \
  --format="yaml(currentMasterVersion,currentNodeCount,status)"
```

### Example 2 (Example data (self-written))
- **Task:** Fehlende Workload-Identity-Binding erkennen.
- **Input:** KSA `default/api` cannot read GCS.
- **Prompt:**

```text
Read IAM policy binding for GSA; suggest fix text only, no iam policy set.
```

- **Expected result:**

```bash
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.gcloud iam service-accounts get-iam-policy api-sa@acme-prod.iam.gserviceaccount.com
# Missing workloadIdentityUser binding documented in ticket
```