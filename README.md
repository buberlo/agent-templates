# agent-templates

Private Template-Datenbank für KI-Agent-Setups (**Hermes Agent**, **Grok Bot**, Claude/Codex-ähnliche und generische Agents). Jedes Template beschreibt **welche Tools für welche Aufgabe** — inklusive kopierfertiger System-Prompts, Workflows und Freigaben.

## Zweck

- Schnelles Onboarding neuer Kunden-Bots ohne Prompt-Chaos
- Einheitliche Qualitäts- und Sicherheitskriterien (`risk_level`, Freigaben)
- Maschinenlesbarer Katalog für CI und interne Portale

## Struktur

```text
categories/<kategorie>/<id>.md   # Ein Template pro Datei (YAML-Frontmatter + Markdown-Body)
adapters/                        # Hinweise: Hermes, Grok Bot, generischer Export
TEMPLATE.md                      # Leere Vorlage
template.schema.json             # JSON Schema für Frontmatter
scripts/validate_and_index.py    # Validierung + INDEX.md + catalog.json
INDEX.md, catalog.json           # generiert — nicht von Hand editieren
.github/workflows/               # CI-Validierung
```

### Kategorien

| Ordner | Thema |
|--------|--------|
| `video-bearbeitung` | Schnitt, Transcode, Remotion |
| `audio` | Transkription, Podcast-Mastering |
| `bild` | Batch, Generative Pipelines |
| `dokumente-office` | Pandoc, LibreOffice |
| `web-recherche` | Browser-Research, Briefings |
| `coding-devops` | CI, IaC |
| `kubernetes-infra` | kubectl, Helm |
| `it-support-remote` | MeshCentral, Patch-Baseline |
| `social-media` | Planung, Shorts-Repurpose |
| `email-kommunikation` | MCP-Triage, DMARC |
| `daten-analyse` | DuckDB, Pandas EDA |
| `finanzen-buchhaltung` | CAMT, DATEV-CSV |

## Neues Template anlegen

1. `TEMPLATE.md` nach `categories/<kategorie>/<id>.md` kopieren (`id`: Kleinbuchstaben, Bindestriche).
2. `category` im Frontmatter **muss** dem Ordnernamen entsprechen.
3. Alle Body-Abschnitte ausfüllen (siehe `TEMPLATE.md`).
4. Validierung lokal ausführen (siehe unten).
5. `INDEX.md` und `catalog.json` mit committen.

## Nutzung mit Agents

| Plattform | Anleitung |
|-----------|-----------|
| Hermes Agent | [adapters/hermes.md](adapters/hermes.md) — Skill/System-Prompt aus **System-Prompt / Instruktionen** |
| Grok Bot | [adapters/grokbot.md](adapters/grokbot.md) — Bot-Bio + Skill |
| Generisch | [adapters/generic.md](adapters/generic.md) — Export-Layout + `catalog.json` |

`target_agents` im Frontmatter zeigt, für welche Plattform das Template gedacht ist.

## Validierung

```bash
python3 scripts/validate_and_index.py
```

Bei Erfolg: Aktualisierung von `INDEX.md` und `catalog.json`. Bei Fehlern: Exit-Code 1 mit Liste der Abweichungen (Schema, fehlende Sektionen, Kategorie ≠ Ordner).

GitHub Actions führt denselben Befehl bei Push und Pull Request aus.

## Lizenz & Daten

Keine Secrets, keine Kundendaten in Templates. Beispiele sind fiktiv.

Siehe [CONTRIBUTING.md](CONTRIBUTING.md) für Kurzregeln zu PRs und Stil.