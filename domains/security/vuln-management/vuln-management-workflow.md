---
id: vuln-management-workflow
title: "Vulnerability Management"
domain: security
category: vuln-management
tags:
  - vuln
  - cve
  - patching
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
required_tools:
  - name: grype / trivy
    install: "container/filesystem scan"
    version_notes: "SBOM optional"
  - name: osv-scanner
    install: "Go ecosystem"
    version_notes: "lockfile"
inputs:
  - "Asset inventory scope"
  - "SLA tiers (critical 7d etc.)"
outputs:
  - "Prioritized vuln list"
  - "Remediation tickets"
risk_level: medium
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Purpose

Consolidate vulnerabilities from scanners, prioritize them by **risk and SLA** and generate remediation tasks — no blind patch Friday.

## When to use

- Weekly VM cycle, according to Pentest report (authorized).
- Container-Image-Release-Gate.

**When not:** Exploit development.

## Tool stack

| Tool | Role | Justification |
|------|-------|------------|
| trivy | images/fs | CVE |
| osv-scanner | deps | lockfile |
| ticket system | track | SLA |

## System prompt

```text
Vulnerability management workflow (security/vuln-management).

Scan: trivy image <ref> --severity HIGH,CRITICAL; grype similarly.
Deps: osv-scanner --lockfile=package-lock.json.
Enrich with EPSS/exploit status only if user provides feed; do not invent exploitability.
Prioritize: internet exposure * severity * asset criticality; user supplies tiers.
Deduplicate CVE across layers (base image vs app).
Remediation: prefer upgrade path with version; workaround only with expiry date.
False positive: require scanner proof + vendor statement reference.
SLA breach list sorted by overdue days.
No active exploitation testing here.
Track ticket id per vuln cluster not per duplicate CVE line.
SBOM export optional CycloneDX for compliance evidence.
```

## Workflow

1. Scope-Assets liste (images, repos).
2. `trivy image ghcr.io/org/app:tag`.
3. `osv-scanner -r.` for Monorepo.
4. Merge findings; dedupe.
5. Priority according to SLA matrix.
6. Ticket per cluster with fixed proposal.
7. Re-scan nach Patch zur Verifikation.

## Definition of done

- [ ] Scanner-Befehle dokumentiert
- [ ] SLA-Tier pro Finding
- [ ] Re-scan Plan

## Security

- Scan-Reports vertraulich.
- Prod-Patching nach Change-Fenster.

## Pitfalls

- Nur CVSS, no Exposure.
- Base image fix vergessen.
- 500 identical CVE lines — grouping required.
- Won't-fix without Expiry.
- Scanner version stale CVE db.

## Basic examples

### Example 1 (Example data)

- **Task:** Image scan release gate.
- **Input:** `app:1.5.0`.
- **Prompt:**

```text
trivy HIGH/CRITICAL; block release if critical unfixed.
```

- **Expected result:**

```bash
trivy image app:1.5.0 --severity HIGH,CRITICAL
# 0 CRITICAL -> pass gate
```

### Example 2 (Example data)

- **Task:** npm osv backlog.
- **Input:** 12 highs overdue.
- **Prompt:**

```text
osv-scanner; group by package; SLA sort.
```

- **Expected result:**

```bash
osv-scanner -r .
# Ticket VM-88 lodash upgrade path
```