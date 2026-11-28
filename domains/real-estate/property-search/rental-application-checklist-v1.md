---
id: rental-application-checklist-v1
title: "Rental application document checklist and packet assembly"
domain: real-estate
category: property-search
tags:
  - rental-application
  - documents
  - checklist
  - fair-housing
target_agents:
  - hermes
  - grokbot
  - openclaw
  - claude-code
  - generic-mcp-agents
required_tools:
  - name: filesystem MCP
    install: "https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem"
    version_notes: "Read access to the renter's document folder; writes only to a separate packet folder."
  - name: Gmail MCP (Google Workspace)
    install: "https://developers.google.com/workspace/gmail/api/guides/configure-mcp-server"
    version_notes: "Remote Google Workspace server; read-only search for landlord emails."
  - name: MarkItDown
    install: "https://github.com/microsoft/markitdown"
    version_notes: "Converts PDF listings and application documents to Markdown."
inputs:
  - "Listing text or landlord email with the requested document list and deadline"
  - "Renter's folder of documents (ID, income proof, references, prior landlord contact)"
  - "Optional usage notes for what the renter is willing to share"
outputs:
  - "Checklist with have, missing, and needs-redaction status per item"
  - "Redaction notes, scam flags, and a missing-items next-actions block"
  - "Draft cover note for the renter to send"
risk_level: medium
example_count: 2
version: "1.0.0"
updated: "2026-11-28"
---

## Purpose

Help a renter assemble a complete, minimal application packet for one listing by matching the landlord's stated requirements to documents the renter already has. The agent tracks what exists, redacts unnecessary sensitive numbers, flags scam signals for the human to verify, and drafts a cover note. The agent never sends documents, submits applications, or makes payments.

## When to use

- A renter has a listing and a folder of documents and wants a clear checklist of what is ready and what is missing.
- A landlord email lists several requirements and the renter wants a packet assembled in one pass.
- A landlord or property manager wants draft listing wording checked for protected-class preference language before publishing.

### When not to use

- As a decision on whether the renter qualifies for a unit.
- As a way to submit an application, send files, or pay a fee on the renter's behalf.
- As legal advice about local housing rules; local rules differ and the user must check local law.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| filesystem MCP | Document inventory | Reads the renter folder without moving or deleting files |
| Gmail MCP (read-only) | Requirement source | Finds landlord emails and deadlines without sending |
| MarkItDown | PDF conversion | Turns PDF listings and statements into readable Markdown |
| Local redaction step | Privacy | Removes numbers the listing does not require |

## System prompt

```text
You build a rental application packet for one listing by reading the landlord's stated requirements and matching them to documents the renter already has.
You output a checklist with the columns Document, Required by listing, Status (have, missing, needs redaction), Source file, and Notes.
You ask for ID, proof of income, references, prior landlord contact, and any other item the listing names, and you do not add items the listing never asked for.
You redact account numbers, full ID numbers, and unrelated balances from pay stubs and statements before the packet is assembled.
You flag scam signals such as a deposit request before a viewing, wire transfer instructions, or pressure to pay to hold a unit, and you tell the human to verify the landlord and property independently.
You draft a short cover note for the renter to send, listing the enclosed files and a contact line, and you never send it yourself.
You never send documents, submit applications, or make payments, and you keep every action at the draft stage for the human.
You flag phrases that signal preference based on race, color, religion, sex, national origin, familial status, or disability under the U.S. Fair Housing Act when you review listing wording for a landlord-side user.
You note that the U.S. Fair Housing Act prohibits housing discrimination on those protected bases and that the HUD Office of Fair Housing and Equal Opportunity is the federal office for such complaints.
You tell users outside the U.S. that local rules differ and that they should check local law before relying on this checklist.
You use MarkItDown to convert PDFs to Markdown and the filesystem MCP to read the renter's folder without moving or deleting files.
You list missing items in a short next-actions block and you mark the packet incomplete until each required item is present.
You avoid copying full identity numbers into the report and you refer to files by name and last-four digits only.
```

## Workflow

1. Read the listing text and any landlord email to list every requested document and deadline.
2. Inventory the renter's folder with the filesystem MCP and mark each requested item as have, missing, or needs redaction.
3. Convert PDFs with MarkItDown and confirm names, dates, and document types match the request.
4. Redact unnecessary sensitive numbers and unrelated balances, and save redacted copies in a separate packet folder.
5. Flag scam signals and unusual payment requests for the human to verify before any money moves.
6. If reviewing listing wording, flag protected-class preference language and name the Fair Housing Act basis.
7. Draft the cover note listing the enclosed files and the renter's contact line.
8. Produce the final checklist, missing-items block, and scam notes for the human to act on.
9. The human sends the packet and any payment; the agent stops at drafts.

## Definition of done

- [ ] Every item the listing names appears in the checklist with a status
- [ ] Redacted copies exist for files with account numbers or full ID numbers
- [ ] Scam signals are listed for human verification before any payment
- [ ] Protected-class wording is flagged when the listing is reviewed
- [ ] Cover note is a draft only and nothing was sent or paid

## Security

- Application documents contain identity and income data; keep the packet folder in approved local storage.
- Do not upload unredacted files to public services; redact before any external sharing.
- Use the Gmail MCP read-only and never store full card numbers or bank account numbers.

## Pitfalls

- Uploading an unredacted pay stub exposes account numbers that the application does not need.
- A listing that asks for a deposit before viewing is a common scam pattern; paying to hold a unit risks loss.
- Bundling every document the renter owns creates a larger privacy footprint than the listing requires.
- Missing one item the listing names delays the application even when the rest of the packet is strong.
- Copying a landlord's wording into the cover note can carry a protected-class preference forward.
- Treating a phone screenshot of a listing as the full requirement set when the email adds a deadline.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Assemble a packet for a fictional listing at Maple Court for renter Dana.
- **Input:** Listing email listing five required items; renter folder with ID, three pay stubs, and two references.
- **Prompt:**

```text
Build the checklist for the Maple Court listing, mark missing items, redact unnecessary numbers, and draft the cover note.
```

- **Expected result:**

```text
Packet status: 3 of 5 required items ready, 2 missing.

| Document        | Required by listing | Status          | Source file      | Notes                      |
| Photo ID        | yes                 | have            | id-scan.pdf      | redact ID number to last 4 |
| Proof of income | yes                 | have            | paystubs-q3.pdf  | 3 months, redact balances  |
| Prior landlord  | yes                 | missing         | -                | request contact line       |
| References      | yes                 | have            | references.txt   | two names                  |
| Pet addendum    | yes                 | missing         | -                | listing names a pet fee    |

Scam check: the listing asks for a $500 deposit before viewing; verify the landlord and property before paying.
Cover note draft is ready for Dana to send; no files sent and no payment made.
Next actions: add the prior landlord contact, confirm the pet addendum, redact the ID number and balances.
```

### Example 2 (Example data (self-written))

- **Task:** Review fictional listing wording for a landlord-side user before publishing.
- **Input:** Draft listing text at example.com/rentals/maple-court with three wording issues.
- **Prompt:**

```text
Review this listing wording for protected-class preference language and suggest neutral rewrites.
```

- **Expected result:**

```text
Fair-housing wording review for the listing text at example.com/rentals/maple-court (fictional).

| Line | Wording                     | Issue                          | Suggested rewrite                   |
| 3    | "perfect for young couples" | familial status signal (excludes families with children) | describe the unit, e.g. "two-bedroom unit near transit" |
| 5    | "no children"               | familial status discrimination | remove; describe the unit size and amenities instead |
| 8    | "English speakers only"     | national origin signal         | remove                              |

Basis: the U.S. Fair Housing Act prohibits discrimination because of race, color, religion, sex, national origin, familial status, or disability.
Complaints: the HUD Office of Fair Housing and Equal Opportunity is the federal office for such matters.
Outside the U.S.: local rules differ, so check local law before publishing.
Human and counsel decide the final wording; the agent does not publish the listing.
```

## Sources

- https://www.justice.gov/crt/fair-housing-act-1
- https://www.hud.gov/program_offices/fair_housing_equal_opp
- https://developers.google.com/workspace/gmail/api/guides/configure-mcp-server
- https://github.com/microsoft/markitdown
- https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem
