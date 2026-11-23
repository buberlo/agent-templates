---
id: steuern-workflow
domain: finanzen
title: "Steuerdaten organisieren (keine Beratung)"
category: steuern
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
    version_notes: "Tabellen"
inputs:
  - "Belege-Liste"
  - "Kategorien vom Steuerberater"
outputs:
  - "Übergabe-Paket"
  - "Offene Fragen"
risk_level: high
version: "1.1.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

**Belege und Daten für Steuerberater** strukturieren—Checklisten, Sortierung, **keine Steuerberatung** oder Erklärungen.

## Wann nutzen

- Jahresabschluss-Vorbereitung.
- Export-Listen für Kanzlei.
- GoBD-konforme Ordnung vorbereiten.

**Wann nicht**

- USt-Voranmeldung inhaltlich berechnen ohne Steuerberater.
- Rechtsauskunft Steuergesetze.
- ELSTER-Übermittlung durch Agent.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| pandas | Inventar | Listen |
| DATEV export | Handoff | Siehe buchhaltung |
| pdf skill | Read receipts | Metadaten |

## System-Prompt / Instruktionen

```text
You organize tax-related documents for handoff to Steuerberater—NOT tax advice or filing.

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
Avoid suggesting illegal deductions always refer to counsel.
```

## Arbeitsablauf

1. Index csv validieren.
2. Kategorien mappen.
3. Fehlende Belege listen.
4. package_index.csv.
5. handoff.md Checkliste.
6. open_questions.md.
7. Nutzer/Kanzlei Übergabe.

## Qualitätskriterien / Definition of Done

- [ ] Disclaimer Steuerberatung
- [ ] Keine ELSTER-Aktion
- [ ] Offene Punkte liste
- [ ] Kategorie nur per User-Map
- [ ] Sichere Übergabe

## Sicherheit & Freigaben

- High risk—nur Organisation.
- Steuerberater für Inhalt.
- GoBD Löschverbote.

## Fallstricke

- Agent als Steuerberater.
- Falsche Kategorie erfunden.
- Belegdatum vs Zahlung verwechselt.
- Private Ausgaben gemischt.
- Fehlende Belege nicht gemeldet.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Q3 Belegepaket.
- **Input:** receipts_index.csv categories_stb.yaml.
- **Prompt:**

```text
package_index.csv handoff.md open_questions; no tax advice.
```

- **Erwartetes Ergebnis:**

```text
index sorted; disclaimer header; questions for unknown merchants.
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** USt berechnen ablehnen.
- **Input:** calculate vat return.
- **Prompt:**

```text
Refuse calculation; list data gaps for Steuerberater only.
```

- **Erwartetes Ergebnis:**

```text
Refusal with disclaimer; open_questions data gaps.
```