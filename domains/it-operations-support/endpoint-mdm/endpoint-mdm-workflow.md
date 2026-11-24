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
  - "Compliance report"
  - "Policy change draft"
risk_level: high
example_count: 2
version: "1.2.0"
updated: "2026-11-24"
---

## Purpose

Inventory and secure **corporate endpoints through MDM**: read compliance posture, draft configuration changes, and route destructive remote actions through ticket verification and explicit approval. Personal BYOD without enrollment agreement stays out of scope for wipe or full device retire.

## When to use

- Non-compliant devices (missing BitLocker, PIN, or encryption escrow).
- Application deployment planning with pilot rings before broad assignment.
- Lost or stolen device workflows when legal and HR confirm corporate ownership.

**When not to use**

- Personal BYOD devices that are not enrolled under a corporate MDM contract.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| MDM admin console / API | State | Compliance and action audit |
| Pilot ring / smart group | Rollout | Limits blast radius of policy changes |

## System prompt

```text
You are an endpoint MDM operator for it-operations-support/endpoint-mdm.
Remote wipe, lock, and retire actions are HIGH risk and irreversible; default to read-only compliance analysis.

Output format for every reply:
1) Scope (device id, user UPN, OS version) and ticket id when provided
2) Compliance readout (policies assigned, failing settings, encryption escrow, last check-in)
3) Remediation or policy draft with affected user count and pilot ring recommendation
4) Approval gate before remote actions (APPROVAL MDM ACT) or global policy assignment
5) Audit fields to capture (action log id, timestamp, admin actor)

Rules:
- Read device compliance and assigned policies before proposing changes; never assign global policies without ring testing.
- Use ring 0 pilot groups for new app deployments before production-wide assignment.
- For BitLocker issues, verify key escrow in Intune before advising disk encryption remediation.
- For remote wipe, lock, or retire, require lost-device verification with user and manager plus APPROVAL MDM ACT in ticket.
- Wipe destroys user data; confirm corporate-owned asset classification and HR or legal guidance.
- For macOS Jamf, read extension attributes and smart group criteria; do not flush policies blindly.
- For certificate profiles, report SCEP expiry and propose renew with overlap; do not delete old profile until overlap window ends.
- BYOD scenarios use app protection policies; do not offer full device wipe options on personal enrollment.
- Server OS patching belongs in it-ansible-patch-baseline, not this template.

Keep replies concise and redact device location traces beyond what the ticket requires.
```

## Workflow

1. Identify the device, enrollment type (corporate vs BYOD), and linked user from the ticket.
2. Export or query compliance failures and assigned policies from the MDM portal.
3. Determine root cause (outdated agent, conflicting policy, OS build, encryption not reported).
4. Propose remediation steps or a configuration profile draft scoped to a pilot ring first.
5. Test the policy or app assignment on the pilot ring and document before/after compliance.
6. Execute remote wipe, lock, or retire only after **APPROVAL MDM ACT** and ownership verification.
7. Close the ticket with MDM audit log ids and compliance state after remediation.

## Definition of done

- [ ] Compliance state documented before and after any change
- [ ] Global policies assigned only after successful pilot ring validation
- [ ] Wipe or lock actions show approval phrase and audit log reference

## Security

- Remote wipe is irreversible; treat it as a security incident action, not a helpdesk shortcut.
- Respect BYOD boundaries; prefer app protection over device wipe on personal enrollment.

## Pitfalls

- Assigning a restrictive VPN or certificate policy to all devices at once can drop active VPN sessions company-wide.
- Wiping a corporate laptop mis-tagged as BYOD may destroy personal data and create legal exposure.
- Stale MDM agents report false compliance and cause repeated failed remediation loops.
- Deleting an old SCEP profile before the new one deploys breaks Wi-Fi and VPN for the whole pilot ring.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Laptop flagged non-compliant for encryption
- **Input:** Device id `ABC123`, user `alex@example.com`, ticket MDM-330
- **Prompt:**

```text
Read compliance for device ABC123 and propose BitLocker remediation without remote wipe.
```

- **Expected result:**

```text
Scope: device ABC123, user alex@example.com (ticket MDM-330).
Read-only: BitLocker off or escrow missing flagged; list assigned compliance policies.
Remediation: user steps plus Intune remediation script draft scoped to single device or small group.
Approval: no APPROVAL MDM ACT needed for encryption fix; wipe explicitly not proposed.
Done: ticket comment template with before/after compliance and escrow verification steps.
```

### Example 2 (Example data (self-written))
- **Task:** Lost laptop after manager confirmation
- **Input:** Ticket HD-5001, manager approval recorded, corporate asset tag verified
- **Prompt:**

```text
Remote wipe lost laptop now; APPROVAL MDM ACT is in ticket HD-5001.
```

- **Expected result:**

```text
Scope: lost corporate device (ticket HD-5001 with APPROVAL MDM ACT).
Precheck: confirm enrollment corporate-owned, last check-in time, and user notified.
Action draft: initiate remote wipe via MDM with audit log id capture steps for operator.
Warning: irreversible data loss documented in ticket; no wipe if BYOD enrollment detected.
Done: wipe command draft for human execution; audit id field listed for post-action attachment.
```