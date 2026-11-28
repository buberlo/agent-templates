---
id: nda-terms-change-diff-v1
title: "NDA and terms-of-service change diff with lawyer boundary"
domain: legal-admin
category: contracts
tags:
  - nda
  - terms-of-service
  - contract-diff
  - legal-review
target_agents:
  - hermes
  - grokbot
  - claude-code
  - cursor
  - codex
  - generic-mcp-agents
required_tools:
  - name: pandoc
    install: "https://pandoc.org/MANUAL.html"
    version_notes: "Converts docx and HTML versions to Markdown or plain text; no version pinned."
  - name: MarkItDown
    install: "https://github.com/microsoft/markitdown"
    version_notes: "Converts PDF and Office files to Markdown for comparison."
  - name: git diff
    install: "https://git-scm.com/docs/git-diff"
    version_notes: "Use --no-index and --word-diff to compare two paths outside a repository."
  - name: Python difflib
    install: "https://docs.python.org/3/library/difflib.html"
    version_notes: "Standard library unified_diff and HtmlDiff as a fallback when git is unavailable."
  - name: filesystem MCP
    install: "https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem"
    version_notes: "Read-only access to the two versions and the review folder."
inputs:
  - "Old and new versions of an NDA or online terms (docx, pdf, or html)"
  - "Contract type and the clauses the requester cares about most"
  - "Counsel contact and any playbook priorities"
outputs:
  - "Clause-level change table with old and new excerpts and plain-language impact"
  - "List of questions for counsel plus a moved and renumbered section note"
  - "Not-legal-advice notice and a review folder with normalized files and raw diff"
risk_level: high
example_count: 2
version: "1.0.0"
updated: "2026-11-28"
---

## Purpose

Compare two versions of an NDA or online terms, produce a clause-level change table, and phrase every impact as a question for counsel. The output is informational only and is not legal advice; a licensed attorney must review before any response, acceptance, or signature. The agent stops at the lawyer boundary and never accepts terms, signs, or sends anything to a counterparty.

## When to use

- A counterparty sends an updated NDA and the requester needs to see exactly what moved before counsel replies.
- A vendor publishes new online terms and the requester wants a clause table of what changed since the saved copy.
- A renewal arrives with a reissued document and the team needs a fast list of high-priority changes.

### When not to use

- As the only review before signing a regulated or high-value agreement.
- As a substitute for counsel's interpretation of enforceability, law, or risk allocation.
- When one version is a scanned image without a text layer and no OCR step is allowed.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| pandoc | Convert docx/html to Markdown | Normalizes both versions to one comparable text form |
| MarkItDown | Convert pdf/docx to Markdown | Handles PDF text extraction into readable Markdown |
| git diff | Word-level comparison | `--no-index --word-diff` shows edits outside a repository |
| Python difflib | Fallback comparison | `unified_diff` and `HtmlDiff` work without git |
| filesystem MCP | File access | Reads the two versions and writes a separate review folder |

## System prompt

```text
You compare two versions of an NDA or online terms and you never state whether a change is enforceable, lawful, or acceptable to either party.
You convert each version to normalized Markdown with `pandoc input.docx -t markdown -o version.md` or `markitdown input.pdf > version.md` before any comparison runs.
You run `git diff --no-index --word-diff=plain old.md new.md` for word-level changes and fall back to Python `difflib.unified_diff` when git is unavailable.
You split each document on headings, numbered clauses, and paragraph breaks so the change table maps old sections to new sections instead of reporting whole-file noise.
You detect renumbered sections and moved paragraphs by matching clause text with normalized whitespace and you report them as moved, not as removed plus added.
You output a table with the columns Change, Section old, Section new, Old excerpt, New excerpt, Impact, and Question for counsel, keeping excerpts under 40 words.
You describe impact in plain language as a risk area or an open question, and you label every legal conclusion as requiring counsel review.
You flag changed definitions, liability caps, indemnity, confidentiality duration, notice periods, governing law, and term and exit language as high-priority rows.
You never accept terms, click agree, sign, or send anything to a counterparty; you produce a review artifact for the human only.
You keep the original files untouched and you write outputs to a new review folder with a timestamp in the folder name.
You list clauses that exist in only one version and you mark them added or removed rather than as modifications.
You end the report with a short list of questions for counsel and a clear statement that this is not legal advice.
```

## Workflow

1. Confirm the two file paths, the document type (NDA or online terms), and the clauses the requester cares about most.
2. Convert each version to normalized Markdown using pandoc or MarkItDown, and store outputs in a fresh review folder.
3. Normalize whitespace, smart quotes, and heading styles with a small script so formatting does not create false changes.
4. Run `git diff --no-index --word-diff=plain` and save the raw diff next to the normalized files.
5. Build a section index by heading and clause number, then match old sections to new sections by text similarity.
6. Classify each difference as added, removed, modified, or moved, and separate real edits from renumbering.
7. Fill the change table with old and new excerpts, plain-language impact, and a question for counsel.
8. Prioritize rows touching liability, indemnity, confidentiality duration, notice, governing law, and term.
9. Deliver the report with the not-legal-advice notice and hand every decision to the human and counsel.

## Definition of done

- [ ] Both versions are normalized and the raw diff is saved in the review folder
- [ ] Change table covers added, removed, modified, and moved rows with section anchors
- [ ] Renumbered sections and moved paragraphs are flagged as false diffs, not real edits
- [ ] Every row has a plain-language impact and a question for counsel
- [ ] Not-legal-advice notice is present and no acceptance, signature, or send action was taken

## Security

- Contracts may contain pricing, personal data, and negotiation positions; keep the review folder in approved storage.
- Do not upload full documents to public services when policy forbids it; process locally where possible.
- Redact personal data and bank details before quoting excerpts in a report shared beyond counsel.

## Pitfalls

- Renumbered clauses look like full rewrites unless you match by text, producing hundreds of false rows.
- Moved paragraphs show as removed plus added when the diff tool does not track section identity.
- PDF text extraction drops tracked changes, comments, and footnotes, so the diff misses edits present in the docx.
- Word-level diffs bury a single changed "shall" or "may" in noise; review high-impact clauses by hand.
- Comparing a signed scan against a draft mixes OCR errors with real edits and inflates the change count.
- Treating a deleted sentence as harmless when it removed a carve-out that protected the requester.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Compare a fictional mutual NDA v1 against v2 for Acme and list clause changes for counsel.
- **Input:** nda-v1.docx and nda-v2.docx from the counterparty, with liability and confidentiality priorities.
- **Prompt:**

```text
Convert both NDA files to Markdown, diff them at word level, and build the clause change table with questions for counsel.
```

- **Expected result:**

```text
NOT LEGAL ADVICE — counsel review required before any response to the counterparty.

Files: nda-v1.md (1,842 words), nda-v2.md (1,905 words); raw diff saved as nda-v1-v2.worddiff.
Detected 7 changed clauses, 2 moved paragraphs, and 1 renumbered section (old 6 became new 7).

| Change   | Section old | Section new | Old excerpt               | New excerpt              | Impact                       | Question for counsel                 |
| Modified | 4.2         | 4.2         | "survive three (3) years" | "survive five (5) years" | Confidentiality lasts longer | Is five years acceptable for Acme?   |
| Modified | 8.1         | 8.1         | "liability shall not exceed" | "no cap on liability" | Uncapped exposure for Acme   | Can a mutual cap be restored?        |
| Removed  | 5.3         | -           | "reciprocal marking duty" | -                        | Marking duty now one-sided   | Was the removal intentional?         |

Moved: the return-of-materials paragraph moved from 3.4 to 9.2 and is not a real edit.
Questions for counsel: (1) uncapped liability in 8.1, (2) five-year survival, (3) one-sided marking duty.
No terms accepted, no signature, and no message sent; the human and counsel decide next steps.
```

### Example 2 (Example data (self-written))

- **Task:** Compare a saved copy of fictional online terms with a newly published version.
- **Input:** terms-2025-09.html and terms-2026-01.html, both downloaded from example.com.
- **Prompt:**

```text
Normalize both terms pages, diff them, and flag new arbitration, renewal, and data-sharing clauses for counsel.
```

- **Expected result:**

```text
NOT LEGAL ADVICE — counsel review required.

Files: terms-2025-09.html converted with pandoc to terms-old.md (4,310 words); terms-2026-01.html to terms-new.md (4,502 words).
Diff tool: git diff --no-index --word-diff=plain; result 14 modified, 3 added, and 1 removed sections.

| Change   | Section old | Section new | Impact                       | Question for counsel              |
| Added    | -           | 11          | New arbitration clause       | Does it remove court access?      |
| Modified | 7           | 7           | Auto-renew notice 30d to 14d | Less time to cancel               |
| Removed  | 12.4        | -           | Class-action waiver dropped  | Does the old waiver still apply?  |

Renumbered: old section 9 became new section 10, matched by text and flagged as moved, not rewritten.
Added data-sharing paragraph names a new subprocessor category; counsel should confirm any notice duty.
Decision: the human reviews the arbitration and renewal rows first; no terms accepted and nothing sent to the provider.
```

## Sources

- https://pandoc.org/MANUAL.html
- https://github.com/microsoft/markitdown
- https://git-scm.com/docs/git-diff
- https://docs.python.org/3/library/difflib.html
- https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem
