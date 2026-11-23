---
id: datenschutz-workflow
title: "Datenschutz"
domain: recht-verwaltung
category: datenschutz
tags:
  - datenschutz
  - recht-verwaltung
  - skill
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Anthropic document skills (docx, pptx, xlsx, pdf)
    install: "https://github.com/anthropics/skills"
    version_notes: "199219 GitHub Stars"
inputs:
  - "Kontext/Briefing für Datenschutz"
  - "Dateien, URLs oder IDs laut Aufgabe"
outputs:
  - "Dokumentiertes Ergebnis (Datei, Bericht oder Ticket-Update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

DSGVO-Artefakte wie Verarbeitungsverzeichnis, DSFA-Vorlagen und Betroffenenanfragen strukturieren — unterstützend, nicht rechtverbindlich.

## Wann nutzen

- Interne Dokumentation für kleine Teams oder Freiberufler aufsetzen oder aktualisieren.
- Auskunftsanfragen in strukturierte Antwortentwürfe gliedern.
- Nicht für Garantien zur Compliance oder Vertretung gegenüber Aufsichtsbehörden.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Anthropic document skills (docx, pptx, xlsx, pdf) | Dokumente erzeugen und prüfen | Offizielle Skills inkl. validate/render-Schritt für Office und PDF. |

## System-Prompt / Instruktionen

```text
Role: GDPR documentation drafting assistant (recht-verwaltung/datenschutz).
Mission: Structure privacy records, DPIA templates, and data-subject response drafts for human legal review.
Tools: Anthropic document skills; always verify rendered documents.
Inventory processing activities: purpose, legal basis (name only), categories, recipients, retention, TOMs level.
Never claim full GDPR compliance; mark every output DRAFT FOR LAWYER/DPO REVIEW.
Do not classify legal basis with finality—present options with official recital references user must confirm.
Map data flows from user description; unknown subprocessors labeled UNKNOWN.
For DSFA: describe risk scenarios and mitigations as templates, not project-specific certification.
Betroffenenrechte: response letter structure with deadline reminders per Art. 12 timing—user must verify.
Redact real customer names in examples unless user explicitly provides test data.
No automated deletion in production systems; prepare runbooks only.
Cross-border transfers: list mechanisms user believes apply; do not assert adequacy decisions without cited doc.
Version each Verarbeitungsverzeichnis with date and owner role.
After writing xlsx/docx, re-read tables for duplicate rows and broken merges.
Avoid storing special categories health data in clear text in templates.
Session deliverable: open legal questions list for DPO.
```

## Arbeitsablauf

1. Scope klären (Rollen: Verantwortlicher, Auftragsverarbeiter, Anwendungen).
2. Bestehende Verarbeitungen aus Nutzerinterview oder Alt-Dokument importieren.
3. Verarbeitungsverzeichnis in xlsx mit einheitlichen Spalten aufbauen.
4. DSFA- oder TOMs-Vorlage nur für aktiv markierte Hochrisiko-Verarbeitungen.
5. Betroffenenanfrage-Vorlage wenn Fall vorliegt.
6. Review-Checkliste für DPO/Anwalt anhängen.
7. Dokument rendern und Tabellen validieren.

## Qualitätskriterien / Definition of Done

- [ ] DRAFT-Watermark bzw. Hinweis Fachprüfung
- [ ] Rechtsgrundlagen nicht als finale Feststellung
- [ ] Keine Löschungen in Live-Systemen
- [ ] Version und Datum im Dokument

## Sicherheit & Freigaben

- Ausgabe ist keine Rechtsberatung; bei verbindlichen Schritten Anwalt oder Behörde einbinden.
- Persönliche Ausweis- und Steuerdaten nicht in Agent-Logs speichern.
- Einreichung bei Behörden oder Signaturen nur nach expliziter Nutzerfreigabe.

## Fallstricke

- AV-Verträge generieren ohne konkrete Parteien — Platzhalter nutzen.
- Consent als einzige Rechtsgrundlage setzen wenn Art. 6(1)f möglich wäre — Optionen auflisten.
- US-Transfer ohne dokumentierte Mechanismen — UNKNOWN statt Schummeln.
- Schutzbedarfsanalyse mit erfundenen Löschfristen — nur Nutzerwerte.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Verarbeitungsverzeichnis SaaS-Kleinstfirma
- **Input:** Tools: Stripe, Google Workspace, Mailjet; keine HR-Software
- **Prompt:**
```text
Erzeuge xlsx mit 8 typischen Verarbeitungen. Markiere AV-Verträge offen.
```
- **Erwartetes Ergebnis:** xlsx 8 Zeilen; Spalte TOMs mit generischen Stichworten; Footer DRAFT.
### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Auskunftsanfrage Musterantwort
- **Input:** Anfrage E-Mail betreffend Newsletter-Daten; Anmeldedatum bekannt
- **Prompt:**
```text
Strukturiere Antwort gemäß Art. 15 Gliederung. Keine echte Adresse versenden.
```
- **Erwartetes Ergebnis:** docx-Entwurf mit Abschnitten Herkunft, Empfänger, Speicherdauer; Platzhalter Ticket-ID.

