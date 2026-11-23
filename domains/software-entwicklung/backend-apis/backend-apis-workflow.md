---
id: backend-apis-workflow
title: "Backend und APIs"
domain: software-entwicklung
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
  - "OpenAPI path oder Route-Liste"
  - "Auth schema (Bearer/API key)"
outputs:
  - "Implementierte Route + Tests"
  - "curl smoke examples"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

REST/GraphQL-Backends entwerfen, implementieren und mit **Contract-Tests** und curl-Smoke verifizieren.

## Wann nutzen

- Neue Endpoints, Versionierung, Pagination.
- Breaking-Change-Vorbereitung.

**Wann nicht:** Vollständige Auth-Platform (eigenes IAM).

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| curl | Smoke | `curl -sf -H` |
| OpenAPI | Contract | single source |
| pytest | Integration | httpx/TestClient |

## System-Prompt / Instruktionen

```text
Backend APIs workflow (software-entwicklung/backend-apis).

OpenAPI first or update spec with every route change.
Validate breaking changes: list removed fields explicitly.
Implement validation at boundary; consistent error envelope {code,message,details}.
Pagination: cursor or offset documented; max limit cap.
Auth: never log tokens; 401 vs 403 distinct.
curl smoke: curl -sf -X POST http://localhost:8080/v1/items -H "Authorization: Bearer $TOKEN" -d @payload.json.
Integration tests use test database or containers; no prod URLs.
Rate limit headers if policy exists: Retry-After.
Idempotency-Key for POST creates when user requests payments style APIs.
Version paths /v1/ stable; /v2/ for breaks.
Document migration notes for clients.
Run tests before suggesting merge.
```

## Arbeitsablauf

1. OpenAPI lesen/ergänzen.
2. Handler + DTOs implementieren.
3. Unit-Tests für Validierung.
4. Integration `pytest tests/api/test_items.py`.
5. `curl` smoke gegen lokale Instanz.
6. Breaking diff gegen alte Spec.
7. Changelog-Eintrag.

## Qualitätskriterien / Definition of Done

- [ ] OpenAPI committed und gültig
- [ ] Tests grün
- [ ] Error codes konsistent

## Sicherheit & Freigaben

- Keine echten Tokens in Repo.
- PII-Logging vermeiden.

## Fallstricke

- Spec ohne Implementierung drift.
- 200 mit error body — verwirrend.
- N+1 in List-Endpoints.
- Fehlende 413/ payload limits.
- CORS * in Prod-Vorschlag.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** GET /v1/items mit Pagination.
- **Input:** OpenAPI exists.
- **Prompt:**

```text
Implement list endpoint; pytest; curl with limit=10.
```

- **Erwartetes Ergebnis:**

```bash
pytest tests/api/test_list_items.py -q
curl -sf 'http://localhost:8080/v1/items?limit=10' -H "Authorization: Bearer test"
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** 422 validation errors.
- **Input:** POST missing field.
- **Prompt:**

```text
Return structured 422; test asserts body.code=VALIDATION_ERROR.
```

- **Erwartetes Ergebnis:**

```bash
curl -s -o /tmp/r.json -w '%{http_code}' -X POST http://localhost:8080/v1/items -H 'Content-Type: application/json' -d '{}'
# 422
```