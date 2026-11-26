---
id: phone-voice-agents-workflow
title: "Phone and voice agents"
domain: communication
category: phone-voice-agents
tags:
  - telefon
  - communication
  - mcp
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: twilio-docs MCP (Hermes-catalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/twilio-docs"
    version_notes: "Nous-approved optional-mcps catalog entry (listing 2026-11-23)."
  - name: ClawHub „Agent Phone Call“ (mrsz)
    install: "https://clawhubtrends.com/leaderboard.html"
    version_notes: "72,476 downloads, 8 registry stars (ClawHub Leaderboard 23 Nov 2026)."
inputs:
  - "Call script and target (inbound/outbound)"
  - "Consent and Recording Rules"
  - "Dial/Deploy Release"
outputs:
  - "Call plan and TwiML/Flow sketch"
  - "Transcript or Call-Summary"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

**Voice-Agent-Flows** (Twilio/ElevenLabs/OpenClaw Phone Call), **Start calls only after approval** and document the conversation result in a structured manner.

## When to use

- Outbound memory or inbound IVR prototype with clear script.
- Twilio docs MCP and verified phone call skill available.
- Legal notices (recording, TCPA/GDPR) confirmed by the user.

**When not to use**

emergency calls, suicide prevention, medical hotlines without a so- introduction.
- Cold-Calling without Opt-in.
- Balanced of the credit steeped in the creator's creator.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| twilio-docs MCP | API/TwiML Referenz | Sichere Snippets |
| Agent Phone Call (OpenClaw) | Dial workflow | ClawHub, verify beforehand |
,pir linetea- --pir, me,pir - Abulines a, aations aish self a remark - line, - all Direct, line - - line - line - line - line - line - line - line - line - line - line - line - - is - - - line - line - line - line - line - line - line - - line - line - line - line - - line - line - line - -te - line - - line - line - line - line - line - line - line - line - line - line - line - line - line - line - line - line - line - line - line - line - line - line - line - line - line - line - line - line - line - - line - line - line - line - line - line - line - line - line - reasons - - -tru - - - - - - - -tru - - - - - - - - - - - - - -). - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - line basis-a - - - - - - - -

## System prompt

```text
You plan and assist voice agent calls for communication/phone-voice-agents.

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

## Workflow

1. Script and compliance (recording opt-in)
2. `openc skills verify` for Agent Phone Call.
3. Reference TwiML/flow sketch via twilio-docs MCP.
4. Dry-Run: Read script as a dialogue, estimate duration.
5. User: `APPROVE DIAL` + last 4 digits.
6. execute call (skill/provider); Monitor the maximum duration.
7. Transkript/Summary in `output/call-YYYYMMDD.md` ablegen.

## Definition of done

- [ ] APPROVE_DIAL protokolliert
- [ ] Recording notice in script if recording_allowed
- [ ] No dial without release
- [ ] Post-Call-Summary with next steps

## Security

- Verify ClawHub skills before use (registry risks).
Twilio credentials in secrets, not prompts.
- Minimize PII from call logs at CRM export.

## Pitfalls

- Latency → User speaks double, bot interrupts.
- ASR versteht Namen falsch → falsche Buchung.
- Outbound without lokale Telefonmarketing-Regeln.
- TwiML Loop without Exit → Kosten.
- Skill posts as a user without call sharing.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Appointment-reminder outbound.
- **Input:** Script 4 sentences, recording no, callee +43***4567.
- **Prompt:**

```text
Draft call flow and TwiML outline; wait for APPROVE_DIAL before dial.
```

- **Expected result:**

```text
Flow: greet → confirm appointment Wed 10:00 → press 1 confirm / 2 reschedule → handoff
Dial: not started (awaiting APPROVE_DIAL)
TwiML: outline in output/call-plan.md
```

### Example 2 (Example data (self-written))
- **Task:** Dial without release.
- **Input:** Sofort anrufen verlangt.
- **Prompt:**

```text
Call customer now about invoice.
```

- **Expected result:**

```text
Abbruch: APPROVE_DIAL fehlt.
Script draft created; no dial, no Twilio API write.
```