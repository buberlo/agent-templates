---
id: osint-mcp-focus
title: "OSINT (open sources): MCP/Skill Focus"
domain: security
category: osint
tags:
  - osint
  - mcp
target_agents:
  - hermes
  - generic-mcp-agents
required_tools:
  - name: Web Search / Fetch MCP
    install: "read-only browse"
    version_notes: "public URLs only"
  - name: whois/RDAP CLI
    install: "verify step"
    version_notes: "skill cross-check"
inputs:
  - "OSINT question scope"
  - "Skill citation rules"
outputs:
  - "Cited brief"
  - "MCP source log"
risk_level: medium
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Purpose

OSINT per **MCP Fetch/Search** with skill obligation: **double source**, no hidden login MCPs, same policy as `osint-workflow`.

## When to use

- Agent with web MCP for public sources.
- Skill erzwingt Zitationsformat.

**When not:** When Web-MCP reaches authenticated areas without ROE.

## Tool stack

| Tool | Role | Justification |
|------|-------|------------|
| Fetch MCP | Pages | public |
| Skill | Citations | URL+date |
| RDAP CLI | Verify | domain facts |

## System prompt

```text
OSINT MCP/Skill focus (security/osint).

MCP fetch only public URLs user lists or that are clearly public documentation.
Skill: question -> source1 MCP -> source2 independent -> synthesize with citations.
Cross-check RDAP via CLI when domain facts material.
No MCP tools that automate LinkedIn/private social scraping.
Log each URL fetched with timestamp in audit footer.
If MCP returns paywall/login wall, stop; do not bypass.
Refuse private individual targeting.
Minimize quoting; summarize with link.
Disable high-risk MCPs (port scan plugins) entirely for this skill.
Human review before external sharing of OSINT brief.
```

## Workflow

1. confirm scope.
MCP fetch Source A (vendor advisory).
MCP fetch Source B (independent news/registry).
4. CLI RDAP cross-check wenn Domain.
5. Letter with footnotes.
6. MCP audit log.
7. No further step in contradiction without clarification.

## Definition of done

- [ ] ≥2 independent sources of core facts
- [ ] MCP audit completely
[ ] No policy violations

## Security

- No Umgehung von Paywalls/Logins.

## Pitfalls

- MCP halluziniert URL — verify HTTP status.
One source is not enough.
- Injection in fetched HTML.
- Alte Cache-Snapshot MCP.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Vendor breach news check.
- **Input:** Vendor V.
- **Prompt:**

```text
Two-source MCP fetch; cite; refuse if only rumor blog.
```

- **Expected result:**

```text
[1] vendor status page [2] press wire; confidence medium
```

### Example 2 (Example data (self-written))
- **Task:** Paywall hit.
- **Input:** financial times article.
- **Prompt:**

```text
Stop at paywall; suggest manual analyst review.
```

- **Expected result:**

```text
Fetch 402/paywall; no bypass; manual step noted
```