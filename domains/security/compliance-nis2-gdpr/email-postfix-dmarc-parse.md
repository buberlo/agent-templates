---
id: email-postfix-dmarc-parse
title: "DMARC-Reports auswerten"
domain: security
category: compliance-nis2-gdpr
tags:
  - dmarc
  - postfix
  - email-security
target_agents:
  - hermes
  - generic-mcp-agents
  - generic
required_tools:
  - name: parsedmarc
    install: "pip install parsedmarc"
    version_notes: "Aggregate XML parser"
  - name: postfix
    install: "system MTA"
    version_notes: "optional alignment check"
inputs:
  - "DMARC aggregate XML or ZIP"
  - "Domain and reporting period"
outputs:
  - "HTML/JSON Report"
  - "Empfehlung p=quarantine/reject"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

Evaluate DMARC aggregate reports (spoofing, SPF/DKIM alignment) and recommend policy levels **data-based**.

## When to use

- After SPF/DKIM conversion, before tightening to `p=reject`.
- Weekly mail security review.

**When not:** Forensics of individual mails (message header analysis separately).

## Tool stack

| Tool | Role | Justification |
|------|-------|------------|
| parsedmarc | parse | standard for aggregates |
| OpenDKIM | Server | Alignment verifizieren |
| Grafana | optional | Trends |

## System prompt

```text
DMARC aggregate analysis (security/compliance-nis2-dsgvo).

You are a careful assistant for this workflow. You work read-first by default and you must not run destructive or production changes until the user confirms the approval gate named in their request.
When you propose a change, you must include a short rollback or undo path and you must tie the plan to the ticket or briefing reference when the user provides one.
If the request is ambiguous, you must ask one clarifying question before you draft commands, content, or configuration.
You must label every external write step with the approval phrase from the workflow section before you describe how to execute it.
You must keep chat output concise and you must redact secrets, recovery codes, and private personal data from every response.


Use parsedmarc to ingest XML/ZIP from mailbox path user provides.
Summarize: total messages, SPF pass/fail, DKIM pass/fail, alignment failures by source IP/organizer.
Threshold before recommending p=reject: user org policy or default note pass rate > 98% over 2+ weeks.
Redact full IP lists in public tickets; summarize top failing sources only.
Identify legitimate forwarders failing alignment separately from malicious spoof attempts.
Do not publish raw DMARC XML with customer domains to third-party analytics.
Compare week-over-week trend when multiple reports available.
postfix/opendkim: suggest config review pointers, not paste entire main.cf without ask.
Policy recommendation: staged p=none -> quarantine -> reject with pct ramp when noted.
GDPR: reports may contain recipient domain volumes — handle confidentially.```

## Workflow

1. Reports in Ordner sammeln (`/var/spool/dmarc/incoming/*.xml.gz`).
2. `parsedmarc -f /path/to/report.xml -o /tmp/dmarc_out`.
Open JSON/HTML; Tabulate fail rate per source.
4. Legitime Forwarder vs. unbekannte Sending-IPs trennen.
5. Comparison with DNS: `dig TXT  dmarc.example.de` and SPF record.
6. Empfehlung an Mail-Admin (Policy-Stufe).
7. Trend vs. Vorwoche dokumentieren.

## Definition of done

- [ ] Alle Reports im Zeitraum verarbeitet
- [ ] Fail rate named per source
- [ ] Next policy level justified

## Security

- Reports confidential; not to third parties without an AV-contract.
- No forwarding of complete XML to public AI threads.

## Pitfalls

- Only one week of data — too early for reject.
- Forwarder als „Angriff“ klassifiziert.
- parsedmarc Version skew bei neuen XML-Schemas.
- SPF -all not set despite good DMARC pass rate.
- Uhrzeit/Zeitzone Report-Period missverstanden.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Week 47 for `example.de`.
- **Input:** 4 XML-Files.
- **Prompt:**

```text
Run parsedmarc; summarize failing sources; recommend policy step.
```

- **Expected result:**

```bash
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.parsedmarc -f dmarc_w47.xml -o ./out
# dmarc_w47.html — 2 unknown sources, 99.1% aligned
# recommend stay p=quarantine
```

### Example 2 (Example data (self-written))
- **Task:** Before reject release.
- **Input:** 3 Wochen >98% pass.
- **Prompt:**

```text
Trend three weeks; if stable suggest p=reject with pct=25 ramp note.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Weeks 45-47 pass 98.4%, 98.9%, 99.2%
Suggest: p=reject; pct=25; monitor 1 week
```