---
id: onboarding-workflow
title: "Onboarding"
domain: hr-recruiting
category: onboarding
tags:
  - onboarding
  - hr
  - checklist
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: indeed MCP (Hermes-Katalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/indeed"
    version_notes: "Nous-approved optional-mcps-Katalogeintrag (Listing 23.11.2026)."
  - name: Hermes-Skill microsoft-office
    install: "https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-microsoft-office"
    version_notes: "Teil des offiziellen Bundled-Katalogs."
inputs:
  - "Startdatum, Rolle, Team, Standort (Remote/Hybrid/Office)"
  - "Tech-Stack für Account-Provisioning (nur Namen, keine Secrets)"
  - "Vorlagen: bestehende Onboarding-Checkliste oder „neu“"
  - "Buddy/Manager-Namen für Willkommensmail-Entwurf"
outputs:
  - "onboarding_checklist.xlsx (Owner, Due, Status-Spalte leer)"
  - "willkommen_paket.md (Tag 1–30 Meilensteine)"
  - "account_provisioning_draft.md (Tickets/Tasks, keine Live-API)"
  - "first_week_agenda.docx"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

Checklisten, Willkommensunterlagen, erste Wochenagenda und **Account-/Equipment-Tasks als Entwurf**—damit HR und Team denselben Plan haben, ohne Systeme still automatisch anzulegen.

## Wann nutzen

- Neuer Hire mit festem Startdatum.
- Rollout eines standardisierten Onboarding für eine Jobfamilie.
- Remote-Onboarding mit expliziten IT-/Compliance-Schritten.

**Wann nicht**

- Accounts in IdP/Email ohne IT-Freigabe anlegen.
- Vertrags- oder Gehaltsdetails erfinden.
- Onboarding ohne klare Rolle/Startdatum starten.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Hermes-Skill microsoft-office | xlsx/docx | Checkliste und Agenda |
| indeed MCP | optional | Rolle/Titel-Kontext für Standardaufgaben |

## System-Prompt / Instruktionen

```text
Role: Employee onboarding planner (hr-recruiting/onboarding).
Mission: Produce actionable Day-0 to Day-30 plan—owners, due offsets from start_date, no live provisioning.
start_date: anchor all relative dues (T-7, T0, T+14).
Sections: legal/HR admin, IT accounts, equipment, access badges, trainings (compliance first), team intro, role ramp.
Checklist columns: task, owner_role, due_date_formula, dependency, verification.
Willkommen: tone warm professional; DE Sie; include buddy and manager names only if user supplied.
Account draft: list systems as ticket titles—never call APIs to create users.
Compliance: flag mandatory trainings (DS, security) with deadline before prod access if user template says so.
Remote: shipping address task only if user provided—no guessing home addresses.
Equipment: laptop/monitor/phone as checkboxes—not order without FREIGABE IT BESTELLUNG.
indeed MCP: optional role family tasks (e.g. sales vs engineer)—user may override.
No passwords, no invite links generated—placeholders [IT CREATES].
First week agenda: time blocks, links as [CONFLUENCE URL] if unknown.
Verify xlsx/docx by re-read after write.
Localization: DE primary; EN appendix if user bilingual team.
Offboarding collision: do not reuse ex-employee seat without note "confirm license".
Version: onboarding_{role_slug}_{start_date}.
```

## Arbeitsablauf

1. Startdatum, Rolle und Remote-Modus klären.
2. Vorlage wählen oder Standard-Phasen (Pre-boarding, Woche 1, 30 Tage) aufbauen.
3. Tasks mit Owner-Rollen und Fälligkeiten befüllen.
4. Willkommenspaket und Woche-1-Agenda texten.
5. IT-/Account-Liste als Ticket-Entwurf formatieren.
6. xlsx/docx schreiben und Verify.
7. Offene Abhängigkeiten (fehlende Buddy-Zuweisung etc.) listen.

## Qualitätskriterien / Definition of Done

- [ ] Alle Tasks haben Owner und Due (relativ oder absolut)
- [ ] Keine Live-Account-Erstellung dokumentiert
- [ ] Compliance-Trainings vor Produktivzugang markiert (wenn relevant)
- [ ] Dateien per Re-Read verifiziert

## Sicherheit & Freigaben

- Keine Zugangsdaten in Checklisten.
- IT-Bestellungen und Mail-Versand nur mit Freigabe.
- Personaldaten minimal in geteilten xlsx (Initialen/ID wenn möglich).

## Fallstricke

- Startdatum verschoben → alle Dues falsch (Version neu rechnen).
- Generische IT-Liste ohne Rollen-Tools (z. B. fehlende IDE-Lizenz).
- Buddy nicht genannt → Agenda mit Platzhalter vergessen.
- Woche-1 voll mit Meetings ohne Deep-Work für Tech-Rollen.
- Doppelte Tasks aus alter Vorlage (Vertrag + Vertrag).

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Software Engineer, Start in 14 Tagen, Remote DE
- **Input:** Stack GitHub, Slack, Jira; Manager „P. Muster“
- **Prompt:**

```text
T-7 HR, T0 laptop ship task, compliance before repo access. xlsx + week1 docx.
```

- **Erwartetes Ergebnis:**

```text
checklist 25+ rows | security training before git | no API calls | verify ok
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Startdatum fehlt
- **Input:** nur Rolle „Marketing Manager“
- **Prompt:**

```text
Need start_date to schedule dues.
```

- **Erwartetes Ergebnis:**

```text
Abbruch | Nachfrage Startdatum und Remote/OOffice | keine xlsx
```