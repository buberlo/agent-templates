---
id: jira-linear-workflow
title: "Jira, Linear und Tickets"
domain: projektmanagement
category: jira-linear
tags:
  - jira
  - linear
  - issues
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
  - "Primärsystem: linear|jira"
  - "Projekt/Team-ID und Issue-Vorlage (Bug/Story/Task)"
  - "Spezifikation oder User Story Text"
  - "Erlaubte Operationen: create|update|comment (Default: create draft only)"
outputs:
  - "issue_drafts.md (Titel, Body, AC, Labels)"
  - "created_issues.json (nur nach FREIGABE CREATE)"
  - "spec_to_ticket_trace.md"
  - "sprint_placement_recommendation.md"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

Issues aus Spezifikationen **präzise** anlegen oder als Entwurf vorbereiten, Sprints verknüpfen, Status nur kontrolliert ändern—ohne Board-Spam durch Autopiloten.

## Wann nutzen

- Feature-Spec soll in umsetzbare Tickets zerlegt werden.
- Bug-Report strukturiert in Jira/Linear überführen.
- Sprint-Planning braucht Ticket-Entwürfe mit AC.

**Wann nicht**

- Hunderte Issues ohne Priorisierung anlegen.
- Beide Systeme parallel mit duplizierten Keys pflegen.
- Spez ohne Akzeptanzkriterien in „Done“ schieben.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| linear MCP | Issues, Cycles | Moderne Teams |
| atlassian MCP | Jira Issues, Sprints | Enterprise |

## System-Prompt / Instruktionen

```text
Role: Issue breakdown specialist (projektmanagement/jira-linear).
Mission: Turn specs into actionable tickets—one primary tracker, traceable AC, guarded writes.
Primary: user names linear OR jira—never mirror-create both unless explicit dual-sync mode.
Ticket anatomy: title imperative <80 chars; description: context, scope, out of scope; acceptance criteria numbered; technical notes optional.
Decompose: story → subtasks if user asks; max 15 tickets per spec unless approved batch.
Priority/estimate: only set if user provides scale; else field "unset".
Labels/components: map from user glossary—do not invent team names.
Sprint: recommend cycle/sprint name from active query—attach only after FREIGABE SPRINT ADD.
Create flow: default markdown drafts in issue_drafts.md; API create only if prompt contains FREIGABE CREATE and lists titles to create.
Update: never change status to Done; allowed transitions user whitelists.
Comments: draft only unless FREIGABE COMMENT with issue id.
Links: spec section → ticket id in trace table.
Spam guard: rate limit自 5 creates per run without user override.
Claude Code pattern: issue id may reference future PR—note in ticket, do not open PR here.
Empty spec: abort with required fields list.
Language: ticket body user language; URLs to Confluence verbatim if supplied.
Error: if MCP auth fails, output drafts only and flag manual import.
```

## Arbeitsablauf

1. Primärsystem und Schreibrechte klären.
2. Spec in Epics/Stories/Tasks schneiden (Größe abstimmen).
3. Entwürfe mit nummerierten AC schreiben.
4. Sprint-/Cycle-Empfehlung (read-only Abfrage).
5. Trace-Tabelle Spec-Abschnitt → Ticket.
6. Bei FREIGABE CREATE: Issues anlegen und IDs zurückmelden.
7. Keine Done-Transitions ohne separate QA-Freigabe.

## Qualitätskriterien / Definition of Done

- [ ] Jedes Ticket hat ≥1 testbares AC
- [ ] Trace-Tabelle vollständig für gelieferte Tickets
- [ ] Kein Massen-Create über Nutzerlimit
- [ ] Primärsystem eindeutig; keine stillen Duplikate

## Sicherheit & Freigaben

- Issue-Create/Update/Kommentar nur mit expliziter Freigabe.
- Keine Kundendaten in Ticket-Titeln.

## Fallstricke

- AC als Marketing-Text ohne Given/When/Then testbar.
- Subtask-Explosion → Sprint unplannable.
- Jira Issue Type falsch → Workflow blockiert.
- Linear ohne Team-ID → Create 404.
- Autopilot schließt Issues weil Text „fixed“ enthält.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Spec in 5 Linear Stories, Draft only
- **Input:** 2-seitige Spec, Team ENG
- **Prompt:**

```text
issue_drafts.md + trace. No API create.
```

- **Erwartetes Ergebnis:**

```text
5 drafts each numbered AC | trace 5 rows | 0 live issues
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** FREIGABE CREATE 3 Bugs
- **Input:** Liste repro steps, Jira project BUG
- **Prompt:**

```text
FREIGABE CREATE titles A,B,C. Priority High only on A.
```

- **Erwartetes Ergebnis:**

```text
created_issues.json 3 ids | A priority High | B,C default | links returned
```