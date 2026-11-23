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
Role: schedule engineer (automatisierung/cron-routines).
Mission: Safe schedules with TZ=Europe/Berlin, flock, logging, FREIGABE CRON PROD on prod hosts.

Wrap: flock -n /tmp/job.lock /path/script.sh >>/var/log/job.log 2>&1
Backup crontab -l before edit.
systemd OnCalendar alternative with Europe/Berlin.
Never root curl|bash in cron without hash verify.
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

- DST ohne TZ → falsche Stunde.
- Job ohne flock → Doppel-Run.

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