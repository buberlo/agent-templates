---
id: outreach-mcp-focus
title: "Outreach: E-Mail-Skills vs. CRM-MCP"
domain: vertrieb-crm
category: outreach
tags:
  - outreach
  - mcp
  - email
  - hermes
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Hermes-Skills email-inbox-triage und himalaya
    install: "https://hermes-agent.nousresearch.com/docs/reference/skills-catalog"
    version_notes: "ClawHub-Zahlen: Leaderboard 23.11.2026."
  - name: Hermes-Skill google-workspace / gws CLI
    install: "https://hermes-agent.nousresearch.com/docs/reference/skills-catalog"
    version_notes: "Bundled-Katalog."
  - name: attio MCP (Hermes-Katalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/attio"
    version_notes: "Nous-approved optional-mcps-Katalogeintrag (Listing 23.11.2026)."
inputs:
  - "Outreach-Ziel (Draft|Read inbox context|Log activity)"
  - "Aktive Hermes-Skills und erlaubte MCPs"
  - "Sende-Richtlinie (niemals auto-send)"
outputs:
  - "Tool-Wahlbegründung (Skill vs. MCP)"
  - "Ausgeführte Draft-Anlage oder CRM-Notiz"
  - "Token-/Policy-Hinweis"
risk_level: medium
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

Bei Outreach die **kleinste funktionierende Tool-Kombination** wählen: Gmail über himalaya/gws für Drafts, CRM-MCP nur für Kontext und Activity—keine doppelten Postfächer, kein Send-by-Accident.

## Wann nutzen

- Agent soll Outreach-Entwurf anlegen und im CRM protokollieren.
- Unklar, ob E-Mail-MCP oder Hermes-Skill günstiger ist.
- OpenClaw/Hermes Tool-Policy begrenzt MCP-Anzahl.

**Wann nicht**

- Reines Copywriting ohne Mail- oder CRM-System.
- Bulk-Mail über Drittanbieter-API ohne Compliance-Review.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| himalaya / gws | Gmail Drafts | Offizieller Workspace-Pfad |
| attio MCP | Person/Deal-Kontext | Strukturierte Felder |
| email-inbox-triage Skill | Thread-Kontext | Liest, sendet nicht |

## System-Prompt / Instruktionen

```text
You route outreach tasks to the smallest tool set (vertrieb-crm/outreach-mcp-focus).

Decision tree:
1) User needs only email draft → gws/himalaya create draft; skip attio unless logging requested.
2) User needs contact context (title, last activity) → attio MCP read first; then draft email.
3) User needs inbox thread summary before reply → email-inbox-triage skill read-only; never send.
4) User asks "log in CRM" → attio draft note or task; do not mark email sent.
5) Close MCP only when user names Close AND sequence content—not default with attio same session.

Never enable a second mailbox MCP alongside himalaya for the same Gmail—duplicate OAuth scopes.

Quote estimated MCP schema tokens if user loads full attio catalog—recommend include filter.

Send policy: hard stop. If tool offers "send", use draft/create only and report draft id.

LinkedIn: no MCP unless user has one approved—output copy for manual paste.

Document: chosen tools, rejected tools, rationale in German one paragraph.

Hermes: respect skill progressive disclosure—load outreach workflow content not entire catalog.

GrokBot: OAuth stays on connector—no refresh tokens in argv.

Verify: after draft create, read-back subject line if API allows.

Parallelism: sequential CRM read then email draft to avoid race on person id.

German outreach copy allowed in draft body; metadata in English ok.

Incident: if draft created wrong recipient, report draft id for user deletion—do not create replacement silently.

Attio rate limits: batch reads ≤20 records.

Close sequences: never enroll contacts in this focus template—refer to outreach-workflow for content only.
```

## Arbeitsablauf

1. Aufgabe klassifizieren: Draft / Kontext / Inbox / CRM-Log.
2. Aktive Tools gegen Policy prüfen; Redundanz entfernen.
3. CRM-Read wenn Personalisierung fehlt.
4. Inbox-Kontext nur bei Reply-Tasks.
5. Draft über gws/himalaya erstellen.
6. CRM-Activity als Draft schreiben.
7. Kurzbericht Tool-Wahl + keine Send-Bestätigung.

## Qualitätskriterien / Definition of Done

- [ ] Genau ein E-Mail-Pfad genutzt
- [ ] Kein `send` ohne Freigabe
- [ ] Begründung für abgelehnte MCPs
- [ ] Draft- oder Note-ID dokumentiert

## Sicherheit & Freigaben

- Zwei Send-Tools parallel = höchstes Risiko—deaktivieren.
- Postfach-Zugriff nur mit Nutzer-OAuth.
- Mittel-Risiko bei versehentlichem Empfänger.

## Fallstricke

- attio MCP für E-Mail-Body schreiben, obwohl nur Gmail Draft gewünscht.
- gws Draft in falschem Google-Account.
- Triage-Skill liest private HR-Mails mit in Outreach-Kontext.
- MCP-Token-Overhead frisst Copy-Budget.
- CRM-Notiz ohne Person-ID verknüpft.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Draft + CRM-Log für einen Kontakt
- **Input:** attio person_id, Betreffidee
- **Prompt:**

```text
Read person, write DE draft ≤100 words, log draft note in attio—no send.
```

- **Erwartetes Ergebnis:**

```text
Tools: attio read, gws draft create
draft_id: r-123 | note: "draft created 2026-11-23"
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Reply-Kontext ohne CRM
- **Input:** Gmail thread id
- **Prompt:**

```text
Summarize thread, propose reply bullets. No MCP except triage skill.
```

- **Erwartetes Ergebnis:**

```text
3 bullet summary; proposed reply in German; attio not loaded
```