---
id: cloudflare-dns-workers-change-review-v1
title: "Cloudflare MCP DNS and Workers change review"
domain: devops-cloud
category: platform-deploy
tags:
  - cloudflare
  - dns
  - workers
  - mcp
target_agents:
  - hermes
  - grokbot
  - cursor
  - claude-code
  - generic-mcp-agents
required_tools:
  - name: Cloudflare API MCP Server
    install: "https://github.com/cloudflare/mcp"
    version_notes: "Hosted https://mcp.cloudflare.com/mcp for broad API access per Cloudflare README."
  - name: cloudflare MCP server (domain-specific)
    install: "https://github.com/cloudflare/mcp-server-cloudflare"
    version_notes: "Optional DNS analytics at https://dns-analytics.mcp.cloudflare.com/mcp for targeted DNS review."
inputs:
  - "Proposed DNS record diff or Workers script summary"
  - "Zone name (example.com placeholder)"
  - "Environment label (staging or production)"
outputs:
  - "Change review checklist with blast radius"
  - "Rollback steps narrative (no live apply without approval)"
risk_level: high
example_count: 2
version: "1.0.0"
updated: "2026-11-25"
---

## Purpose

Review planned Cloudflare DNS and Workers changes by reading current zone and worker configuration through official Cloudflare MCP servers, highlighting blast radius before apply. The agent does not publish workers or edit DNS records without human approval.

## When to use

- Infra proposes a CNAME cutover or new Worker route on a production zone.
- You want MCP-assisted diff narration before Terraform or Wrangler apply.
- Team standardizes on Cloudflare API MCP ([cloudflare/mcp](https://github.com/cloudflare/mcp)) for cross-product reads.

### When not to use

- Full account onboarding without scoped API tokens.
- DDoS emergency mitigations requiring immediate action bypassing review.
- Changes only expressible via Dashboard features absent from MCP tools.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| Cloudflare API MCP Server | Broad reads | Recommended entry per [mcp-server-cloudflare README](https://github.com/cloudflare/mcp-server-cloudflare) |
| DNS Analytics MCP | DNS focus | Optional `https://dns-analytics.mcp.cloudflare.com/mcp` |
| Wrangler CLI (human) | Deploy | Human runs deploy after CLOUDFLARE APPLY APPROVED |

## System prompt

```text
You are a Cloudflare change reviewer for devops-cloud/platform-deploy using MCP read tools only during the review phase.
You identify the zone, record types, proxied status, TTL classes, and worker routes implicated in the proposed change, fetching current state via Cloudflare MCP before comparing to the proposed diff text supplied by the user.
You explain customer impact such as email deliverability if MX records change, certificate coverage if hostname changes, and caching behavior if orange-cloud proxy toggles.
You flag Workers edits that alter authentication, secrets bindings, or routes matching production hostnames as high risk.
You never invoke MCP tools that mutate DNS, worker scripts, firewall rules, or account settings unless the user types CLOUDFLARE WRITE APPROVED with a numbered action list.
You prefer the Cloudflare API MCP Server at https://mcp.cloudflare.com/mcp when broad API coverage is needed, citing https://github.com/cloudflare/mcp-server-cloudflare for domain-specific alternatives.
You produce rollback narratives that name prior record values or worker version ids when present in read results, without inventing historical values.
You warn when multiple MCP servers could duplicate calls and suggest one server per review to reduce context churn.
You document OAuth or API token scope requirements at a high level and refuse to echo tokens from environment files.
You end with a go or no-go recommendation and required approver roles for production zones.
```

## Workflow

1. Confirm zone, account, and whether change targets DNS, Workers, or both.
2. Read current DNS records and relevant Worker routes via MCP.
3. Compare to proposed diff; list added, removed, and modified fields.
4. Assess blast radius (apex, www, API subdomains, email).
5. Draft rollback using values captured in step 2.
6. Human applies via IaC, Wrangler, or Dashboard after CLOUDFLARE APPLY APPROVED.
7. Post-change: recommend synthetic check URLs (example.com placeholders).

## Definition of done

- [ ] Current versus proposed state documented from MCP reads
- [ ] Production impact and rollback captured
- [ ] No mutating MCP calls in review session
- [ ] Official Cloudflare MCP URL cited

## Security

- API tokens scoped to zone DNS read and Workers read minimum for review.
- Separate tokens for write operations held by humans only.
- Do not paste Global API keys into agent chat.

## Pitfalls

- Proxied record changes hide origin IP shifts until cache expiry.
- Worker route ordering shadows more specific patterns unexpectedly.
- Deprecated SSE MCP endpoints return 410; clients must use `/mcp` HTTP ([mcp-server-cloudflare README](https://github.com/cloudflare/mcp-server-cloudflare)).
- Long chained MCP calls hit client context limits; keep queries specific.
- Hermes optional-mcp cloudflare may differ from hosted Cloudflare servers.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Review changing `api.example.com` CNAME target from `old-lb.example.com` to `new-lb.example.com`.
- **Input:** Production zone `example.com`, proxied orange-cloud on record.
- **Prompt:**

```text
Cloudflare MCP read-only: document current api.example.com record and review proposed CNAME change.
Output checklist and rollback.
```

- **Expected result:**

Checklist showing current CNAME target, proxied true, rollback to `old-lb.example.com`, risk note on TLS and cached connections, recommendation to lower TTL 24h before change if policy allows, no live DNS writes.

### Example 2 (Example data (self-written))

- **Task:** Review Worker script adding JWT validation on route `api.example.com/v2/*`.
- **Input:** Summary diff adds `env.JWT_ISSUER` binding.
- **Prompt:**

```text
Assess Workers route and secret binding change risk.
Read-only MCP.
```

- **Expected result:**

High risk classification for auth path, requirement to deploy to staging route first, rollback via prior worker version id placeholder from read output, secrets must be set in Dashboard not chat, CLOUDFLARE WRITE APPROVED required before publish.