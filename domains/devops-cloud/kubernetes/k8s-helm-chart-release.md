---
id: k8s-helm-chart-release
domain: devops-cloud
title: "Helm Chart installieren und upgraden"
category: kubernetes
tags:
  - helm
  - kubernetes
  - release
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
required_tools:
  - name: helm
    install: "curl/apt: Helm v3.15+"
    version_notes: "OCI und classic repo"
  - name: kubectl
    install: "apt: kubectl"
    version_notes: "Zugriff auf Zielcluster"
  - name: helm-diff
    install: "helm plugin install https://github.com/databus23/helm-diff"
    version_notes: "Upgrade-Vorschau"
inputs:
  - "Chart (OCI oder Repo-URL)"
  - "values.yaml pro Umgebung"
  - "Release-Name und Namespace"
outputs:
  - "Installiertes oder upgraded Release"
  - "Gespeichertes values-Diff"
risk_level: high
version: "1.1.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

Helm-Releases mit gepinnter Chart-Version und git-versionierten Values ausrollen — Diff vor Upgrade, atomic rollback bei Fehler.

## Wann nutzen

- Standard-Apps (Ingress, Observability, interne Services).
- Wiederholbare Promotions dev → staging → prod.

**Wann nicht:** Wenn ausschließlich Kustomize-Policy ohne Ausnahme gilt.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| helm | Package manager | install, upgrade, history |
| helm diff | Review | PR-taugliches Manifest-Delta |
| kubectl | Verify | Pods/Services nach Release |

## System-Prompt / Instruktionen

```text
You are a Helm release engineer (devops-cloud/kubernetes).

Pin chart version explicitly; never upgrade to latest without user consent.
Workflow: helm repo add/update or OCI login as needed; helm show chart for version sanity.
Render locally: helm template <release> <chart> -f values.yaml -n <ns> > /tmp/rendered.yaml (review size).
Before upgrade: helm diff upgrade <release> <chart> -f values.yaml -n <ns>.

Use helm upgrade --install with --atomic --timeout when supported for prod-like envs.
Never put plaintext secrets in values; use External Secrets or SealedSecrets references.
Record helm history after change; rollback command documented but run only after approval.

Prod upgrades: require explicit approval message; document revision number in output.
Post-check: kubectl get pods -n <ns> -l app.kubernetes.io/instance=<release>.
Do not helm uninstall without approval and dependency check.
```

## Arbeitsablauf

1. `helm version` und `kubectl config current-context` prüfen.
2. Chart-Version: `helm search repo <chart> --version <x.y.z>` oder `helm show chart oci://...`.
3. `helm template ingress ingress-nginx/ingress-nginx -f values.yaml -n ingress`.
4. `helm diff upgrade ingress ingress-nginx/ingress-nginx -f values.yaml -n ingress --version 4.11.1`.
5. Nach Freigabe: `helm upgrade --install ingress ingress-nginx/ingress-nginx -f values.yaml -n ingress --version 4.11.1 --atomic --timeout 10m`.
6. `helm history ingress -n ingress` und `kubectl -n ingress get pods`.
7. `values.yaml` ins Git committen (PR), nicht nur Helm-Revisions-Geheimnis.

## Qualitätskriterien / Definition of Done

- [ ] Chart-Version und App-Version dokumentiert
- [ ] Diff reviewed; Release `deployed` und Pods Ready
- [ ] values-Änderungen im VCS

## Sicherheit & Freigaben

- Keine Secrets in values.yaml im Klartext.
- Prod-Upgrades nur im Runbook-Fenster und mit Freigabe.
- OCI-Credentials nicht in Shell-History loggen.

## Fallstricke

- `helm upgrade` ohne `--atomic` — halb kaputter Release bleibt.
- Subchart-Versionen unpinned — Drift bei `helm dependency update`.
- Namespace fehlt — `helm install` scheitert oder landet in `default`.
- CRD-Upgrade-Reihenfolge — manche Charts brauchen zwei Step-Upgrades.
- `helm diff` ignoriert Hooks — prüfe pre/post hooks separat.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** ingress-nginx 4.x mit eigener values in Staging.
- **Input:** Release `ingress`, NS `ingress`, values mit `controller.replicaCount: 2`.
- **Prompt:**

```text
helm diff then upgrade with atomic; pin chart version; show history after.
```

- **Erwartetes Ergebnis:**

```bash
helm diff upgrade ingress ingress-nginx/ingress-nginx -f values/staging.yaml -n ingress --version 4.11.1
helm upgrade --install ingress ingress-nginx/ingress-nginx -f values/staging.yaml -n ingress --version 4.11.1 --atomic
helm history ingress -n ingress
# REVISION 7 deployed
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Fehlgeschlagenes Upgrade rollback.
- **Input:** REVISION 7 failed, REVISION 6 healthy.
- **Prompt:**

```text
Show failed revision pods; rollback to 6 after approval.
```

- **Erwartetes Ergebnis:**

```bash
helm history ingress -n ingress
helm rollback ingress 6 -n ingress
kubectl -n ingress rollout status deploy/ingress-nginx-controller
```