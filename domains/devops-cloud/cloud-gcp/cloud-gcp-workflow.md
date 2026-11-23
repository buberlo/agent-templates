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
    version_notes: "Pflicht für moderne GKE kubeconfig"
inputs:
  - "Projekt-ID und Region"
  - "GKE-Cluster oder Compute-Ressource"
outputs:
  - "gcloud-Protokoll"
  - "Empfehlung / Terraform-google-Modul-Hinweis"
risk_level: high
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

GCP-Projekte mit **gcloud** inventarisieren, GKE read-only prüfen und Änderungen nur über IaC oder freigegebene `gcloud`-Mutationspfade.

## Wann nutzen

- GKE-Version, Node-Pool-Status, IAM-Bindings lesen.
- Fehlersuche nach fehlgeschlagenem Deploy auf Cloud Run/GKE.

**Wann nicht:** Org-Policy-Änderungen ohne Cloud-Admin.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| gcloud | CLI | config, container, iam |
| kubectl | GKE | nach get-credentials |
| terraform-google | optional | Modulvorschläge |

## System-Prompt / Instruktionen

```text
GCP cloud workflow (devops-cloud/cloud-gcp).

Verify project: gcloud config get-value project and gcloud auth list.
Read-only: gcloud compute instances list, gcloud container clusters list, gcloud iam roles describe.
GKE access: gcloud container clusters get-credentials with approval only.

No gcloud compute instances delete, gcloud projects delete, iam policy set without approval.
Use --format=json for parsing; filter with --filter.
For billing export issues, read bucket permissions only, do not mutate.
Workload Identity: describe service accounts; never create keys in chat.

Log every command with project and region flags.
Respect VPC-SC and org constraints; paste Permission denied for escalation.
Prefer regional flags: --region europe-west3.
```

## Arbeitsablauf

1. `gcloud auth list` und `gcloud config set project <id>`.
2. `gcloud container clusters list --region <r>`.
3. Cluster: `gcloud container clusters describe <name> --region <r> --format="value(currentMasterVersion,status)"`.
4. Nach Freigabe: `gcloud container clusters get-credentials <name> --region <r>`.
5. `kubectl get nodes` und `kubectl get pods -A | head`.
6. IAM read: `gcloud projects get-iam-policy <id> --format=json` (Ausschnitt).
7. Mutationen als Terraform-Vorschlag, nicht direkt ausführen.

## Qualitätskriterien / Definition of Done

- [ ] Projekt-ID in jeder Antwort
- [ ] GKE Master/Node-Version dokumentiert
- [ ] Keine Service-Account-Keys erzeugt

## Sicherheit & Freigaben

- Prod-Projekt: high risk; Deletes verboten ohne Ticket.
- IAM `roles/owner` nicht als Default-Vorschlag.
- Audit-Logs nicht massenexportieren in öffentliche Threads.

## Fallstricke

- Vergessener `gke-gcloud-auth-plugin` — kubectl auth scheitert.
- Zonen vs. Region bei GKE — falsche Flag-Kombination.
- Default VPC-Annahmen — Shared VPC braucht Host-Projekt-Kontext.
- Quotas — Create schlägt fehl, List funktioniert; Quota separat prüfen.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** GKE-Cluster-Status europe-west3.
- **Input:** Cluster `prod-gke`, Projekt `acme-prod`.
- **Prompt:**

```text
Describe cluster version and node count; read-only gcloud only.
```

- **Erwartetes Ergebnis:**

```bash
gcloud container clusters describe prod-gke --region europe-west3 \
  --format="yaml(currentMasterVersion,currentNodeCount,status)"
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Fehlende Workload-Identity-Binding erkennen.
- **Input:** KSA `default/api` kann GCS nicht lesen.
- **Prompt:**

```text
Read IAM policy binding for GSA; suggest fix text only, no iam policy set.
```

- **Erwartetes Ergebnis:**

```bash
gcloud iam service-accounts get-iam-policy api-sa@acme-prod.iam.gserviceaccount.com
# Missing workloadIdentityUser binding documented in ticket
```