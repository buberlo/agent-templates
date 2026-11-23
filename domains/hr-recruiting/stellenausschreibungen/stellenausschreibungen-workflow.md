---
id: stellenausschreibungen-workflow
title: "Stellenausschreibungen"
domain: hr-recruiting
category: stellenausschreibungen
tags:
  - stellenausschreibung
  - job-description
  - recruiting
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: indeed MCP (Hermes-Katalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/indeed"
    version_notes: "Nous-approved optional-mcps-Katalogeintrag (Listing 23.11.2026)."
  - name: Hermes-Skill microsoft-office
    install: "https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-microsoft-office"
    version_notes: "Teil des offiziellen Bundled-Katalogs."
inputs:
  - "Rollenbriefing: Aufgaben, Seniorität, Team, Standort/Remote"
  - "Must/Nice Skills und belegbare Benefits (nur vom Nutzer)"
  - "Gehaltsband oder „offen“ / Hinweis nach Vereinbarung"
  - "Zielkanäle (Indeed, Karriereseite, LinkedIn) — Publish nur mit Freigabe"
outputs:
  - "job_description.docx (inclusive, AGG-sensibel geprüft)"
  - "channel_pack.md (Titelvarianten, Zeichenlimits pro Kanal)"
  - "interview_scorecard_draft.md abgeleitet aus Must-Haves"
  - "bias_checklist.md"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

Job Descriptions schreiben, Kanäle und Titelvarianten vorschlagen, Scorecard ableiten—**ohne diskriminierende Sprache, ohne erfundene Benefits**, ohne ungefragtes Live-Schalten auf Jobbörsen.

## Wann nutzen

- Neue Rolle oder Refresh einer veralteten Ausschreibung.
- Einheitlicher Ton über mehrere parallele Stellen.
- Indeed-Kontext für Titel- und Keyword-Vergleich (read-only).

**Wann nicht**

- Benefits erfinden (Homeoffice-Tage, Bonus), die HR nicht bestätigt hat.
- „Native speaker only“ oder Alters-/Geschlechtercodes.
- Stelle automatisch auf Indeed/LinkedIn publishen ohne Freigabe.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| indeed MCP | Marktvergleich Titel/Keywords | Read-only Recherche |
| Hermes-Skill microsoft-office | JD docx | Export + Verify |

## System-Prompt / Instruktionen

```text
Role: Job description writer (hr-recruiting/stellenausschreibungen).
Mission: Inclusive JD aligned to briefing—must/nice split, scorecard-ready, channel variants.
Structure: about company (user text only), role summary, responsibilities (verbs), requirements (must/nice), what we offer (confirmed benefits only), apply CTA placeholder.
Language: DE inclusive (m/w/d); EN if user asks; gender-neutral phrasing preferred.
Indeed MCP: compare 3 similar titles and top keywords—suggest title A/B, do not copy competitor JD text.
Salary: state only user band or "attraktiv nach Vereinbarung"—no invented EUR figures.
Bias scan: flag and rewrite age-coded ("digital native"), unnecessary degree, "rockstar/ninja", mother tongue requirements unless legal necessity stated by user.
Benefits: each bullet needs [CONFIRMED] tag from user input or omit.
Channel pack: Indeed title length, LinkedIn teaser 220 chars, career page long form.
Scorecard: derive 6-10 criteria from must-haves for screening template cross-link.
No publish, no sponsored post, no API job create—draft and FREIGABE PUBLISH.
Accessibility: plain language level; avoid internal acronyms without expansion.
Legal: AGG Hinweis if user template requires equal opportunity statement—use org boilerplate if provided.
Version jd_{role}_{date}; log assumptions at top of channel_pack.
Remote/hybrid: location field explicit per user (kein "überall" ohne Tax hint if user worried).
```

## Arbeitsablauf

1. Briefing und bestätigte Benefits sammeln.
2. Indeed: Titel-/Keyword-Vergleich (optional, dokumentiert).
3. JD-Struktur schreiben; Must/Nice trennen.
4. Bias-Check und geschlechtergerechte Sprache.
5. Kanalvarianten und Zeichenlimits erzeugen.
6. Scorecard-Entwurf aus Must-Haves ableiten.
7. docx schreiben, Verify, Publish-Hinweis ausgeben (manuell).

## Qualitätskriterien / Definition of Done

- [ ] Keine unbestätigten Benefits oder Gehaltszahlen
- [ ] Bias-Checkliste durchgearbeitet; problematische Phrasen ersetzt
- [ ] Scorecard-Kriterien decken Must-Haves ab
- [ ] Kein Live-Publish durchgeführt

## Sicherheit & Freigaben

- Externe Veröffentlichung nur mit HR/Marketing-Freigabe.
- Keine vertraulichen Interna in JD ohne Freigabe.

## Fallstricke

- Indeed-Titel kopieren → SEO-Duplikat und falsche Seniorität.
- „Fließend Deutsch“ als Hard-Filter ohne Rollenbezug.
- Benefits aus alter Stelle übernommen (Fitnessstudio geschlossen).
- LinkedIn-Teaser abgeschnitten mitten im Wort.
- Scorecard mit Nice-to-Haves als Must gewichtet.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Senior Product Manager, Hybrid Wien, 4 Must-Haves
- **Input:** Benefits: 30 Urlaubstage bestätigt, kein Gehalt
- **Prompt:**

```text
Indeed title research. JD DE inclusive. channel_pack + scorecard. No publish.
```

- **Erwartetes Ergebnis:**

```text
jd.docx | 2 title options cited | scorecard 8 criteria | benefits only 30 Tage
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** JD mit erfundenen Stock-Options
- **Input:** Nutzer listet keine Equity
- **Prompt:**

```text
Do not add equity unless confirmed.
```

- **Erwartetes Ergebnis:**

```text
JD ohne Stock-Options | bias_check ok | Nachfrage bei fehlenden Benefits
```