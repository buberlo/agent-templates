# SEO

- **Domain:** `content-marketing`
- **Category:** `seo`
- **As of:** 2026-11-23

## Summary

Technisches and inhaltliches SEO: Audits, Keywords, On-Page, interne Verlinkung.

## Recommended tool stack

- Crawler + authorized Search Console access
- Third-party skills on X were often ads – verify carefully

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| Firecrawl MCP | MCP | https://github.com/firecrawl/firecrawl-mcp-server | Web search, scraping, and crawling as context for agents. | Official MCP repo, typically npx or hosted per the README. | 7,886 Stars; Upstream 207,417 Stars | https://github.com/firecrawl/firecrawl-mcp-server | no (as cited) |
| Brave Search MCP | MCP | https://github.com/brave/brave-search-mcp-server | Web search via the Brave Search API. | Official Brave repository. | 1,585 Stars | https://github.com/brave/brave-search-mcp-server | no (as cited) |

## Typical workflows

- Set the task, allowed tools, and definition of done.
- Read or research first, then draft, then request approval for any action that has effects.
- Recheck the output (file, URL, ticket) and cite the source.
- Crawl important URLs, list issues, provide fixes as a PR or CMS draft.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok Bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a verify step (read the file again, render PDF/PNG).

## Sources

- https://github.com/firecrawl/firecrawl-mcp-server
- https://x.com/Naruto79z/status/2119108886477033981
- https://github.com/brave/brave-search-mcp-server
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
- https://code.claude.com/docs/en/features-overview
- https://github.com/ComposioHQ/awesome-claude-skills
- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
