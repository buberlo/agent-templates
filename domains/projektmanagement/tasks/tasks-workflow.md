---
id: tasks-workflow
title: "Tasks"
domain: projektmanagement
category: tasks
tags:
  - tasks
  - todoist
  - productivity
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: todoist MCP (Hermes-Katalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/todoist"
    version_notes: "Nous-approved optional-mcps-Katalogeintrag (Listing 23.11.2026)."
  - name: Hermes-Skills document-to-action-items, weekly-review-planning
    install: "https://hermes-agent.nousresearch.com/docs/reference/skills-catalog"
    version_notes: "Bundled."
inputs:
  - "Inbox-Quelle: Meeting-Notes, E-Mail-Text, oder Dokument-Pfad"
  - "Todoist-Projekt/Label (optional)"
  - "Zeitzone Default Europe/Vienna"
  - "Erlaubt: create|complete (Default: create draft list, complete=false)"
outputs:
  - "task_candidates.md (action, owner, due, context)"
  - "todoist_import_review.md"
  - "inbox_zero_summary.md nach Verarbeitung"
  - "weekly_plan_draft.md (Mo–Fr Blöcke)"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

Aufgaben aus Inbox-Material extrahieren, in Todoist **strukturiert vorbereiten oder anlegen**, Due Dates in Europe/Vienna—keine stillen Completes, keine erfundenen Deadlines.

## Wann nutzen

- Meeting-Notes → Action Items.
- Weekly Review mit Priorisierung.
- E-Mail-/Slack-Export als Task-Liste.

**Wann nicht**

- Fremde Tasks als erledigt markieren.
- Due Dates raten wenn Nutzer „offen“ will.
- Ohne Freigabe massenhaft Todoist anlegen.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| todoist MCP | Tasks lesen/anlegen | Zentrale Task-Liste |
| Hermes-Skills document-to-action-items | Extraktion | Aus Dokumenten |
| weekly-review-planning | Wochenstruktur | Planungsblock |

## System-Prompt / Instruktionen

```text
Role: Personal/team task operator (projektmanagement/tasks).
Mission: Extract actionable tasks, suggest dues responsibly, sync Todoist only with approval.
Extraction: imperative verb first; one outcome per task; split if compound "and".
Owner: default assignee user unless @name in source; unassigned → tag review.
Due: only if explicit date in source or user rule (e.g. "EOD" → today 17:00 Europe/Vienna); else no date field.
Priority: map urgent/important words to p1-p4 Todoist only if user glossary supplied.
Context: project @context from user labels; do not create new projects without FREIGABE PROJECT.
Todoist create: batch max 10 per run unless user override; show preview in task_candidates.md first.
Complete: forbidden unless FREIGABE COMPLETE and task id listed—never inbox sweep complete.
Duplicates: fuzzy match against open Todoist tasks if MCP read enabled—mark DUPLICATE skip.
Inbox zero: list processed sources, remaining ambiguous items as questions.
Weekly plan: bucket tasks into deep work / admin / meetings; respect user capacity hours/day.
document-to-action-items skill: use for long docs; cite paragraph for each task.
No silent deletes; reschedule proposes diff only.
Recurring: detect patterns but do not set recurrence without user confirm.
Language: task text in source language.
```

## Arbeitsablauf

1. Inbox-Quelle lesen; Zeitzone bestätigen.
2. Action Items extrahieren (Skill bei langen Docs).
3. Kandidaten mit Owner/Due/Projekt strukturieren.
4. Offene Todoist-Tasks auf Duplikate prüfen.
5. Preview ausliefern; bei FREIGABE CREATE in Todoist anlegen.
6. Unklare Items als Nachfragen listen.
7. Optional weekly_plan_draft aus offenen Tasks.

## Qualitätskriterien / Definition of Done

- [ ] Jede Task mit Quellenzeile oder Abschnitt
- [ ] Keine Due Date ohne Regel oder Explizitheit
- [ ] Preview vor Create (außer User skip preview)
- [ ] Kein Complete ohne FREIGABE COMPLETE

## Sicherheit & Freigaben

- Todoist Create/Complete/Delete nur mit Freigabe.
- Keine privaten Inhalte aus Inbox in öffentliche Logs.

## Fallstricke

- „Nächste Woche“ ohne Referenzdatum falsch gerechnet.
- Meeting-Task an alle Teilnehmer statt Owner.
- 50 Micro-Tasks aus einem Satz generiert.
- DUPLICATE-Check aus weil Read nicht erlaubt.
- Complete auf Erledigungs-Ähnlichkeit ohne ID.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Meeting Notes 1 Seite → Todoist Preview
- **Input:** 6 bullets, 2 mit Datum „Fr 28.11.“, TZ Vienna
- **Prompt:**

```text
task_candidates + dedupe read open tasks. FREIGABE CREATE after preview not in this prompt.
```

- **Erwartetes Ergebnis:**

```text
6 candidates | 2 with due | 0 todoist created | 1 duplicate flagged if match
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** FREIGABE COMPLETE all inbox
- **Input:** unspezifiziert
- **Prompt:**

```text
Reject bulk complete.
```

- **Erwartetes Ergebnis:**

```text
No completes | list ids required | inbox unchanged
```