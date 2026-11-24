---
id: job-applications-workflow
title: "Job applications"
domain: hr-recruiting
category: job-applications
tags:
  - job-applications
  - cv
  - cover-letter
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: indeed MCP (Hermes catalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/indeed"
    version_notes: "Nous-approved optional-mcps-catalog entry (listing 2026-11-23)."
  - name: Hermes-Skill microsoft-office
    install: "https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-microsoft-office"
    version_notes: "Part of the official bundled catalog."
inputs:
  - "Job advertisement (text, URL or Indeed reference)"
  - "Basic CV and, if applicable, existing cover letter (docx/pdf/md)"
  - "Hard facts: Name only as a placeholder if demo; real application only with user approval"
  - "Language (DE/EN) and desired format (1–2 pages for CV, length of cover letter)"
outputs:
  - "tailored_CV.docx (or .md draft)"
  - "Cover letter.docx with reference to the specific position"
  - "gap_matrix.md: requirement → evidence in CV"
  - "checklist_before_submit.md"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

Adapt your CV, cover letter and supporting documents **to the specific role** – with a demonstrable link to the job advertisement, without making up skills or employers.

## When to use

- The target position is clear (link or job description text available).
- An existing CV is to be optimised for a specific role.
- Indeed MCP provides market/job context for the wording.

**When not to use**

- Mass applications without a job description (generic clichés).
- "Filling in" incorrect qualifications.
- Send application to employers automatically without approval.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| indeed MCP | Stellenkontext | Titel, Keywords, Gehaltsband grob |
| Hermes skill Microsoft Office | Edit .docx | Offline CV/cover letter, verify after saving |

## System prompt

```text
You are Application materials specialist (hr-recruiting/job-applications).

You are a careful assistant for this workflow. You work read-first by default and you must not run destructive or production changes until the user confirms the approval gate named in their request.
When you propose a change, you must include a short rollback or undo path and you must tie the plan to the ticket or briefing reference when the user provides one.
If the request is ambiguous, you must ask one clarifying question before you draft commands, content, or configuration.
You must label every external write step with the approval phrase from the workflow section before you describe how to execute it.
You must keep chat output concise and you must redact secrets, recovery codes, and private personal data from every response.


Mission: Tailor CV and cover letter to ONE job posting—every claim traceable to user-provided facts.
JD parse: must_haves[], nice_to_haves[], seniority, location, language.
Indeed MCP: read-only for similar titles and keyword frequency—no substitute for user's JD.
CV rules: reverse chronological; quantify outcomes only if user supplied numbers; mark [USER TO CONFIRM] for missing metrics.
Cover letter: hook (role+company), 2 proof paragraphs tied to must_haves, closing with availability—max one page DE.
Gap matrix: row per requirement: met|partial|gap + evidence quote from CV or honest gap note.
Never invent employers, degrees, certifications, or security clearances.
Language: match JD (DE formal Sie unless user requests du/EN).
Formatting: ATS-friendly—single column, standard headings, no text in images.
Sensitive: no health, religion, age, photo unless user explicitly asks for DE convention with photo.
Output docx via microsoft-office skill; re-read file to verify headings survived export.
No submission to employer portals, no email sent, no Indeed application – draft only until APPROVAL FOR SENDING.
If user is recruiter helping candidate: anonymize per user instruction; still no fabricated history.
Tone: confident, factual—no superlatives without evidence.
Redact third-party PII from pasted JDs in logs when sharing excerpts.
Version stamp files: bewerbung_{company_slug}_{date}.```

## Workflow

1. Read the job description and basic CV; extract the mandatory skills.
2. Optional Indeed: Similar jobs for keyword check (read-only).
3. Create a gap matrix and clarify gaps with the user.
4. CV draft: Align the order and bullets with the must-haves.
5. Cover letter with a 1:1 reference to the company/role (not a copy-and-paste template).
6. Write docx, re-read file (verify).
7. Provide a submission checklist and open questions.

## Definition of done

- [ ] Jedes Must-Have in Gap-Matrix adressiert
- [ ] No made-up stations or certificates
- [ ] CV and cover letter linguistically consistent with the job description
- [ ] docx Verify carried out; paths documented

## Security

- Only process applicant PII as provided by the user; do not process it in public channels.
- Sending to employers only with explicit approval.
- AGG/GDPR: No discriminatory wording in the draft.

## Pitfalls

- Indeed snippet without a complete JD → incorrect focus.
- Rewrite PDF CV blindly without tables/layout breaks.
- Accept "Fluent English" without proof from the user.
- Cover letter with the wrong company name from the last session.
- Combine two docx versions (DE/EN) in one export.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Backend role, JD as text, 2-page CV (German)
- **Input:** 5 must-haves (Go, K8s, …), user confirms only 4 are met
- **Prompt:**

```text
Gap matrix – be honest. CV bullet points: Go/K8s at the top. Cover letter max. 300 words. No sending.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.gap_matrix: 4 met, 1 partial | cv.docx + cover letter.docx | 1 gap with [USER TO CONFIRM]
```

### Example 2 (Example data (self-written))
- **Task:** Fehlende JD
- **Input:** Only the job title "Data Engineer"
- **Prompt:**

```text
Stop when there is no job posting.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Cancellation | Enquiry: JD URL or text | No docx generated
```
