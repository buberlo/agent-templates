---
id: codex-workflow
title: "Codex"
domain: agent-platforms
category: codex
tags:
  - codex
  - agent-platforms
  - skill
target_agents:
  - codex
  - generic-mcp-agents
required_tools:
  - name: Hermes-Skill codex
    install: "https://hermes-agent.nousresearch.com/docs/reference/skills-catalog"
    version_notes: "Bundled; delegiert an OpenAI Codex CLI"
  - name: OpenClaw MCP serve / ACP
    install: "https://docs.openclaw.ai/cli/mcp/serve"
    version_notes: "Bridge openclaw mcp serve or openclaw acp"
inputs:
  - "Feature-Briefing or PR-Beschreibung"
  - "Repo-URL or Pfad; Orchestrator (Hermes/OpenClaw)"
outputs:
  - "Branch/diff from Codex loop"
  - "Review summary in orchestrator thread"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---
## Purpose

Use OpenAI **Codex CLI** as focused coding runtime — often **delegated by Hermes** (‘Hermes-Skill codex’) or via **OpenClaw** (‘openclaw mcp serve’ / ‘openclaw acp’). The orchestra holds context and releases; Codex provides implementation loops.

## When to use

- Hermes/OpenClaw should plan, audit and release; Codex writes code in an isolated loop.
OpenClaw Gateway is intended to serve as an MCP server for external clients (Codex, Claude Code).

###### When not to use

- If two agents write in parallel without a lock on the same repo. If you expect Office-Verify (document-skills render) in Codex instead of in the Orchestrator/Skill. If no feedback to the parent thread is planned.

## Tool stack

| Tool | Role | Rationale |
|------|-------|-----------|
| Hermes-Skill codex | Delegation |Bundled Skill aus Skills-catalog|
| OpenAI Codex CLI | Coding Runtime | MCP-capable like other clients |
| openclaw mcp serve | Bridge | OpenClaw as MCP for Codex |
| openclaw acp | Alternative Host | OpenClaw hostet Coding-Runtime |
| Parent Orchestrator | Review | Hermes/OpenClaw thread with release |

## System prompt

```text
Du nutzt Codex als Coding-Runtime unter einem Orchestrator (Hermes or OpenClaw).
Codex session only for implementation, testing and local diffs — no production deploys without parent release.
Hermes-Skill codex: Task klar abgrenzen (Scope, Files, not ganze Monorepo umschreiben).
OpenClaw Bridge: openclaw mcp serve (stdio) only with tool policy that limits writes.
Zwei Schreiber auf ein Repo: Serialisierung — ein aktiver Codex-Job pro Branch.
MCP in Codex minimal halten (Schema-Overhead wie bei anderen Clients).
Parent thread must get Diff and Test status back.
No API-Keys in Delegations-Prompt or Codex-argv.
Nach Codex-Lauf: Orchestrator reviewt, merged not automatisch.
Define skills in Parent Verify (Lint/Test); Codex executes, Parent sign-off.
Bei ClawHub-Skills am Gateway: verify vor Nutzung durch Codex-Bridge.
Document-Verify (Render) bleibt Parent-/Skill-Task, not Codex allein.
```

## Workflow

Open the orchestra thread; Record briefing and acceptance criteria.
2. Clarify repo lock/branch strategy (a Codex job).
3. Launch Hermes `codex` skill or configure OpenClaw `mcp serve` for Codex client.
4. Codex: implementieren, Tests laufen lassen, Diff erzeugen.
5. Log the result (diff, test log) back to Parent.
6. Parent: Review, Security Check, Release for Push/Merge.
7. Optional zweite Codex-Runde nur nach Review-Kommentaren.
8. Graduation in the Orchestrator with links to Commits/PR.

## Definition of done

- [ ] One writer per branch during Codex run
- [ ] Diff and test status documented in the parent thread
- [ ] No merge/deploy without parent release
- [ ] MCP/Bridge-Policy verhindert unerwartete Remote-Writes
- [ ] No Secrets in Delegations-Metadaten

## Security

- OpenClaw-Bridge: Tool-Policy wie Gateway-Standard.
- Parent muss destructive Aktionen freigeben.
- Bei Registry-Skills am Gateway: ClawHub verify (~12 % Malware-Kontext).

## Pitfalls

- **Two scribes:** Hermes and Codex change in parallel — Merge conflicts and data loss.
- **Delegation without review:** Codex pushes; Parent does not know Diff.
- **MCP-Overhead:** Voller MCP-Stack in Codex + Parent — doppelter Schema-Druck.
- **openclaw acp vs. serve:** Wrong bridge — client sees wrong tools.
- **Skill vs. MCP:** Parent-Skill muss Verify-Schritte (Test/Lint) benennen.
*ClawHub on Gateway:** Codex over Bridge uses compromised skills, if not verified.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Hermes delegiert kleines Feature
- **Input:** “Add Endpoint GET /health in Express”, Repo locally cloned
- **Prompt:**
```text
(Hermes) Nutze codex-Skill nur for src/routes/*. Codex: Implementation + npm test. Kein git push.
```
- **Expected result:**
```text
Diff: +12 Zeilen health route
npm test: 14 passed
Parent-Thread: Review-OK, User gibt Push frei
```

### Example 2 (Example data (self-written))
- **Task:** Parallele Schreiber — Fehlmodus
- **Input:** Same branch main, Hermes agent and Codex without lock
- **Prompt:**
```text
Codex: Refactor auth; parallel Hermes: Update README auf main.
```
- **Expected result:**
```text
Merge-Konflikt in main
Parent stoppt: „Serialisiere Jobs — ein Branch, ein aktiver Writer“
Kein force-push
```