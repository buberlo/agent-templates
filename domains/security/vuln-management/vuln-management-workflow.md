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

## Zweck

Schwachstellen aus Scannern konsolidieren, nach **Risiko und SLA** priorisieren und Remediation-Tasks erzeugen — kein blindes Patch-Friday.

## Wann nutzen

- Wöchentliche VM-Zyklus, nach Pentest-Report (authorized).
- Container-Image-Release-Gate.

**Wann nicht:** Exploit-Entwicklung.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| trivy | images/fs | CVE |
| osv-scanner | deps | lockfile |
| ticket system | track | SLA |

## System-Prompt / Instruktionen

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

## Arbeitsablauf

1. Scope-Assets liste (images, repos).
2. `trivy image ghcr.io/org/app:tag`.
3. `osv-scanner -r .` für Monorepo.
4. Merge findings; dedupe.
5. Priorität nach SLA-Matrix.
6. Ticket pro Cluster mit Fix-Vorschlag.
7. Re-scan nach Patch zur Verifikation.

## Qualitätskriterien / Definition of Done

- [ ] Scanner-Befehle dokumentiert
- [ ] SLA-Tier pro Finding
- [ ] Re-scan Plan

## Sicherheit & Freigaben

- Scan-Reports vertraulich.
- Prod-Patching nach Change-Fenster.

## Fallstricke

- Nur CVSS, keine Exposure.
- Base image fix vergessen.
- 500 gleiche CVE Zeilen — Gruppierung nötig.
- Won't-fix ohne Expiry.
- Scanner version stale CVE db.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Image scan release gate.
- **Input:** `app:1.5.0`.
- **Prompt:**

```text
trivy HIGH/CRITICAL; block release if critical unfixed.
```

- **Erwartetes Ergebnis:**

```bash
trivy image app:1.5.0 --severity HIGH,CRITICAL
# 0 CRITICAL -> pass gate
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** npm osv backlog.
- **Input:** 12 highs overdue.
- **Prompt:**

```text
osv-scanner; group by package; SLA sort.
```

- **Erwartetes Ergebnis:**

```bash
osv-scanner -r .
# Ticket VM-88 lodash upgrade path
```