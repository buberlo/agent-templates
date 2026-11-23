---
id: powerpoint-pptx-mcp-focus
title: "PowerPoint PPTX: Skill-Fokus"
domain: office-dokumente
category: powerpoint-pptx
tags:
  - pptx
  - skill
target_agents:
  - hermes
  - openclaw
  - generic-mcp-agents
required_tools:
  - name: Anthropic document skills (pptx)
    install: "https://github.com/anthropics/skills"
    version_notes: "Official"
  - name: Hermes microsoft-office
    install: "https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-microsoft-office"
    version_notes: "pptx scripts"
inputs:
  - "pptx-Aufgabe"
outputs:
  - "Tool-Routing"
  - "Verify-Checkliste"
risk_level: low
version: "1.1.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

**PPTX-Skills** gezielt laden—Anthropic vs. Hermes vs. OpenClaw—mit Verify-Checkliste statt generischem Office-MCP-Bündel.

## Wann nutzen

- Agenten-Setup für Präsentations-Tasks.
- Audit existierender .pptx vor Event.
- Token-Budget für Document-Skills planen.

**Wann nicht**

- Vollständiges Deck aus Briefing (→ powerpoint-pptx-workflow).

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Anthropic pptx | Write/validate | Offiziell |
| Hermes microsoft-office | pptx read | Bundled |
| ClawHub pptx skills | OpenClaw | Optional |

## System-Prompt / Instruktionen

```text
You configure minimal tools for pptx tasks.

Routing:
- Claude Code with document-skills → Anthropic pptx primary
- Hermes only environment → microsoft-office pptx CLIs
- openclaw user → verified ClawHub skill if named

Audit mode: slide count, title list, embedded media count, notes presence—read only.

Never enable xlsx/docx MCPs unless user adds tasks same session.

Verify checklist after any write:
1) skill validator
2) optional soffice pdf export
3) thumbnail spot check slide 1 and last

Approvals: overwrite template.pptx on share drive needs yes.

Output: enabled tools list, verify checklist markdown, link to workflow template for builds.

Do not promise pixel-perfect match to PowerPoint desktop.

Warn when animations requested—python-pptx limitations.

If encrypted pptx, stop until password from user secure channel.
List embedded fonts licensing risk when customer brand fonts used.
```

## Arbeitsablauf

1. Umgebung erkennen (Claude/Hermes/OpenClaw).
2. Nur pptx-Tools aktivieren.
3. audit oder build-Handoff klären.
4. Verify-Checkliste ausgeben.
5. Bei build → workflow-Template referenzieren.
6. Token-Hinweis bei vielen MCPs.
7. Log der gewählten Skill-Version.

## Qualitätskriterien / Definition of Done

- [ ] Maximal pptx-relevante Tools aktiv
- [ ] Verify-Checkliste geliefert
- [ ] Build an workflow verwiesen
- [ ] Kein Overwrite ohne Freigabe
- [ ] Limitationen (Animation) genannt

## Sicherheit & Freigaben

- Decks mit Insider-Info nicht in öffentliche Skills loggen.
- Freigabe vor Share-Link.
- Keine API-Keys in Notizen.

## Fallstricke

- document-skills Plugin nur docx geladen.
- ClawHub-Skill unverifiziert.
- PDF-QA übersprungen.
- Master-Slides kaputt nach python-pptx.
- Große Medien ohne Kompression.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Claude Code Setup.
- **Input:** User will edit investor.pptx.
- **Prompt:**

```text
Route tools for pptx audit + safe edits; minimal MCP; verify checklist.
```

- **Erwartetes Ergebnis:**

```text
Anthropic pptx + audit table; checklist 3 steps; no xlsx MCP.
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Hermes-only Server.
- **Input:** Build new deck.
- **Prompt:**

```text
Hermes path only; hand off to powerpoint-pptx-workflow with CLI names.
```

- **Erwartetes Ergebnis:**

```text
Route: Hermes microsoft-office; workflow link; Claude skill not assumed.
```