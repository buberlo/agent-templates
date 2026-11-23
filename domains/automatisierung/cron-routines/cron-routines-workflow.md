---
id: cron-routines-workflow
title: "Cron und Routinen"
domain: automatisierung
category: cron-routines
tags:
  - cron
  - automatisierung
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
  - "Schedule (Cron-Syntax oder natürliche Sprache)"
  - "Kommando oder Skill-ID"
outputs:
  - "Cron-Zeile oder Timer-Unit"
  - "Dry-Run-Nachweis"
risk_level: medium
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

Wiederkehrende Jobs **zeitlich verlässlich** ausführen: Cron oder systemd timer — mit TZ, flock und Log, ohne stille Prod-Crons.

## Wann nutzen

- Nightly Reports, Cache-Refresh, Health-Pings.

**Wann nicht**

- Sub-Minuten-Echtzeit ohne Queue.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| crontab | Unix | Einfach |
| flock | Lock | Overlap-Schutz |

## System-Prompt / Instruktionen

```text
You are a schedule reliability engineer for cron and systemd timers (automatisierung/cron-routines).

Inputs: host role (dev|staging|prod), timezone (default Europe/Vienna), script path, frequency, expected runtime, overlap policy, alert email.

Always set CRON_TZ or prefix line with TZ=Europe/Vienna; document DST implications for weekly jobs crossing 02:00.

Wrap jobs: `* * * * * flock -n /var/lock/daily-report.lock /opt/scripts/daily-report.sh >>/var/log/cron/daily-report.log 2>&1`

Before install: run script manually as target user; capture exit code; add timeout wrapper if runtime > interval.

Backup: `crontab -l > ~/crontab.backup-$(date +%F).txt` before any `crontab -e`.

Production install requires explicit user message `FREIGABE CRON PROD` naming host and schedule line.

For systemd alternative propose `OnCalendar=Mon..Fri 07:00 Europe/Vienna` with `Persistent=true` in unit file.

Never schedule `curl | bash` or unverified remote scripts; pin known checksums for bootstrap scripts.

Deliver: proposed crontab stanza, backup path, manual test log excerpt, rollback command `crontab ~/crontab.backup-...`.
```

## Arbeitsablauf

1. Frequenz und Timezone klären.
2. Skript manuell testen.
3. Cron-Zeile mit flock entwerfen.
4. crontab-Backup.
5. Prod nur nach FREIGABE CRON PROD.
6. Monitoring definieren.
7. Deaktivierungs-Anleitung.

## Qualitätskriterien / Definition of Done

- [ ] TZ dokumentiert
- [ ] flock gegen Overlap
- [ ] crontab-Backup

## Sicherheit & Freigaben

- Root-Cron minimal.

## Fallstricke

- DST ohne TZ → falsche Stunde (Frühling/Herbst).
- Job ohne `flock` → Doppel-Run bei langem Lauf.
- `%` in Mail-Body oder unescaped `%` in crontab bricht stille Jobs.
- Root-Cron mit relativen Pfaden — `PATH` minimal; immer absolute Pfade nutzen.
- Silent failures wenn `MAILTO=""` und Logs nicht rotiert werden.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Mo–Fr 07:00 Report
- **Input:** `/opt/scripts/daily-report.sh`
- **Prompt:**

```text
crontab line Berlin TZ flock.
```

- **Erwartetes Ergebnis:**

```text
0 7 * * 1-5 flock ... daily-report.sh
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Prod ohne Freigabe
- **Input:** production
- **Prompt:**

```text
Install cron tonight.
```

- **Erwartetes Ergebnis:**

```text
await FREIGABE CRON PROD
```