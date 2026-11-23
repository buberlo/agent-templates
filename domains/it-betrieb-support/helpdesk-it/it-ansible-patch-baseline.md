---
id: it-ansible-patch-baseline
domain: it-betrieb-support
title: "Patch-Baseline mit Ansible"
category: helpdesk-it
tags:
  - ansible
  - patching
  - baseline
target_agents:
  - hermes
  - generic
required_tools:
  - name: ansible
    install: "pip: ansible-core"
    version_notes: "2.17+; collections aktuell"
  - name: ssh
    install: "system"
    version_notes: "Key-based auth"
inputs:
  - "Inventory"
  - "Playbook-Scope"
  - "Wartungsfenster"
outputs:
  - "Play recap"
  - "Compliance-Report"
risk_level: high
version: "1.0.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

Linux-Server auf definierten Patch-Stand und Hardening-Baseline bringen.

## Wann nutzen

- Monatliches Patch-Fenster, CIS-Hardening.
- Nicht auf produktiven DB-Clustern ohne Failover-Plan.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Ansible | Automation | Idempotent |
| apt/dnf modules | Patching | Native Paketmgr |
| ansible-lint | Qualität | Playbook lint |

## System-Prompt / Instruktionen

```text
Run ansible-playbook in check mode first (--check --diff).
Limit blast radius with --limit and serial batches.
Reboot only when required and approved in window.
Output recap JSON for CMDB update.
```

## Arbeitsablauf

1. Inventory und Drift prüfen.
2. Check-Mode auf Staging.
3. Serial 10 % Prod-Rollout.
4. Monitoring nach Reboot.
5. Report an Security.

## Qualitätskriterien / Definition of Done

- [ ] 0 failed hosts (oder dokumentierte Ausnahme)
- [ ] CVE-Zielliste abgearbeitet
- [ ] Check-Mode-Log archiviert

## Sicherheit & Freigaben

- become/sudo nur über Vault-Rollen.
- Keine Passwörter in Playbooks.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

_Siehe vorheriger Abschnitt; bei Migration ergänzt._

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Validierung
- **Input:** n/a
- **Prompt:** `validate output`
- **Erwartetes Ergebnis:** OK

## Beispiele (Legacy)

**Eingabe:** 40 Ubuntu 22.04 Webserver, Patch-2026-11
**Erwartetes Ergebnis:** `recap.json`, alle OK nach Reboot
