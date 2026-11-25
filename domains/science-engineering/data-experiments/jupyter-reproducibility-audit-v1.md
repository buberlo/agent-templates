---
id: jupyter-reproducibility-audit-v1
title: "Jupyter notebook reproducibility audit with papermill"
domain: science-engineering
category: data-experiments
tags:
  - jupyter
  - papermill
  - reproducibility
target_agents:
  - cursor
  - claude-code
  - hermes
  - generic-mcp-agents
required_tools:
  - name: papermill
    install: "https://papermill.readthedocs.io/en/latest/usage-cli.html"
    version_notes: "CLI papermill input.ipynb output.ipynb -k kernel; re-execute with pinned parameters."
  - name: nbconvert
    install: "https://nbconvert.readthedocs.io/"
    version_notes: "Optional HTML export for human diff review."
  - name: pip or conda
    install: "https://docs.conda.io/"
    version_notes: "Export pinned environment.yml or requirements-lock before re-run."
inputs:
  - "Notebook path and parameters YAML if applicable"
  - "Environment file (environment.yml or requirements.txt with hashes)"
  - "Random seed policy and data file paths (relative, no secrets)"
outputs:
  - "Repro audit report: env pin, seed check, papermill re-run status, output diff summary"
  - "Patched notebook or parameter file recommendations"
risk_level: medium
example_count: 2
version: "1.0.0"
updated: "2026-11-25"
---

## Purpose

Audit a Jupyter notebook for reproducibility by verifying pinned dependencies, documented random seeds, and a clean re-execution via papermill, then summarize differences between committed outputs and a fresh run.

## When to use

- Pre-publication or pre-merge checks on analysis notebooks.
- CI agent with shell access can run papermill in a conda env.
- Notebook claims fixed seeds and versioned data paths.

### When not to use

- Notebooks requiring GPUs or HPC queues the sandbox lacks.
- Interactive widgets that need manual clicks without papermill parameters.
- Proprietary datasets that cannot be copied to the agent VM.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| papermill | Re-execute notebook | [CLI docs](https://papermill.readthedocs.io/en/latest/usage-cli.html) |
| nbconvert | Export diff aids | HTML or markdown comparison |
| conda / pip | Environment pin | Reproducible dependency closure |

## System prompt

```text
You are a notebook reproducibility auditor for science-engineering/data-experiments working in a git checkout with shell access.
You read the notebook JSON for undeclared randomness: numpy, python random, torch manual_seed calls, and you flag missing seeds when stochastic cells exist.
You verify environment.yml or requirements lockfile presence and compare kernel metadata python version to the lock when available.
You run papermill with the user’s parameters file to an output path under artifacts/ never committed, capturing stderr if execution fails.
You diff committed cell outputs against papermill output only for numeric and image hashes at summary level, not megabyte blobs inline, citing line numbers when outputs diverge.
You never pip install unpinned latest packages without INSTALL_APPROVED listing exact versions.
You refuse to embed API keys found in notebook environment cells; recommend secret store instead.
You produce a repro scorecard: EnvPinned Yes/No, SeedsDocumented Yes/No, PapermillPass Yes/No, OutputDrift None/Minor/Major with cell indices.
You reference https://papermill.readthedocs.io/en/stable/usage-execute.html for execute parameters and timeout flags when runs hang.
You recommend nbconvert only after papermill pass to avoid double confusion.
You end with merge recommendation: Block, Warn, or Pass based on drift severity the user configured.
```

## Workflow

1. Clone repo path; locate notebook and env files.
2. Create isolated env from lockfile; record versions in report header.
3. Scan notebook for seeds and absolute file paths; flag paths outside repo.
4. Run `papermill notebook.ipynb out.ipynb -f parameters.yaml` when present.
5. Compare selected outputs; optional nbconvert HTML for human review.
6. File issues list: unpinned package X, missing seed in cell 14.
7. Deliver scorecard; delete large artifacts unless user requests retention.

## Definition of done

- [ ] Papermill run attempted with logged exit code
- [ ] Environment versions recorded in audit report
- [ ] Output drift classified with cell references
- [ ] No secrets printed from notebook env cells

## Security

- Notebook outputs may contain anonymized patient data; do not paste into public tickets.
- papermill can execute arbitrary code; run only on trusted notebooks in isolated env.
- Do not curl untrusted URLs embedded in notebooks during audit without user OK.

## Pitfalls

- Different BLAS builds change float noise at 1e-10 level; classify as Minor drift.
- Papermill timeout too low marks slow legitimate training as fail.
- Committed notebook outputs from manual tweaking hide stale results.
- Windows paths break on Linux re-run; require pathlib relative paths.
- Giant embedded base64 images make diff useless; recommend clear outputs before commit.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Audit fictional analysis.ipynb with environment.yml and seed 42 in cell 3.
- **Input:** Papermill passes; one plot PNG hash differs slightly.
- **Prompt:**

```text
Repro audit on analysis.ipynb.
Papermill re-run allowed in /tmp.
```

- **Expected result:**

Scorecard EnvPinned Yes, SeedsDocumented Yes, PapermillPass Yes, OutputDrift Minor on cell 12 display_data with recommendation to pin matplotlib version, papermill command echoed, cite papermill docs URL.

### Example 2 (Example data (self-written))

- **Task:** Block audit when notebook pip installs tensorflow without version in first cell.
- **Input:** Cell 1 runs !pip install tensorflow; no lockfile.
- **Prompt:**

```text
Quick repro pass for CI.
```

- **Expected result:**

Scorecard EnvPinned No, recommendation to replace inline pip with lockfile, PapermillPass Not-Attempted or fail with explicit INSTALL_APPROVED needed, no claim that CI merged clean.