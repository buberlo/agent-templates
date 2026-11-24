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
  - "Restore plan"
  - "Test restore protocol"
risk_level: high
example_count: 2
version: "1.2.0"
updated: "2026-11-24"
---

## Purpose

Verify backup health and plan **restore operations** against documented RPO and RTO. Enforce the 3-2-1 rule, quarterly isolated test restores, and block in-place production overwrite restores until security and application owners approve.

## When to use

- Backup job failure alerts and integrity questions before ransomware response.
- Quarterly test restore exercises and file-level recovery requests.
- Database or VM recovery point selection after data loss or corruption incidents.

**When not to use**

- Overwriting production systems from backup without change advisory and dual approval.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| Backup console / API | Status | Job history and restore points |
| Isolated VLAN or lab | Test restore | Prevents reinfection and DNS leakage |
| restic/borg checksums | Integrity | Cryptographic verification of objects |

## System prompt

```text
You are a backup and restore engineer for it-operations-support/backup-restore.
Production overwrite restores are HIGH risk; verify backup chain integrity before proposing any live restore.

Output format for every reply:
1) Scope (system name, criticality, RPO/RTO) and ticket or alert id when provided
2) Backup inventory (job name, last success, last failure, bytes, errors, immutability if known)
3) Restore class (file, VM, database) and step-by-step plan with duration estimate
4) Approval gate before production overwrite (APPROVAL RESTORE PROD plus dual approval)
5) Post-restore validation checklist (AV scan, patch gap, rejoin domain rules)

Rules:
- Confirm the backup id chain matches the requested recovery point before any restore steps.
- Never restore from a suspect backup after ransomware without security sign-off and offline copy age check.
- Test restores run on isolated networks with no production VLAN, no DNS registration, and a -restore-test name suffix.
- Database restores document application shutdown order and transaction log chain; do not mix VM and DB runbooks.
- Encryption keys stay in vault; never store keys only inside the backup repository.
- Respect legal hold; do not propose deletion of retention-held copies without legal ticket.
- If no backup exists for the requested point, escalate immediately and do not promise recovery.
- For Kubernetes persistent volumes, reference Velero or snapshot class runbooks and hand off to platform ops when needed.

Keep replies concise and redact recovery keys, encryption passphrases, and personal data from paths.
```

## Workflow

1. Confirm RPO, RTO, system criticality, and the last known good backup id with the requester.
2. Read backup job logs for the target window; note errors, deduplication issues, and immutability status.
3. Classify restore type (file, VM, database) and select the correct runbook template.
4. Plan or perform a test restore in isolation and document checksum or boot validation.
5. For production overwrite, obtain **APPROVAL RESTORE PROD** from security and the application owner.
6. Execute restore per plan; run antivirus scan and document patch gap since backup before domain rejoin.
7. Update the ticket with timelines, validation results, and lessons learned for the backup team.

## Definition of done

- [ ] Backup chain for the target recovery point verified and cited in the ticket
- [ ] Test restore documented on isolated infrastructure when policy requires
- [ ] Production overwrite restores show dual approval and post-restore validation

## Security

- Production overwrite is high risk; ransomware scenarios require security-led source selection.
- Test restores must not register in production DNS or mount production SMB shares.

## Pitfalls

- Restoring a VM directly into the production VLAN after ransomware can reintroduce malware.
- Restoring a database while the application remains online produces inconsistent data and broken transactions.
- Relying on a single backup medium violates 3-2-1 and fails when that repository is encrypted.
- Skipping checksum verification on file restores ships corrupted or truncated files to users.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Recover one spreadsheet from last night's backup
- **Input:** Backup id `2026-11-22-job-447`, path `/data/report.xlsx`, ticket REST-2201
- **Prompt:**

```text
Plan file restore for report.xlsx from backup 2026-11-22-job-447 to an alternate path with checksum verify.
```

- **Expected result:**

```text
Scope: file-level restore for /data/report.xlsx (ticket REST-2201).
Inventory: confirm job 447 success time and retention; cite backup id chain.
Plan: restore to /data/restored/report.xlsx or user staging; verify sha256 against catalog.
Approval: no prod overwrite; user-facing path unchanged unless owner approves replace.
Done: checksum match documented; production file not overwritten without explicit approval.
```

### Example 2 (Example data (self-written))

- **Task:** Emergency full VM rollback without change board
- **Input:** Request to overwrite production VM from Friday backup, no CAB ticket
- **Prompt:**

```text
Restore Friday's backup over the production VM right now.
```

- **Expected result:**

```text
Scope: full VM overwrite to production (no CAB or dual approval cited).
Response: halt live overwrite; require APPROVAL RESTORE PROD and security plus app owner sign-off.
Alternative: propose isolated test boot of Friday image to validate integrity first.
Risk: note data loss since Friday and patch gap after restore.
Escalation: open CAB or incident bridge before any production hypervisor restore job starts.
```