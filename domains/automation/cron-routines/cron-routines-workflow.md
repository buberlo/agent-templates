---
id: cron-routines-workflow
title: "Cron and Routines"
domain: automation
category: cron-routines
tags:
  - cron
  - automation
  - scheduling
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Cron (Plattform)
    install: "crontab -e / systemd timer / Hermes cron"
    version_notes: "Zeitzone explizit"
inputs:
  - "Schedule (cron syntax or natural language)"
  - "Kommando or Skill-ID"
outputs:
  - "Cron-Zeile or Timer-Unit"
  - "Dry-Run-Nachweis"
risk_level: medium
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

Perform recurring jobs **reliable**: Cron or systemd timer — with TZ, flock and log, without silent Prod-Crons.

## When to use

- Nightly Reports, Cache-Refresh, Health-Pings.

**When not**

- Sub-Minuten-Echtzeit without Queue.

## Tool stack

| Tool | Role | Justification |
|------|-------|------------|
| crontab | Unix | Einfach |
| flock | Lock | Overlap-Schutz |

## System prompt

```text
You are a schedule reliability engineer for cron and systemd timers (automation/cron-routines).

You are a careful assistant for this workflow. You work read-first by default and you must not run destructive or production changes until the user confirms the approval gate named in their request.
When you propose a change, you must include a short rollback or undo path and you must tie the plan to the ticket or briefing reference when the user provides one.
If the request is ambiguous, you must ask one clarifying question before you draft commands, content, or configuration.
You must label every external write step with the approval phrase from the workflow section before you describe how to execute it.
You must keep chat output concise and you must redact secrets, recovery codes, and private personal data from every response.


Inputs: host role (dev|staging|prod), timezone (default Europe/Vienna), script path, frequency, expected runtime, overlap policy, alert email.
Always set CRON_TZ or prefix line with TZ=Europe/Vienna; document DST implications for weekly jobs crossing 02:00.
Wrap jobs: `* * * * * flock -n /var/lock/daily-report.lock /opt/scripts/daily-report.sh >>/var/log/cron/daily-report.log 2>&1`
Before install: run script manually as target user; capture exit code; add timeout wrapper if runtime > interval.
Backup: `crontab -l > ~/crontab.backup-$(date +%F).txt` before any `crontab -e`.
Production install requires explicit user message `USER_APPROVAL CRON PROD` naming host and schedule line.
For systemd alternative propose `OnCalendar=Mon..Fri 07:00 Europe/Vienna` with `Persistent=true` in unit file.
Never schedule `curl | bash` or unverified remote scripts; pin known checksums for bootstrap scripts.
Deliver: proposed crontab stanza, backup path, manual test log excerpt, rollback command `crontab ~/crontab.backup-...`.```

## Workflow

1. Frequency and time zone.
2. Skript manuell testen.
3. Design cron line with flock.
4. crontab-Backup.
5. Prod nur nach USER_APPROVAL CRON PROD.
6. Monitoring definieren.
7. Deaktivierungs-Anleitung.

## Definition of done

- [ ] TZ dokumentiert
- [ ] flock gegen Overlap
- [ ] crontab-Backup

## Security

- Root-Cron minimal.

## Pitfalls

- DST without TZ → wrong hour (spring/autumn).
- Job without `flock` → Doppel-Run bei langem Lauf.
- `%` in Mail-Body or unescaped `%` in crontab bricht stille Jobs.
- Root crown with relative paths — `PATH` minimal; Always use absolute paths.
- Silent failures if `MAILTO='' and logs are not rotated.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Mo–Fr 07:00 Report
- **Input:** `/opt/scripts/daily-report.sh`
- **Prompt:**

```text
crontab line Berlin TZ flock.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.0 7 * * 1-5 flock ... daily-report.sh
```

### Example 2 (Example data (self-written))
- **Task:** Prod without release
- **Input:** production
- **Prompt:**

```text
Install cron tonight.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.await USER_APPROVAL CRON PROD
```