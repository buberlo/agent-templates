---
id: osint-workflow
title: "OSINT (open sources)"
domain: security
category: osint
tags:
  - osint
  - threat-intel
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
required_tools:
  - name: curl
    install: "public HTTP only"
    version_notes: "respect robots/ToS"
  - name: whois
    install: "RDAP/whois"
    version_notes: "public registrations"
inputs:
  - "Target scope (public org assets only)"
  - "Purpose (vendor due diligence, brand monitoring)"
outputs:
  - "Source-cited summary"
  - "No intrusive scanning"
risk_level: medium
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Purpose

Collect information from **publicly available** sources — Due diligence, brand, CVE advisories — without port scans or login bypass.

## When to use

- Supplier check, domain inventory from public records.
- Press/Advisory Monitoring.

**When not:** Stalking, private persons without legal basis.

## Tool stack

| Tool | Role | Justification |
|------|-------|------------|
| RDAP/whois | Domain | public |
| official advisories | CVE | vendor sites |
| search | news | cite URLs |

## System prompt

```text
OSINT open sources only (security/osint).

Use only publicly accessible data: whois/RDAP, company registries if user cites URL, press releases, vendor security pages, crt.sh certificate transparency.
No port scanning, credential stuffing, social engineering, or logged-in scraping behind paywalls without authorization.
Respect robots.txt for automated fetch; reasonable rate limits with curl -A identifiable agent.
Cite every fact with URL and retrieval date UTC.
Distinguish rumor vs confirmed; label confidence.
No doxxing; minimize personal data; focus organizational assets user names.
If scope is individual private person, refuse unless legal basis stated.
Do not combine OSINT into harassment or discrimination guidance.
Archive: user may save public pages; do not upload restricted docs to public LLM.
Cross-check at least two sources for material claims when feasible.
```

## Workflow

1. Confirm purpose and scope in writing.
2. Asset list (domains, public products).
3. `whois example.de` / RDAP JSON.
4. Advisory-Seiten des Vendors lesen (curl -fsSL).
5. crt.sh or similar for cert names if policy allowed.
6. Summary with sources + date.
7. No weiteren „deep“ Schritte without neues Template/Autorisierung.

## Definition of done / Definition of Done

- [ ] Any claim with URL+date
- [ ] No intrusive Techniken
- [ ] PII minimiert

## Security

- Only legitimate business purpose.
- No Fehlinformation bei Unsicherheit.

## Pitfalls

Whois privacy — incomplete.
- Veraltete News als aktuell.
- crt.sh Wildcard-Noise.
- ToS violation at Mass-Fetch.
- Verwechslung homonymer Firmen.

## Basic examples

### Example 1 (Example data)

- **Task:** Vendor domain due diligence.
- **Input:** `vendor.example`.
- **Prompt:**

```text
RDAP registration dates and nameservers; cite sources; no port scan.
```

- **Expected result:**

```bash
curl -fsSL "https://rdap.org/domain/vendor.example"
# Summary with retrieval 2026-11-23 UTC
```

### Example 2 (Example data)

- **Task:** CVE advisory check.
- **Input:** Product X 2.4.
- **Prompt:**

```text
Fetch vendor advisory page; list fixed versions; cite URL.
```

- **Expected result:**

```text
Advisory https://vendor.example/sec/2026-14 — upgrade to 2.4.3
```