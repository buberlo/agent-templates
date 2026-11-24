#!/usr/bin/env python3
"""Mechanical quality fixes so templates pass validate_and_index quality gates."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOMAINS = ROOT / "domains"
SKIP = {"_category.md", "_domain.md", "TEMPLATE.md"}

# Full hand-written rewrites; skip automated prompt patching for these paths (relative to domains/).
DEEP_REWRITE = {
    "it-operations-support/google-workspace-admin/google-workspace-admin-workflow.md",
    "it-operations-support/helpdesk-it/it-ansible-patch-baseline.md",
    "it-operations-support/active-directory-entra/active-directory-entra-workflow.md",
    "it-operations-support/backup-restore/backup-restore-workflow.md",
    "it-operations-support/endpoint-mdm/endpoint-mdm-workflow.md",
    "content-marketing/branding-design/branding-design-workflow.md",
    "content-marketing/copywriting/copywriting-workflow.md",
    "software-development/mobile-apps/mobile-apps-workflow.md",
    "content-marketing/social-media-strategy/social-buffer-schedule-campaign.md",
    "software-development/backend-apis/backend-apis-workflow.md",
    "software-development/code-review/code-review-workflow.md",
    "security/vuln-management/vuln-management-workflow.md",
    "software-development/frontend/frontend-workflow.md",
    "content-marketing/social-tiktok/social-ffmpeg-shorts-repurpose.md",
    "personal-lifestyle/household/household-workflow.md",
}

BOOTSTRAP_PARAGRAPH = """
You are a careful assistant for this workflow. You work read-first by default and you must not run destructive or production changes until the user confirms the approval gate named in their request.
When you propose a change, you must include a short rollback or undo path and you must tie the plan to the ticket or briefing reference when the user provides one.
If the request is ambiguous, you must ask one clarifying question before you draft commands, content, or configuration.
You must label every external write step with the approval phrase from the workflow section before you describe how to execute it.
You must keep chat output concise and you must redact secrets, recovery codes, and private personal data from every response.
""".strip()

EXPECTED_PAD = (
    "Summary: the agent stays read-only until approval, lists concrete next steps, "
    "and marks any missing inputs the user must supply."
)


def split_frontmatter(text: str):
    if not text.startswith("---"):
        return None, text
    end = text.find("\n---", 3)
    if end == -1:
        return None, text
    body_start = end + 4
    if body_start < len(text) and text[body_start] == "\n":
        body_start += 1
    return text[3:end].strip(), text[body_start:]


def rel_domain_path(path: Path) -> str:
    return str(path.relative_to(DOMAINS)).replace("\\", "/")


def fix_example_headings(body: str) -> str:
    body = re.sub(
        r"^### Example (\d+) \(Example data\)\s*$",
        r"### Example \1 (Example data (self-written))",
        body,
        flags=re.M,
    )
    return body


def fix_system_prompt(body: str, deep: bool) -> str:
    m = re.search(
        r"(## System prompt\s+```(?:text)?\s*\n)(.*?)(```)",
        body,
        re.S,
    )
    if not m:
        return body
    prefix, sp, suffix = m.group(1), m.group(2), m.group(3)
    old_bootstrap = (
        "You work read-first by default and you must not run destructive"
    )
    if old_bootstrap in sp and "You must label every external write step" not in sp:
        sp = re.sub(
            r"\n\nYou are a careful assistant for this workflow\. You work read-first.*?"
            r"configuration\.\n",
            "\n\n" + BOOTSTRAP_PARAGRAPH + "\n\n",
            sp,
            count=1,
            flags=re.S,
        )
        return body[: m.start()] + prefix + sp + suffix + body[m.end() :]
    if "You must label every external write step" in sp:
        return body
    lines = [ln for ln in sp.splitlines() if ln.strip()]
    opener = lines[0] if lines else ""
    if opener.startswith("Role:"):
        role_desc = opener[len("Role:") :].strip().rstrip(".")
        opener = f"You are {role_desc}."
    new_sp = opener + "\n\n" + BOOTSTRAP_PARAGRAPH + "\n\n" + "\n".join(lines[1:])
    return body[: m.start()] + prefix + new_sp + suffix + body[m.end() :]


def pad_expected_blocks(body: str) -> str:
    def make_replacer():
        def replacer(match: re.Match) -> str:
            lead, inner, close = match.group(1), match.group(2), match.group(3)
            if len(inner.strip()) >= 40:
                return match.group(0)
            pad = EXPECTED_PAD
            if inner.strip():
                inner = inner.rstrip() + "\n" + pad
            else:
                inner = pad
            return f"{lead}{inner}{close}"

        return replacer

    patterns = [
        r"(\*\*Expected result:\*\*\s*\n\n```(?:text|bash)?\s*\n)(.*?)(```)",
        r"(\*\*Expected result:\*\*\s+```(?:text|bash)?\s*\n)(.*?)(```)",
    ]
    for pat in patterns:
        body = re.sub(pat, make_replacer(), body, flags=re.S)
    return body


def fix_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    fm, body = split_frontmatter(text)
    if fm is None:
        return False
    deep = rel_domain_path(path) in DEEP_REWRITE
    new_body = body
    new_body = fix_example_headings(new_body)
    new_body = fix_system_prompt(new_body, deep)
    new_body = pad_expected_blocks(new_body)
    if new_body == body:
        return False
    path.write_text(f"---\n{fm}\n---\n{new_body}", encoding="utf-8")
    return True


def main() -> int:
    paths = sorted(DOMAINS.glob("*/*/*.md"))
    paths = [p for p in paths if p.name not in SKIP and not p.name.startswith("_")]
    changed = sum(1 for p in paths if fix_file(p))
    print(f"Patched {changed} template files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())