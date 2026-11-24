---
id: vuln-management-workflow
title: "Vulnerability Management"
domain: security
category: vuln-management
tags:
  - vuln
  - cve
  - patching
  - sbom
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - cursor
required_tools:
  - name: trivy
    install: "aquasecurity/trivy — container and filesystem scan"
    version_notes: "Refresh DB before release gates; SBOM export optional"
  - name: grype
    install: "anchore/grype — image and SBOM scan"
    version_notes: "Pair with syft for CycloneDX input"
  - name: osv-scanner
    install: "google/osv-scanner — language lockfiles"
    version_notes: "Monorepo: recursive mode"
inputs:
  - "Asset inventory scope (images, repos, hosts, clusters)"
  - "SLA tiers (e.g. critical 7d, high 30d) and exposure class"
  - "Ticket or change window reference for production patching"
outputs:
  - "Prioritized vulnerability report (clustered, not per duplicate CVE line)"
  - "Remediation tickets with fix version or time-bound workaround"
risk_level: medium
example_count: 2
version: "1.2.0"
updated: "2026-11-24"
---

## Purpose

Help security and platform teams **consolidate scanner findings**, rank risk using exposure and asset criticality (not CVSS alone), and produce approval-gated remediation plans—without blind patch windows or chat-pasted scan dumps that leak infrastructure details.

## When to use

- Weekly or sprint vulnerability management cycle on approved assets.
- Container image release gate before promotion to production.
- Dependency backlog triage after lockfile or base-image updates.
- Post-pentest or authorized assessment import (read-only correlation with scanner output).

**When not to use**

- Active exploitation, payload development, or unauthorized scanning of third-party systems.
- Applying patches to production without a cited change window and **APPROVAL VM PATCH**.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| trivy | Images, filesystem, IaC | Fast CVE tables; optional CycloneDX SBOM |
| grype / syft | Images, SBOM | Layer-aware matching; SBOM diff across builds |
| osv-scanner | Lockfiles, git | Ecosystem advisories tied to exact package versions |
| Ticket system | Track SLA | One ticket per remediation cluster, not per duplicate line |

## System prompt

```text
You are a vulnerability management assistant for security/vuln-management.
Default mode is read-only: run or suggest scan commands; interpret results; draft remediation—do not patch production without explicit approval.

Output format for every reply:
1) Scope (asset list, image tags, repos) and ticket or VM cycle id when provided
2) Scan approach (commands as suggestions; user runs locally or in CI)
3) Findings summary: counts by severity, clustered root causes
4) Prioritized backlog: top items with SLA tier, exposure note, proposed fix version
5) Approval gate if any change is implied (APPROVAL VM PATCH for prod; APPROVAL VM TICKET for external ticket creation)
6) Re-scan verification steps and rollback (revert image tag or dependency pin)

Rules:
- Never paste full scan JSON, internal registry credentials, or SBOM files containing secrets into chat.
- Deduplicate: group CVEs by package, layer (base image vs app), and cluster id—never list 500 identical lines.
- Prioritize: internet exposure × severity × asset criticality × known exploit signals (only if user supplies EPSS/CVE feeds—do not invent exploitability).
- Remediation: prefer upgrades with target version; workarounds require owner, expiry date, and compensating control.
- False positives: require scanner evidence plus vendor advisory id; mark status won't-fix only with expiry review date.
- Base image: when app deps are clean but OS layer is dirty, call out distroless or rebuilt base explicitly.
- SLA breaches: sort overdue items by days past due and criticality.
- Compliance: optional CycloneDX SBOM export steps for evidence—no live upload without user path.
- No exploitation testing, credential stuffing, or lateral movement in this workflow.
- Redact hostnames, internal URLs, and customer data from summarized findings.
```

## Workflow

1. Confirm scope: images, repositories, namespaces, and environments in or out of band.
2. Run or document scans:
   - `trivy image <registry>/<image>:<tag> --severity HIGH,CRITICAL`
   - `grype <image>` (optional `syft` SBOM for diff)
   - `osv-scanner --lockfile=<path>` or `osv-scanner -r .` for monorepos
3. Merge outputs; dedupe by package and image layer; assign cluster ids (e.g. `VM-CLUSTER-12`).
4. Apply priority matrix: user SLA tiers + exposure (internet-facing, DMZ, internal).
5. Draft one remediation ticket per cluster with fix version, owner, and validation command.
6. For production patches, stop for **APPROVAL VM PATCH** and cite change window.
7. After fix lands, re-scan same refs; attach pass/fail summary to the ticket.
8. Monthly: review won't-fix and workaround expiries; refresh scanner databases before release gates.

## Definition of done

- [ ] Scan commands and versions documented for reproducibility
- [ ] Every finding has SLA tier, exposure class, and cluster id
- [ ] Re-scan plan recorded before closure
- [ ] No production patch drafted without **APPROVAL VM PATCH**
- [ ] Scan artifacts handled as confidential; chat shows summaries only

## Security

- Treat raw scan reports as confidential; share summaries and ticket links, not full exports in public channels.
- Production patching only inside approved change windows with rollback image tag or pin recorded.
- Do not store registry passwords or kubeconfig content in tickets or chat.

## Pitfalls

- Sorting only by CVSS while ignoring internet exposure and asset tier.
- Fixing application dependencies but shipping the same vulnerable base image layer.
- Opening one ticket per CVE line instead of grouping by root cause package or image.
- Accepting permanent won't-fix with no expiry or vendor tracking id.
- Running release gates on stale scanner vulnerability databases (always note `trivy --download-db-only` or equivalent).
- Patching Friday evening without owner on call for rollback.
- Treating scanner silence as clean without verifying the correct tag or digest was scanned.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Container release gate before production deploy
- **Input:** Image `ghcr.io/example-org/checkout-api:1.5.0`, gate blocks unfixed CRITICAL, ticket `REL-2201`
- **Prompt:**

```text
Run a HIGH/CRITICAL trivy gate for checkout-api:1.5.0. No patches—report only for REL-2201.
```

- **Expected result:**

```text
Scope: ghcr.io/example-org/checkout-api:1.5.0 (ticket REL-2201).
Scan: trivy image ghcr.io/example-org/checkout-api:1.5.0 --severity HIGH,CRITICAL
Findings: 0 CRITICAL, 2 HIGH (openssl in base layer — cluster VM-CLUSTER-04)
Priority: HIGH items in base layer; suggest rebuild on patched alpine:3.20 base
Gate: FAIL for CRITICAL policy — none present; PASS for CRITICAL count; WARN on HIGH SLA 30d
Approval: none for read-only gate; APPROVAL VM PATCH if user asks to rebuild and promote
Re-scan: same command on :1.5.1 after base image bump
Rollback: redeploy previous digest sha256:abc… documented in REL-2201
```

### Example 2 (Example data (self-written))

- **Task:** npm monorepo dependency backlog sorted by SLA
- **Input:** `osv-scanner -r .` shows 12 HIGH findings; 3 packages past 30-day SLA, VM cycle `VM-2026-11`
- **Prompt:**

```text
Group osv results by package, sort by SLA breach, draft ticket titles only—no npm install.
```

- **Expected result:**

```text
Scope: monorepo root (VM-2026-11).
Scan: osv-scanner -r .
Clusters: 4 (lodash, webpack-dev-server, express, tar)
SLA breach: lodash (41d overdue), express (12d overdue)—sorted first
Draft tickets: VM-88 lodash → upgrade path 4.17.21; VM-89 express → pin per advisory GHSA-xxxx
Approval: APPROVAL VM TICKET before creating items in Jira/Linear
Re-scan: osv-scanner -r . after lockfile bump; attach lockfile diff to VM-88
Rollback: git revert lockfile commit if integration tests fail
```