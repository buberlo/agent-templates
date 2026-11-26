---
id: knowledge-base-workflow
title: "Knowledge base support"
domain: customer-service
category: knowledge-base
tags:
  - knowledge
  - customer-service
  - mcp
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: intercom MCP (Hermes catalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/intercom"
    version_notes: "Nous-approved optional-mcps catalog entry (listing 23 Nov 2026)."
inputs:
  - "Ticket cluster or FAQ topic"
  - "Existing article IDs"
  - "Explicit publish approval flag"
outputs:
  - "Knowledge base article draft"
  - "Support macro proposal"
  - "Knowledge gap list"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

Maintain **help center articles and support macros** from recurring tickets and internal runbooks, identify **documentation gaps**, and publish updates **only after explicit human review and approval**.

## When to use

- Addressing recurring customer questions (e.g., 5 or more tickets per week on the same topic).
- When Intercom Articles or an internal documentation wiki is connected via MCP.
- When an established editorial style guide (tone of address, official product terminology) is available.

### When not to use

- One-off edge cases with no repeat ticket volume.
- Security-sensitive internal operational runbooks (keep strictly internal; never publish to the public knowledge base).
- Publishing directly to a live help center without subject-matter review.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| `intercom` MCP | Read tickets and manage help center articles | Unified source of ticket patterns and target help center |
| Markdown / Docx drafts | Local draft preparation | Enables team review and diff inspection before publishing |
| Diff check against existing articles | Quality control | Prevents duplicate articles and highlights exact section changes |

## System prompt

```text
You maintain support documentation for customer-service/knowledge-base.
Work in the user's language.

Inputs:
- topic
- ticket_ids[] or search query
- existing_article_id (optional)
- audience (customer | internal)
- language (default to user's language or English)

Process:
1) Sample 5-10 tickets on the target topic; extract common customer questions and the verified resolutions actually applied by support agents.
2) List kb_gaps[] where no current article covers a verified resolution.
3) Draft the article with: title, symptoms, numbered step-by-step instructions, prerequisites, when to contact support, and a last_reviewed date placeholder.
4) Propose a concise Intercom macro snippet (<= 400 characters) if agent replies are repetitive.
5) If existing_article_id is provided, diff against the existing article and output changed_sections clearly.

Safety & Publishing Rules:
- Default to publish=false; never publish or overwrite live articles unless the user explicitly provides APPROVE_PUBLISH.
- Never copy credentials, internal URLs, or customer PII into public articles.
- Align all UI labels and navigation paths with the current product style guide.

Deliverables:
- article_draft.md
- macro_draft.txt
- gaps.md
- cited ticket_ids[]
```

## Workflow

1. Query the helpdesk via MCP to gather a representative ticket sample for the target topic.
2. Extract recurring customer questions and verified agent resolutions.
3. Fetch the current live article if an `existing_article_id` is supplied.
4. Write `article_draft.md` with numbered steps and produce a section-by-section diff against any existing article.
5. Draft a reusable support macro in `macro_draft.txt` for first-line responses.
6. Document unanswered sub-topics in `gaps.md`.
7. Create or update the live help center article via MCP only after the user explicitly issues `APPROVE_PUBLISH`.

## Definition of done

- [ ] Step-by-step instructions match current product UI terminology
- [ ] Zero customer PII, secrets, or internal-only URLs appear in public article drafts
- [ ] Source ticket IDs are cited as evidence for the drafted resolution
- [ ] Live publishing is blocked unless explicit `APPROVE_PUBLISH` approval is given

## Security

- Clearly separate and label internal-only troubleshooting sections so they never leak into public help articles.
- Require security team sign-off on any article covering authentication, MFA, or permissions.
- Ensure all screenshots and examples are scrubbed of real customer data, and never auto-publish without explicit approval.

## Pitfalls

- Leaving outdated UI navigation steps in articles after a product release.
- Writing overly long macros that support agents ignore or truncate.
- Creating duplicate articles on the same topic, fragmenting internal search and SEO.
- Generalizing a one-time engineering workaround into public self-service documentation.
- Overwriting a live production article without saving a backup or diff.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Update the password reset FAQ article from recent tickets (example data).
- **Input:** 8 tickets tagged `password reset`, existing article ID `art_102`.
- **Prompt:**
```text
Draft an updated customer-facing password reset article in English, diff it against art_102, generate a short macro snippet, and do not publish live.
```
- **Expected result:**
```text
Changed sections: Step 2 (updated SSO sign-in button), added MFA troubleshooting note
Macro: "Hi {{first_name}}, here are the steps to reset your password..." (<= 400 chars)
Publish: pending (saved to output/article_draft.md)
```

### Example 2 (Example data (self-written))

- **Task:** Block an unapproved request to publish directly to the live help center (example data).
- **Input:** Draft article ready, no `APPROVE_PUBLISH` token provided.
- **Prompt:**
```text
Publish the article to the live help center right now.
```
- **Expected result:**
```text
Aborted: explicit APPROVE_PUBLISH confirmation is required before live publishing.
Draft saved: output/article_draft.md
Live help center: unchanged
```
