---
id: forensics-workflow
title: "Forensik (nur autorisiert)"
domain: security
category: forensics
tags:
  - forensics
  - incident
  - authorized
target_agents:
  - hermes
  - generic-mcp-agents
required_tools:
  - name: chain-of-custody
    install: "Org forensics SOP"
    version_notes: "Hash before analyze"
  - name: read-only images
    install: "E01/DD per legal"
    version_notes: "No mount write"
inputs:
  - "Legal/HR authorization"
  - "Evidence IDs and hashes"
outputs:
  - "Chain-of-custody notes"
  - "Timeline template (no destructive steps)"
risk_level: high
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Purpose

Forensics **frame**: Chain of Custody, Timeline, Reporting — no step-by-step data recovery or malware detonation in this template.

## When to use

- IR team needs structured agent help for documentation.
- Nach Autorisierung durch Legal/Security.

**When not:** Without custody form or personal devices without policy.

## Tool stack

| Tool | Role | Justification |
|------|-------|------------|
| SOP | Process | org-specific |
| Hash tools | Integrity | sha256 before open |
| Human examiner | Analysis | off-template |

## System prompt

```text
Forensics framework ONLY (security/forensik).

Do not instruct live disk writes, malware execution, memory scraping tools, or circumvention of encryption on seized media.
Require: case id, authorizing officer, evidence list with sha256, storage location, and retention schedule.
Outputs allowed: chain-of-custody log template, timeline columns (UTC, host, artifact, analyst, hash), interview question bank (high level).
If evidence hash mismatch, stop and escalate; do not analyze.
Minimize PII in chat; reference evidence ids only.
Coordinate with incident response; preserve originals; work on forensic copies per SOP.
Jurisdiction and privacy law reminder in summary.
No cloud exfiltration of disk images to public AI services.
Handoff to certified forensic analyst for tooling steps.
```

## Workflow

1. Check authorization and case ID.
2. Enter the evidence list with SHA256.
3. Custody log: who, when, where.
4. Timeline-Template anlegen (leer, strukturiert).
5. Copy vs. original according to SOP confirm.
6. Human analyst takes over tooling.
7. Agent nur Dokumentation fortsetzen.

## Definition of done

- [ ] Custody completely
- [ ] No destruktiven/analyse-Befehle generiert
- [ ] Hashes vor Analyse dokumentiert

## Security

- **high risk**; Legal Release Mandatory.
- Do not upload evidence to cloud LLM.

## Pitfalls

Mount read-write — traces destroyed.
- Fehlende Uhrzeit-Sync in Timeline.
- Analyst-Tool-Output without Hash-Referenz.
- GDPR for employee devices.
- Chain-of-custody gaps invalidate court use.

## Basic examples

### Example 1 (Example data)

- **Task:** Custody log for USB-STICK-7.
- **Input:** sha256 `abc...`, Case FIR-2026-03.
- **Prompt:**

```text
Create custody table and timeline headers only; no acquisition commands.
```

- **Expected result:**

```text
Custody: received FIR-2026-03 by Analyst M; hash abc...; sealed bag ID 7
Timeline columns ready UTC|Host|Event|Ref
```

### Example 2 (Example data)

- **Task:** Hash mismatch.
- **Input:** re-hash differs.
- **Prompt:**

```text
Apply mismatch policy.
```

- **Expected result:**

```text
STOP analysis; escalate integrity failure; do not mount image
```