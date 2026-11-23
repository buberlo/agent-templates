# Cloud: GCP

- **Domain:** `devops-cloud`
- **Category:** `cloud-gcp`
- **As of:** 2026-11-23

## Summary

GCP/GKE-Ressourcen, inkl. verwalteter MCP-Endpunkte wo angeboten.

## Recommended tool stack

- CLI (kubectl/terraform/docker) or official cloud MCPs, default read-only

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| GitHub Official MCP | MCP | https://github.com/github/github-mcp-server | Repos, Issues, PRs, Code Search, Actions. |Remote e.g. claude mcp add --transport http github https://api.githubcopilot.com/mcp/ with PAT header (Claude code docs) or local server from the repo.| 34.686 Stars | https://code.claude.com/docs/en/mcp | no (as documented) |
| Sentry MCP | MCP | https://github.com/getsentry/sentry-mcp | Production errors, issues, and context for coding agents. | Offizielles getsentry/sentry-mcp Repo. | 973 Stars | https://github.com/getsentry/sentry-mcp | no (as documented) |

## Typical workflows

- Confirm the task, allowed tools, and definition of done.
- Read/research first, then draft, then approval for consequential steps.
- Review output (file, URL, ticket) and cite sources.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure); MCP servers are connections and tools. Combine both; do not conflate them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/skills the task needs. Hermes filters via include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not put tokens or passwords in chat, skill files, or custom MCP command arguments. Grok Bot wiki: OAuth tokens stay on the connector backend; command servers must not pass credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy, and delete only after explicit approval; good document skills require a verify step (re-read the file, render PDF/PNG).

## Sources

- https://code.claude.com/docs/en/mcp
- https://github.com/github/github-mcp-server
- https://github.com/getsentry/sentry-mcp
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
