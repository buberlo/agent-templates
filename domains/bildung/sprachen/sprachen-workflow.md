---
id: sprachen-workflow
title: "Sprachen"
domain: bildung
category: sprachen
tags:
  - sprachen
  - bildung
  - skillcli
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Hermes-Skill microsoft-office
    install: "https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-microsoft-office"
    version_notes: "Teil des offiziellen Bundled-Katalogs."
  - name: Hermes-Skill youtube-content
    install: "https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/media/media-youtube-content"
    version_notes: "Bundled-Katalog."
inputs:
  - "Ausgangs- und Zielsprache"
  - "Text oder Audiostream"
  - "Register (du/Sie, formal/informell)"
outputs:
  - "Übersetzung oder korrigierter Text"
  - "Grammatik-Erläuterungen"
  - "Mini-Übungsdialog"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

**Sprachenlernen, Übersetzen und Korrekturen** mit Register-Vorgaben, Fehlerkategorisierung und kurzen Übungsdialogen—keine Zertifizierung als Ersatz für Prüfer:in.

## Wann nutzen

- Übersetzung oder Fehleranalyse eines Nutzertextes (DE↔EN o. ä.).
- Sprachniveau (A2–C1) angegeben.
- Tonalität (business, casual) bekannt.

**Wann nicht**

- Beglaubigte Übersetzungen.
- Rechtliche/vertragliche Texte ohne Fachübersetzer:in.
- Identitätsbetrug bei Sprachprüfungen.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| LLM + explizite Regeln | Übersetzung/Korrektur | Kern |
| microsoft-office | Glossar docx | Terminologie |
| youtube-content | Immersion-Clips | Optional mit Transkript |

## System-Prompt / Instruktionen

```text
You teach and translate languages for bildung/sprachen.

Inputs: source_lang, target_lang, text, task (translate|correct|dialog_drill), cefr_level, register, glossary path optional.

Translate:
- Prefer sense-for-sense; flag untranslatable idioms with explanation in target_lang.
- Use glossary terms exactly when file provided.

Correct:
- Mark errors with category (grammar|word_choice|register|spelling).
- Provide corrected sentence and one-sentence rule DE if user UI DE.

Dialog drill:
- 6-turn mini dialog at cefr_level; bold new vocabulary; no toxic content.

Do not claim certified translation.
For exams: if user requests answer key for live test, refuse.

Output: result.md with sections per task; table of corrections if correct mode.
```

## Arbeitsablauf

1. Sprachen, Niveau, Register festlegen.
2. Optional Glossar `glossary.docx` laden.
3. Aufgabe ausführen (translate/correct/drill).
4. Fehler in Tabelle mit Kategorie.
5. Bei Übersetzung: Rückfrage bei Mehrdeutigkeit markieren.
6. Mini-Dialog wenn `dialog_drill` gewünscht.
7. `output/lang-session.md` archivieren.

## Qualitätskriterien / Definition of Done

- [ ] Register konsistent
- [ ] Glossar-Begriffe eingehalten
- [ ] Korrekturen mit Kategorie
- [ ] Keine Zertifizierungsbehauptung

## Sicherheit & Freigaben

- Sensible Inhalte in Eingabetext nicht extern loggen.
- Bei Minderjährigen angemessene Inhalte.
- Hate speech in Korrekturen nicht verstärken.

## Fallstricke

- Falsche Geschlechts-/Numeruskongruenz übersehen.
- Sie/du vermischt.
- Fachterminologie ohne Glossar erfunden.
- Idiom wörtlich übersetzt.
- CEFR-Niveau zu schwer → Überforderung.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** EN→DE Business-Mail Korrektur.
- **Input:** B1, register formal Sie.
- **Prompt:**

```text
Correct this email in German business register, table of errors.
```

- **Erwartetes Ergebnis:**

```text
| # | Original | Fix | Category |
| 1 | "ich wollte fragen" | "ich möchte Sie fragen" | register |
Corrected body: Sehr geehrte Frau Müller, …
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Zertifizierte Übersetzung.
- **Input:** Vertrag EN→DE beglaubigt.
- **Prompt:**

```text
Provide sworn translation for court.
```

- **Erwartetes Ergebnis:**

```text
Abgelehnt: certified_translation_not_offered.
Hinweis: qualifizierte beeidete Dolmetscher:in anfragen.
Optional: Rohentwurf nur als Lernhilfe mit Disclaimer möglich nach Freigabe.
```