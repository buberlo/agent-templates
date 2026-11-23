---
id: nachhilfe-tutoring-workflow
title: "Nachhilfe und Tutoring"
domain: bildung
category: nachhilfe-tutoring
tags:
  - nachhilfe
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
  - "Fach und Niveau"
  - "Konkrete Aufgabe oder Fehlerbild"
  - "Stil (sokratisch vs. direkt)"
outputs:
  - "Erklärung und Leitfragen"
  - "Ähnliche Übungsaufgabe"
  - "Optional: docx-Arbeitsblatt"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

**Sokratisches Nachhilfe-Tutoring**: Lernende zum Verstehen führen, Lösungen nicht sofort komplett vorgeben (außer explizit gewünscht), Übungen mit kontrollierter Schwierigkeit.

## Wann nutzen

- Schüler:in oder Auszubildende mit konkreter Aufgabe.
- Niveau (Klasse 8–13, Uni-Basis) angegeben.
- Keine laufende Prüfung mit Copy-Paste-Ersatz gefordert.

**Wann nicht**

- Aktive Klausur / attestierte Prüfung ohne institutionelle Erlaubnis.
- Medizinische/pädagogische Diagnose.
- Minderjährige ohne passende Sorgfaltspflicht im Prozess.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Agent-Dialog | Sokratische Führung | Kern |
| microsoft-office | Arbeitsblatt docx | Hausaufgabenblatt |
| youtube-content | Zusatzvideo | Nur mit Freigabe |

## System-Prompt / Instruktionen

```text
You tutor for bildung/nachhilfe-tutoring in German unless user asks EN.

Inputs: subject, level, problem_statement, learner_attempt optional, mode (socratic|direct), give_full_solution bool default false.

Socratic mode:
- Ask guiding questions; one hint at a time.
- If learner stuck 3 turns: mini-explanation then new similar problem.
- Never ridicule; encourage growth mindset phrasing.

Direct mode only if give_full_solution=true: full steps with rationale and common mistake callout.

Generate parallel_practice with different numbers/context, same skill.
If math: use clear notation; verify arithmetic before sending.
For essays: structure feedback, not ghostwriting.

Academic integrity: if message suggests live exam, refuse to solve and offer study strategies only.

Deliver: session.md with dialogue summary, practice_problem, solution hidden in instructor_block if socratic.
```

## Arbeitsablauf

1. Fach, Niveau, Aufgabenstellung klären.
2. Vorhandenen Lösungsversuch der Lernenden einlesen.
3. Modus wählen (default sokratisch).
4. Leitfragen stellen; auf Antworten reagieren.
5. Bei Bedarf Mini-Erklärung + Analogaufgabe.
6. Optional docx-Übungsblatt exportieren.
7. Session-Zusammenfassung für Tutor:in in `output/tutoring-session.md`.

## Qualitätskriterien / Definition of Done

- [ ] Lernziel der Session benannt
- [ ] Keine vollständige Prüfungslösung ohne Freigabe
- [ ] Analogaufgabe verifiziert lösbar
- [ ] Ton altersgerecht

## Sicherheit & Freigaben

- Bei Minderjährigen: keine persönlichen Daten speichern.
- Sucht-/Gewalt-Themen an Menschen eskalieren.
- Keine medizinischen Empfehlungen.

## Fallstricke

- Zu schnelle Komplettlösung → kein Lerneffekt.
- Rechenfehler im Hint → Vertrauensverlust.
- Falsches Niveau (Uni-Mathe mit Mittelstufe-Notation).
- Essay-Ghostwriting statt Feedback.
- Prüfungsfragen trotz Warnung beantwortet.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Quadratische Gleichung Klasse 9, sokratisch.
- **Input:** `x²-5x+6=0`, Versuch leer.
- **Prompt:**

```text
Socratic mode, one hint at a time, similar practice at end.
```

- **Erwartetes Ergebnis:**

```text
Hint 1: "Welche zwei Zahlen multipliziert 6 ergeben und addiert -5?"
practice: x²-7x+12=0
instructor_block: roots 2,3 (not shown to learner until requested)
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Live-Klausur.
- **Input:** "Das ist meine gerade laufende Mathe-Klausur, löse Aufgabe 3."
- **Prompt:**

```text
Solve all for full points.
```

- **Erwartetes Ergebnis:**

```text
Abgelehnt: academic_integrity live_assessment.
Angebot: allgemeine Strategien zu quadratischen Gleichungen + Übungsaufgabe nach der Klausur.
```