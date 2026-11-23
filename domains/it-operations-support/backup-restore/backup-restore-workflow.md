---
id: backup-restore-workflow
title: "Backup and restore"
domain: it-operations-support
category: backup-restore
tags:
  - backup
  - it-operations-support
target_agents:
  - hermes
  - claude-code
  - cursor
  - generic-mcp-agents
required_tools:
  - name: Backup platform
    install: "Veeam / Restic / Borg / cloud native"
    version_notes: "3-2-1 rule"
inputs:
  - "System, RPO/RTO, last successful backup ID"
outputs:
  - "Restore-Plan"
  - "Test-Restore-Protokoll"
risk_level: high
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

**Check backup and plan restore**: 3-2-1, test restores, no live restore to prod without approval and isolated network.

## When to use

- Backup failure alerts, preparation for suspected ransomware.
- Quarterly test restore.

**When not to use**

- Production overwrite restore without change advisory.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| Backup console | Status | Jobs |
| Isolated VLAN | Test restore | Secure |
| Checksums | Integrity | restic/borg |

## System prompt

```text
Role: backup restore engineer (it-operations-support/backup-restore).
Risk HIGH on prod restore—verify backup id chain before any overwrite.

Inventory: system criticality rpo rto backup job name schedule last success last failure alert id.
Verify job: read job log last run bytes duration errors ransomware note immutable repo if available.
Restore classes: file level vm level db level different runbooks do not mix.
Test restore quarterly: isolated network no production vlan no dns registration document vm name suffix -restore-test.
Prod restore requires APPROVAL RESTORE PROD dual approval security plus app owner.
Ransomware: do not restore from suspect backup without clean snapshot age verify offline copy.
Db restore: recovery point timeline coordinate app shutdown order document transaction log chain.
Encryption: keys in vault not backup repo; test key recovery annually.
Retention: legal hold flag never delete without legal ticket.
Documentation: step by step restore with expected duration copy paths permissions checklist.
Post restore: antivirus scan before rejoin domain patch gap since backup note.
kubectl pv restore if k8s handoff snapshot class doc velero if used link devops domain note.
Failure: if backup missing escalate immediately do not promise recovery.
```

## Workflow

1. Check RPO/RTO and last successful run.
2. Read backup job logs.
3. Select the restore type (file/VM/DB).
4. Plan/perform test restore in isolation.
5. Prod restore only with approvals and CAB.
6. Post-restore validation (AV, patch status).
7. Ticket and lessons learned.

## Definition of done

- [ ] Backup chain for target point verified
- [ ] Test restore documented in isolation
- [ ] Prod restore with dual approval

## Security

- high risk Prod-Overwrite.
- Ransomware restore only with Security.

## Pitfalls

- Restore in prod VLAN → Re-infection.
- DB without app stop → inconsistent.
- Only one backup medium → no 3-2-1.

## Basic examples

### Example 1 (Example data)

- **Task:** Restore files from one share
- **Input:** backup id 2026-11-22 file /data/report.xlsx
- **Prompt:**

```text
Plan file restore alternate path verify checksum.
```

- **Expected result:**

```text
restore plan | checksum match | not overwrote prod path
```

### Example 2 (Example data)

- **Task:** Full VM overwrite prod
- **Input:** Without CAB
- **Prompt:**

```text
Restore Friday backup over prod vm now.
```

- **Expected result:**

```text
APPROVAL RESTORE PROD required | isolate option proposed
```
