---
id: pdf-mcp-focus
title: "PDF: MCP/Skill-Fokus"
domain: office-dokumente
category: pdf
tags:
  - pdf
  - office-dokumente
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
  - name: Hermes-Skill pdf
    install: "https://hermes-agent.nousresearch.com/docs/reference/skills-catalog"
    version_notes: "Bundled-Katalog."
inputs:
  - "Kontext/Briefing für PDF"
  - "Dateien, URLs oder IDs laut Aufgabe"
outputs:
  - "Dokumentiertes Ergebnis (Datei, Bericht oder Ticket-Update)"
risk_level: low
example_count: 3
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

PDFs lesen, mergen, ausfüllen, OCR und gezielt editieren.

## Wann nutzen

- Anfragen passen zur Kategorie **PDF**.
- Nicht nutzen, wenn ein menschlicher Freigabe-Prozess noch nicht geklärt ist (`risk_level: low`).

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Anthropic document skills (docx, pptx, x | Skill | Aus Recherche 2026-11-23 |
| Hermes-Skill pdf | Skill | Aus Recherche 2026-11-23 |
| MarkItDown | CLI / Bibliothek | Aus Recherche 2026-11-23 |
| ClawHub „Nano Pdf“ (steipete) | Skill | Aus Recherche 2026-11-23 |

## System-Prompt / Instruktionen

```text
You are a specialist for PDF (office-dokumente/pdf).
Use only tools listed in required_tools. Follow safety gates.
Workflow hint: - Lesen/Mergen/Formularfuellung mit pypdf; visuell per Render pruefen.
```

## Arbeitsablauf

- Lesen/Mergen/Formularfuellung mit pypdf; visuell per Render pruefen.

## Qualitätskriterien / Definition of Done

- [ ] Eingaben vollständig und dokumentiert
- [ ] Tool-Aufrufe nachvollziehbar (Log/Pfade)
- [ ] Ergebnis entspricht Kategorie-Beschreibung
- [ ] Bei Schreib-/Sendeaktionen: explizite Nutzerfreigabe

## Sicherheit & Freigaben

- OCR-Fehler in Zahlen und Aktenzeichen; keine finale Einreichung ohne Sichtpruefung.
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Standard-PDF-Aufgabe im Agenten-Thread
- **Input:** Parameter-Satz für `pdf` (Testdaten)
- **Prompt:**
```text
Nutze den empfohlenen Stack für PDF. Dokumentiere jeden Tool-Aufruf. Keine Schreibaktion ohne Freigabe.
```
- **Erwartetes Ergebnis:**
```text
Status: OK
Artefakt: output/{slug}-demo.txt
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Fehlerfall / Validierung in PDF
- **Input:** Unvollständige oder ungültige Eingabe
- **Prompt:**
```text
Erkenne fehlende Pflichtfelder, brich ab und liste konkrete Nachfragen.
```
- **Erwartetes Ergebnis:**
| Feld | Status |
|------|--------|
| input | fehlt |
| Aktion | keine Ausführung |

### Beispiel 3 (Praxisbeispiel)

- **Aufgabe:** Das im selben Tutorial aus dem DOCX gerenderte PDF mit der pdf-Skill zuruecklesen.
- **Input:** briefing.pdf aus dem DOCX-Render von Schritt 2.
- **Prompt:**
```text
Anthropic pdf-Skill, pypdf PdfReader.
```
- **Erwartetes Ergebnis:**
  Das Tutorial nutzt das PDF als Testdatei zum Auslesen von Seitenzahl und Text (Quick-Start pypdf). Es ist derselbe verifizierte Render-Workflow, kein separates Fremdprojekt.
- **Quelle:** https://aifrontierpost.com/articles/anthropic-official-agent-skills-tutorial/
