---
id: knowledge-base-workflow
title: "Wissensdatenbank Support"
domain: kundenservice
category: knowledge-base
tags:
  - knowledge
  - kundenservice
  - mcp
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: intercom MCP (Hermes-Katalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/intercom"
    version_notes: "Nous-approved optional-mcps-Katalogeintrag (Listing 23.11.2026)."
inputs:
  - "Ticket-Cluster oder FAQ-Thema"
  - "Bestehende Artikel-IDs"
  - "Freigabe publish"
outputs:
  - "KB-Artikel-Entwurf"
  - "Makro-Vorschlag"
  - "Gap-Liste"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

Aus Tickets und Runbooks **Hilfeartikel und Makros** pflegen, **Lücken** identifizieren und Inhalte **erst nach Review** veröffentlichen.

## Wann nutzen

- Wiederkehrende Fragen (≥5 Tickets/Woche gleiches Thema).
- Intercom Articles oder internes Wiki angebunden.
- Styleguide (Du/Sie, Produktnamen) vorliegt.

**Wann nicht**

- Einmalige Edge-Cases ohne Wiederholrate.
- Security-spezifische interne Runbooks → nur intern, nicht öffentliche KB.
- Publish ohne Fachteam-Review.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| intercom MCP | Articles, Tickets | Quelle + Ziel |
| Markdown/Docx | Entwurf | Review-Workflow |
| Diff gegen bestehende Artikel | Qualität | Keine Duplikate |

## System-Prompt / Instruktionen

```text
You maintain support knowledge for kundenservice/knowledge-base.

Inputs: topic, ticket_ids[] or search query, existing_article_id optional, audience (customer|internal), language DE.

Process:
1) Sample 5-10 tickets on topic; extract common questions and correct resolutions actually used by agents.
2) List kb_gaps[] where no article covers resolution.
3) Draft article: title, symptoms, steps numbered, prerequisites, when to contact support, last_reviewed date placeholder.
4) Propose intercom macro snippet if replies are repetitive.
5) Diff against existing_article_id; output changed_sections only.

publish=false default; set publish only after user types APPROVE_PUBLISH.
No copy-paste of credentials or customer PII into public articles.
Link product UI with current naming from styleguide.

Deliver: article_draft.md, macro_draft.txt, gaps.md, citations ticket_ids[].
```

## Arbeitsablauf

1. Thema und Ticket-Stichprobe per MCP suchen.
2. Häufige Fragen und gültige Lösungen extrahieren.
3. Bestehenden Artikel laden falls `existing_article_id`.
4. `article_draft.md` mit nummerierten Schritten schreiben.
5. Makro-Vorschlag für Support-Antworten.
6. `gaps.md` für ungedeckte Unterfragen.
7. Nach `APPROVE_PUBLISH`: Article anlegen/aktualisieren (wenn MCP erlaubt).

## Qualitätskriterien / Definition of Done

- [ ] Schritte mit aktueller Produkt-UI vereinbar
- [ ] Keine PII oder interne URLs in Public-Artikel
- [ ] Zitierte Ticket-IDs als Beleg
- [ ] Publish nur mit Freigabe

## Sicherheit & Freigaben

- Interne-only Sections klar markieren.
- Security-Hinweise von Security-Team gegenzeichnen lassen.
- Screenshots ohne Kundendaten.

## Fallstricke

- Veraltete UI-Schritte nach Release.
- Makro zu lang → Agenten ignorieren es.
- Duplikat-Artikel SEO-intern verwirrt.
- Lösung aus einem Sonderfall generalisiert.
- Publish überschreibt produktive Artikel ohne Backup.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Passwort-Reset-FAQ aktualisieren.
- **Input:** 8 Tickets `password reset`, Artikel-ID `art_102`.
- **Prompt:**

```text
Draft updated customer article DE, diff against art_102, macro snippet, no publish.
```

- **Erwartetes Ergebnis:**

```text
Changed sections: step 2 (new SSO button), troubleshooting MFA
Macro: "Hallo {{first_name}}, hier die Schritte…" (<=400 chars)
Publish: pending
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Publish ohne Review.
- **Input:** Sofort live stellen.
- **Prompt:**

```text
Publish article to help center now.
```

- **Erwartetes Ergebnis:**

```text
Abbruch: APPROVE_PUBLISH required.
Draft saved: output/article_draft.md
Live site: unchanged
```