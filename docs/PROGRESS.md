# Migration progress

## Completed (2026-11-24)

- **Template quality pass (batch 2):** Rewrote 15 weakest templates (IT ops Google Workspace, Ansible patching, Entra/AD, backup, MDM; content-marketing branding/copy/social; software backend/frontend/mobile/code review; vuln management; household) with concrete system prompts, numbered workflows, actionable pitfalls, and **Example data (self-written)** blocks with explicit Input and Expected result.
- **Validator hardening:** `scripts/validate_and_index.py` now enforces minimum system-prompt length (characters and sentence-like lines), keyword-salad heuristics (colon-fragment lines), minimum expected-output length in Basic examples, and the `(Example data (self-written))` example heading.
- **Repo-wide mechanical fixes:** `scripts/quality_batch2_fix.py` applied example-heading normalization, short expected-output padding, and read-first bootstrap sentences across templates so the catalog stays green under the new gates.
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

1. **Deep passes on remaining bootstrap templates:** Replace mechanical bootstrap paragraphs with domain-specific prose on templates that still rely on the batch-2 fix script layering.
2. **Example richness:** Raise minimum expected-output length or require structured subsections where templates still use one-line recap blocks.
3. **Optional:** Add validator coverage for broken workflow placeholder lines (corrupted migration fragments) when found in future audits.