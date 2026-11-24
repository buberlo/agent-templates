# Migration progress

## Completed (2026-11-24)

- **Template quality pass (batch 2):** Hand-rewrote 15 templates (IT ops Google Workspace, Ansible patching, Entra/AD, backup, MDM; content-marketing branding/copy/social; software backend/frontend/mobile/code review; vuln management; household) with concrete system prompts, numbered workflows, actionable pitfalls, and **Example data (self-written)** blocks with explicit Input and Expected result.
- **Validator hardening:** `scripts/validate_and_index.py` enforces minimum system-prompt length, sentence-like lines, keyword-salad heuristics, minimum expected-output length in Basic examples, the `(Example data (self-written))` example heading, and a cap on identical non-trivial system-prompt lines shared across templates (max 10).
- **Quality backlog:** Removed mechanical bootstrap padding from batch 2. **152** templates are listed in `scripts/quality_backlog.txt` and emit **warnings** (not hard errors) until rewritten. Future quality batches must improve backlog entries by hand—no scripted padding or shared guardrail paragraphs.
- **Catalogs:** Regenerated root `catalog.json` and `INDEX.md` via the validator (deterministic ordering).

## Completed (2026-11-23)

- **English migration (full repo):** Domain and category slugs, all template bodies and frontmatter, `_domain.md` / `_category.md` files, and root docs (`README.md`, `CONTRIBUTING.md`, `TEMPLATE.md`, adapter guides) are in English with the standard section headings (Purpose, When to use, Tool stack, System prompt, Workflow, Definition of done, Security, Pitfalls, Basic examples).
- **Validator:** `scripts/validate_and_index.py` enforces English (strict language gate), required sections, schema, and deterministic `catalog.json` / `INDEX.md` generation.
- **Catalogs:** Root `catalog.json`, `INDEX.md`, and `mcp/catalog.json` paths/descriptions aligned to English domain slugs.
- **CI:** `validate-templates.yml` passes locally with regenerated artifacts.

## Hygiene

- Replaced example-only German domains (`firma.de`, etc.) with `example.com` where found.
- No API keys, private keys, or live tokens found in tracked content.

## Backlog (next)

1. **Hand rewrites for `scripts/quality_backlog.txt`:** Work through the 152 backlog templates in small batches; shrink the backlog as each template passes all quality gates without mechanical padding.
2. **Example richness:** Expand short expected-output blocks with domain-specific outcomes while rewriting backlog templates.
3. **Optional:** Add validator coverage for broken workflow placeholder lines (corrupted migration fragments) when found in future audits.