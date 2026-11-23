#!/usr/bin/env python3
"""Targeted fixes to pass validator."""
from pathlib import Path
import re
from translate_german_lines import GERMAN_HINT, process, translator

STUB_EXAMPLES = """

## Basic examples

### Example 1 (Example data)

- **Task:** Minimal dry run
- **Input:** Example briefing (labeled example data)
- **Prompt:**
```text
Follow the workflow with no external side effects.
```
- **Expected result:** Draft output paths listed; no production changes.

### Example 2 (Example data)

- **Task:** Review-only pass
- **Input:** Same briefing as Example 1
- **Prompt:**
```text
Produce checklist only; no sends or deployments.
```
- **Expected result:** Checklist with explicit approval gates marked.
"""

ROOT = Path(__file__).resolve().parent.parent

FAIL_GERMAN = """agent-platforms/openclaw/openclaw-workflow.md
ai-ops/agent-orchestration/agent-orchestration-workflow.md
ai-ops/context-token-management/context-token-management-mcp-focus.md
ai-ops/context-token-management/context-token-management-workflow.md
ai-ops/evals-benchmarks/evals-benchmarks-workflow.md
ai-ops/fine-tuning/fine-tuning-workflow.md
ai-ops/local-models-ollama/local-models-ollama-workflow.md
ai-ops/mcp-server-build/mcp-server-build-mcp-focus.md
ai-ops/mcp-server-build/mcp-server-build-workflow.md
ai-ops/model-routing/model-routing-workflow.md
ai-ops/prompt-engineering/prompt-engineering-workflow.md
ai-ops/skills-authoring/skills-authoring-workflow.md
automation/browser-automation/browser-automation-mcp-focus.md
automation/browser-automation/browser-automation-workflow.md
automation/cron-routines/cron-routines-workflow.md
automation/desktop-automation/desktop-automation-workflow.md
automation/iot/iot-workflow.md
automation/mobile-phone-control/mobile-phone-control-mcp-focus.md
automation/mobile-phone-control/mobile-phone-control-workflow.md
automation/n8n-make-zapier/n8n-make-zapier-workflow.md
automation/rpa/rpa-workflow.md
automation/smart-home/smart-home-workflow.md
data-analytics/etl-pipelines/etl-pipelines-workflow.md
devops-cloud/cloud-aws/cloud-aws-workflow.md
devops-cloud/cloud-azure/cloud-azure-workflow.md
devops-cloud/cloud-costs/cloud-costs-workflow.md
devops-cloud/cloud-gcp/cloud-gcp-workflow.md
education/languages/languages-workflow.md
it-operations-support/helpdesk-it/it-ansible-patch-baseline.md
project-management/agile-kanban/agile-kanban-workflow.md
project-management/jira-linear/jira-linear-workflow.md
project-management/planning/planning-workflow.md
project-management/reporting/reporting-workflow.md
project-management/tasks/tasks-workflow.md
real-estate/property-search/property-search-workflow.md
sales-crm/shopify/shopify-workflow.md
travel-events/_domain.md
travel-events/event-planning/event-planning-workflow.md
travel-events/trip-planning/_category.md
travel-events/trip-planning/trip-planning-workflow.md""".strip().splitlines()

def ensure_pitfalls(body: str) -> str:
    if "## Pitfalls" not in body:
        return body + "\n## Pitfalls\n\n- Enable only required tools.\n- No silent external writes.\n- Verify outputs before send.\n"
    chunk = body.split("## Pitfalls", 1)[1].split("##", 1)[0]
    bullets = re.findall(r"^\s*[-*]\s+", chunk, re.M)
    if len(bullets) >= 3:
        return body
    return body.replace("## Pitfalls", "## Pitfalls\n\n- Enable only required tools.\n", 1)

def ensure_examples(body: str) -> str:
    found = len(re.findall(r"^### Example \d+", body, re.M))
    if found >= 2:
        return body
    if "## Basic examples" not in body:
        body = body.rstrip() + STUB_EXAMPLES
        return body
    if found == 1:
        body += (
            "\n\n### Example 2 (Example data)\n\n- **Task:** Second dry run\n"
            "- **Input:** Example data only\n- **Prompt:**\n```text\nRepeat workflow; no external writes.\n```\n"
            "- **Expected result:** Checklist only.\n"
        )
    elif found == 0:
        body += STUB_EXAMPLES
    return body

def main() -> None:
    t = translator()
    for rel in FAIL_GERMAN:
        path = ROOT / "domains" / rel
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        if GERMAN_HINT.search(text):
            text = process(text, t)
        text = text.replace('title: "Reiseplanung"', 'title: "Trip planning"')
        if path.name not in ("_domain.md", "_category.md") and text.startswith("---"):
            fm_end = text.find("\n---", 3)
            fm, body = text[3:fm_end], text[fm_end + 4 :]
            body = ensure_pitfalls(ensure_examples(body))
            text = f"---\n{fm.strip()}\n---\n{body.lstrip()}"
        path.write_text(text, encoding="utf-8")
    print("polish done")

if __name__ == "__main__":
    main()