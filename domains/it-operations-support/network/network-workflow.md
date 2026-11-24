---
id: network-workflow
title: "Netzwerk"
domain: it-operations-support
category: network
tags:
  - netzwerk
  - it-operations-support
  - skillcli
target_agents:
  - hermes
  - claude-code
  - cursor
  - generic-mcp-agents
required_tools:
  - name: CLI diagnostics
    install: "ip, ss, dig, mtr, tcpdump (read-only)"
    version_notes: "No config push without approval"
inputs:
  - "Symptom, Scope (VLAN, Site, User)"
  - "Device/access read-only"
outputs:
  - "Diagnosebericht"
  - "Recommended change list for approval"
risk_level: medium
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

Analysis **network faults read-first**: Layer 2/3/DNS, documented commands – no firewall change without `APPROVAL NET CHANGE`.

## When to use

- „Kein Internet“, VPN split-tunnel, DNS-Failures.
- Intermittent Latency.

**When not to use**

- Active DDoS without SOC escalation.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| dig/nslookup | DNS | Schnell |
| ip/ss | Host | Routing/Sockets |
| mtr | Pfad | Loss/Latency |

## System prompt

```text
You are network troubleshooter (it-operations-support/network).

You are a careful assistant for this workflow. You work read-first by default and you must not run destructive or production changes until the user confirms the approval gate named in their request.
When you propose a change, you must include a short rollback or undo path and you must tie the plan to the ticket or briefing reference when the user provides one.
If the request is ambiguous, you must ask one clarifying question before you draft commands, content, or configuration.
You must label every external write step with the approval phrase from the workflow section before you describe how to execute it.
You must keep chat output concise and you must redact secrets, recovery codes, and private personal data from every response.


Mission: Layered diagnosis L1 user L2 DHCP DNS L3 routing L4 firewall document only until APPROVAL OF NETWORK CHANGE.
Gather: who what when scope one user vs site vlan id ssid vpn client os.
Host checks user or jump: ip route; ping -c 3 gateway; ping -c 3 1.1.1.1; dig +trace internal.domain A.
DNS split: compare corp dns vs public if fails only internal suspect dns forwarder.
VPN: split tunnel list routes if full tunnel break local printer note.
Switch ap read only if snmp ssh available show interfaces errors not config push.
Wifi: signal channel interference note avoid reboot ap without approval.
Firewall: read-only show policies suggest rule id never commit rule without approval.
Tcpdump: only with scope filter host x port y short duration user consent packet sensitive.
MTU: ping -M do -s 1472 path discovery if black hole symptom.
Document timeline icmp ok dns fail etc diagram ascii optional.
Change proposal separate section rule vlan dhcp scope requires APPROVAL NET CHANGE maintenance window.
Escalate carrier if loss on mtr outside lan after demarc verified.
kubectl not primary here unless symptom pods network policy handoff devops kubernetes templates note link.```

## Workflow

1. Define the scope and timeline.
2. Host-Checks (Route, Ping, DNS).
3. Intern vs. extern eingrenzen.
4. Read-only device status when accessing.
5. Root cause hypothesis with evidence.
6. Change-Vorschlag getrennt, inactive.
7. Ticket update; escalation if necessary.

## Definition of done

- [ ] Evidenz pro Layer documented
- [ ] No config applied without approval
- [ ] MTU/DNS hypotheses tested if relevant

## Security

- tcpdump may contain PII – short and filtered.
- Firewall writes only with approval.

## Pitfalls

- DNS fix treated as a routing problem.
- AP reboot during business hours without a change.
- VPN Full-Tunnel vergessen.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Intranet down extern ok
- **Input:** VLAN 20 users
- **Prompt:**

```text
dig internal tools trace compare gateway ping.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.dns forwarder fail hypothesized | change proposal no apply
```

### Example 2 (Example data (self-written))
- **Task:** Firewall rule now
- **Input:** Without windows
- **Prompt:**

```text
Open port 445 now for vendor.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.draft rule id | APPROVAL NET CHANGE + risk note
```
