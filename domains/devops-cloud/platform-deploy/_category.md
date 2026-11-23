# Platform Deploy

- **Domain:** `devops-cloud`
- **Category:** `plattform-deploy`
- **As of:** 2026-11-23

## Summary

Vercel, Netlify, Railway, Cloudflare and similar deployment platform

## Recommended tool stack

- Vercel/Netlify/Railway/Cloudflare aus Hermes catalog

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| vercel MCP (Hermes catalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/vercel | Vercel-Deploys. | hermes mcp install vercel | Nous-approved optional-mcps catalog entry (listing 2026-11-23). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | no (as documented) |
| netlify MCP (Hermes catalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/netlify | Netlify. | hermes mcp install netlify | Nous-approved optional-mcps catalog entry (listing 2026-11-23). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | no (as documented) |
| railway MCP (Hermes catalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/railway | Railway. | hermes mcp install railway | Nous-approved optional-mcps catalog entry (listing 2026-11-23). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | no (as documented) |
| cloudflare MCP (Hermes catalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/cloudflare | Cloudflare. | hermes mcp install cloudflare | Nous-approved optional-mcps catalog entry (listing 2026-11-23). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | no (as documented) |

## Typical workflows

- Preview deploys preferred, production only after release.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure); MCP servers are connections and tools. Combine both; do not conflate them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/skills the task needs. Hermes filters via include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not put tokens or passwords in chat, skill files, or custom MCP command arguments. Grok Bot wiki: OAuth tokens stay on the connector backend; command servers must not pass credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy, and delete only after explicit approval; good document skills require a verify step (re-read the file, render PDF/PNG).

## Sources

- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/vercel
- https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/netlify
- https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/railway
- https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/cloudflare
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
