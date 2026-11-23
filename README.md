# agent-templates

Private **Template-Datenbank** für KI-Agenten (Hermes, Grok Bot, OpenClaw, Claude Code, Codex, Cursor, generische MCP-Agenten): **welche Tools für welche Aufgabe**, mit Workflows, MCP-Katalog, Grundbeispielen und Freigaben.

Recherche-Stand: **23.11.2026** (siehe `research/SOURCES.md`; Roharchiv nicht versioniert).

## Umfang

| Kennzahl | Wert |
|----------|------|
| Domains | 27 |
| Kategorien | 198 (`_category.md` je Kategorie) |
| Templates | 247 (≥1 pro Kategorie, 2+ wo Recherche reich) |
| MCP-Einträge | 91 (`mcp/catalog.json`) |

## Struktur

```text
domains/<domain>/_domain.md
domains/<domain>/<category>/_category.md   # Tool-Stack, MCP-Tabelle, Fallstricke, Quellen
domains/<domain>/<category>/*.md             # Ausführbare Templates (YAML + Body)
mcp/catalog.json, mcp/README.md
adapters/                                    # Einbindung pro Agenten-Plattform
scripts/validate_and_index.py                # Validierung + INDEX.md + catalog.json (+ Qualitäts-Gates Phase 3)
TEMPLATE.md, template.schema.json
INDEX.md, catalog.json                       # generiert
research/SOURCES.md                          # bereinigte Quellenliste
```

## Template-Anatomie

- **Frontmatter:** `id`, `title`, `domain`, `category`, `tags`, `target_agents`, `required_tools`, `inputs`, `outputs`, `risk_level`, `example_count` (2–3), `version`, `updated`
- **Body:** Zweck, Wann nutzen (inkl. Wann nicht), Tool-Stack, System-Prompt (15–40 Zeilen), Arbeitsablauf (5–10 Schritte), Qualitätskriterien, Sicherheit, **Fallstricke**, **Grundbeispiele** (konkrete Beispiele; `Beispieldaten` oder `Praxisbeispiel` + URL)

Kategorie-Metadaten liegen in `_category.md` (nicht im Template-Frontmatter duplizieren).

## Neues Template

1. `TEMPLATE.md` nach `domains/<domain>/<category>/<id>.md` kopieren.
2. `domain` / `category` müssen zum Ordner passen.
3. Inhalt an `_category.md` und Recherche koppeln — keine unbelegten Tool-Claims.
4. `python3 scripts/validate_and_index.py` → `INDEX.md` / `catalog.json` committen.

## Agenten-Adapter

| Plattform | Datei |
|-----------|--------|
| Hermes | [adapters/hermes.md](adapters/hermes.md) |
| Grok Bot | [adapters/grokbot.md](adapters/grokbot.md) |
| OpenClaw | [adapters/openclaw.md](adapters/openclaw.md) |
| Claude Code | [adapters/claude-code.md](adapters/claude-code.md) |
| Cursor | [adapters/cursor.md](adapters/cursor.md) |
| Generisch | [adapters/generic.md](adapters/generic.md) |

Agent-Plattform-Setups: `domains/agent-platforms/<plattform>/`.

## Validierung

```bash
python3 scripts/validate_and_index.py
```

Prüft Schema, Pflichtsektionen (inkl. **Fallstricke**), `example_count`, Anti-Boilerplate (kein `{slug}`, keine Kurz-Prompts &lt;10 Zeilen, min. 5 Workflow-Schritte). CI: `.github/workflows/validate-templates.yml`.

Templates werden **manuell** gepflegt (kein Massen-Generator). Recherchearchiv nur lokal zur Einordnung.

## Datenschutz

Keine Secrets, keine Kundendaten. [CONTRIBUTING.md](CONTRIBUTING.md).