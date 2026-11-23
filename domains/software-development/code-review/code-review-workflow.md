---
id: code-review-workflow
title: "Code-Review"
domain: software-development
category: code-review
tags:
  - review
  - gh
  - quality
target_agents:
  - hermes
  - claude-code
  - cursor
  - generic-mcp-agents
required_tools:
  - name: gh
    install: "gh pr diff, review"
    version_notes: "Required"
  - name: git
    install: "local checkout optional"
    version_notes: "deeper review"
inputs:
  - "PR number or branch"
  - "Review focus (security, perf)"
outputs:
  - "Structured review comments"
  - "Approve/block recommendation"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Purpose

Pull requests with **gh pr diff** and checklist review — constructive, prioritized, without silent merge.

## When to use

- Vor Merge: Bugs, Security, Tests fehlen.
- Author braucht konkretes Feedback.

**When not:** Does not replace human duty review in regulated teams.

## Tool stack

| Tool | Role | Justification |
|------|-------|------------|
| gh | Diff, checks | `gh pr diff` |
| git | Optional lokal | run tests |
| linters | optional | project scripts |

## System prompt

```text
Code review workflow (software-development/code-review).

Fetch: gh pr view <n> --json title,body,author,files,additions,deletions.
Diff: gh pr diff <n>; focus files user lists or high risk paths (auth, migrations).
Checks: gh pr checks <n>; block merge recommendation if required check missing.
Comment structure: severity (blocker/suggestion/nit), file:line, suggested fix snippet.
Security: secrets, injection, authz gaps, unsafe deserialization.
No approve via gh pr review --approve without human REVIEW_APPROVE.
Never request changes without at least one concrete finding or LGTM rationale.
Test expectation: new behavior has test or documented exception.
Scope creep: call out unrelated changes.
Link official docs for API misuse suggestions.
Summarize decision: LGTM with nits, Request changes, or Comment only.
Do not run destructive git commands on reviewer's machine without ask.
```

## Workflow

1. `gh pr view 42 --json files,title`.
2. `gh pr checks 42`.
3. `gh pr diff 42 --patch` or pro Datei.
4. Optional `gh pr checkout 42 && npm test`.
5. Review-Kommentare strukturieren.
6. Draft `gh pr review 42 --comment --body-file review.md`.
7. Submit nur nach User OK.

## Definition of done

- [ ] Any blocker with file/line
[ ] Checks taken into account
- [ ] Kein ungefragtes Approve

## Security

- Diff kann Secrets enthalten — redigieren vor externem Teilen.

## Pitfalls

- Nur Summary without Diff — Halluzination.
- Riesige PRs ungesliced — nach Module fragen.
- Style-Nits dominieren Blocker.
- Approve trotz roter CI.
- Feedback without Vorschlag — weniger hilfreich.

## Basic examples

### Example 1 (Example data)

- **Task:** Review PR 42 security focus.
- **Input:** auth middleware changed.
- **Prompt:**

```text
gh pr diff 42; list blockers; draft comment only.
```

- **Expected result:**

```bash
gh pr diff 42
gh pr checks 42
# Review draft: BLOCKER missing authz on DELETE /admin
```

### Example 2 (Example data)

- **Task:** LGTM with tests ok.
- **Input:** small doc fix.
- **Prompt:**

```text
Confirm checks green; suggest approve text; do not submit approve.
```

- **Expected result:**

```bash
gh pr checks 55
# Suggested body: LGTM — checks pass, scope doc-only
```