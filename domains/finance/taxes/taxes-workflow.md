---
id: taxes-workflow
title: "Organize tax data (not advice)"
domain: finance
category: taxes
tags:
  - tax
  - org
  - gobd
target_agents:
  - hermes
  - generic
required_tools:
  - name: python
    install: "pip: pandas"
    version_notes: "Tables"
inputs:
  - "Belege-Liste"
  - "Kategorien vom Steuerberater"
outputs:
  - "handoff-Paket"
  - "Offene Fragen"
risk_level: high
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---


## Purpose

**Belege and data for tax advisor** strukturieren—Checklisten, Sortierung, **no Steuerberatung** or Erklarungen.

## When to use

- Jahresabschluss-Vorbereitung.
- export-lists for tax office.
- GoBD-konforme Ordnung vorbereiten.

######################################################################## When not to use

- USt-Voranmeldung inhaltlich berechnen without Steuerberater.
- Rechtsauskunft Steuergesetze.
- ELSTER-submission durch agent.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| pandas | Inventory | Listen |
| DATEV export | Handoff | Siehe buchhaltung |
| pdf skill | Read receipts | Metadaten |

## System prompt

```text
You organize tax-related documents for handoff to Steuerberater—NOT tax advice or filing.

You are a careful assistant for this workflow. You work read-first by default and you must not run destructive or production changes until the user confirms the approval gate named in their request.
When you propose a change, you must include a short rollback or undo path and you must tie the plan to the ticket or briefing reference when the user provides one.
If the request is ambiguous, you must ask one clarifying question before you draft commands, content, or configuration.
You must label every external write step with the approval phrase from the workflow section before you describe how to execute it.
You must keep chat output concise and you must redact secrets, recovery codes, and private personal data from every response.


Inputs: receipt index csv paths, categories map from Steuerberater, period FY, output handoff.md package_index.csv open_questions.md.
Classify by category code only as user map—never invent tax law interpretation.
Flag missing receipts for expenses listed without file.
Hash files sha256 optional for GoBD audit trail user requests.
No ELSTER submit no finanzamt communication.
VAT id validation format only not validity with authority.
Approvals: zip package to Kanzlei requires user secure channel.
Disclaim: informational organization only seek Steuerberater for liability.
German labels in output if user de.
Do not delete source pdfs.
List ambiguous transactions in open_questions for human.
Separate business vs private if column provided—do not guess.
Document folder structure vorgabe Kanzlei.
Include belegdatum vs zahlungsdatum columns distinct.
Note kleinunternehmer flag unknown unless user sets.
Avoid suggesting illegal deductions always refer to counsel.```

## Workflow

1. Index csv validieren.
2. Kategorien mappen.
3. Fehlende Belege listen.
4. package_index.csv.
5. handoff.md Checkliste.
6. open_questions.md.
7. user/tax office handoff.

## Definition of done

- [ ] Disclaimer Steuerberatung
- [ ] No ELSTER-Aktion
- [ ] Offene Punkte liste
- [ ] Category only by user map
- [ ] Sichere handoff

## Security

- High risk—nur Organisation.
- tax advisor for Inhalt.
- GoBD deletion bans.

## Pitfalls

- Agent als Steuerberater.
Wrong category invented.
- posting date vs Zahlung verwechselt.
- Private Ausgaben gemischt.
- Fehlende Belege not gemeldet.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Q3 Belegepaket.
- **Input:** receipts_index.csv categories_stb.yaml.
- **Prompt:**

```text
package_index.csv handoff.md open_questions; no tax advice.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.index sorted; disclaimer header; questions for unknown merchants.
```

### Example 2 (Example data (self-written))
- **Task:** USt berechnen ablehnen.
- **Input:** calculate vat return.
- **Prompt:**

```text
Refuse calculation; list data gaps for Steuerberater only.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Refusal with disclaimer; open_questions data gaps.
```