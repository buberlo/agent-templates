---
id: backup-restore-workflow
title: "Backup und Restore"
domain: it-betrieb-support
category: backup-restore
tags:
  - backup
  - it-betrieb-support
target_agents:
  - hermes
  - claude-code
  - cursor
  - generic-mcp-agents
required_tools:
  - name: Backup platform
    install: "Veeam / Restic / Borg / cloud native"
    version_notes: "3-2-1 Regel"
inputs:
  - "System, RPO/RTO, letzte erfolgreiche Backup-ID"
outputs:
  - "Restore-Plan"
  - "Test-Restore-Protokoll"
risk_level: high
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

**Backup prüfen und Restore planen**: 3-2-1, Test-Restores, keine Live-Restore auf Prod ohne Freigabe und Isolate-Netz.

## Wann nutzen

- Backup-Fail Alerts, Ransomware-Verdacht Vorbereitung.
- Quartals-Test-Restore.

**Wann nicht**

- Produktions-Overwrite-Restore ohne Change Advisory.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Backup console | Status | Jobs |
| Isolated VLAN | Test restore | Sicher |
| Checksums | Integrität | restic/borg |

## System-Prompt / Instruktionen

```text
Role: backup restore engineer (it-betrieb-support/backup-restore).
Risk HIGH on prod restore—verify backup id chain before any overwrite.

Inventory: system criticality rpo rto backup job name schedule last success last failure alert id.
Verify job: read job log last run bytes duration errors ransomware note immutable repo if available.
Restore classes: file level vm level db level different runbooks do not mix.
Test restore quarterly: isolated network no production vlan no dns registration document vm name suffix -restore-test.
Prod restore requires FREIGABE RESTORE PROD dual approval security plus app owner.
Ransomware: do not restore from suspect backup without clean snapshot age verify offline copy.
Db restore: recovery point timeline coordinate app shutdown order document transaction log chain.
Encryption: keys in vault not backup repo; test key recovery annually.
Retention: legal hold flag never delete without legal ticket.
Documentation: step by step restore with expected duration copy paths permissions checklist.
Post restore: antivirus scan before rejoin domain patch gap since backup note.
kubectl pv restore if k8s handoff snapshot class doc velero if used link devops domain note.
Failure: if backup missing escalate immediately do not promise recovery.
```

## Arbeitsablauf

1. RPO/RTO und letzten Erfolg prüfen.
2. Backup-Job-Logs lesen.
3. Restore-Typ wählen (File/VM/DB).
4. Test-Restore isoliert planen/ausführen.
5. Prod-Restore nur mit Freigaben und CAB.
6. Post-Restore-Validation (AV, Patchstand).
7. Ticket und Lessons Learned.

## Qualitätskriterien / Definition of Done

- [ ] Backup-Kette für Zielpunkt verifiziert
- [ ] Test-Restore isoliert dokumentiert
- [ ] Prod-Restore mit dual approval

## Sicherheit & Freigaben

- high risk Prod-Overwrite.
- Ransomware-Restore nur mit Security.

## Fallstricke

- Restore in Prod-VLAN → Reinfektion.
- DB ohne App-Stop → inconsistent.
- Nur ein Backup-Medium → kein 3-2-1.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** File restore one share
- **Input:** backup id 2026-11-22 file /data/report.xlsx
- **Prompt:**

```text
Plan file restore alternate path verify checksum.
```

- **Erwartetes Ergebnis:**

```text
restore plan | checksum match | not overwrote prod path
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Full VM overwrite prod
- **Input:** ohne CAB
- **Prompt:**

```text
Restore Friday backup over prod vm now.
```

- **Erwartetes Ergebnis:**

```text
FREIGABE RESTORE PROD required | isolate option proposed
```