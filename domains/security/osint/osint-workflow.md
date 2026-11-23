---
id: osint-workflow
title: "OSINT (offen zugängliche Quellen)"
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

## Zweck

Informationen aus **öffentlich zugänglichen** Quellen sammeln — Due Diligence, Brand, CVE-Advisories — ohne Port-Scans oder Login-Umgehung.

## Wann nutzen

- Lieferanten-Check, Domain-Inventar aus öffentlichen Records.
- Press/Advisory Monitoring.

**Wann nicht:** Stalking, private Personen ohne Rechtsgrundlage.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| RDAP/whois | Domain | public |
| official advisories | CVE | vendor sites |
| search | news | cite URLs |

## System-Prompt / Instruktionen

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

## Arbeitsablauf

1. Zweck und Scope schriftlich bestätigen.
2. Asset-Liste (Domains, öffentliche Produkte).
3. `whois example.de` / RDAP JSON.
4. Advisory-Seiten des Vendors lesen (curl -fsSL).
5. crt.sh oder ähnlich für cert names wenn policy erlaubt.
6. Zusammenfassung mit Quellen + Datum.
7. Keine weiteren „deep“ Schritte ohne neues Template/Autorisierung.

## Qualitätskriterien / Definition of Done

- [ ] Jede Behauptung mit URL+Datum
- [ ] Keine intrusive Techniken
- [ ] PII minimiert

## Sicherheit & Freigaben

- Nur legitimer Geschäftszweck.
- Keine Fehlinformation bei Unsicherheit.

## Fallstricke

- whois privacy — unvollständig.
- Veraltete News als aktuell.
- crt.sh Wildcard-Noise.
- ToS-Verstoß bei Mass-Fetch.
- Verwechslung homonymer Firmen.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Vendor domain due diligence.
- **Input:** `vendor.example`.
- **Prompt:**

```text
RDAP registration dates and nameservers; cite sources; no port scan.
```

- **Erwartetes Ergebnis:**

```bash
curl -fsSL "https://rdap.org/domain/vendor.example"
# Summary with retrieval 2026-11-23 UTC
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** CVE advisory check.
- **Input:** Product X 2.4.
- **Prompt:**

```text
Fetch vendor advisory page; list fixed versions; cite URL.
```

- **Erwartetes Ergebnis:**

```text
Advisory https://vendor.example/sec/2026-14 — upgrade to 2.4.3
```