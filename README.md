# agent-templates

Public **template database** for AI agents (Hermes, Grok Bot, OpenClaw, Claude Code, Codex, Cursor, generic MCP agents): **which tools fit which job**, with workflows, MCP catalog, basic examples, and approval rules.

Research baseline: **2026-11-24** (see `research/SOURCES.md`; raw archive is not versioned).

## Scope

| Metric | Value |
|--------|------:|
| Domains | 27 |
| Categories | 199 (`_category.md` per category) |
| Templates | 279 (≥1 per category, 2+ where research was rich) |
| MCP entries | 105 (`mcp/catalog.json`) |

## Layout

```text
domains/<domain>/_domain.md
domains/<domain>/<category>/_category.md   # tool stack, MCP table, pitfalls, sources
domains/<domain>/<category>/*.md             # executable templates (YAML + body)
mcp/catalog.json, mcp/README.md
adapters/                                    # wiring per agent platform
scripts/validate_and_index.py                # validation + INDEX.md + catalog.json
TEMPLATE.md, template.schema.json
INDEX.md, catalog.json                       # generated
research/SOURCES.md                          # curated source list
docs/PROGRESS.md                             # migration status and backlog
```

## Template anatomy

- **Frontmatter:** `id`, `title`, `domain`, `category`, `tags`, `target_agents`, `required_tools`, `inputs`, `outputs`, `risk_level`, `example_count` (2–3), `version`, `updated`
- **Body:** Purpose, When to use (incl. When not to use), Tool stack, System prompt, Workflow, Definition of done, Security, Pitfalls, Basic examples (`Example data` or `Real-world example` + source URL)

Category metadata lives in `_category.md` (not duplicated in template frontmatter).

## New template

1. Copy `TEMPLATE.md` to `domains/<domain>/<category>/<id>.md`.
2. `domain` / `category` must match the folder path.
3. Tie content to `_category.md` and research — no unsupported tool claims.
4. Run `python3 scripts/validate_and_index.py` and commit `INDEX.md` / `catalog.json`.

## Agent adapters

| Platform | File |
|----------|------|
| Hermes | [adapters/hermes.md](adapters/hermes.md) |
| Grok Bot | [adapters/grokbot.md](adapters/grokbot.md) |
| OpenClaw | [adapters/openclaw.md](adapters/openclaw.md) |
| Claude Code | [adapters/claude-code.md](adapters/claude-code.md) |
| Cursor | [adapters/cursor.md](adapters/cursor.md) |
| Codex | [adapters/codex.md](adapters/codex.md) |
| Generic | [adapters/generic.md](adapters/generic.md) |

Platform setup templates: `domains/agent-platforms/<platform>/`.

## Validation

```bash
python3 scripts/validate_and_index.py
```

Checks schema, required English sections, `example_count`, anti-boilerplate rules, and a strict English language gate. CI: `.github/workflows/validate-templates.yml`.

Templates are **maintained manually** (no bulk generator). Research archives stay local for curation only.

## Privacy

No secrets or customer data in examples. See [CONTRIBUTING.md](CONTRIBUTING.md).