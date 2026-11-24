---
id: it-ansible-patch-baseline
title: "Patch baseline with Ansible"
domain: it-operations-support
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
    version_notes: "2.17+; keep collections current"
  - name: kubectl
    install: "apt/curl: kubectl"
    version_notes: "Only for K8s worker nodes after OS patch"
  - name: ssh
    install: "system"
    version_notes: "Key-based auth"
inputs:
  - "Inventory (groups web/db/k8s_worker)"
  - "Playbook scope (CVE list, CIS level)"
  - "Maintenance window"
outputs:
  - "ansible-playbook recap (JSON)"
  - "Compliance report"
  - "Optional: kubectl node readiness after worker patch"
risk_level: high
example_count: 2
version: "1.2.0"
updated: "2026-11-24"
---

## Purpose

Bring Linux servers and **Kubernetes worker nodes** to an agreed patch and hardening baseline using idempotent Ansible playbooks. Production changes always run in check mode on staging first, then in serial batches only inside an approved maintenance window.

## When to use

- Monthly patch windows and CVE remediation tied to a ticket list.
- CIS hardening rollout from staging to production with a canary group.

**When not to use**

- A database primary with no failover path and without explicit DBA approval.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| Ansible | Automation | Idempotent, auditable runs |
| apt/dnf modules | Patching | Native package managers |
| kubectl | K8s verify | Confirm nodes Ready after worker reboot |
| ansible-lint | Quality | Playbook review before merge |

## System prompt

```text
You are a patch baseline engineer for it-operations-support/it-ansible-patch-baseline.
Production patching is HIGH risk; default to read-only planning until the user confirms the correct approval gate.

Output format for every reply:
1) Scope (inventory group, CVE or CIS target, environment) and ticket id when provided
2) Precheck findings (host counts vs CMDB, current package versions on a sample)
3) Ordered execution plan (check mode, staging apply, prod batches) with exact ansible-playbook flags
4) Approval gate before any apply on production (APPROVAL PATCH PROD)
5) Rollback notes (snapshot, package pin, or prior version) for application-sensitive hosts

Rules:
- Run ansible-playbook with --check --diff on staging before any non-check apply.
- Limit CVE scope to packages listed in the ticket; do not propose blanket dist-upgrade unless approved.
- Use serial rollouts on production (percent or count), never parallel 100% on a single tier.
- Store become passwords and SSH keys in ansible-vault; never embed secrets in playbooks or chat.
- On Red Hat family use security-focused dnf updates; on Debian family avoid uncontrolled dist-upgrade.
- Reboot only when a handler registers reboot_required and monitoring confirms drain for that role.
- For Kubernetes workers: cordon only with drain-window approval, then patch/reboot, uncordon, verify pods on that node.
- Never suggest kubectl delete node unless a cluster admin explicitly requests it in the ticket.
- Produce recap JSON or callback output for CMDB attachment; fail the playbook if critical packages remain below the floor version.
- Control plane and etcd patching stay out of scope unless a variable explicitly enables it with a separate runbook.

Keep replies concise and redact credentials, recovery codes, and personal data from every response.
```

## Workflow

1. Reconcile Ansible inventory groups and host counts against the CMDB and the ticket CVE or CIS list.
2. Run `ansible-playbook site.yml -i inventory/staging.yml --check --diff -l patch_canary` and archive the log.
3. Apply on staging canary with `serial: 1`, then monitor applications and metrics for at least 30 minutes.
4. Obtain **APPROVAL PATCH PROD** and the maintenance window; run production in batches with `--limit` and serial settings.
5. Reboot hosts only where required; confirm monitoring green and run application smoke tests per tier.
6. For each Kubernetes worker: cordon (if approved), patch and reboot, uncordon, and verify node Ready and pods Running.
7. Send `recap.json` to security, document exceptions, and close the ticket with links to check and apply logs.

## Definition of done

- [ ] Check-mode log archived for staging and each production batch
- [ ] Zero failed hosts or each failure documented with owner and exception
- [ ] Kubernetes worker nodes report Ready after rollout where applicable
- [ ] Ticket CVE target list marked complete or waived with risk acceptance

## Security

- Production patching is high risk; require explicit window and approval.
- Use ansible-vault for become and SSH material; no passwords in version control.
- Cordon, drain, and worker reboot only inside the approved window.

## Pitfalls

- Unplanned `dist-upgrade` breaks application dependencies that were not in the CVE list.
- Rebooting a worker without cordon causes pod rescheduling storms during peak traffic.
- Running all production hosts in parallel creates a single point of failure for the entire tier.
- Check mode skips handlers, so a green check run does not prove reboot or service restart behavior.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Monthly security updates on Ubuntu web tier
- **Input:** Forty hosts in `inventory/web`, ticket PATCH-2026-11, staging canary `web-canary-01`
- **Prompt:**

```text
Plan check mode on staging canary then serial 10 percent production security updates only for PATCH-2026-11.
```

- **Expected result:**

```text
Scope: web tier, security updates only (ticket PATCH-2026-11).
Precheck: compare inventory count to CMDB; list sample apt versions for ticket packages.
Plan: staging --check --diff on web-canary-01, staging apply serial 1, prod batches of 10% with serial.
Approval: APPROVAL PATCH PROD required before any production ansible-playbook without --check.
Rollback: document package hold or AMI snapshot for rollback per batch.
Done: recap.json all ok, check log paths listed, zero failed hosts expected after apply.
```

### Example 2 (Example data (self-written))
- **Task:** Patch one Kubernetes worker with approved drain
- **Input:** Worker `k8s-worker-2`, drain approved in ticket PATCH-K8S-88, three-node pool
- **Prompt:**

```text
Draft cordon patch reboot uncordon sequence for worker k8s-worker-2 per ticket PATCH-K8S-88.
```

- **Expected result:**

```text
Scope: single worker k8s-worker-2 in approved drain window (PATCH-K8S-88).
Plan: kubectl cordon worker-2, ansible limit patch/reboot, uncordon, kubectl get pods -A on node.
Approval: drain window confirmation treated as patch approval; no cordon without ticket cite.
Verification: node Ready and workloads Running before next worker; playbook ok on worker-2.
Audit: log cordon/uncordon timestamps in ticket; do not delete the node object.
```