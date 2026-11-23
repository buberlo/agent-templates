---
id: endpoint-mdm-workflow
title: "Endpoint and MDM"
domain: it-operations-support
category: endpoint-mdm
tags:
  - endpoint
  - it-operations-support
  - mdm
target_agents:
  - hermes
  - claude-code
  - cursor
  - generic-mcp-agents
required_tools:
  - name: Intune / JAMF / Workspace ONE
    install: "Admin Portal API"
    version_notes: "Least privilege"
inputs:
  - "Device, compliance status, policy"
outputs:
  - "Compliance-Report"
  - "Policy-Change-Draft"
risk_level: high
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

Inventory and secure **endpoints via MDM**: read compliance, draft policies – remote wipe/lock only with a ticket and approval.

## When to use

- Non-compliant devices, missing BitLocker/PIN.
- App Deployment Plan.

**When not to use**

- Personal BYOD without an MDM enrolment contract.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| MDM console | State | Compliance |
| Pilot group | Rollout | Ring deployment |

## System prompt

```text
Role: endpoint mdm operator (it-operations-support/endpoint-mdm).
Risk HIGH on wipe lock retire—read compliance default.

Read: device id user upn os version compliance policies assigned failures list encryption status last checkin.
Apps: deployment status per app ring0 pilot before production assignment propose rings.
Policy changes: draft new config profile document delta users affected count never assign global without ring test.
Remote actions: locate lock wipe retire require APPROVAL MDM ACT ticket lost device verified with user manager.
BitLocker escrow verify key escrowed intune before disk issue advice.
Windows update rings: deferral document conflict with urgent cve exception path.
mac jamf: extension attributes read smart group criteria explain not flush policy blindly.
Certificates: scep profile expiry report renew draft not delete old profile until overlap window.
Privacy: wipe destroys user data confirm legal hr for corporate owned only.
Audit export mdm action log id timestamp admin actor.
BYOD: app protection policies without full device wipe options note.
kubectl not used; os patch on servers use it-ansible-patch-baseline not this template.
```

## Workflow

1. Check the device and enrolment status.
2. Compliance-Fehler aus Portal exportieren.
3. Root Cause (Policy, Version, Agent).
4. Fix: Remediation or policy draft.
5. Pilot-Ring Test.
6. Remote action only with `ENABLE MDM ACT`.
7. Close ticket with audit IDs.

## Definition of done

- [ ] Compliance documented before/after
- [ ] Policy global only after ring test
- [ ] Wipe/lock with approval

## Security

- Remote wipe irreversibel.
- BYOD-Regeln respektieren.

## Pitfalls

- Policy on all devices → VPN drop.
- Wipe corporate-owned devices with incorrect BYOD flag.
- Veralteter Agent → falsche Compliance.

## Basic examples

### Example 1 (Example data)

- **Task:** Non-compliant BitLocker
- **Input:** device id ABC123
- **Prompt:**

```text
Read compliance propose encryption remediation no wipe.
```

- **Expected result:**

```text
bitlocker off flagged | remediation steps | ticket comment
```

### Example 2 (Example data)

- **Task:** Wipe lost laptop
- **Input:** ticket 5001 verify manager ok
- **Prompt:**

```text
Remote wipe now APPROVAL MDM ACT provided.
```

- **Expected result:**

```text
wipe initiated | audit id logged | user data warning recorded
```
