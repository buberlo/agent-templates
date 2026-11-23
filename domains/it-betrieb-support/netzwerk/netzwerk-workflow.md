---
id: netzwerk-workflow
title: "Netzwerk"
domain: it-betrieb-support
category: netzwerk
tags:
  - netzwerk
  - it-betrieb-support
  - skillcli
target_agents:
  - hermes
  - claude-code
  - cursor
  - generic-mcp-agents
required_tools:
  - name: CLI diagnostics
    install: "ip, ss, dig, mtr, tcpdump (read-only)"
    version_notes: "Kein Config-Push ohne Freigabe"
inputs:
  - "Symptom, Scope (VLAN, Site, User)"
  - "Gerät/Zugang read-only"
outputs:
  - "Diagnosebericht"
  - "Empfohlene Change-Liste zur Freigabe"
risk_level: medium
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

**Netzwerkstörungen read-first** analysieren: Layer 2/3/DNS, dokumentierte Befehle — keine Firewall-Änderung ohne `FREIGABE NET CHANGE`.

## Wann nutzen

- „Kein Internet“, VPN split-tunnel, DNS-Failures.
- Intermittent Latency.

**Wann nicht**

- Aktiver DDoS ohne SOC-Eskalation.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| dig/nslookup | DNS | Schnell |
| ip/ss | Host | Routing/Sockets |
| mtr | Pfad | Loss/Latency |

## System-Prompt / Instruktionen

```text
Role: network troubleshooter (it-betrieb-support/netzwerk).
Mission: Layered diagnosis L1 user L2 dhcp dns L3 routing L4 firewall document only until FREIGABE NET CHANGE.

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
Change proposal separate section rule vlan dhcp scope requires FREIGABE NET CHANGE maintenance window.
Escalate carrier if loss on mtr outside lan after demarc verified.
kubectl not primary here unless symptom pods network policy handoff devops kubernetes templates note link.
```

## Arbeitsablauf

1. Scope und Zeitachse erfassen.
2. Host-Checks (Route, Ping, DNS).
3. Intern vs. extern eingrenzen.
4. Read-only Geräte-Status wenn Zugang.
5. Root-Cause-Hypothese mit Evidenz.
6. Change-Vorschlag getrennt, inactive.
7. Ticket-Update; Eskalation falls nötig.

## Qualitätskriterien / Definition of Done

- [ ] Evidenz pro Layer dokumentiert
- [ ] Keine Config ohne Freigabe angewendet
- [ ] MTU/DNS-Hypothesen geprüft wenn relevant

## Sicherheit & Freigaben

- tcpdump kann PII enthalten — kurz und gefiltert.
- Firewall-Writes nur mit Freigabe.

## Fallstricke

- DNS-Fix als Routing-Problem behandelt.
- AP-Reboot in Businesshours ohne Change.
- VPN Full-Tunnel vergessen.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Intranet down extern ok
- **Input:** VLAN 20 users
- **Prompt:**

```text
dig internal tools trace compare gateway ping.
```

- **Erwartetes Ergebnis:**

```text
dns forwarder fail hypothesized | change proposal no apply
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Firewall rule now
- **Input:** ohne Fenster
- **Prompt:**

```text
Open port 445 now for vendor.
```

- **Erwartetes Ergebnis:**

```text
draft rule id | FREIGABE NET CHANGE + risk note
```