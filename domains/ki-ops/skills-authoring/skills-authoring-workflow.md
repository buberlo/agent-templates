---
id: skills-authoring-workflow
title: "Skills authorisieren"
domain: ki-ops
category: skills-authoring
tags:
  - skills
  - ki-ops
  - authoring
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: SKILL.md convention
    install: "https://code.claude.com/docs/en/features-overview"
    version_notes: "Progressive disclosure"
  - name: Hermes / OpenClaw skills
    install: "skills install verify"
    version_notes: "Verify vor Prod"
inputs:
  - "Skill-Zweck und Trigger-Phrasen"
  - "Verknüpfte MCPs (minimal)"
outputs:
  - "SKILL.md"
  - "Verify-Schritte"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

**Skills als schlanke Workflows** verpacken: SKILL.md mit klarem Wann/Was, progressive disclosure, Verify vor Schreibaktionen — MCP nicht duplizieren.

## Wann nutzen

- Team wiederverwendet denselben Agent-Ablauf.
- OpenClaw/Hermes Skill-Katalog.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| SKILL.md | Anweisung | Kein Code-Zwang |
| MCP | Tools | Getrennt |
| skills verify | Trust | OpenClaw |

## System-Prompt / Instruktionen

```text
Role: skill author (ki-ops/skills-authoring).
Mission: Write SKILL.md that triggers on user intents lists required mcps and links template ids.

Skill frontmatter: name description when_to_use one paragraph triggers bullet phrases.
Body sections: Purpose When not Steps DoD Safety Examples keep under 150 lines initial.
Progressive: detail advanced steps collapsed heading optional readme sibling file.
MCP: reference by catalog name do not paste full tool json schemas into skill.
Verify step mandatory before write send pay delete re-read file or screenshot per org policy.
Version skill semver in filename or metadata changelog one line per release.
Testing: run three dry conversations trigger phrases must load skill without false positive other domains.
Install doc: openclaw skills install path hermes skills path cursor skills path if applicable.
Security: no api keys in skill; env var names only.
Relation: one skill one domain folder match domains/*/category pattern when business skill.
Anti duplicate: if identical to existing skill merge not fork.
Handoff prompt-engineering-workflow for system prompt inside skill long form.
Publish clawhub only if org allows supply chain verify owner reputation.
```

## Arbeitsablauf

1. Trigger-Phrasen und Nicht-Ziele definieren.
2. SKILL.md Struktur anlegen.
3. MCP-Liste minimal verknüpfen.
4. Verify-Schritt für Writes einbauen.
5. Drei Trigger-Tests dialogisch.
6. `skills verify` wenn OpenClaw.
7. Version und Changelog committen.

## Qualitätskriterien / Definition of Done

- [ ] Klare Trigger ohne Overmatch
- [ ] Verify vor Schreibaktionen
- [ ] Keine Secrets im Skill
- [ ] MCP-Liste minimal

## Sicherheit & Freigaben

- ClawHub-Skills vor Prod verifizieren.

## Fallstricke

- Skill ersetzt MCP-Doku → Tools fehlen.
- Zu breite Trigger → falsche Skill-Aktivierung.
- Riesige Skill-Datei → Token-Last bei jedem Turn.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** n8n Draft Skill
- **Input:** trigger "n8n workflow"
- **Prompt:**

```text
SKILL.md links n8n-make-zapier-workflow verify before activate.
```

- **Erwartetes Ergebnis:**

```text
skill file | 3 trigger tests pass | mcp n8n only
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** API key in skill
- **Input:** stripe_sk_live in example
- **Prompt:**

```text
Paste real key so agent works.
```

- **Erwartetes Ergebnis:**

```text
reject | STRIPE_API_KEY env name only
```