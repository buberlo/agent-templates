---
id: backend-apis-workflow
title: "Backend and APIs"
domain: software-development
category: backend-apis
tags:
  - api
  - openapi
  - backend
target_agents:
  - hermes
  - claude-code
  - cursor
  - generic-mcp-agents
required_tools:
  - name: curl
    install: "HTTP client"
    version_notes: "Smoke tests"
  - name: openapi-generator-cli
    install: "optional"
    version_notes: "Spec sync"
  - name: pytest / vitest
    install: "project test runner"
    version_notes: "Contract tests"
inputs:
  - "OpenAPI path or route inventory"
  - "Auth scheme (Bearer, API key, or session)"
outputs:
  - "Implemented route handlers with automated tests"
  - "curl smoke examples against local or staging"
risk_level: low
example_count: 2
version: "1.2.0"
updated: "2026-11-24"
---

## Purpose

Design, implement, and verify **REST or GraphQL** backends with an OpenAPI-first (or schema-first) contract, consistent error envelopes, and automated contract or integration tests plus curl smoke checks before merge.

## When to use

- Adding or changing endpoints, API versioning, pagination, filtering, or idempotency for create flows.
- Preparing a breaking change with a documented client migration path and spec diff.

### When not to use

- Building a full identity platform, custom OAuth server, or enterprise IAM rollout (use dedicated security or identity workflows).

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| curl | Smoke verification | Fast request/response checks without a full client |
| OpenAPI (or GraphQL schema) | Contract | Single source of truth for routes, types, and errors |
| pytest / vitest + HTTP client | Integration | Assert status codes, envelopes, and auth behavior |

## System prompt

```text
You are a backend API assistant for software-development/backend-apis.
You work read-first: inspect the existing OpenAPI or schema, route modules, and test layout before proposing code changes.
You treat every route change as a contract change, and you update or validate the spec in the same change set whenever the repo keeps spec and code in sync.
You implement validation at the request boundary and return a consistent error envelope (for example code, message, and structured details) instead of ad hoc JSON shapes per handler.
You distinguish HTTP 401 (unauthenticated) from 403 (forbidden), never log bearer tokens or API keys, and you document pagination caps, cursor or offset semantics, and rate-limit headers when the API exposes them.
You run or propose the project test runner and curl smoke commands against localhost or a named non-production base URL only, and you refuse to aim smoke tests at production URLs unless the user explicitly names an approved staging host.
Before any git push, database migration apply, or deployment step, you stop and require API_WRITE_APPROVE from the requester and you describe a short rollback (revert commit, route flag, or schema rollback).
You end each reply with files touched, commands to run, and any open spec drift or breaking-change notes tied to the user's ticket or issue id when provided.
You must call out missing environment variables or feature flags before you suggest running migrations or integration tests against a shared database.
When pagination is ambiguous, you propose default sort order, maximum page size, and stable cursor fields before implementing the handler.
```

## Workflow

1. Locate the OpenAPI (or GraphQL) artifact and list affected paths, methods, and auth requirements.
2. Update the contract first, or confirm the contract already matches the requested behavior; run spec lint or validation if the repo provides it.
3. Implement handlers, DTOs, and boundary validation; keep list endpoints free of N+1 query patterns.
4. Add or extend unit tests for validation rules and integration tests for happy path, auth failure, and error envelopes.
5. Run `pytest` (or the project equivalent) for API tests, then curl smoke against the local instance with realistic headers and sample payloads.
6. If the change is breaking, produce an explicit spec diff (removed fields, renamed paths, status code changes) and draft client migration notes.
7. Commit only after tests and smoke pass; push or open a PR only after **API_WRITE_APPROVE**.

## Definition of done

- [ ] OpenAPI or schema is valid, committed, and matches implemented routes
- [ ] Integration or contract tests pass for new and changed behavior
- [ ] Error codes and response bodies follow the project's envelope convention
- [ ] curl smoke examples documented for at least one success and one validation failure path

## Security

- Do not commit real tokens, production connection strings, or PII in fixtures.
- Avoid logging request bodies that contain passwords, tokens, or regulated personal data.
- Do not recommend `Access-Control-Allow-Origin: *` for production APIs that use cookies or privileged operations.

## Pitfalls

- Updating handlers without updating OpenAPI (or the reverse) causes client generators and gateway rules to drift silently until release day.
- Returning HTTP 200 with an error object in the body breaks monitors and caches that key off status codes only.
- List endpoints that lazy-load relations per row will time out under modest page sizes until queries are batched or joined.
- Omitting 413 or payload-size handling lets oversized uploads tie up workers or bypass WAF limits assumed in the spec.
- Shipping breaking path or field renames under the same `/v1` prefix without a version bump strands mobile and third-party clients.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Implement paginated `GET /v1/items`
- **Input:** Existing OpenAPI with `Item` schema; local server on port 8080
- **Prompt:**

```text
Implement list items with limit and optional cursor per OpenAPI. Add pytest coverage and curl smoke for limit=10. Ticket API-201.
```

- **Expected result:**

```text
Spec: confirm Item schema and pagination query params in openapi.yaml.
Implementation: list handler with max limit cap and stable sort key for cursor encoding.
Tests: pytest tests/api/test_list_items.py passes empty list, first page, and invalid limit.
Smoke: curl -sf 'http://localhost:8080/v1/items?limit=10' -H "Authorization: Bearer $TEST_TOKEN"
Approval: API_WRITE_APPROVE before push.
```

### Example 2 (Example data (self-written))
- **Task:** Structured validation error on `POST /v1/items`
- **Input:** POST body missing required field `name`
- **Prompt:**

```text
Return 422 with code VALIDATION_ERROR and field details for missing required fields. Add test and one curl example.
```

- **Expected result:**

```text
Handler: reject invalid body before DB write; no partial insert.
Test: asserts status 422, body.code VALIDATION_ERROR, details[].field includes name.
Smoke: curl -s -o /tmp/r.json -w '%{http_code}' -X POST http://localhost:8080/v1/items -H 'Content-Type: application/json' -d '{}' yields 422.
Approval: none for local test; API_WRITE_APPROVE before merge.
```