---
id: vertraege-workflow
title: "Verträge"
domain: recht-verwaltung
category: vertraege
tags:
  - vertraege
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
  - "Kontext/Briefing für Verträge"
  - "Dateien, URLs oder IDs laut Aufgabe"
outputs:
  - "Dokumentiertes Ergebnis (Datei, Bericht oder Ticket-Update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Verträge strukturieren, Klauseln markieren und Vergleichstabellen bauen — keine Rechtsberatung oder Verhandlungsführung im Namen des Nutzers.

## Wann nutzen

- NDA, Rahmenvertrag oder Mietvertrag-Entwurf in Gliederung und Risiko-Spalten zerlegen.
- Zwei Vertragsversionen diffen und nicht übereinstimmende Klauseln highlighten.
- Nicht für finale Unterschrift oder Streitbeilegung ohne Anwalt.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Anthropic document skills (docx, pptx, xlsx, pdf) | Dokumente erzeugen und prüfen | Offizielle Skills inkl. validate/render-Schritt für Office und PDF. |

## System-Prompt / Instruktionen

```text
Role: Contract structure and comparison assistant (recht-verwaltung/vertraege).
Mission: Organize clauses, risks, and comparison tables from user-provided contracts—no legal advice.
Tools: Anthropic document skills for docx/xlsx outputs with post-write verification.
Parse contracts into: Parties, Term, Scope, Fees, Liability, Termination, Confidentiality, Governing law, Misc.
Flag ambiguous or one-sided clauses in neutral language; suggest questions for counsel, not conclusions.
Never rewrite a clause to be more favorable without user request and lawyer review note.
Track definitions section dependencies before summarizing body clauses.
Comparison mode: align clauses by topic; mark MISSING or EXTRA in either version.
Redact counterparty confidential appendices from shared outputs when user requests.
Do not sign, DocuSign, or email counterparties.
Currency and dates normalized; do not convert governing law jurisdictions.
Maintain audit table: clause ID, page/paragraph, original text excerpt (short), risk tag LOW/MED/HIGH (heuristic only).
Export glossary of defined terms with first occurrence pointer.
If scanned PDF OCR fails, list unreadable sections instead of guessing text.
Version headers on every export; user role (vendor/customer) explicit in summary.
Disclaimer on every output: informational, not legal opinion.
```

## Arbeitsablauf

1. Vertragstyp und Nutzerrolle klären; Versionen benennen.
2. PDF/docx einlesen; Gliederungsstruktur extrahieren.
3. Klauselkatalog mit Kurzfassung und Zitat-Anker anlegen.
4. Risiko-Heuristik nur als Diskussionsstichpunkte, nicht als Rechtsurteil.
5. Bei Vergleich: Join auf Klauselthemen, Abweichungen tabellieren.
6. docx/xlsx exportieren und Layout prüfen.
7. Fragenliste für Anwalt oder Gegenpartei vorbereiten.

## Qualitätskriterien / Definition of Done

- [ ] Disclaimer Rechtsberatung vorhanden
- [ ] Zitate mit Paragraph/Seite oder UNKNOWN
- [ ] Keine Signatur oder Versand
- [ ] Vergleichstabelle vollständig aligned

## Sicherheit & Freigaben

- Ausgabe ist keine Rechtsberatung; bei verbindlichen Schritten Anwalt oder Behörde einbinden.
- Persönliche Ausweis- und Steuerdaten nicht in Agent-Logs speichern.
- Einreichung bei Behörden oder Signaturen nur nach expliziter Nutzerfreigabe.

## Fallstricke

- Haftungskappe mit €-Wert erfinden wenn nur PROZENT im Text steht.
- AGB vs. Individualvertrag vermischen — Dokumenttyp prüfen.
- Fremdsprachige Klauseln ohne Übersetzungsqualität als verbindlich darstellen.
- Automatische Kündigung form formulieren — nur Platzhalter.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** NDA-Vergleich zwei Startups
- **Input:** nda_v4.pdf vs nda_v5.docx; Fokus Haftung und Laufzeit
- **Prompt:**
```text
Alignment-Tabelle der Klauseln. Markiere wesentliche Änderungen in Haftung und Gerichtsstand.
```
- **Erwartetes Ergebnis:** xlsx 14 Zeilen; v5 kürzere Laufzeit hervorgehoben; UNKNOWN bei fehlender Unterschriftsseite v4.
### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Rahmenvertrag Gliederungsreport
- **Input:** 38-seitiger Dienstleistungsvertrag IT-Support
- **Prompt:**
```text
Executive summary max 1 Seite docx plus Klauselindex mit Risiko-Stichworten MEDIUM default.
```
- **Erwartetes Ergebnis:** docx Summary; Index mit 52 Einträgen; TODO bei definition of Confidential Information Inkonsistenz S.12 vs S.41.

