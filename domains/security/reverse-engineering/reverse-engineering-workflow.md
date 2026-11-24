---
id: reverse-engineering-workflow
title: "Reverse Engineering (nur autorisiert)"
domain: security
category: reverse-engineering
tags:
  - reverse-engineering
  - authorized
  - malware
target_agents:
  - hermes
  - generic-mcp-agents
required_tools:
  - name: authorization
    install: "Ownership or contract"
    version_notes: "Binary scope"
  - name: isolated-lab
    install: "Org mandated VM"
    version_notes: "No host execution"
inputs:
  - "Legal right to analyze artifact"
  - "File hash and source"
outputs:
  - "Analysis plan template"
  - "Safety gates checklist"
risk_level: high
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Purpose

*Planning and compliance**, no malware disassembly, or running malware in agent instructions.

## When to use

- Own binaries, licensed audits, incident with authorized sample.
- Lab-Setup-Checkliste vor menschlicher Analyse.

**When not:** Third party software without license/ROE; Crack/Keygen targets.

## Tool stack

| Tool | Role | Justification |
|------|-------|------------|
| Isolated lab | Safety | air-gap policy |
| Hash | Identity | sha256 |
| Human analyst | RE execution | off-template |

## System prompt

```text
Reverse engineering framework ONLY (security/reverse-engineering).

Do not provide disassembly walkthroughs, crack patches, license bypass, or malware unpacking steps for unauthorized binaries.
Require proof of authorization: owned product, vendor contract, or law enforcement case id.
Allowed: lab isolation checklist, snapshot before analysis, network isolation confirmation, YARA rule *placement* policy (org handles rules), report sections (static vs dynamic).
Never run untrusted binaries on host; refer to org isolated VM with no outbound.
If sample is malware, escalate to CERT/incident; do not detonate in shared agent environment.
Respect DMCA/contract/EULA; refuse if scope illegal.
Outputs stop at planning; operational RE by qualified analysts with org tooling.
No public sharing of extracted strings containing secrets.
Record analyst training certification ids when org requires them in plan header.
Version control for lab images must be noted before first execution.
Export controls and cryptography regulations may apply; flag dual-use uncertainty to legal.
Snapshot hypervisor metadata and host firewall state in checklist without enabling new rules.
Maintain separate evidence storage encryption keys from production KMS where possible.
Schedule peer review of analysis plan before any human executes dynamic steps.
```

## Workflow

1. Rechtsgrundlage dokumentieren.
2. SHA256 des Artefakts notieren.
3. Lab-Isolation Checkliste (VM snapshot, no USB, VLAN).
4. Analysis plan headings: static, dynamic, memory — without tool commands.
5. Human analyst takes over.
6. Findings in encrypted report template.
7. Artefakt-Safe-Storage verifizieren.

## Definition of done

- [ ] Authorization dokumentiert
- [ ] No RE-Befehle im Agent-Output
- [ ] Isolation checklist completely

## Security

- **high risk**; Malware nur im Org-Lab.
No samples of public models.

## Pitfalls

- „Nur schnell auf dem Laptop“ — Kontamination.
- Shared VM Snapshots veraltet.
- Strings leak secrets in chat.
- Unauthorized game RE — rechtliches Risiko.
Dynamic analysis with network — C2 triggered.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Eigene Firmware audit plan.
- **Input:** signed contract AUDIT-12, hash `def456...`.
- **Prompt:**

```text
Lab checklist and report outline; no disassembly steps.
```

- **Expected result:**

```text
Checklist: VM snapshot, no internet, case AUDIT-12
Sections: static overview (human), findings table
```

### Example 2 (Example data (self-written))
- **Task:** Crack request abweisen.
- **Input:** „bypass Adobe trial“.
- **Prompt:**

```text
Authorization gate.
```

- **Expected result:**

```text
Refused: no authorization; reverse-engineering for license bypass not supported
```