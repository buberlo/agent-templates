---
id: kurse-erstellen-mcp-focus
title: "Kurse erstellen: MCP/Skill-Fokus"
domain: bildung
category: kurse-erstellen
tags:
  - kurse
  - bildung
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
  - name: Hermes-Skill microsoft-office
    install: "https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-microsoft-office"
    version_notes: "Teil des offiziellen Bundled-Katalogs."
inputs:
  - "Gewünschte Ausgabeformate"
  - "Validator-Verfügbarkeit"
outputs:
  - "Skill-Auswahl und Tooling-Doc"
  - "Probe-pptx Smoke-Test"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

**Office/Skill-Stack für Kursmaterial wählen**: Anthropic document skills vs. Hermes microsoft-office vs. YouTube-Quellen—inkl. Validatoren und Verify-Schritten.

## Wann nutzen

- Agent-Setup für Kursproduktion; Unsicherheit welcher Skill pptx erzeugt.
- CI-artiger Validate-Schritt vor LMS-Upload.
- Minimales Toolset gegen Prompt-Leaks.

**Wann nicht**

- Konkretes Curriculum schreiben → `kurse-erstellen-workflow`.
- Kein Python/LibreOffice für PDF-Render verfügbar und PDF gefordert.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Anthropic pptx/docx | Validierung | validate.py |
| Hermes microsoft-office | Offline Generierung | Bundled |
| youtube-content | Primärquellen | Transkript-Import |

## System-Prompt / Instruktionen

```text
You configure course authoring tools for bildung/kurse-erstellen.

Inputs: outputs_needed (pptx|docx|pdf|xlsx), host (claude_skills|hermes), run_validate bool.

Produce course-authoring-tooling.md:
- Primary generator per format with install path
- Validate commands: python skills/pptx/scripts/office/validate.py file.pptx OR hermes skill verify equivalent
- youtube-content: when to use fetch_transcript vs user-provided PDF
- Disable unused document MCPs

Require post-write verify: re-read file listing slide count or docx paragraph count.
Note: pptx hex colors without # per Anthropic skill docs; warn on off-slide coordinates.

Deliver smoke test: 1-slide pptx title "Tooling OK" and validation result line.
```

## Arbeitsablauf

1. Benötigte Formate notieren.
2. Anthropic vs. Hermes-Pluginfähigkeit prüfen.
3. `course-authoring-tooling.md` schreiben.
4. Mini-pptx erzeugen (1 Folie).
5. Validator ausführen falls vorhanden.
6. YouTube-Skill nur aktivieren wenn Video-Quellen.
7. Nutzer bestätigt Stack vor Kurserstellung.

## Qualitätskriterien / Definition of Done

- [ ] Ein Primary-Tool pro Ausgabeformat
- [ ] Validate- oder Read-back-Schritt dokumentiert
- [ ] Smoke-pptx erfolgreich oder Fehler mit Fix
- [ ] Unnötige Skills deaktiviert

## Sicherheit & Freigaben

- Skripte aus vertrauenswürdigen Repos (anthropics/skills, Hermes bundled).
- Keine Makros in generierten Office-Dateien.
- Externe YouTube-URLs nur mit Nutzerliste.

## Fallstricke

- Zwei pptx-Generatoren → inkonsistente Layouts.
- PDF via LibreOffice fehlt auf Host.
- Validator nicht im PATH.
- youtube venv nicht vorbereitet.
- Große Skills → Kontext-Overflow.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Nur Hermes pptx.
- **Input:** `outputs_needed=pptx`, hermes host.
- **Prompt:**

```text
Document tooling and run 1-slide smoke test with validate if available.
```

- **Erwartetes Ergebnis:**

```text
Primary: hermes microsoft-office → python-pptx
Smoke: tooling-smoke.pptx (1 slide)
Validate: SKIPPED (anthropic path not installed) | paragraphs counted via read-back
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Anthropic validate Pfad.
- **Input:** claude_skills, run_validate true.
- **Prompt:**

```text
Configure anthropic pptx skill with validate.py command in tooling doc.
```

- **Erwartetes Ergebnis:**

```text
Validate cmd: python skills/pptx/scripts/office/validate.py <file.pptx>
Smoke: tooling-smoke.pptx → All validations PASSED
File: course-authoring-tooling.md
```