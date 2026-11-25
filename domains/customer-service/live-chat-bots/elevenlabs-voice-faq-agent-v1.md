---
id: elevenlabs-voice-faq-agent-v1
title: "ElevenLabs voice phone FAQ agent with human escalation"
domain: customer-service
category: live-chat-bots
tags:
  - elevenlabs
  - voice
  - faq
  - escalation
target_agents:
  - hermes
  - generic-mcp-agents
required_tools:
  - name: ElevenLabs ElevenAgents
    install: "https://elevenlabs.io/docs/eleven-agents/build/overview"
    version_notes: "Configure agent, knowledge base, and transfer_to_number; optional hosted MCP at https://api.elevenlabs.io/v1/mcp for management."
  - name: Twilio
    install: "https://www.twilio.com/en-us/blog/developers/tutorials/integrations/ai-agent-to-human-agent-elevenlabs-call-handoffs-twilio"
    version_notes: "Telephony bridge pattern when using Twilio numbers; follow blueprint security guidance."
inputs:
  - "FAQ knowledge base articles (no customer PII in KB text)"
  - "Business hours and escalation phone or SIP URI"
  - "No-PII logging policy and data retention days"
outputs:
  - "Agent system prompt, first message, and knowledge base attachment plan"
  - "transfer_to_number rules with warm-handoff summary fields"
  - "Test call script and evaluation checklist"
risk_level: high
example_count: 2
version: "1.0.0"
updated: "2026-11-25"
---

## Purpose

Design and document an ElevenLabs ElevenAgents voice FAQ agent that answers top phone questions from an approved knowledge base, refuses to collect or log PII beyond what telephony already carries, and escalates to a human via the transfer_to_number system tool when conditions match.

## When to use

- Support team wants after-hours answers for shipping, hours, and password reset policy without staffing phones.
- You can publish a scrubbed FAQ knowledge base with no live customer records.
- Telephony is on a supported provider (Twilio, SIP, Exotel) documented in ElevenLabs transfer guides.

### When not to use

- HIPAA or Zero Retention Mode workspaces where ElevenLabs MCP and some agent features are unavailable per vendor docs.
- Payment card capture or account changes without human agents.
- Jurisdictions requiring recorded consent scripts you have not legal-reviewed.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| ElevenLabs ElevenAgents | Voice agent runtime | [Build overview](https://elevenlabs.io/docs/eleven-agents/build/overview) |
| transfer_to_number | Human escalation | [System tool docs](https://elevenlabs.io/docs/eleven-agents/customization/tools/system-tools/transfer-to-number) |
| Twilio (optional) | Phone ingress | Reference handoff pattern with dynamic variables |
| Internal FAQ markdown | Grounding | Source of truth without ticket exports |

## Example escalation diagram

Example data (self-written): see [assets/example-elevenlabs-faq-escalation.svg](assets/example-elevenlabs-faq-escalation.svg).

## System prompt

```text
You are an ElevenLabs voice FAQ configuration assistant for customer-service/live-chat-bots.
You write the agent system prompt for a phone-only FAQ agent that answers from the uploaded knowledge base, never improvises policy beyond KB text, and says "I do not have that information" when retrieval is empty.
You mandate transfer_to_number when the caller asks for a human, repeats the same unresolved question twice, mentions legal action, or requests billing changes beyond read-only FAQs.
You configure warm transfer when operators need a spoken summary and cold transfer only when the user explicitly accepts no summary.
You prohibit the agent from asking for full credit card numbers, government ID numbers, or passwords, and you include a line directing callers to the secure web portal for authentication.
You specify conversation metadata logging: store call duration, topic tags, and escalation reason only; do not persist caller speech transcripts containing names or account numbers when the user’s no-PII policy is strict.
You reference https://elevenlabs.io/docs/eleven-agents/customization/tools/system-tools/transfer-to-number for rule conditions and list Twilio warm conference parameters when that provider is selected.
You deliver a first message under fifteen seconds of speech, business hours disclaimer, and optional recording notice placeholder for legal to fill.
You produce a test matrix of ten FAQ intents plus three escalation triggers with expected agent behavior, citing elevenlabs.io docs for tool enablement steps.
You refuse to publish agent changes to production without PUBLISH_APPROVED from the workspace owner.
```

## Workflow

1. Inventory FAQ topics; strip PII from KB sources.
2. Draft agent system prompt, first message, and knowledge base file list.
3. Add transfer_to_number rules: human request, repeat frustration, out-of-scope billing.
4. Set logging: disable full transcript export if no-PII policy requires it.
5. Configure telephony (Twilio or SIP) with fictional test numbers in dev.
6. Run simulated test calls using ElevenLabs test tools; document failures.
7. On PUBLISH_APPROVED, publish branch; monitor escalation rate first week.

## Definition of done

- [ ] KB contains zero real customer records
- [ ] transfer_to_number rules documented per provider in use
- [ ] No-PII logging policy reflected in agent prompt
- [ ] Test matrix executed with pass or fail notes

## Security

- ElevenLabs workspace secrets for SIP and API stay in workspace secret store.
- Warm transfer summaries must not read aloud full account numbers from CRM.
- Review Twilio blueprint as reference only; harden auth on escalation webhooks before production.

## Pitfalls

- Chat widget agents lack transfer_to_number; this template is phone-only per vendor docs.
- Over-broad KB lets the model invent return policies not in articles.
- Cold transfer without summary frustrates operators; default warm when staffing allows.
- Logging every utterance violates no-PII policy even when storage is “internal.”
- MCP on ElevenLabs disabled in HIPAA workspaces; plan manual dashboard configuration instead.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Draft FAQ agent for fictional retailer Example Outfitters hours and shipping.
- **Input:** KB three articles; escalation +1-555-0100; Twilio; no transcript retention.
- **Prompt:**

```text
ElevenAgents FAQ phone agent config package.
Draft only, no publish.
```

- **Expected result:**

System prompt block, first message, knowledge base manifest, transfer rule "Caller asks for human" with twilio_warm_conference_transfer to +1-555-0100, logging section banning transcript export, and link to transfer_to_number docs.

### Example 2 (Example data (self-written))

- **Task:** Evaluate failed test where agent guessed return window.
- **Input:** Test caller asked 90-day returns; KB says 30 days; agent said 90.
- **Prompt:**

```text
Fix KB grounding and add disambiguation line.
No PII in examples.
```

- **Expected result:**

Revised prompt sentence citing KB-only answers, suggested retrieval threshold tweak described qualitatively, added clarification question before stating policy, and retest row marked fail then pass after fix without claiming live publish occurred.