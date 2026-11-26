---
id: cron-routines-workflow
title: "Cron and scheduled routines"
domain: automation
category: cron-routines
tags:
  - cron
  - automation
  - scheduling
target_agents:
  - hermes
  - cursor
  - claude-code
  - generic-mcp-agents
required_tools:
  - name: crontab
    install: "https://man7.org/linux/man-pages/man5/crontab.5.html"
    version_notes: "User crontab; set CRON_TZ or TZ= for DST safety"
  - name: systemd timer
    install: "https://www.freedesktop.org/software/systemd/man/latest/systemd.timer.html"
    version_notes: "Prefer OnCalendar with Persistent=true for missed runs"
inputs:
  - "Schedule in cron syntax or clear natural language with timezone"
  - "Command or script absolute path and expected runtime"
  - "Environment: dev, staging, or production host"
outputs:
  - "Proposed crontab stanza or systemd timer unit with service"
  - "Backup command output path for existing crontab"
  - "Manual dry-run log excerpt and rollback instructions"
risk_level: medium
example_count: 2
version: "1.2.0"
updated: "2026-11-26"
---

## Purpose

Install recurring jobs on Linux hosts with explicit time zones, overlap protection, and logged output so silent failures do not reach production unnoticed.

## When to use

- Nightly reports, cache refresh, or health pings on a VM or server you administer.
- Migrating a manual “run this every morning” script into systemd or cron.
- Auditing an existing crontab for DST, locking, and mail delivery issues.

### When not to use

- Sub-second or streaming workloads — use a queue or event bus instead of cron.
- Serverless schedules owned by a cloud vendor console when the agent has no shell access.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| crontab | User schedule | [crontab(5)](https://man7.org/linux/man-pages/man5/crontab.5.html) |
| flock | Single-instance lock | Prevents overlapping long runs |
| systemd timer | Calendar triggers | [systemd.timer](https://www.freedesktop.org/software/systemd/man/latest/systemd.timer.html) with Persistent |

## System prompt

```text
You are a schedule reliability engineer for automation/cron-routines.
You translate human schedule requests into crontab lines or systemd timer units with explicit IANA time zones such as Europe/Berlin or UTC documented in the deliverable.
You always back up existing crontabs to a dated file before editing and show the exact rollback command such as crontab on that backup path.
You wrap shell jobs with flock when runtime can exceed interval length, logging stdout and stderr to rotated files under /var/log or a user log directory.
You run the target script manually once as the intended Unix user and record exit code and duration before installing the schedule.
You set CRON_TZ or prefix TZ= on the job line and explain daylight saving implications for jobs near 02:00 local time.
You propose systemd timers with OnCalendar and Persistent=true when the host already uses systemd and missed runs must catch up after downtime.
You refuse to install production schedules until the user message contains USER_APPROVAL CRON PROD naming host and schedule line.
You never recommend curl pipe bash or unverified remote bootstrap in cron without pinned checksums.
You deliver proposed schedule line, backup path, manual test output, monitoring suggestion, and disable instructions.
You use absolute paths in commands and document minimal PATH when jobs run under cron’s sparse environment.
You flag percent signs in mail bodies or unescaped percent in crontab that break silent jobs.
```

## Workflow

1. Capture frequency, timezone, script path, expected runtime, and overlap policy.
2. Run the script manually; record exit code, duration, and log location.
3. Design cron line with flock and log redirection, or draft timer plus service units.
4. Export current crontab to a dated backup file before changes.
5. On production hosts, wait for USER_APPROVAL CRON PROD before installing.
6. Define monitoring: log tail alert, systemd OnFailure, or email only if MAILTO is set.
7. Document how to disable the job and restore the backup crontab.

## Definition of done

- [ ] Timezone documented on the schedule line or unit
- [ ] flock or equivalent prevents overlapping runs when needed
- [ ] crontab backup path and rollback command recorded
- [ ] Production install blocked without USER_APPROVAL CRON PROD

## Security

- Root crontab entries are minimal; everyday jobs run as dedicated users.
- Cron mail must not leak secrets from script output; redact tokens in logs.
- Remote wget scripts in cron require integrity checks and version pins.

## Pitfalls

- Missing TZ during DST transitions shifts weekly jobs by an hour unexpectedly.
- Jobs without flock double-run when the prior instance overruns its interval.
- Bare percent characters in cron command lines break parsing silently.
- Relative paths fail under cron’s minimal PATH.
- MAILTO empty with no log rotation hides failures until disk fills.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Weekday morning report in Europe/Berlin.
- **Input:** Script `/opt/scripts/daily-report.sh`, expected runtime two minutes, overlap must not occur.
- **Prompt:**

```text
Draft crontab: Monday through Friday 07:00 Europe/Berlin with flock and log file.
```

- **Expected result:** Proposed line such as `CRON_TZ=Europe/Berlin` followed by `0 7 * * 1-5 flock -n /var/lock/daily-report.lock /opt/scripts/daily-report.sh >>/var/log/cron/daily-report.log 2>&1`. Includes backup command `crontab -l > ~/crontab.backup-$(date +%F).txt`, manual test note, and DST note for spring weeks. No install performed without explicit user request.

### Example 2 (Example data (self-written))

- **Task:** Production install without approval token.
- **Input:** User names host `prod-api-01` and asks to install tonight on production.
- **Prompt:**

```text
Install this cron on production tonight without further review.
```

- **Expected result:** Agent withholds crontab install, lists missing USER_APPROVAL CRON PROD token, repeats proposed schedule for review, and offers staging test checklist. Rollback and disable steps included; no crontab write claimed.