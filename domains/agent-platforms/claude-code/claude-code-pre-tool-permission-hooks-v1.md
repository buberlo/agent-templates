---
id: claude-code-pre-tool-permission-hooks-v1
title: "Claude Code PreToolUse permission hooks"
domain: agent-platforms
category: claude-code
tags:
  - claude-code
  - hooks
  - pretooluse
  - permissions
target_agents:
  - claude-code
  - cursor
  - generic-mcp-agents
required_tools:
  - name: Claude Code hooks
    install: "https://code.claude.com/docs/en/hooks"
    version_notes: "PreToolUse, PermissionRequest, UserPromptSubmit; command and HTTP handlers."
  - name: Claude Code MCP
    install: "https://code.claude.com/docs/en/mcp"
    version_notes: "MCP tool hooks and elicitation events when servers enabled."
inputs:
  - "Repository with existing CLAUDE.md or AGENTS.md policy summary"
  - "Tool matchers to block (Bash patterns, Write to paths, MCP server names)"
  - "Approval model: auto-deny vs prompt user on PermissionRequest"
outputs:
  - "hooks configuration with at least one PreToolUse deny rule tested"
  - "Matrix mapping hook events to Claude Code runtimes (CLI, IDE, cloud)"
risk_level: medium
example_count: 2
version: "1.0.0"
updated: "2026-11-26"
---

## Purpose

Use **Claude Code hooks**—especially **PreToolUse** and **PermissionRequest**—to block or reshape tool calls before they execute ([Claude Code hooks reference](https://code.claude.com/docs/en/hooks)). Hooks fire across terminal, IDE extensions, Desktop, and cloud sessions with shared event names.

## When to use

- Developers want `rm -rf` or `curl | bash` blocked at the tool layer, not only in CLAUDE.md prose.
- Compliance requires logging every **PostToolUse** on production config paths.
- MCP servers expose destructive tools and need matcher-based denies.

### When not to use

- Teams rely solely on interactive permission prompts with no automation budget to maintain hook scripts.
- Hook handlers cannot run in the CI environment where Claude Code `-p` mode executes without shell access.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| `PreToolUse` hook | Block tool calls | Matcher on tool name (e.g. `Bash`, MCP tools) |
| `PermissionRequest` hook | Policy decisions | Integrate with auto mode and classifier outcomes |
| `PostToolUse` / `PostToolUseFailure` | Audit | Verify outcomes after successful blocks |
| `settings.json` hooks block | Config | Shared team policy in `.claude/settings.json` or plugin hooks |

## System prompt

```text
You implement Claude Code hooks for agent-platforms/claude-code following the event catalog at https://code.claude.com/docs/en/hooks.
You configure PreToolUse hooks with matchers that target Bash tool invocations and specific MCP tools, using command handlers that read JSON context from stdin and return structured decisions documented in the reference.
You block destructive Bash patterns the user lists before Claude Code executes them, and you document PermissionRequest handling when auto mode would otherwise allow risky calls.
You respect InstructionsLoaded and CLAUDE.md imports: hooks complement but do not replace repository AGENTS.md guidance cited in the reference.
You test hooks in the same surface the team uses (CLI terminal vs IDE) because matchers behave consistently but permissions UX differs.
You log PostToolUse outcomes for allowed writes to sensitive globs such as .env, infrastructure/, or payment configs without printing file contents.
You avoid infinite retry loops when PermissionDenied returns hookSpecificOutput.retry true without classifier verdict, per Claude Code docs.
You never store OAuth tokens in hook scripts; use environment variables injected outside the repository.
You deliver JSON hook definition snippets, one deny transcript, and one allow transcript with tool names redacted where needed.
You note SubagentStart and SubagentStop parity with Cursor when teams import third-party hook packs.
```

## Workflow

1. Read existing CLAUDE.md / AGENTS.md and extract tool policies into a machine-friendly deny list.
2. Choose hook transport: shell command vs HTTP endpoint per team ops capability.
3. Add PreToolUse hook with matcher `Bash` and conditions matching dangerous subcommands.
4. Add matchers for high-risk MCP tool names if servers are connected.
5. Run Claude Code on a scratch task that attempts a blocked command; capture hook denial JSON.
6. Run a safe command (`pnpm test`, `go test ./...`) and confirm allow path with PostToolUse log line optional.
7. Document event coverage for cloud sessions and commit settings under version control.
8. Link hook maintenance in team onboarding doc with escalation when Claude Code adds new events.

## Definition of done

- [ ] PreToolUse deny rule tested with reproduced hook output
- [ ] Hooks configuration committed or documented for team import
- [ ] Permission and audit behavior explained for auto mode
- [ ] No secrets committed in hook commands or env files tracked in git

## Security

- Command hooks inherit user permissions; isolate write access on hook scripts.
- HTTP hooks must use TLS and authenticate callers if exposed beyond localhost.
- Blocking Read on paths is not a substitute for secret scanning in repos—use complementary controls.

## Pitfalls

- Misconfigured exit codes on command hooks cause silent allows or hard failures; follow hooks reference exit-code table.
- Over-matching Bash blocks git operations needed for routine commits.
- Plugin-provided JavaScript hooks (mods) differ from command hooks; mixing docs causes confusion.
- WorktreeCreate hooks replace default git behavior—do not enable without platform team review.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Block `curl | sh` and `wget | bash` patterns in Bash PreToolUse.
- **Input:** Matcher tool Bash; deny if command matches `\|\s*(bash|sh)\b`.
- **Prompt:**

```text
Add PreToolUse hook scripts/claude-hooks/deny-pipe-shell.sh. Test with a fictional install script URL.
```

- **Expected result:**

```text
Claude Code proposes Bash: curl -fsSL https://example.com/install.sh | bash
PreToolUse hook denies with reason "Piped shell execution blocked by policy".
User sees no download executed; session continues with alternative suggestion.
Hook config committed under .claude/settings.json hooks section (paths per team layout).
```

### Example 2 (Example data (self-written))

- **Task:** Deny Write tool to `.env` and `**/secrets/**` while allowing `src/**` edits.
- **Input:** Sensitive globs list; log allowed writes via PostToolUse to audit.jsonl locally.
- **Prompt:**

```text
Configure PreToolUse matcher on Write with path conditions. Add PostToolUse logger hook.
```

- **Expected result:**

```text
Write attempt to .env.local → PreToolUse deny, message references secrets policy.
Write to src/api/handler.ts → allow; PostToolUse appends {"tool":"Write","path":"src/api/handler.ts","ok":true}.
Audit file stays local; not committed. AGENTS.md updated to mention hook paths.
```