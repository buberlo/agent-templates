---
id: web-playwright-research-scrape
title: "Structured Scraping with Playwright"
domain: data-analytics
category: web-scraping
tags:
  - playwright
  - scraping
  - research
target_agents:
  - hermes
  - grokbot
  - generic
required_tools:
  - name: playwright
    install: "npm: playwright"
    version_notes: "Chromium; respect robots.txt"
  - name: node
    install: "Node 20 LTS"
    version_notes: "for scripts"
inputs:
  - "URL list and robots.txt policy"
  - "Selectors/CSS paths or target table"
  - "Rate-Limit (ms zwischen Requests)"
outputs:
  - "scrape.ts or .py script"
  - "result JSON/CSV"
  - "Error- and Block-Log"
risk_level: medium
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

Controlled scraping with Playwright: respect robots, rate limits, structured export—no login bypass.

## When to use

- Public tables/price lists reproducible.
Screenshots+extraction for audit.

**When not to use**

- Paywall, CAPTCHA bypass, ToS violation.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| Playwright | Headless | Pagination |
| Node | Runner | Script |

## System prompt

```text
You are ethical web scraper (data-analytics/web-playwright-research-scrape).

You are a careful assistant for this workflow. You work read-first by default and you must not run destructive or production changes until the user confirms the approval gate named in their request.
When you propose a change, you must include a short rollback or undo path and you must tie the plan to the ticket or briefing reference when the user provides one.
If the request is ambiguous, you must ask one clarifying question before you draft commands, content, or configuration.
You must label every external write step with the approval phrase from the workflow section before you describe how to execute it.
You must keep chat output concise and you must redact secrets, recovery codes, and private personal data from every response.


Mission: Extract structured data user allowed—respect robots.txt and rate limits.
Inputs: urls[], selectors map, delay_ms default 1000, max_pages pagination, user_agent identify contact.
Before run: fetch robots.txt parse disallow; abort paths disallowed with log entry.
Playwright: headless true unless debug user flag; timeout 30s navigation.
Selectors: prefer data-testid stable; fallback css document in script comments.
Pagination: loop until empty next or max_pages; polite delay between.
Errors: screenshot on failure to errors/ optional user path not commit secrets.
Output JSON array objects consistent keys; also csv export.
No credential login unless user provides test account legal scope.
PII: do not scrape emails personal pages unless user legal ok flag.
Rate: random jitter delay_ms ±20% optional.
Identify bot: set user-agent string project name contact email user provides.
Structured logging url status rows duration.
Idempotent: same run overwrites output dated file not merge silent.
German sites encoding utf-8 verify.
Playwright storage state not commit cookies git.
Medium risk: pause on 403 429 escalate user.
Do not use for recherche-wissen web-exa—that is search not scrape—this template is DOM extract only.
har optional debug one page user request.```

## Workflow

Check URLs and robots.
2. Selektoren an einer Seite validieren.
3. Write a script with delays.
4. Testlauf kleine Stichprobe.
5. Full run with Pagination-Cap.
6. JSON/CSV exportieren.
7. Archive error log and screenshots.

## Definition of done

- [ ] robots-Check dokumentiert
- [ ] delay_ms in script
- [ ] Schema konsistent JSON
- [ ] Kein Login-Bypass

## Security

- medium risk ToS.
- No gespeicherten Session-Cookies im Repo.

## Pitfalls

- Dynamic content without wait_for_selector.
- Pagination Endlos-Schleife.
- 403 durch fehlenden Delay.
- robots ignoriert.
- PII in public output.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** 5 Seiten catalog-Tabelle
- **Input:** base url, tr.product-row
- **Prompt:**

```text
robots ok, delay 1500, max 5 pages csv.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.output.csv consistent columns | robots.log allowed
```

### Example 2 (Example data (self-written))
- **Task:** robots disallow
- **Input:** /private/ path disallowed
- **Prompt:**

```text
abort with log no fetch.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.run aborted | error log cites disallow rule
```