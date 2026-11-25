---
id: kubernetes-mcp-focus
title: "Kubernetes: MCP focus"
domain: devops-cloud
category: kubernetes
tags:
  - kubernetes
  - mcp
  - kubectl
target_agents:
  - hermes
  - cursor
  - claude-code
  - grokbot
  - generic-mcp-agents
required_tools:
  - name: kubernetes-mcp-server
    install: "https://github.com/containers/kubernetes-mcp-server"
    version_notes: "kubeconfig; readonly default"
  - name: kubectl
    install: "Fallback when MCP limits logs"
    version_notes: "Same RBAC as MCP"
inputs:
  - "Cluster context and namespace"
  - "Skill with diagnose, mitigate, verify steps"
outputs:
  - "Skill to MCP tool matrix"
  - "Diagnosis report with MCP versus CLI flags"
risk_level: high
example_count: 2
version: "1.2.0"
updated: "2026-11-25"
---

## Purpose

Combine **Kubernetes MCP** with **kubectl** under a skill: readonly default, approval for writes, and explicit notes when CLI replaces MCP for logs.

## When to use

- Cursor or Hermes with kubernetes-mcp-server wired.
- Team docs mapping skill steps to MCP tools versus shell kubectl.

### When not to use

- Helm-only releases without diagnosis — see k8s rollout templates.
- Clusters where MCP cannot be scoped to readonly RBAC.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| kubernetes-mcp-server | MCP | get/describe workloads |
| kubectl | Supplement | logs --previous, rollout status |
| AKS Kubernetes MCP (optional) | Azure | Microsoft docs; readonly flag |

## System prompt

```text
You are a Kubernetes MCP focus assistant for devops-cloud/kubernetes.
You state default access as readonly and escalate to readwrite only with an approval keyword in the skill.
You map steps: verify context, list workloads, describe failing pod, fetch logs, propose patch or rollback.
You inherit RBAC from kubeconfig; on Forbidden you report the exact API error and do not switch contexts silently.
You use one cluster per session unless the user lists multiples and you document each context switch.
You prefer MCP for get and describe and kubectl for logs --previous when MCP truncates.
You pass readonly access level in mcp.json for AKS MCP when that server is used.
You forbid delete collection and cluster-admin MCP in production skill templates.
You avoid Helm changes through MCP unless helm-mcp is explicit in required_tools.
You run kubectl rollout status as verify after mitigation skill steps.
You mark whether each command ran via MCP or shell in the report.
You keep kubeconfig contents out of chat transcripts.
```

## Workflow

1. Verify context: `kubectl config current-context`.
2. Build skill matrix for Diagnose, Mitigate, Verify columns.
3. MCP: read namespaces, deployments, and events.
4. kubectl logs when MCP output truncates or lacks --previous.
5. Propose mitigation; hold until APPROVE.
6. After approval: rollout undo or patch with channel documented.
7. Verify rollout status and MCP pod ready checks.

## Definition of done

- [ ] access-level recorded in skill and MCP config
- [ ] Each step labeled MCP or CLI
- [ ] No admin MCP in prod without exception protocol

## Security

- **High risk** on production clusters.
- kubeconfig never pasted into chat; MCP uses secure transport from host.
- Write tools disabled until approval keyword present.

## Pitfalls

- Wrong context despite MCP — human must confirm context name aloud.
- Admin access-level as default — production incident risk.
- MCP without --previous logs hides crash loops.
- Two Kubernetes MCP servers register duplicate tool names.
- Helm drift when only MCP describe is used without release history.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** CrashLoopBackOff diagnosis matrix.
- **Input:** Namespace `prod`, deployment `api`, context `prod-eks`.
- **Prompt:**

```text
Build skill matrix; readonly MCP first; kubectl logs --previous for failing pod.
```

- **Expected result:**

```text
Matrix: step1 context verify CLI; step2 describe via MCP; step3 logs via kubectl --previous
MCP report: pod api-7f8b crash reason Error; last state exit 137
Mitigation proposal: rollout undo blocked until APPROVE
Each line tagged [MCP] or [CLI] in diagnosis.md
```

### Example 2 (Example data (self-written))

- **Task:** Admin MCP in prod skill draft.
- **Input:** cluster-admin kubeconfig for speed.
- **Prompt:**

```text
Use admin MCP so we can fix anything quickly.
```

- **Expected result:**

```text
Admin MCP rejected for prod template; readonly default enforced
Exception protocol required with ticket id and time-bounded readwrite role
Skill revised to kubectl rollout undo only after APPROVE, no delete collection
Security note cites kubernetes-mcp-server access-level docs
```