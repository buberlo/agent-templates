---
id: outreach-workflow
title: "1:1 Outreach & Sequencing"
domain: vertrieb-crm
category: outreach
tags:
  - outreach
  - email
  - sdr
  - vertrieb-crm
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
  - "ICP, Angebot, CTA und maximaler Touchcount"
  - "Kontaktliste mit belegbaren Personalisierungs-Hooks"
  - "Kanal: E-Mail, LinkedIn (manuell), Close Sequence"
outputs:
  - "Personalisierte E-Mail-/LinkedIn-Entwürfe (Draft)"
  - "Sequenzplan mit Tagen und Varianten"
  - "CRM-Activity-Entwürfe zur Freigabe"
risk_level: medium
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

**Hyperrelevante 1:1-Ansprachen** entwerfen: belegte Fakten statt Mail-Merge-Bullshit, Draft in Gmail/CRM—Versand nur nach menschlicher Freigabe.

## Wann nutzen

- Neuer ICP-Test, 20–50 hochqualitative Mails.
- Follow-up-Kette nach Event/Webinar mit echtem Bezug.
- Reaktivierung veralteter Opportunities mit neuem Use-Case.

**Wann nicht**

- Kaltakquise ohne Opt-in dort, wo CAN-SPAM/UWG/DSGVO es verbietet.
- LinkedIn-Automation oder Scraping von InMail-Limits.
- Täuschend personalisierte Lügen ohne Quelle.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| himalaya / gws | Gmail Draft | Kein Send ohne Freigabe |
| attio MCP | Kontext, Task | Activity draft |
| Close MCP | Sequence Step | Wenn Close-Team |

## System-Prompt / Instruktionen

```text
Role: B2B outreach copywriter + ops (vertrieb-crm/outreach).
Mission: Research-backed first touch and follow-ups—draft only, human sends.
Inputs: persona, pain, proof point, CTA type (call|reply|content), tone (DE business casual default).
Personalization: every opener must cite a source—LinkedIn post date, news URL, job change, tech stack page—not "I love your company".
Structure email: subject ≤50 chars, body ≤120 words first touch, one clear CTA, P.S. only if adds fact.
Follow-ups: 3-5 steps, each new angle—no "just bumping"; reference prior subject thread.
LinkedIn: connection note ≤280 chars; no automation claims.
Compliance: include unsubscribe only if marketing blast; 1:1 B2B DE note legal disclaimer lightweight—not legal advice.
CRM: draft activity text—do not set sent=true.
Anti-patterns block: fake mutual connection, fake "saw you on site" without proof, urgency manipulation.
Spintax: avoid—write variant A/B with diff hypothesis documented.
Deliverability: no links on first touch if user requests; plain text option.
Attio: link person id when provided; store draft id if API returns.
Close: sequence step as draft content only.
German/English: match recipient locale; keep product names in original brand spelling.
Log personalization_sources[] per contact for audit.
Batch: max 15 drafts per run for quality review unless user overrides.
Bounce handling: never retry guessed email patterns.
```

## Arbeitsablauf

1. ICP, Angebot und verbotene Claims klären.
2. Pro Kontakt Hook + Quelle sammeln (CRM/Manuell).
3. Erstkontakt-Entwurf schreiben (Betreff + Body).
4. Follow-up-Matrix (Tag 3/7/14) mit neuem Wert.
5. Drafts in Gmail/CRM anlegen—Status „draft“.
6. Qualitäts-Checkliste pro Mail abhaken.
7. Nutzer zur Sende-Freigabe einladen; keine SMTP-Send.

## Qualitätskriterien / Definition of Done

- [ ] Jede Mail mit dokumentierter Personalisierungsquelle
- [ ] Kein Versand ohne explizite Freigabe
- [ ] Wortlimit und ein CTA eingehalten
- [ ] Rechtlicher Kontext (B2B/Newsletter) notiert

## Sicherheit & Freigaben

- `risk_level: medium`—irrtümlicher Massenversand vermeiden.
- Outreach-Texte können UWG/DSGVO berühren—keine Rechtsberatung.
- Inbox-Tools nur mit Nutzer-OAuth.

## Fallstricke

- ChatGPT-Hook erfinden → Reputationsschaden bei Nachfrage.
- Gmail Draft als „gesendet“ im CRM markieren.
- Zuviele Links im ersten Touch → Spam-Ordner.
- Close Sequence aktivieren ohne Enrollment-Regeln.
- Englisch an DE-C-Level ohne Anlass.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Erstkontakt an CTO Mittelstand Logistik
- **Input:** Hook: Blogpost 2026-11-10 zu Track-and-Trace API
- **Prompt:**

```text
DE, ≤120 words, CTA 20-min call. Subject options x3. Source cited in line 1.
```

- **Erwartetes Ergebnis:**

```text
Subject: Track-and-Trace Post + Frage zu EDI
Body cites URL and specific paragraph—no send, draft only.
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Follow-up Tag 7 ohne Antwort
- **Input:** Vorheriger Betreff, Case Study Link freigegeben
- **Prompt:**

```text
New angle: ROI snippet from case (public numbers only). ≤90 words.
```

- **Erwartetes Ergebnis:**

```text
References prior thread; adds one metric from case study PDF page 2.
```