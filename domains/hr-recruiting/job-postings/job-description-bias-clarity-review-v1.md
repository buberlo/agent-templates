---
id: job-description-bias-clarity-review-v1
title: "Job description bias and clarity review"
domain: hr-recruiting
category: job-postings
tags:
  - job-descriptions
  - bias-review
  - recruiting
  - inclusive-language
target_agents:
  - hermes
  - grokbot
  - claude-code
  - cursor
  - generic-mcp-agents
required_tools:
  - name: gender-decoder
    install: "https://github.com/lovedaybrooke/gender-decoder"
    version_notes: "Open-source word-stem check based on Gaucher, Friesen and Kay (2011)."
  - name: google_workspace_mcp
    install: "https://github.com/taylorwilsdon/google_workspace_mcp"
    version_notes: "Read-only access to the draft Google Doc."
  - name: filesystem MCP
    install: "https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem"
    version_notes: "Read exported docx or text copies and write the findings file."
inputs:
  - "Draft job description text, Google Doc URL, or exported docx"
  - "Role title, level, and the responsibilities the hiring manager needs"
  - "The team's salary-range policy and the approver for the final posting"
outputs:
  - "Findings table with line reference, excerpt, issue type, and suggested rewrite"
  - "Gender-decoder stem counts and relative proportions with a heuristic caveat"
  - "A short list of policy and clarity questions for the recruiter and legal/HR reviewer"
risk_level: medium
example_count: 2
version: "1.0.0"
updated: "2026-11-28"
---

## Purpose

Review a draft job description for exclusionary or gender-coded wording, unnecessary degree or years requirements, age-coded phrases, unclear responsibilities, and a missing salary range when the team's policy expects one. Output is a findings table with line references and suggested rewrites for the human recruiter and legal/HR reviewer to approve before posting. Word lists are heuristics and not proof of bias.

## When to use

- Before posting a new role, review a draft for exclusionary wording and unclear requirements.
- Refreshing an old posting that may contain age-coded phrases or stale degree requirements.
- Checking whether a draft includes a salary range per the team's stated policy.
- Aligning a hiring manager's draft with the recruiter's inclusive-language guidance.

### When not to use

- As a legal opinion or a guarantee that a posting complies with local law.
- As the only check when a regulator, union agreement, or accessibility rule applies.
- Scoring individual candidates or screening applications.
- Rewriting a role's level or scope without the hiring manager's confirmation.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| gender-decoder | Word-stem check | Open-source implementation of the published masculine and feminine stem lists |
| google_workspace_mcp | Read draft Doc | Read-only access keeps the source document unchanged |
| filesystem MCP | Read local drafts | Handles exported docx or text copies with line numbers |
| Python (optional) | Normalize text | Preserves line references for the findings table |

## System prompt

```text
You review a draft job description for hr-recruiting/job-postings and you report wording findings for a human recruiter and legal/HR reviewer.
You read the draft Google Doc through google_workspace_mcp in read-only mode and you never edit, comment on, or publish the document.
You run the gender-decoder word stems, treating compet, lead, and driven as masculine-coded and collab, support, and related stems as feminine-coded, then report the relative proportion rather than a verdict.
You state that word lists are heuristics and not proof of bias, and that the Gender Decoder study did not include non-binary people.
You flag age-coded phrases such as digital native, recent graduate, young and energetic, or digital savvy with the exact line reference.
You flag degree requirements and years-of-experience requirements that are not tied to a listed responsibility, and you ask the recruiter to justify or remove each one.
You flag wording that shows a preference or discourages applicants based on race, color, religion, sex (including transgender status, sexual orientation, and pregnancy), national origin, age (40 or older), disability, or genetic information and you cite the EEOC prohibited-practices page.
You identify unclear responsibilities, missing scope statements, and vague phrases such as wear many hats, then propose a concrete rewrite for each.
You check whether a salary range is present when the user's policy requires one and you note its absence as a policy finding, not a legal conclusion.
You output a findings table with columns line, excerpt, issue type, why it matters, and suggested rewrite, sorted by severity.
You propose rewrites in neutral, specific language and you keep the original meaning and seniority level unless the recruiter confirms a change.
You send the final table to the recruiter for approval and you do not post the role or change the source document.
```

## Workflow

1. Confirm the role, the draft Doc URL, the team's salary-range policy, and who approves the final version.
2. Open the draft through google_workspace_mcp in read-only mode and copy the text with paragraph or line numbers preserved.
3. Run gender-decoder on the full text and record the masculine-coded and feminine-coded stem counts and relative proportions.
4. Scan for age-coded phrases, unnecessary degree or years requirements, and exclusionary wording with exact line references.
5. Check clarity of responsibilities, scope, and reporting lines, and mark vague or missing sections.
6. Check for a salary range and compare it with the user's stated policy.
7. Build the findings table with line, excerpt, issue type, why it matters, and suggested rewrite, sorted by severity.
8. Send the table to the recruiter and legal/HR reviewer and wait for approval before any posting step.

## Definition of done

- [ ] Findings table covers every flagged line with excerpt, issue type, and suggested rewrite
- [ ] Gender-decoder proportions reported with the heuristic caveat and the study limitation
- [ ] Age-coded and unnecessary requirement findings include exact line references
- [ ] Salary-range check reflects the user's policy without a legal conclusion
- [ ] Draft document remains unchanged and no posting action taken

## Security

- Request read-only Google Workspace scopes and revoke the token after the review.
- Keep draft job text and findings in the recruiter's internal storage, not in public tools.
- Do not add candidate names, employee data, or hiring-manager notes to the findings file.
- Do not post, edit, or share the document; the recruiter and legal/HR reviewer control distribution.
- Store the reviewed version hash or date with the findings so line references stay traceable.

## Pitfalls

- Word-stem counts flip direction in short ads, so a two-paragraph draft can show a strong proportion from only one or two hits.
- Replacing a masculine-coded word with a feminine-coded synonym swaps one heuristic for another without improving clarity.
- Removing a years requirement that the hiring manager actually needs weakens the posting, so confirm each requirement with the recruiter.
- Line numbers shift after edits, so references must be tied to the reviewed version with a date or hash.
- A salary range may be required by local law in some places, but this review only checks the user's policy and does not decide legal duties.
- Age-coded meaning can be subtle, such as fast-paced startup environment implying youth, and a simple word list misses it.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Review a fictional draft for an Acme support lead role before posting.
- **Input:** Google Doc with 34 lines, salary range missing, phrases include digital native, recent graduate, and wear many hats.
- **Prompt:**

```text
Read the Acme support lead draft through google_workspace_mcp in read-only mode. Check gender-decoder stems, age-coded phrases, unnecessary requirements, and the salary-range policy. Return a findings table with line references and suggested rewrites; do not edit the Doc.
```

- **Expected result:**

```text
Findings for Acme support lead draft (reviewed 2026-11-28, 34 lines, read-only)
Word lists are heuristics, not proof of bias; the Gender Decoder study did not include non-binary people.

| Line | Excerpt | Issue type | Why it matters | Suggested rewrite |
| 4 | digital native | age-coded | implies a preferred age | comfortable with common support tools |
| 9 | recent graduate | age-coded | discourages older applicants | early-career or equivalent experience |
| 12 | degree required | unnecessary requirement | not tied to any listed duty | remove, or state the specific knowledge needed |
| 18 | wear many hats | unclear scope | hides the real workload | list the three main duties |
| 27 | fast-paced startup environment | age-coded | can imply youth | describe the actual pace and on-call load |
| 34 | no salary range | policy gap | conflicts with the team policy | add the approved range from the recruiter |

Gender-decoder: 7 masculine-coded stems, 3 feminine-coded stems, relative proportion 70/30.
Next step: recruiter confirms each rewrite and legal/HR approves before posting; no Doc changes made.
```

### Example 2 (Example data (self-written))

- **Task:** Review a fictional operations manager draft that already includes a salary range and check clarity only.
- **Input:** Exported docx with 22 lines; salary range present; responsibilities vague in two sections.
- **Prompt:**

```text
Read /drafts/ops-manager.docx. The salary range is present, so skip the policy check. Flag only unclear responsibilities and any exclusionary wording, then propose neutral rewrites with line references.
```

- **Expected result:**

```text
Findings for operations manager draft (reviewed 2026-11-28, 22 lines, docx copy)

| Line | Excerpt | Issue type | Why it matters | Suggested rewrite |
| 6 | help with various projects | unclear responsibility | no measurable scope | own the quarterly vendor review and the weekly backlog triage |
| 11 | support the team as needed | unclear responsibility | open-ended duty | provide scheduling and onboarding support for 12 staff |
| 15 | driven self-starter | gender-coded heuristic | masculine-coded stem, weak evidence | works independently on assigned deadlines |
| 19 | culture fit | exclusionary wording | can hide bias in hiring | shared examples of collaboration and feedback |

Salary range: present on line 21, so no policy finding recorded.
Gender-decoder: 2 masculine-coded stems, 1 feminine-coded stem; sample too small for a stable proportion.
Next step: recruiter confirms line 6 and line 11 scope with the hiring manager; legal/HR approval still required.
No document edits and no posting action taken.
```

## Sources

- https://github.com/lovedaybrooke/gender-decoder
- https://gender-decoder.katmatfield.com/about (based on Gaucher, Friesen and Kay, 2011, Journal of Personality and Social Psychology 101(1), 109-128)
- https://www.eeoc.gov/prohibited-employment-policiespractices
- https://github.com/taylorwilsdon/google_workspace_mcp
