# Logging

- **Domain:** `devops-cloud`
- **Category:** `logging`
- **As of:** 2026-11-23

## Summary

Logsuche, Korrelation and Alert-Kontext.

## Recommended tool stack

- CLI (kubectl/terraform/docker) or official cloud MCPs, read-only by default

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| GitHub Official MCP | MCP | https://github.com/github/github-mcp-server | Repos, issues, PRs, code search, Actions. | Remote, e.g. claude mcp add --transport http github https://api.githubcopilot.com/mcp/ with PAT header (Claude Code docs) or local server from the repo. | 34,686 stars | https://code.claude.com/docs/en/mcp | no (as cited) |
| Sentry MCP | MCP | https://github.com/getsentry/sentry-mcp | Produktionsfehler, Issues and Kontext for Coding-Agenten. | Officials getsentry/sentry-mcp Repo. | 973 Stars | https://github.com/getsentry/sentry-mcp | no (as cited) |

## Typical workflows

- Set the task, allowed tools, and definition of done.
- Read or research first, then draft, then request approval for any action that has effects.
- Recheck the output (file, URL, ticket) and cite the source.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok Bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a verify step (read the file again, render PDF/PNG).

## Sources

- https://code.claude.com/docs/en/mcp
- https://github.com/github/github-mcp-server
- https://github.com/getsentry/sentry-mcp
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
- https://api.githubcopilot.com/mcp/
- https://code.claude.com/docs/en/features-overview
- https://github.com/ComposioHQ/awesome-claude-skills
- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
