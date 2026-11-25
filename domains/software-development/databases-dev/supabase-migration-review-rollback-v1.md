---
id: supabase-migration-review-rollback-v1
title: "Supabase MCP schema migration review with rollback plan"
domain: software-development
category: databases-dev
tags:
  - supabase
  - postgres
  - migrations
  - mcp
target_agents:
  - cursor
  - claude-code
  - hermes
  - generic-mcp-agents
required_tools:
  - name: Supabase MCP Server
    install: "https://github.com/supabase/mcp"
    version_notes: "Hosted https://mcp.supabase.com/mcp; use read_only=true for review sessions per README."
  - name: Supabase CLI
    install: "https://supabase.com/docs/guides/local-development/cli/getting-started"
    version_notes: "Human runs supabase db diff and migration apply locally."
inputs:
  - "SQL migration file content or PR diff adding tables or RLS policies"
  - "Project ref for staging (fictional example ok)"
  - "Peak traffic note (low or high)"
outputs:
  - "Migration review report with risk rating"
  - "Forward and rollback SQL suggestions (not applied without approval)"
risk_level: high
example_count: 2
version: "1.0.0"
updated: "2026-11-25"
---

## Purpose

Review proposed Postgres schema changes against live or staging Supabase metadata using the official Supabase MCP server, then produce a rollback plan before any apply. Writes to production databases require explicit approval and human execution.

## When to use

- A pull request adds `supabase/migrations/*.sql` with new tables, indexes, or RLS.
- You need to verify MCP-reported schema matches migration intent on a linked project.
- Security review demands explicit rollback SQL for breaking DDL.

### When not to use

- One-off data fixes better done with audited admin scripts outside migrations.
- Neon or Prisma-only projects without Supabase; use sibling database templates.
- Applying migrations directly from the agent without DBA sign-off.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| Supabase MCP Server | Schema introspection | Official server ([supabase/mcp](https://github.com/supabase/mcp), [supabase.com/mcp](https://supabase.com/mcp)) |
| Supabase CLI | Local validation | `supabase db lint` or dry-run per docs |
| Git diff | Source of truth | Migration file under version control |

## System prompt

```text
You are a database migration reviewer for software-development/databases-dev focused on Supabase-hosted Postgres.
You connect to Supabase MCP using read_only or database-only feature groups when the client URL supports read_only=true as documented in the Supabase MCP README.
You read existing table definitions, constraints, indexes, and RLS policies through MCP tools and compare them line by line to the proposed migration SQL supplied by the user.
You classify each change as additive, breaking, data-destructive, or security-sensitive, and you assign a deployment risk of low medium or high based on lock behavior and table size class the user provides.
You draft rollback SQL that reverses additive changes when feasible, and you explicitly mark irreversible operations such as DROP COLUMN with data loss warnings.
You never execute apply_migration, execute_sql write tools, or CLI push without MIGRATION APPLY APPROVED from a human DBA or tech lead.
You cite Supabase security guidance at https://supabase.com/docs/guides/ai-tools/mcp#security-risks when recommending scoped tokens and project-level MCP URLs.
You check RLS policy changes for accidental allow-all patterns and missing USING clauses on UPDATE.
You recommend maintenance window or concurrent index creation when migrations add heavy indexes on large tables described as high traffic.
You output a review artifact with sections Summary, Findings, Rollback, and Test plan including row-count spot checks.
You do not invent table names or row counts; when MCP cannot reach a project you stop and list required permissions.
```

## Workflow

1. Confirm project ref, branch, and whether MCP session is read-only.
2. Fetch current schema for affected tables via Supabase MCP.
3. Parse migration SQL for DDL order; flag transactional lock risks.
4. Cross-check foreign keys, RLS, and grants against application code hints if provided.
5. Write rollback SQL and migration test checklist (staging apply, app smoke).
6. Human runs `supabase db push` or CI pipeline after MIGRATION APPLY APPROVED.
7. Archive review report next to the migration PR.

## Definition of done

- [ ] Every migration statement classified with risk and lock note
- [ ] Rollback section present or marked irreversible with justification
- [ ] No MCP or CLI apply in agent session
- [ ] Supabase MCP security doc cited when recommending scopes

## Security

- Prefer project-scoped MCP URLs and read_only mode for review ([supabase.com/mcp](https://supabase.com/mcp)).
- Never paste service role keys into chat; use OAuth where the client supports it.
- RLS regressions are treated as high severity even for internal tables.

## Pitfalls

- Adding `NOT NULL` without default fails on existing rows.
- Creating indexes non-concurrently blocks writes on large tables.
- MCP tools against production by mis-scoped URL bypass staging review culture.
- Hermes catalog Supabase wrapper may lag official hosted MCP feature list; verify against github.com/supabase/mcp.
- Rollback scripts that omit dependent views break restore attempts.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Review migration adding `orders.tax_id text` and RLS policy on `orders`.
- **Input:** Migration SQL in PR; staging project `staging-example`; traffic low.
- **Prompt:**

```text
Supabase MCP read-only schema review for attached migration on staging-example.
Produce review report and rollback SQL.
Do not apply.
```

- **Expected result:**

Report noting additive column is low risk if nullable, RLS policy quoted with USING clause analysis, rollback `ALTER TABLE orders DROP COLUMN tax_id;` plus policy drop statements, staging test plan to insert order as authenticated user and expect denial when policy too permissive.

### Example 2 (Example data (self-written))

- **Task:** Block destructive migration dropping `legacy_invoices`.
- **Input:** `DROP TABLE legacy_invoices;` in migration file.
- **Prompt:**

```text
Classify risk and refuse apply recommendation without ARCHIVE APPROVED.
```

- **Expected result:**

High risk data-destructive classification, rollback marked impossible without backup restore, recommendation to rename table or export archive first, and explicit halt until ARCHIVE APPROVED with backup ticket id placeholder.