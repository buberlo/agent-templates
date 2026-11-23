---
id: diagramme-whiteboard-workflow
domain: office-dokumente
title: "Diagramme und Whiteboards dokumentieren"
category: diagramme-whiteboard
tags:
  - mermaid
  - excalidraw
  - diagrams
target_agents:
  - cursor
  - claude-code
  - generic
required_tools:
  - name: mermaid-cli
    install: "npm: @mermaid-js/mermaid-cli"
    version_notes: "mmdc SVG/PNG"
  - name: draw.io
    install: "https://github.com/jgraph/drawio-desktop or CLI export"
    version_notes: "Optional"
inputs:
  - "Architektur- oder Prozessbeschreibung"
  - "Zielformat (SVG, PNG, embed in MD)"
outputs:
  - "Diagrammdateien"
  - "Quelltext (mmd/drawio)"
risk_level: low
version: "1.1.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

**Prozess- und Architekturdiagramme** als versionierbare Quellen (Mermaid, draw.io) erzeugen und für Docs/PDF exportieren.

## Wann nutzen

- Workshop-Ergebnisse in Wiki-fähige Diagramme überführen.
- CI-Docs mit eingebetteten SVGs.
- Agent iteriert an Text-quelle statt Pixel.

**Wann nicht**

- UX-High-Fidelity in Figma.
- GIS oder CAD (→ hardware/wissenschaft).
- Live-Whiteboard-Sync ohne Export-Snapshot.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Mermaid | Text-Diagramme | Git-diff-freundlich |
| mmdc | Render | SVG für Pandoc |
| draw.io | Komplexe Layouts | Optional |
| Excalidraw | Skizzen | JSON-Export wenn vorhanden |

## System-Prompt / Instruktionen

```text
You create maintainable diagrams from user descriptions—prefer Mermaid for flow/sequence/C4 unless layout needs draw.io.

Inputs: diagram type, nodes and edges list, style (light/dark), output paths (diagram.mmd, diagram.svg), language DE labels if requested.

Mermaid rules:
- Unique node ids; avoid reserved words; quote labels with special chars.
- Max ~25 nodes per diagram—split into linked diagrams if larger.
- Run mmdc -i diagram.mmd -o diagram.svg before claiming done.

draw.io: only when user needs freeform; keep .drawio source in repo; export svg/png.

Whiteboard import: if user pastes Excalidraw JSON, clean and export svg—do not trace screenshots unless no source.

Accessibility: title/desc in svg metadata when embedding in docs.

Approvals: publish diagrams with customer names requires user yes.

Output: source file, rendered svg, render command log.

Never invent infrastructure the user did not describe—use TBD nodes.

Version filenames with v1 v2 when iterating major layout changes.

Validate mermaid syntax with mmdc stderr empty.
For C4 use official mermaid C4 blocks when applicable.
Keep legend for color semantics when more than 3 colors.
```

## Arbeitsablauf

1. Knoten/Kanten aus Briefing tabellarisch.
2. Mermaid-Quelle schreiben.
3. `mmdc` rendern; bei Fehler Syntax fixen.
4. SVG in MD einbinden testen.
5. Optional draw.io für Layout-Korrektur.
6. Review mit Nutzer (Screenshot oder SVG).
7. Quellen ins Repo committen.

## Qualitätskriterien / Definition of Done

- [ ] mmdc exit 0
- [ ] Source in Repo versioniert
- [ ] Lesbare Labels (DE/EN konsistent)
- [ ] Große Diagramme aufgeteilt
- [ ] Kundennamen nur mit Freigabe

## Sicherheit & Freigaben

- Interne Architektur nicht öffentlich posten ohne Freigabe.
- Keine echten Hostnames in öffentlichen Demos.
- Whiteboard-Screenshots können PII enthalten.

## Fallstricke

- Mermaid-Knoten mit Klammern ohne Quotes.
- SVG riesig durch eingebettete Fonts.
- draw.io ohne CLI-Export manuell vergessen.
- Sequenzdiagramm mit falschem activate/deactivate.
- Dark-Theme in Print-PDF unleserlich.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Onboarding-Prozess Flowchart.
- **Input:** 8 Schritte von Registrierung bis Go-Live.
- **Prompt:**

```text
Mermaid flowchart TD; render deploy_flow.svg; German labels.
```

- **Erwartetes Ergebnis:**

```text
deploy_flow.mmd, deploy_flow.svg; mmdc log success.
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Sequenz Auth-Service.
- **Input:** 4 Akteure, 6 Messages.
- **Prompt:**

```text
Mermaid sequenceDiagram; export auth_seq.svg.
```

- **Erwartetes Ergebnis:**

```text
auth_seq.mmd/svg; actors User, API, IdP, DB documented.
```