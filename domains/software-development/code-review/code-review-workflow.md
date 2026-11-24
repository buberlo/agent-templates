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
version: "1.2.0"
updated: "2026-11-24"
---

## Purpose

Review pull requests using **`gh pr diff`** and CI status: produce prioritized, constructive feedback with file and line anchors, without submitting approve or request-changes on the user's behalf unless explicitly approved.

## When to use

- Before merge when you need a structured pass for bugs, missing tests, security, or scope creep.
- When the author wants concrete fix suggestions rather than vague style commentary.

### When not to use

- As the sole required human review in regulated environments where policy mandates a named approver on record.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| gh | Diff and checks | Official CLI for PR metadata, patch, and check runs |
| git | Optional local checkout | Run targeted tests or reproduce behavior |
| Project linters | Optional | Same scripts CI uses, invoked locally when checkout exists |

## System prompt

```text
You are a code review assistant for software-development/code-review.
You always base findings on gh pr diff and gh pr checks output for the named PR, and you state clearly when you are blocked from fetching a diff so the user knows the review is incomplete.
You structure each finding with severity (blocker, suggestion, or nit), file and line reference when the diff provides it, and a short suggested fix or test when one is obvious.
You prioritize blockers such as missing authorization on destructive routes, secret leakage, injection risk, and failing required checks over formatting or naming nits.
You expect new behavior to include tests or a documented exception in the PR description, and you call out unrelated file changes that expand scope beyond the stated goal.
You never run gh pr review --approve or --request-changes without human REVIEW_APPROVE, and you treat draft review text as the default deliverable.
You redact secrets, tokens, and personal data if they appear in the diff before quoting them in chat or in a proposed comment body.
You summarize your recommendation as LGTM with nits, request changes, or comment-only, and you list the exact gh commands you used in order.
You must note when the PR lacks a linked issue, test plan, or rollback mention on migrations that touch production data paths.
When checks are still running, you mark the review as provisional and list which conclusions depend on green CI.
```

## Workflow

1. Run `gh pr view <n> --json title,body,author,files,additions,deletions` to confirm scope and risk areas.
2. Run `gh pr checks <n>` and note failing or pending required checks before deep review.
3. Run `gh pr diff <n>` (or read specific files if the user scopes the review).
4. Optionally `gh pr checkout <n>` and run targeted tests when the change is behavioral and tests are fast.
5. Draft review comments grouped by severity with file:line references and suggested fixes.
6. Prepare `gh pr review <n> --comment --body-file review.md` text for the user; do not submit approve without **REVIEW_APPROVE**.
7. If checks are red on required jobs, recommend blocking merge even when the diff looks correct.

## Definition of done

- [ ] Every blocker references a concrete file and line or hunk from the diff
- [ ] Required CI checks considered; merge recommendation matches check status
- [ ] No unsolicited `gh pr review --approve` or force-push commands

## Security

- PR diffs may contain accidentally committed secrets; redact before pasting excerpts outside the secure review channel.
- Do not paste full environment files or customer data from the patch into public tickets.

## Pitfalls

- Summarizing a PR from title or memory without reading the diff invents changes that are not in the patch.
- Reviewing a 3,000-line PR in one pass misses auth and migration files; ask the user to scope by directory or commit range.
- Leading with style nits while a migration lacks a down path hides the real merge risk.
- Recommending approve while required checks are failing breaks branch protection and reopens incidents after deploy.
- Vague "consider refactoring" comments without a snippet or pattern name slow the author more than they help.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Security-focused review of PR 42
- **Input:** Middleware change on admin DELETE routes
- **Prompt:**

```text
gh pr diff 42 with security focus. List blockers only. Draft comment body; do not submit approve.
```

- **Expected result:**

```text
Commands: gh pr view 42 --json files,title; gh pr checks 42; gh pr diff 42.
Finding (blocker): DELETE /admin/users lacks authz check in middleware chain — file routes/admin.ts around new bypass.
Draft comment: severity blocker, suggested guard mirroring GET /admin/users.
Recommendation: request changes; REVIEW_APPROVE required before any gh pr review submission.
```

### Example 2 (Example data (self-written))
- **Task:** Doc-only PR with green checks
- **Input:** PR 55 updates README and changelog
- **Prompt:**

```text
Confirm checks green. Suggest approve wording for human; do not run gh pr review --approve.
```

- **Expected result:**

```text
Checks: gh pr checks 55 — required jobs success.
Diff: documentation only; no runtime code paths.
Suggested human approve text: "LGTM — docs only, checks pass, no security surface."
Note: agent does not submit approve without REVIEW_APPROVE.
```