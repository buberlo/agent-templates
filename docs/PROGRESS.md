# Migration progress

## Completed (2026-11-28) — Batch 11

- **Eight new templates (thin domains):** KiCad BOM, ERC, and DRC pre-fab review with kicad-cli (`hardware-embedded/cad`); ESPHome device YAML review before flashing (`hardware-embedded/arduino-esp32`); NDA and terms-of-service change diff with lawyer boundary (`legal-admin/contracts`); rental application document checklist with fair-housing wording notes (`real-estate/property-search`); weekly sleep and workout review from wearable exports, explicitly not medical advice (`health-fitness/health-data-organization`); job description bias and clarity review citing EEOC and Gender Decoder (`hr-recruiting/job-postings`); flight disruption rebooking and EU passenger-rights checklist (`travel-events/flights-hotels`); personal subscription audit from statements and receipts (`personal-lifestyle/household`).
- **MCP catalog:** Added kicad-mcp (lamaalrajih) for `hardware-embedded/cad` (requires KiCad 9.0+, DRC through the KiCad CLI); reused Gmail MCP, google_workspace_mcp, homeassistant-mcp, strava MCP, MarkItDown, and the reference filesystem, fetch, and time servers.
- **Sources:** `research/SOURCES.md` gained 24 URLs (KiCad 9.0 docs, ESPHome CLI/YAML/security/API/OTA, pandoc, git diff, Python difflib/csv/xml.etree, Your Europe air passenger rights, Apple Health export, EEOC prohibited practices, DOJ Fair Housing Act, HUD FHEO, Gender Decoder, kicad-mcp, MCP reference servers); every new URL checked for HTTP 200.
- **Counts:** README templates 288 → 296, MCP entries 107 → 108; `mcp/README.md` 107 → 108; unique HTTP sources 187 → 211.
- **Validator:** `python3 scripts/validate_and_index.py` — 0 errors, no warnings for the new templates; regenerated `INDEX.md` and root `catalog.json`.
- **Template total:** **296** templates, **27** domains, **199** categories.

## Completed (2026-11-26) — Cleanup batch

- **English-only repair:** Restored official source URLs (verified with HTTP 200) and remapped 12 dead `mcp/catalog.json` category references. Rewrote 17 MT-garbled templates from pre-migration German sources. Translated residual German and Denglisch in templates, category/domain pages, frontmatter, checklists, and system prompts. System prompts now respond in the user's language (default English). Normalized leftover German slug mentions in prose (folders were already English). No website folder-slug redirects required (`buberlo/agent-templates-web` has no hardcoded German slugs).
- **Headings and quality backlog:** All templates now use the exact `## Definition of done` heading. Quality backlog **115 → 108** after rewritten templates passed existing quality gates.
- **Validator:** Hardened `scripts/validate_and_index.py` — German markers (including heading markers; no `\bdie\b`), German date/thousand-separator checks, repetition/token-loop detection, allowlist-free URL hygiene (known-bad typo patterns and suspicious TLDs), exact required headings, Expected-result extraction beyond `text`/`bash` fences, MCP category referential integrity, published count checks, and `--check` mode. `python3 scripts/validate_and_index.py` — 0 errors; regenerated `INDEX.md` and root `catalog.json`.
- **Repo hygiene:** Removed 27 leftover translation/migration scripts under `scripts/` (kept `validate_and_index.py` and `quality_backlog.txt`). Added `adapters/codex.md`. Corrected count drift: README templates **279 → 288**, MCP entries **105 → 107**; `mcp/README.md` **94 → 107**; `mcp/catalog.json` count **107**; `research/SOURCES.md` unique HTTP sources **187**, with English number/date formats.
- **Template total:** **288** templates, **27** domains, **199** categories.

## Completed (2026-11-26) — Batch 10

- **Hand rewrites (12 templates):** Browser automation MCP routing and Playwright workflow; cron and systemd scheduling; desktop GUI automation; MQTT and IoT; mobile MCP focus and device workflow; n8n/Make/Zapier integration design; RPA solution design; Home Assistant smart home; iMessage and SMS on macOS; meeting transcription MCP stack selection.
- **Sources:** `research/SOURCES.md` — added citations for Playwright docs, crontab/systemd timers, Home Assistant, Mosquitto, OpenRPA, UiPath, Make, Zapier, n8n API, ffmpeg, and Google Workspace CLI where referenced in templates.
- **MCP catalog:** No new servers; existing Playwright MCP, Mobile MCP, Mobilerun, homeassistant-mcp, fireflies MCP, and n8n entries reused with official URLs in template bodies.
- **Quality backlog:** **127 → 115** entries in `scripts/quality_backlog.txt` (12 removed after passing all quality gates).
- **Validator:** `python3 scripts/validate_and_index.py` — 0 errors; regenerated `INDEX.md` and root `catalog.json`.
- **Template total:** unchanged count at **288** (rewrites only, no new template files).

## Completed (2026-11-26) — Batch 9

- **Nine new templates (agent platforms and thin ops):** Cursor shell/MCP hook gates and subagent governance; Claude Code PreToolUse permission hooks; Codex nested `AGENTS.md` overrides; Hermes optional MCP sprint onboarding; OpenClaw ClawHub verify-and-install; Grok Bot scheduled X research brief (read-only); personal monthly budget variance review (`finance/budget`); parent-child agent handoff contract (`ai-ops/agent-orchestration`).
- **Assets:** Example data SVGs under `domains/agent-platforms/cursor/assets/` and `domains/agent-platforms/openclaw/assets/`.
- **MCP catalog:** Added Pattern entries for Cursor Agent hooks, Claude Code hooks, and Codex AGENTS.md discovery; tightened `OpenClaw MCP serve / ACP` risk notes and category mapping.
- **Sources:** `research/SOURCES.md` — https://cursor.com/docs/agent/hooks, https://code.claude.com/docs/en/hooks, https://learn.chatgpt.com/docs/agent-configuration/agents-md.
- **Validator:** `python3 scripts/validate_and_index.py` — 0 errors; regenerated `INDEX.md` and root `catalog.json`.
- **Template total:** **288** after regeneration.

## Completed (2026-11-25) — Batch 8

- **Eight new templates (thin domains):** Personal Gmail daily digest (`personal-lifestyle/household`); meeting transcript to Notion actions (`project-management/planning`); ElevenLabs voice FAQ with human escalation (`customer-service/live-chat-bots`); pantry weekly meal plan with USDA FDC API (`health-fitness/nutrition`); rubric assignment feedback drafter (`education/tutoring`); Jupyter reproducibility audit with papermill (`science-engineering/data-experiments`); landlord maintenance triage and quote compare (`real-estate/hoa-management`); n8n workflow builder and reviewer via instance MCP (`automation/n8n-make-zapier`).
- **Assets:** Example data (self-written) SVG diagrams under `domains/personal-lifestyle/household/assets/` and `domains/customer-service/live-chat-bots/assets/`.
- **MCP catalog:** Added Gmail MCP (Google Workspace remote), ElevenLabs ElevenAgents, n8n Instance MCP, papermill CLI, and USDA FoodData Central API; extended Notion MCP (hosted) to `project-management/planning`.
- **Sources:** New URLs in `research/SOURCES.md` (Google Gmail MCP, Notion workflow via mcp.notion.com already listed, ElevenLabs ElevenAgents and transfer_to_number, USDA FDC API, papermill, n8n instance MCP connect guide, Twilio ElevenLabs handoff blueprint, markitdown, nbconvert).
- **Validator:** `python3 scripts/validate_and_index.py` — 0 errors; regenerated `INDEX.md` and root `catalog.json`.
- **Template total:** **279** after regeneration.

## Completed (2026-11-25) — Batch 7

- **Hand rewrites (13 templates):** Full **ai-ops** backlog cluster (evals-benchmarks, fine-tuning, local-models-ollama, mcp-server-build, model-routing, prompt-engineering, skills-authoring) plus six **devops-cloud** templates (incident-response workflow and MCP focus, monitoring-observability MCP focus, platform-deploy, cloud-aws, kubernetes MCP focus) with English prose, numbered workflows, approval gates, and **Example data (self-written)** blocks citing official tool docs.
- **Sources:** Added Ollama, OpenAI fine-tuning, LiteLLM, Vercel AI Gateway, promtool, AWS CLI install, and MCP Python SDK URLs to `research/SOURCES.md` where cited in templates; Grok Bot Wiki cited only as an unofficial community guide where noted.
- **Quality backlog:** **140 → 127** entries in `scripts/quality_backlog.txt` (13 removed after passing all quality gates with no warnings).
- **Validator:** `python3 scripts/validate_and_index.py` — 0 errors; regenerated `INDEX.md` and root `catalog.json`.

## Completed (2026-11-25) — Batch 6

- **Eight new templates (MCP dev and ops):** Playwright MCP E2E authoring and flaky-test triage; Sentry MCP production error triage to fix PR plan (with example SVG flow); Stripe read-only refund and dispute investigation; Supabase MCP schema migration review with rollback plan; Figma remote MCP design-to-component implementation; Cloudflare MCP DNS and Workers change review; Grafana MCP alert investigation and incident timeline (with example SVG timeline); Linear hosted MCP backlog grooming and sprint prep.
- **Assets:** Example data (self-written) SVG diagrams under `domains/devops-cloud/incident-response/assets/` and `domains/devops-cloud/monitoring-observability/assets/`.
- **MCP catalog:** Added official entries for Supabase MCP Server, Grafana MCP (mcp-grafana), Cloudflare API MCP Server, Figma MCP server (remote), and Linear MCP (hosted) in `mcp/catalog.json`. New source URLs in `research/SOURCES.md` (Sentry CLI MCP, Supabase, Cloudflare, Grafana, Figma, Linear hosted endpoints).
- **Validator:** `python3 scripts/validate_and_index.py` — 0 errors; regenerated `INDEX.md` and root `catalog.json`.
- **Template total:** **271** after regeneration.

## Completed (2026-11-24) — Batch 5

- **Eight new templates (thin domains):** Game mod packaging and LOOT-style compatibility report; dedicated server admin via RCON/CLI with restart approval gates; wearable export training plan builder (Strava API, FIT/GPX, not-medical-advice); multi-city trip itinerary and booking checklist (no payments); event run-of-show and attendee comms drafters; course material to Anki TSV and quiz with source-grounded cards; weekly status report from GitHub / Linear / Jira (read-only); arXiv and Semantic Scholar literature search pipeline with required citations.
- **Sources and MCP:** Added CLI/API citations to `research/SOURCES.md` (LOOT, Vortex, MO2, mcrcon, rcon-cli, Strava API, fitparse, gpxpy, arXiv API, Semantic Scholar API, Anki import docs, Minecraft RCON wiki). Extended `GitHub Official MCP` category mapping to `project-management/reporting` in `mcp/catalog.json` (no new MCP servers; Nexus/LOOT and paper APIs use CLI/API).
- **Validator:** `python3 scripts/validate_and_index.py` — 0 errors; regenerated `INDEX.md` and root `catalog.json`.
- **Template total:** **263** after regeneration.

## Completed (2026-11-24) — Batch 4

- **Hand rewrites (12 templates):** Nine `agent-platforms` templates (Claude Code MCP focus and workflow, Codex, Cursor, generic MCP focus and workflow, Hermes, OpenClaw MCP focus and workflow) plus three `ai-ops` templates (agent orchestration, context-token management MCP focus and workflow) with platform-specific system prompts, numbered workflows, security gates, and **Example data (self-written)** blocks citing official docs.
- **GDPR source fix:** `gdpr-dsar-intake-response-v1.md` now cites EUR-Lex for the official GDPR text; gdpr.eu retained as a labeled secondary explainer.
- **Quality backlog:** **152 → 140** entries in `scripts/quality_backlog.txt` (12 removed after passing all quality gates with no warnings).
- **Catalogs:** Regenerated root `catalog.json` and `INDEX.md` via the validator.

## Completed (2026-11-24) — Batch 3

- **Eight new templates (thin domains):** Support ticket triage and reply drafting (Zendesk MCP, drafts only); Help Center KB gap analysis from resolved tickets; HR interview scheduling coordinator (Google Workspace MCP, human sends invites); new-hire onboarding checklist and provisioning tracker; contract review summary with lawyer boundary; GDPR DSAR intake and response workflow; property listing description with comps research (fair-housing-safe wording); firmware build / flash / serial debug loop (PlatformIO, ESP-IDF, optional platformio.mcp).
- **New category:** `hr-recruiting/interview-scheduling` with `_category.md`.
- **MCP catalog:** English cleanup for remaining German labels in `mcp/catalog.json`; added zendesk-mcp-server (reminia), google_workspace_mcp, and platformio.mcp entries with official URLs (94 servers total).
- **Validator:** `scripts/validate_and_index.py` applies the German language gate to string fields in `mcp/catalog.json`.
- **Template total:** **255** after regeneration (`INDEX.md`, root `catalog.json`).

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

- Fixed invalid YAML frontmatter in four templates (strict `yaml.safe_load` / js-yaml compatible quoting).
- Validator now parses all `domains/` and `adapters/` frontmatter with PyYAML `safe_load` (mapping required); CI installs `pyyaml`.
- Replaced example-only German domains (`firma.de`, etc.) with `example.com` where found.
- No API keys, private keys, or live tokens found in tracked content.

## Backlog (next)

1. **Hand rewrites for `scripts/quality_backlog.txt`:** Work through the 152 backlog templates in small batches; shrink the backlog as each template passes all quality gates without mechanical padding.
2. **Example richness:** Expand short expected-output blocks with domain-specific outcomes while rewriting backlog templates.
3. **Optional:** Add validator coverage for broken workflow placeholder lines (corrupted migration fragments) when found in future audits.