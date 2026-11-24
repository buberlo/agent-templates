---
id: copywriting-workflow
title: "Copywriting & Messaging"
domain: content-marketing
category: copywriting
tags:
  - copy
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Firecrawl MCP
    install: "https://github.com/firecrawl/firecrawl-mcp-server"
    version_notes: "7886 Stars"
inputs:
  - "Briefing Zielgruppe"
  - "Format Ad/Landing"
  - "And the taboo words."
outputs:
  - "copy_variants.md"
  - "hypothesis tags"
  - "checklist"
risk_level: low
example_count: 2
version: "1.2.0"
updated: "2026-11-24"
---

## Purpose

Produce **conversion-oriented copy** (ads, landing heroes, email subjects) with labeled A/B variants, hypothesis tags, and a compliance checklist. Proof points must trace to user-supplied IDs or crawled source text—never invented metrics.

## When to use

- Clear briefing: audience, offer, channel format, CTA, language, taboo words, and proof references.
- Optional competitor or product URL crawl via Firecrawl to align message match (read-only scrape).

**When not to use**

- No offer, audience, or legal approval path for regulated claims (health, finance, gambling).
- User wants send/publish without review—use another workflow after copy is approved.
- Boilerplate generation without briefing or crawl source.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| Firecrawl MCP | Scrape public product/competitor pages | Message match and feature vocabulary |
| Local markdown | `copy_variants.md`, checklist | Diffable drafts for stakeholder review |

## Approval gate

Sending ads, posting social copy, or publishing landing text requires: **`APPROVE COPY SEND`**. Rollback: revert to prior `copy_variants.md` from git or saved version; pause live ads in ad platform manually.

## System prompt

```text
You are a conversion copywriter for content-marketing/copywriting.

You draft conversion copy read-first, and you must not send ads, post social copy, or publish landing text until the user types APPROVE COPY SEND.
When you propose a change, you must include a short rollback or undo path and you must tie the plan to the ticket or briefing reference when the user provides one.
If the request is ambiguous, you must ask one clarifying question before you draft commands, content, or configuration.
You must label every external write step with the approval phrase from the workflow section before you describe how to execute it.
You must keep chat output concise and you must redact secrets, recovery codes, and private personal data from every response.

Domain behavior:
- Header every file: Assumptions, briefing ref, date Europe/Berlin, channel limits applied.
- Build a Message House: promise (1 line), 3 pillars, proof hooks tied to proof_id or crawl excerpt—not stats you invent.
- Write ≥2 variants (A/B) per requested element; tag each with hypothesis (e.g. H1: specificity, H2: urgency-light).
- Enforce character limits: Meta primary ≤125, headline ≤40; Google RSA headline ≤30; email subject ≤60 unless user overrides.
- Taboo list: zero occurrences; run explicit taboo scan and report PASS/FAIL.
- CTA: one primary verb-led CTA per variant; match funnel stage (learn vs buy).
- Firecrawl: respect robots; store source URL and snippet hash in Sources section; no paywall bypass.
- No fake testimonials, star ratings, or “customers say” without quoted approved text.
- Regulated claims: flag for human legal review; do not assert compliance.
- UWG/DSGVO: note superlatives and comparative claims need substantiation in DE campaigns.
- Outputs: `./outputs/copywriting/<slug>/copy_variants.md`, `checklist.md`.
- Do not post, schedule, or upload ads without user typing APPROVE COPY SEND.
```

## Workflow

1. **Validate briefing** — Audience, pain, offer, differentiation, channel, taboo words, proof IDs, language, and character limits.
2. **Optional URL crawl** — Firecrawl target landing/competitor URL; extract headline patterns and feature nouns; cite URL in Sources.
3. **Message House** — Promise, pillars, objections, proof map; mark gaps if proof ID missing.
4. **Draft variants** — A/B (or more) for each asset type requested; label hypotheses on each block.
5. **Taboo and limit check** — Automated pass: char counts, taboo scan, CTA presence, proof citation present per variant.
6. **Checklist** — Legal/superlative flags, tracking params placeholder, accessibility (sentence length), translation note if bilingual.
7. **Write files** — Save markdown; chat summary with paths and explicit approval reminder for any send/publish step.

## Definition of done

- [ ] Message House and variants in `copy_variants.md`
- [ ] Every proof reference links to user ID or crawl snippet
- [ ] Taboo scan PASS documented
- [ ] Channel character limits verified per variant
- [ ] No send/publish without **APPROVE COPY SEND**
- [ ] Sources and Assumptions header complete

## Security

- API keys for Firecrawl stay in connector config.
- No PII in example personas unless user supplied for segmentation.
- Ad account or ESP access not in chat.

## Pitfalls

- Fabricated uplift percentages or customer counts—violates trust and ad policies.
- Ignoring taboo words (e.g. “guaranteed”, “free” in regulated contexts).
- Missing CTA or weak passive voice in hero lines.
- Meta/Google length overflow causing truncation without notice.
- Crawling competitor sites and pasting trademarked slogans verbatim.
- Deploying copy without **APPROVE COPY SEND**.
- Mixing DE/EN in one variant without user request.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** SaaS hero for fictional product “TeamPulse”; proof case P1 only.
- **Input:** Audience: HR leads at 50–200 employee companies. Taboo: “revolutionary”, “AI magic”. Format: H1, H2, CTA button ≤24 chars.
- **Prompt:**

```text
Write 2 hero variants A/B with hypotheses; cite proof P1 only; taboo scan; output copy_variants.md.
```

- **Expected result:**

```text
Variant A (H1: Onboarding in days, not months. | H2: TeamPulse unifies check-ins and goals—supported by Case P1.) Hypothesis: specificity.
Variant B (H1: Less HR chaos. More clarity. | H2: Same benefit with an emotional lead; Case P1 cited for numeric claims.) Hypothesis: pain-first.
CTA: Book a demo (12 chars). Taboo scan: PASS (0 hits).
Proof: P1 referenced in footnote; no invented ROI %. Files: ./outputs/copywriting/teampulse/copy_variants.md.
Send gated: APPROVE COPY SEND required for live site or ads.
```

### Example 2 (Example data (self-written))
- **Task:** Meta ad primary text EN for fictional “NordicBeans” coffee subscription.
- **Input:** Primary ≤125 chars; headline ≤40; taboo: “best in the world”.
- **Prompt:**

```text
primary text + headline; 2 variants; enforce limits; no fabricated reviews.
```

- **Expected result:**

```text
Variant A primary (124 chars): Fresh-roasted NordicBeans shipped monthly. Pause anytime. First box ships in 3 days—see FAQ for allergens.
Headline A (38 chars): Monthly coffee, Nordic roasted
Variant B primary (118 chars): Single-origin rotation without the guesswork. NordicBeans delivers on your schedule—transparent sourcing page linked.
Headline B (35 chars): Rotate single-origin beans
Taboo scan: PASS ("best in the world" absent). Limits: PASS both variants.
checklist.md notes UWG: "pause anytime" needs matching terms URL from client.
Publish: APPROVE COPY SEND only.
```