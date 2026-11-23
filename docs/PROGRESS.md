# Migration progress

## Completed (2026-11-23)

- **English migration (full repo):** Domain and category slugs, all template bodies and frontmatter, `_domain.md` / `_category.md` files, and root docs (`README.md`, `CONTRIBUTING.md`, `TEMPLATE.md`, adapter guides) are in English with the standard section headings (Purpose, When to use, Tool stack, System prompt, Workflow, Definition of done, Security, Pitfalls, Basic examples).
- **Validator:** `scripts/validate_and_index.py` enforces English (strict language gate), required sections, schema, and deterministic `catalog.json` / `INDEX.md` generation.
- **Catalogs:** Root `catalog.json`, `INDEX.md`, and `mcp/catalog.json` paths/descriptions aligned to English domain slugs.
- **CI:** `validate-templates.yml` passes locally with regenerated artifacts.

## Hygiene (this PR)

- Replaced example-only German domains (`firma.de`, etc.) with `example.com` where found.
- No API keys, private keys, or live tokens found in tracked content.

## Backlog (next)

1. **Template quality pass:** Shorten and deepen telegraphic templates (e.g. `it-operations-support/helpdesk-it/google-workspace-admin`) so prompts, pitfalls, and examples are actionable rather than keyword lists.
2. **Validator hardening:** Minimum length for example expected outputs; heuristic check for keyword-salad system prompts.