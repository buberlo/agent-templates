---
id: imessage-sms-workflow
title: "iMessage und SMS"
domain: kommunikation
category: imessage-sms
tags:
  - imessage
  - kommunikation
  - skillcli
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Hermes-Skill imessage
    install: "https://hermes-agent.nousresearch.com/docs/reference/skills-catalog"
    version_notes: "Bundled apple/imessage, macOS."
  - name: Hermes-Skill google-workspace / gws CLI
    install: "https://hermes-agent.nousresearch.com/docs/reference/skills-catalog"
    version_notes: "Optional: Termin-Kontext aus Calendar."
inputs:
  - "Kontakt-Handle oder Chat"
  - "Nachrichtenentwurf oder Leseauftrag"
  - "Freigabe SEND ja/nein"
outputs:
  - "Konversationsauszug"
  - "Gesendete oder vorgelegte SMS/iMessage"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

**Kurznachrichten** über Hermes **imessage** (macOS/imsg CLI) lesen und **nur nach Freigabe** senden; SMS/iMessage-Log für Follow-ups dokumentieren.

## Wann nutzen

- macOS-Host mit Messages-Account und Hermes imessage-Skill.
- Kurze Koordination (Verspätung, Termin, OTP-Hinweis ohne OTP selbst zu speichern).
- Entwurf zuerst, Senden mit explizitem `SEND`.

**Wann nicht**

- Linux/Windows ohne macOS-Bridge → Skill wird übersprungen.
- Massen-SMS/Marketing ohne Opt-in und Carrier-Policy.
- MFA-Codes oder Passwörter per Chat versenden.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Hermes imessage | Lesen/Senden | Offizielles bundled Skill |
| gws Calendar (optional) | Kontext | Terminzeit im Entwurf |
| Markdown-Log | Audit | Handle redacted, Zeitstempel |

## System-Prompt / Instruktionen

```text
You operate iMessage/SMS on macOS via Hermes imessage skill (imsg CLI). Read chats, draft short replies; send only on explicit "SEND <handle>".

Inputs: handle (phone or email), action (list | read | draft | send), max_messages, draft_text, language DE.

Read: list recent messages with timestamps; quote last inbound for context.
Draft: <= 320 chars for SMS-safe; mark iMessage vs SMS if known.
Send: echo exact body; require user confirmation string; log message_id if returned.

Do not automate 2FA codes delivery to third parties.
Redact handles in external summaries (show last 2 digits only).
If not on darwin, stop and report platform_unsupported—do not fake send.

Deliver: conversation-excerpt.md, draft block, send receipt or "draft only".
```

## Arbeitsablauf

1. `uname -s` — bei nicht-Darwin abbrechen mit klarer Meldung.
2. Handle und Auftrag klären (lesen vs. senden).
3. `imsg` über Skill: letzte N Nachrichten lesen.
4. Antwortentwurf (kurz, klar, ohne Links wenn SMS-only vermutet).
5. Nutzer prüft Text; bei OK: `SEND` mit Handle wiederholen.
6. Nach Send: letzte Zeile aus Chat verifizieren.
7. `output/imessage-log.md` mit Zeit, Aktion, redacted handle.

## Qualitätskriterien / Definition of Done

- [ ] Plattform macOS bestätigt oder sauber abgebrochen
- [ ] Gesendeter Text byte-identisch mit freigegebenem Entwurf
- [ ] Keine Secrets im Log
- [ ] Empfänger-Handle im internen Log dokumentiert

## Sicherheit & Freigaben

- Apple-ID und Geräte-Trust liegen beim Nutzer; Agent nutzt nur skill-exponierte CLI.
- Keine Weiterleitung von Gesundheits- oder Finanz-PII in SMS ohne Einwilligung.
- Senden gesperrt ohne zweites explizites Kommando.

## Fallstricke

- Grüne vs. blaue Blase (SMS vs. iMessage) ändert Zeichenlimit.
- Falscher Handle → Nachricht an falschen Kontakt (Handle vor Send doppelt zeigen).
- Skill auf Linux still skipped ohne Agent-Hinweis wenn Prompt schwach.
- Automatische Links → Carrier-Splitting bei SMS.
- Gruppenchats: Reply-Kontext leicht verloren.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Verspätung 15 Min melden.
- **Input:** Handle `+43…901`, Draft DE.
- **Prompt:**

```text
Draft SMS: "Bin in 15 Min da, sorry!" — show draft, wait for SEND.
```

- **Erwartetes Ergebnis:**

```text
Draft: Bin in 15 Min da, sorry!
Status: draft_only (awaiting SEND +43***901)
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Linux-Server.
- **Input:** `uname` = Linux, imessage angefragt.
- **Prompt:**

```text
Send meeting link via iMessage.
```

- **Erwartetes Ergebnis:**

```text
Abbruch: platform_unsupported (imessage requires darwin).
Alternative: E-Mail-Entwurf oder manuelles Senden vom Mac vorschlagen.
```