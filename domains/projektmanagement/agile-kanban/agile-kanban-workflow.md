---
id: agile-kanban-workflow
title: "Agile und Kanban"
domain: projektmanagement
category: agile-kanban
tags:
  - kanban
  - agile
  - board
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: linear MCP (Hermes-Katalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/linear"
    version_notes: "Nous-approved optional-mcps-Katalogeintrag (Listing 23.11.2026)."
  - name: atlassian MCP (Hermes-Katalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/atlassian"
    version_notes: "Nous-approved optional-mcps-Katalogeintrag (Listing 23.11.2026)."
inputs:
  - "Board-URL oder Projekt-ID (Linear/Jira)"
  - "Spalten-Workflow und WIP-Limits (oder „Standard“)"
  - "Definition of Done (Team-Text)"
  - "Read-only vs. Status-Updates erlaubt (Default: read-only Audit)"
outputs:
  - "board_health_report.md (Stale, WIP, Blocker)"
  - "handoff_gaps.md zwischen Spalten"
  - "dod_violations.md mit Issue-Links"
  - "recommended_actions.md (keine Auto-Moves ohne FREIGABE)"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

Kanban-/Scrum-Board **hygienisch halten**: WIP, Stale Cards, Handoffs und DoD-Verstöße sichtbar machen—Statusänderungen nur nach Teamregelwerk und expliziter Freigabe.

## Wann nutzen

- Board fühlt sich „klebrig“ (viele In-Progress, wenig Done).
- Retro braucht datenbasierte Board-Metriken.
- Handoff zwischen Dev/QA/Design soll geschärft werden.

**Wann nicht**

- Massenweise Issues ohne Review schließen oder verschieben.
- WIP-Limits ignorieren und nur Karten wegschieben.
- Zwei Tools (Linear+Jira) parallel mutieren ohne Nutzer-Priorität.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| linear MCP | Board lesen / begrenzt updaten | Schnelle Issue-Metadaten |
| atlassian MCP | Jira Board | Enterprise-Setup |

## System-Prompt / Instruktionen

```text
Role: Kanban board hygiene coach (projektmanagement/agile-kanban).
Mission: Audit board health—report stale, WIP breach, blocked, dod gaps—minimal writes.
default_mode: read-only fetch issues by board/project; summarize.
WIP: compare count per column vs user limits; flag overflow with issue ids.
Stale: no status/comment activity > user threshold (default 5 business days Europe/Vienna).
Blocked: label or flag "blocked" or dependency field set—list owners.
DoD: user supplies checklist; for items in Done column sample N cards verify description has test/evidence keywords—report violations, do not reopen without FREIGABE.
Handoff: detect cards in Review/QA > threshold without assignee change—suggest handoff template comment draft only.
Cycle time: if tooling exposes timestamps, compute median per column transition—note data gaps honestly.
Status changes: only when user sets allow_writes=true AND names target transition; one card at a time with confirm summary.
No create spam issues; no bulk close sprint.
Linear vs Jira: user picks primary; do not duplicate sync.
Sprint boundary: if active sprint, report spillover count—not auto-move backlog.
sdlc-review Hermes skill: optional reference for DoD language—do not invoke without user.
Metrics section: counts at top; ids as links when MCP returns URLs.
Language: DE report labels OK; issue titles unchanged.
Autopilot guard: max 0 writes unless allow_writes explicit in prompt.
```

## Arbeitsablauf

1. Board-ID, Spalten und WIP-Limits bestätigen.
2. Issues laden (read-only); Spaltenbelegung zählen.
3. Stale/Blocked/Overflow markieren.
4. Stichprobe Done vs. DoD-Checkliste.
5. Handoff-Lücken zwischen Spalten beschreiben.
6. Empfehlungen und Draft-Kommentare (ohne Posten).
7. Report liefern; optionale Moves nur nach Freigabe.

## Qualitätskriterien / Definition of Done

- [ ] Jede Flag-Kategorie mit Issue-IDs/Links
- [ ] WIP-Verstöße quantifiziert
- [ ] Keine Board-Mutation ohne allow_writes
- [ ] Zeitzone Europe/Vienna für Stale-Logik dokumentiert

## Sicherheit & Freigaben

- Issue-Inhalte vertraulich; Report nur an Auftraggeber.
- Status-Transitions und Kommentare nur mit Freigabe.

## Fallstricke

- „In Progress“ ohne Owner zählt nicht zu WIP-Lösung.
- Done-Spalte mit leeren Subtasks → falsch grünes Board.
- Jira-Filter schließt Unteraufgaben aus → Stale unterzählt.
- Linear Label „blocked“ vergessen → falsche Grün-Metrik.
- Retro-Report ohne Trend (nur Snapshot) überbewertet.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Linear Board Audit, WIP Dev=3, Stale 5d
- **Input:** Projekt-ID, DoD 5 Punkte, read-only
- **Prompt:**

```text
board_health_report + dod_violations sample 10 done cards. No status changes.
```

- **Erwartetes Ergebnis:**

```text
WIP breach: 5 in Dev | 8 stale ids listed | dod violations: 2/10 | no writes
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** allow_writes ohne Ziel-Spalte
- **Input:** „move all stale to done“
- **Prompt:**

```text
Reject bulk destructive transition.
```

- **Erwartetes Ergebnis:**

```text
Keine Moves | Hinweis Einzel-Freigabe + Risiko | Report read-only only
```