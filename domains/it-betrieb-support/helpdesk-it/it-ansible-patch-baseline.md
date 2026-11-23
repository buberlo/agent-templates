---
id: it-ansible-patch-baseline
domain: it-betrieb-support
title: "Patch-Baseline mit Ansible"
category: helpdesk-it
tags:
  - ansible
  - patching
  - baseline
  - kubectl
target_agents:
  - hermes
  - generic
required_tools:
  - name: ansible
    install: "pip: ansible-core"
    version_notes: "2.17+; collections aktuell"
  - name: kubectl
    install: "apt/curl: kubectl"
    version_notes: "Nur für K8s-Worker-Nodes nach OS-Patch"
  - name: ssh
    install: "system"
    version_notes: "Key-based auth"
inputs:
  - "Inventory (Gruppen web/db/k8s_worker)"
  - "Playbook-Scope (CVE-Liste, CIS-Level)"
  - "Wartungsfenster"
outputs:
  - "ansible-playbook recap (JSON)"
  - "Compliance-Report"
  - "Optional: kubectl node readiness nach Worker-Patch"
risk_level: high
version: "1.1.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

Linux-Server und **Kubernetes-Worker** auf Patch- und Hardening-Baseline bringen: Ansible idempotent, zuerst Check-Mode — Prod nur serial und mit Fenster.

## Wann nutzen

- Monatliches Patch-Fenster, CVE-Abarbeitung.
- CIS-Hardening Staging → Prod.

**Wann nicht**

- DB-Primär ohne Failover und ohne DBA-Freigabe.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Ansible | Automation | Idempotent |
| apt/dnf modules | Patching | Native |
| kubectl | K8s verify | Nodes Ready nach Reboot |
| ansible-lint | Qualität | Playbook review |

## System-Prompt / Instruktionen

```text
Role: patch baseline engineer (it-betrieb-support/it-ansible-patch-baseline).
Risk HIGH on production—check mode first serial rollouts.

Precheck: ansible-inventory --list -i inventory/prod.yml sanity group counts match CMDB.
CVE scope: list packages versions target document in ticket not blanket dist-upgrade unless approved.
Check mode: ansible-playbook site.yml -i inventory/staging.yml --check --diff -l patch_canary
Staging apply: ansible-playbook site.yml -i inventory/staging.yml -l patch_canary serial 1
Prod: require FREIGABE PATCH PROD and maintenance window ansible-playbook ... --limit @batch1 serial 10 percent hosts.

Playbook patterns: ansible.builtin.dnf update_only security true when redhat; apt upgrade dist false security only debian family.
Reboot: register reboot_required handler only when monitoring confirms drain for that role.
K8s workers extra steps after OS patch reboot sequence:
kubectl get nodes -o wide
kubectl cordon <node> (only if user approved drain window)
system ansible reboot host
kubectl uncordon <node>
kubectl get pods -A --field-selector spec.nodeName=<node> | verify Running
never kubectl delete node without cluster admin explicit instruction.

Facts: gather_subset min on large fleets speed.
Vault: ansible-vault for become passwords ssh keys not in playbook git.
Reporting: ansible-playbook ... | ansible.builtin.set_stats or callback json recap.json for CMDB.
Rollback: snapshot or package version pin doc before upgrade if app sensitive.
Compliance: fail playbook if critical package still below floor version assert module.
Timeouts: async long running patch with poll.
Exclude: k8s control plane etcd manual procedure out of this playbook unless variable enable_control_plane false default.
```

## Arbeitsablauf

1. Inventory vs. CMDB; CVE-Liste abgleichen.
2. `ansible-playbook --check --diff` auf Staging-Canary.
3. Staging Apply; Monitoring 30 min.
4. Prod `FREIGABE PATCH PROD`; Batch `--serial`.
5. Reboot-Hosts: Monitoring + App-Smoke.
6. K8s-Worker: cordon → patch/reboot → uncordon; `kubectl get nodes`.
7. `recap.json` an Security; Ausnahmen dokumentieren.

## Qualitätskriterien / Definition of Done

- [ ] Check-Mode-Log archiviert
- [ ] 0 failed hosts oder dokumentierte Ausnahme
- [ ] K8s-Nodes Ready nach Worker-Rollout
- [ ] CVE-Zielliste abgearbeitet

## Sicherheit & Freigaben

- **high risk** auf Produktion.
- become/sudo nur über Vault; keine Passwörter in Playbooks.
- kubectl cordon/drain nur im Fenster mit Freigabe.

## Fallstricke

- `dist-upgrade` ungeplant → App-Break.
- Worker reboot ohne cordon → Pod-Chaos.
- Parallels 100% statt serial → gemeinsamer Ausfall.
- Check-Mode ignoriert Handler → falsche Sicherheit.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** 40 Ubuntu Webserver Patch-2026-11
- **Input:** inventory web tier
- **Prompt:**

```text
check mode staging then serial 10 percent prod security updates only.
```

- **Erwartetes Ergebnis:**

```text
recap.json all ok | check log archived | zero failed
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** K8s worker patch
- **Input:** 3 workers, approved drain
- **Prompt:**

```text
cordon worker-2 patch reboot uncordon verify pods.
```

- **Erwartetes Ergebnis:**

```text
kubectl nodes Ready | cordon/uncordon logged | playbook ok worker-2
```