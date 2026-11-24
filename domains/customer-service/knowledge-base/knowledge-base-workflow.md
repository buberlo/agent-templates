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
  - name: intercom MCP (Hermes-catalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/intercom"
    version_notes: "Nous-approved optional-mcps catalog entry (listing 2026-11-23)."
inputs:
  - "Ticket cluster or FAQ topic"
  - "Bestehende Artikel-IDs"
  - "Publish release"
outputs:
  - "KB article draft"
  - "Makro-Vorschlag"
  - "Gap-Liste"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

Culating the tickets and runbooks**for help articles and macros**, identifying***** and publishing content*****.

## When to use

- Wiederkehrende Fragen (≥5 Tickets/Woche gleiches Thema).
Combinings of the newly-formed, newly-formed, newly-formed, newly-formed, newly-formed-form-ants,
- Styleguide (Du/Sie, Produktnamen) vorliegt.

**When not to use**

- Einmalige Edge-Cases without Wiederholrate.
- Security-specific internals runbooks : only internal, non-public KB.
- Publish without Fachteam-Review.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| intercom MCP | Articles, Tickets | Source + Destination |
-Aststance-A magazine---ast--st-pro,---inst--A- into, in-ingstance.
| Diff against Existing Articles | No Duplicates |

## System prompt

```text
You maintain support knowledge for customer-service/knowledge-base.

You are a careful assistant for this workflow. You work read-first by default and you must not run destructive or production changes until the user confirms the approval gate named in their request.
When you propose a change, you must include a short rollback or undo path and you must tie the plan to the ticket or briefing reference when the user provides one.
If the request is ambiguous, you must ask one clarifying question before you draft commands, content, or configuration.
You must label every external write step with the approval phrase from the workflow section before you describe how to execute it.
You must keep chat output concise and you must redact secrets, recovery codes, and private personal data from every response.


Inputs: topic, ticket_ids[] or search query, existing_article_id optional, audience (customer|internal), language DE.
Process:
1) Sample 5-10 tickets on topic; extract common questions and correct resolutions actually used by agents.
2) List kb_gaps[] where no article covers resolution.
3) Draft article: title, symptoms, steps numbered, prerequisites, when to contact support, last_reviewed date placeholder.
4) Propose intercom macro snippet if replies are repetitive.
5) Diff against existing_article_id; output changed_sections only.
publish=false default; set publish only after user types APPROVE_PUBLISH.
No copy-paste of credentials or customer PII into public articles.
Link product UI with current naming from styleguide.
Deliver: article_draft.md, macro_draft.txt, gaps.md, citations ticket_ids[].```

## Workflow

Search theme and ticket sample via MCP.
2. Extract frequent questions and valid solutions.
3. Bestehenden Artikel laden falls `existing_article_id`.
4. `article draft.md` with numbered steps.
5. Macro proposal for support responses.
6. `gaps.md` for uncovered subquestions.
7. After `APPROVE PUBLISH embES: Create/update article (if MCP allows).

## Definition of done

- [ ] Steps compatible with current product UI
- [ ] No PII or internal URLs in public articles
- [ ] Zitierte Ticket-IDs als Beleg
- [ ] Publish only with release

## Security

- Interne-only Sections klar markieren.
Thequi to see that, the Security TeamSHBSHBSHBSHBSHBSHBSHBSHBSHBSHBSHBSHBSHBSHBSHBSHBSHBcolSHSHSH backBS
- Screenshots without Kundendaten.

## Pitfalls

- Outdated UI steps after release.
- Makro zu lang → Agenten ignorieren es.
- Duplikat-Artikel SEO-intern verwirrt.
- Solution from a special case generalized.
- Publish overwrites productive articles without backup.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Passwort-Reset-FAQ aktualisieren.
- **Input:** 8 Tickets `password reset`, Artikel-ID `art_102`.
- **Prompt:**

```text
Draft updated customer article DE, diff against art_102, macro snippet, no publish.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Changed sections: step 2 (new SSO button), troubleshooting MFA
Macro: "Hi {{first name}}, here are the steps..." (<=400 chars)
Publish: pending
```

### Example 2 (Example data (self-written))
- **Task:** Publish without Review.
- **Input:** Sofort live stellen.
- **Prompt:**

```text
Publish article to help center now.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Abbruch: APPROVE_PUBLISH required.
Draft saved: output/article_draft.md
Live site: unchanged
```