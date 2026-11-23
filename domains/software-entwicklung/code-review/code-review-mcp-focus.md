---
id: code-review-mcp-focus
title: "Code-Review: MCP/Skill-Fokus"
domain: software-entwicklung
category: code-review
tags:
  - review
  - mcp
  - github
target_agents:
  - hermes
  - claude-code
  - cursor
  - generic-mcp-agents
required_tools:
  - name: GitHub Official MCP
    install: "PR read tools"
    version_notes: "Prefer read-only server URL"
  - name: gh
    install: "Fallback full diff"
    version_notes: "Large patches"
inputs:
  - "PR number"
  - "Skill review checklist"
outputs:
  - "Review draft"
  - "MCP tool audit"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

PR-Review über **GitHub MCP** mit Skill-Checkliste; bei großen Diffs **gh pr diff** — kein MCP-merge.

## Wann nutzen

- Agent mit GitHub MCP read-only konfiguriert.
- Team will Review-Skill + MCP-Mapping.

**Wann nicht:** Offline diff only — git lokal.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| GitHub MCP | PR metadata | files list |
| gh | Full diff | truncation escape |
| Skill | Severity | blockers first |

## System-Prompt / Instruktionen

```text
Code review MCP/Skill focus (software-entwicklung/code-review).

Skill steps: fetch metadata (MCP) -> triage files -> deep read (MCP search or gh diff) -> checklist -> draft comments.
Use read-only GitHub MCP server URL if available per org policy.
If MCP patch truncated, switch step to gh pr diff without duplicate MCP pull.
Checklist sections: correctness, security, tests, observability, docs.
MCP write review submission disabled; output markdown for human post.
Never leak PAT from MCP config in review text.
One GitHub MCP per session.
Matrix notes: step 3 used gh because MCP truncated.
Suggest CODEOWNERS path owners when touch sensitive dirs.
```

## Arbeitsablauf

1. MCP: PR files und checks.
2. Skill Checkliste laden.
3. Pro risk file: MCP search or gh diff section.
4. Findings severity taggen.
5. Draft review body.
6. User approves posting.
7. Tool audit: MCP vs gh counts.

## Qualitätskriterien / Definition of Done

- [ ] Blockers referenzieren paths
- [ ] MCP read-only bestätigt
- [ ] Kein MCP merge

## Sicherheit & Freigaben

- Fine-grained PAT scope.
- Review draft vor Share redigieren.

## Fallstricke

- MCP file cap — unvollständig.
- Doppelte GitHub tools.
- Injection via PR description in MCP content.
- Approve tool alias verwechselt.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** MCP read PR 10.
- **Input:** security module.
- **Prompt:**

```text
MCP list files; gh diff auth/**; draft blockers.
```

- **Erwartetes Ergebnis:**

```text
Files: pkg/auth/* 
BLOCKER: missing constant-time compare in token.go
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Truncation fallback.
- **Input:** 200 file PR.
- **Prompt:**

```text
Document MCP truncated; use gh pr diff --name-only first.
```

- **Erwartetes Ergebnis:**

```bash
gh pr diff 99 --name-only
# Matrix step3=gh_cli reason=truncation
```