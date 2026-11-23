---
id: meetings-transkription-mcp-focus
title: "Meetings und Transkription: MCP/Skill-Fokus"
domain: kommunikation
category: meetings-transkription
tags:
  - meetings
  - kommunikation
  - skill
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: ClawHub / OpenClaw Skill Openai Whisper (steipete)
    install: "https://clawhubtrends.com/leaderboard.html"
    version_notes: "303 GitHub Stars"
  - name: Hermes-Skills meeting-action-items, teams-meeting-pipeline
    install: "https://hermes-agent.nousresearch.com/docs/reference/skills-catalog"
    version_notes: "Bundled."
inputs:
  - "Transkript-Quelle (lokal vs. Fireflies)"
  - "Erlaubte Datenabflüsse"
outputs:
  - "Tool-Entscheidungsbaum"
  - "Minimales MCP/Skill-Set"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

**Transkriptions-Stack festlegen**: lokales Whisper vs. Fireflies MCP vs. Teams-Pipeline—Datenresidenz, Skills und MCP minimal halten.

## Wann nutzen

- Compliance fragt nach Cloud vs. on-device ASR.
- Agent soll nur Fireflies lesen, nicht erneut hochladen.
- OpenClaw Whisper installieren und verifizieren.

**Wann nicht**

- Fertiges Audio bereits transcribed → direkt Action-Item-Extraktion.
- Kein Fireflies-Konto und keine GPU/CPU-Zeit für Whisper.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| OpenClaw Whisper | Lokal ASR | Kein Audio-Upload |
| fireflies MCP | Vorhandene Transkripte | SaaS bereits im Einsatz |
| meeting-action-items | Post-Processing | Struktur, keine ASR |

## System-Prompt / Instruktionen

```text
You design meeting transcription tooling for kommunikation/meetings-transkription.

Inputs: data_residency (local_only | saas_ok), has_fireflies (bool), openclaw_available (bool), gpu (bool).

Decision tree:
- local_only → openclaw whisper + ffmpeg; disable fireflies mcp
- has_fireflies + saas_ok → fireflies MCP read only; whisper optional for gaps
- teams_meeting_pipeline skill if recordings live in M365 and skill configured

Document in meeting-tooling.md:
install commands, verify steps (openclaw skills verify whisper), model size recommendation from gpu flag.
Set never upload_without_approval default true.

List disabled tools explicitly.
```

## Arbeitsablauf

1. Datenresidenz-Policy vom Nutzer (`local_only` / `saas_ok`).
2. Verfügbarkeit prüfen: OpenClaw, Fireflies Token, Hermes Skills.
3. Entscheidungsbaum in `meeting-tooling.md` schreiben.
4. `openclaw skills verify` für Whisper-Skill.
5. Fireflies MCP nur bei `saas_ok` aktivieren.
6. Test: kurzer 30s Sample-Clip lokal ODER Fireflies get last transcript metadata.
7. Nutzer sign-off auf Tooling-Doc.

## Qualitätskriterien / Definition of Done

- [ ] Datenabfluss dokumentiert (lokal vs. SaaS)
- [ ] Unbenutzte Upload-Tools deaktiviert
- [ ] Verify-Schritt für ClawHub-Skill
- [ ] Modellwahl begründet (CPU vs. GPU)

## Sicherheit & Freigaben

- Aufzeichnungsrecht und Einwilligung außerhalb Tooling, aber im Doc verlinkt.
- Fireflies-Exports nicht in öffentliche Tickets.
- Whisper-Modelle aus vertrauenswürdiger Quelle.

## Fallstricke

- Fireflies + Whisper parallel → doppelte Kosten/Zeit.
- Whisper large auf CPU → Stunden Laufzeit ohne Warnung.
- Teams-Pipeline ohne OAuth → leere Runs.
- MCP Upload-Tool vergessen zu disable bei local_only.
- Veraltetes Whisper-Skill ohne VAD → schlechte Segmente.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** local_only Setup.
- **Input:** `data_residency=local_only`, GPU nein.
- **Prompt:**

```text
Choose tools for on-device transcription only, recommend whisper model for CPU.
```

- **Erwartetes Ergebnis:**

```text
ASR: openclaw whisper base or small
Disabled: fireflies mcp, any upload MCP
Model note: small for CPU, expect ~2x realtime
File: meeting-tooling.md
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Fireflies-only read.
- **Input:** `has_fireflies=true`, `saas_ok=true`.
- **Prompt:**

```text
Enable only fireflies MCP read; meeting-action-items for parsing.
```

- **Erwartetes Ergebnis:**

```text
Read: fireflies MCP get_transcript
Post: hermes meeting-action-items
Disabled: whisper install required false
upload_without_approval: false (enforced)
```