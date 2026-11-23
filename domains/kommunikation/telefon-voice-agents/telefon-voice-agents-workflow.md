---
id: telefon-voice-agents-workflow
title: "Telefon und Voice-Agents"
domain: kommunikation
category: telefon-voice-agents
tags:
  - telefon
  - kommunikation
  - mcp
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: twilio-docs MCP (Hermes-Katalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/twilio-docs"
    version_notes: "Nous-approved optional-mcps-Katalogeintrag (Listing 23.11.2026)."
  - name: ClawHub „Agent Phone Call“ (mrsz)
    install: "https://clawhubtrends.com/leaderboard.html"
    version_notes: "72.476 Downloads, 8 Registry-Stars (ClawHub Leaderboard 23.11.2026)."
inputs:
  - "Call-Script und Ziel (Inbound/Outbound)"
  - "Einwilligung und Aufzeichnungsregeln"
  - "Freigabe für Dial/Deploy"
outputs:
  - "Call-Plan und TwiML/Flow-Skizze"
  - "Transkript oder Call-Summary"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

**Voice-Agent-Flows** planen (Twilio/ElevenLabs/OpenClaw Phone Call), **Anrufe nur nach Freigabe** starten und Gesprächsergebnis strukturiert dokumentieren.

## Wann nutzen

- Outbound-Erinnerung oder Inbound-IVR-Prototyp mit klarem Script.
- Twilio-Docs MCP und verifizierter Phone-Call-Skill verfügbar.
- Rechtliche Hinweise (Recording, TCPA/DSGVO) vom Nutzer bestätigt.

**Wann nicht**

- Notrufe, Suizidprävention, medizinische Hotlines ohne Mensch.
- Cold-Calling ohne Opt-in.
- Ungeprüfte ClawHub Call-Skills in Produktion.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| twilio-docs MCP | API/TwiML Referenz | Sichere Snippets |
| Agent Phone Call (OpenClaw) | Dial-Workflow | ClawHub, vor verify |
| Transkript/Notizen | Post-Call | QA und CRM |

## System-Prompt / Instruktionen

```text
You plan and assist voice agent calls for kommunikation/telefon-voice-agents.

Inputs: direction (inbound|outbound), purpose, callee_e164 (redact in logs), script bullets, recording_allowed, max_duration_sec, provider (twilio|other).

Before any dial:
- Confirm recording_disclosure text if recording_allowed
- Confirm user typed APPROVE_DIAL with callee last-4 digits

Use twilio-docs MCP for TwiML patterns only; do not expose account_sid in chat.
Design: greeting, intent, 2 FAQ branches, human handoff phrase, voicemail fallback.

After call (if transcript provided): summary, sentiment, promised_followups[], compliance_flags[].

Never initiate chargeable calls without APPROVE_DIAL.
ClawHub skills: remind verify before use.
```

## Arbeitsablauf

1. Script und Compliance (Recording, Opt-in) dokumentieren.
2. `openclaw skills verify` für Agent Phone Call.
3. TwiML/Flow-Skizze via twilio-docs MCP referenzieren.
4. Dry-Run: Script als Dialog lesen, Dauer schätzen.
5. Nutzer: `APPROVE_DIAL` + letzte 4 Ziffern.
6. Call ausführen (Skill/Provider); Max-Dauer überwachen.
7. Transkript/Summary in `output/call-YYYYMMDD.md` ablegen.

## Qualitätskriterien / Definition of Done

- [ ] APPROVE_DIAL protokolliert
- [ ] Recording-Hinweis im Script wenn recording_allowed
- [ ] Kein Dial ohne Freigabe
- [ ] Post-Call-Summary mit nächsten Schritten

## Sicherheit & Freigaben

- ClawHub-Skills verify vor Einsatz (Registry-Risiken).
- Twilio-Credentials in Secrets, nicht in Prompts.
- PII aus Call-Logs bei CRM-Export minimieren.

## Fallstricke

- Latenz → Nutzer spricht doppelt, Bot unterbricht.
- ASR versteht Namen falsch → falsche Buchung.
- Outbound ohne lokale Telefonmarketing-Regeln.
- TwiML Loop ohne Exit → Kosten.
- Skill postet als User ohne Anruf-Freigabe.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Termin-Erinnerung Outbound.
- **Input:** Script 4 Sätze, recording no, callee +43***4567.
- **Prompt:**

```text
Draft call flow and TwiML outline; wait for APPROVE_DIAL before dial.
```

- **Erwartetes Ergebnis:**

```text
Flow: greet → confirm appointment Wed 10:00 → press 1 confirm / 2 reschedule → handoff
Dial: not started (awaiting APPROVE_DIAL)
TwiML: outline in output/call-plan.md
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Dial ohne Freigabe.
- **Input:** Sofort anrufen verlangt.
- **Prompt:**

```text
Call customer now about invoice.
```

- **Erwartetes Ergebnis:**

```text
Abbruch: APPROVE_DIAL fehlt.
Script-Entwurf erstellt; kein Dial, keine Twilio API write.
```