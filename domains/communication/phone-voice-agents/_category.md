Phones and Voices

- **Domain:** `communication`
- **Category:** `phone-voice-agents`
- **As of:** 2026-11-23

## Summary

Outbound/inbound calls via voice agent platforms, transcripts and post processing.

## Recommended tool stack

- Spezialplattformen separat pruefen
- Twilio-Docs-MCP in the Hermes catalogue is documentation, not automatically a dialer

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| twilio-docs MCP (Hermes-catalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/twilio-docs |Documentation on Twilio, not tacitly equating to a productive call agent.| hermes mcp install twilio-docs | Nous-approved optional-mcps catalog entry (listing 2026-11-23). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | no (as cited) |
| ClawHub „Agent Phone Call“ (mrsz) | Skill | https://clawhubtrends.com/leaderboard.html |In the leaderboard with warning marking, only 8 registry stars at high downloads. In the leaderboard with warning marking – verify before use.|openclaw skills install (Owner mrsz) and openclaw skills verify.| 72.476 Downloads, 8 Registry-Stars (ClawHub Leaderboard 23.11.2026). | https://clawhubtrends.com/leaderboard.html | no (as cited) |

## Typical workflows

- Claim call content and consent; Observe recording rules.

## Pitfalls

- Check ClawHub skills before use (`openclaw skills verify`). In February 2026, Koi Security audited 2,857 registry skills and rated 341 as defective (about 12%). Source: https://thehackernews.com/2026/02/researchers-find-341-malicious-clawhub.html , https://docs.openclaw.ai/skills/
- Do not unload warning-marked ClawHubs.
in business day in and dayr organizations in arrived at instantly and shops in the; day with day diss day day, day day in day better day diss day day increasingly means day in day day day day day inElion day day day day day destination destination day day day day day day to the day, the day, the day, the number, the number, the number, the number, the number Donbass and outlet, his day so payment passing day Don't confuse the two together. Sources, https://code.claude.com/docs/features-overview , https://github Grounds/ComposioHQ/awesome-claude-skills.
usingmide, Hermes filters per include/exclude; Openforms have prompt-and-money-policy. Source: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. OAuth tokens remain on the connector backend; Command servers must not contain using credves in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; Conf.

## Sources

- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://clawhubtrends.com/leaderboard.html
- https://thehackernews.com/2026/02/researchers-find-341-malicious-clawhub.html
- https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/twilio-docs
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
