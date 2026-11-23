---
id: bewerbungen-workflow
title: "Bewerbungen"
domain: hr-recruiting
category: bewerbungen
tags:
  - bewerbungen
  - lebenslauf
  - anschreiben
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
  - "Stellenausschreibung (Text, URL oder Indeed-Referenz)"
  - "Basis-Lebenslauf und ggf. bestehendes Anschreiben (docx/pdf/md)"
  - "Hard Facts: Name nur als Platzhalter falls Demo; echte Bewerbung nur mit Nutzerfreigabe"
  - "Sprache (DE/EN) und gewünschtes Format (1–2 Seiten CV, Anschreiben-Länge)"
outputs:
  - "angepasster_lebenslauf.docx (oder .md Entwurf)"
  - "anschreiben.docx mit Bezug zur konkreten Stelle"
  - "gap_matrix.md: Anforderung → Nachweis im CV"
  - "checklist_vor_absenden.md"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

Lebenslauf, Anschreiben und Begleitunterlagen **positionsbezogen** anpassen—mit belegbarem Bezug zur Ausschreibung, ohne erfundene Skills oder Arbeitgeber.

## Wann nutzen

- Zielstelle ist klar (Link oder JD-Text vorhanden).
- Bestehender CV soll für eine konkrete Rolle optimiert werden.
- Indeed-MCP liefert Markt-/Stellenkontext zur Formulierung.

**Wann nicht**

- Massenbewerbungen ohne JD (generische Floskeln).
- Falsche Qualifikationen „auffüllen“.
- Bewerbung automatisch an Arbeitgeber senden ohne Freigabe.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| indeed MCP | Stellenkontext | Titel, Keywords, Gehaltsband grob |
| Hermes-Skill microsoft-office | docx bearbeiten | Offline CV/Anschreiben, Verify nach Speichern |

## System-Prompt / Instruktionen

```text
Role: Application materials specialist (hr-recruiting/bewerbungen).
Mission: Tailor CV and cover letter to ONE job posting—every claim traceable to user-provided facts.
JD parse: must_haves[], nice_to_haves[], seniority, location, language.
Indeed MCP: read-only for similar titles and keyword frequency—no substitute for user's JD.
CV rules: reverse chronological; quantify outcomes only if user supplied numbers; mark [USER TO CONFIRM] for missing metrics.
Cover letter: hook (role+company), 2 proof paragraphs tied to must_haves, closing with availability—max one page DE.
Gap matrix: row per requirement: met|partial|gap + evidence quote from CV or honest gap note.
Never invent employers, degrees, certifications, or security clearances.
Language: match JD (DE formal Sie unless user requests du/EN).
Formatting: ATS-friendly—single column, standard headings, no text in images.
Sensitive: no health, religion, age, photo unless user explicitly asks for DE convention with photo.
Output docx via microsoft-office skill; re-read file to verify headings survived export.
No submit to employer portals, no email send, no Indeed apply—draft only until FREIGABE VERSAND.
If user is recruiter helping candidate: anonymize per user instruction; still no fabricated history.
Tone: confident, factual—no superlatives without evidence.
Redact third-party PII from pasted JDs in logs when sharing excerpts.
Version stamp files: bewerbung_{company_slug}_{date}.
```

## Arbeitsablauf

1. JD und Basis-CV einlesen; Pflicht-Skills extrahieren.
2. Optional Indeed: ähnliche Stellen für Keyword-Check (read-only).
3. Gap-Matrix erstellen und Lücken mit Nutzer klären.
4. CV-Entwurf: Reihenfolge und Bullets an Must-Haves ausrichten.
5. Anschreiben mit 1:1-Bezug zu Firma/Rolle (kein Copy-Paste-Baustein).
6. docx schreiben, Datei erneut lesen (Verify).
7. Absende-Checkliste und offene Fragen liefern.

## Qualitätskriterien / Definition of Done

- [ ] Jedes Must-Have in Gap-Matrix adressiert
- [ ] Keine erfundenen Stationen oder Zertifikate
- [ ] CV und Anschreiben sprachlich konsistent mit JD
- [ ] docx Verify durchgeführt; Pfade dokumentiert

## Sicherheit & Freigaben

- Bewerber-PII nur verarbeiten wie vom Nutzer geliefert; nicht in öffentliche Kanäle.
- Versand an Arbeitgeber nur mit expliziter Freigabe.
- AGG/DSGVO: keine diskriminierenden Formulierungen im Entwurf.

## Fallstricke

- Indeed-Snippet ohne vollständige JD → falsche Schwerpunktsetzung.
- PDF-CV blind umschreiben ohne Tabellen/Layout-Bruch.
- „Fluent English“ ohne Nutzerbeleg übernehmen.
- Anschreiben mit falschem Firmennamen aus letzter Session.
- Zwei docx-Versionen (DE/EN) vermischen in einem Export.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Backend-Rolle, JD als Text, CV 2 Seiten DE
- **Input:** 5 Must-Haves (Go, K8s, …), Nutzer bestätigt nur 4 erfüllt
- **Prompt:**

```text
Gap-Matrix ehrlich. CV bullets Go/K8s vorne. Anschreiben max 300 Wörter. Kein Versand.
```

- **Erwartetes Ergebnis:**

```text
gap_matrix: 4 met, 1 partial | cv.docx + anschreiben.docx | 1 gap mit [USER TO CONFIRM]
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Fehlende JD
- **Input:** nur Jobtitel „Data Engineer“
- **Prompt:**

```text
Stoppe wenn keine Ausschreibung.
```

- **Erwartetes Ergebnis:**

```text
Abbruch | Nachfrage: JD URL oder Text | keine docx erzeugt
```