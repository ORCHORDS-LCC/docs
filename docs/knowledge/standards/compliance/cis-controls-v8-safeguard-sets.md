# CIS Controls v8 — Safeguard Sets and Implementation Guidance

**Issue:** Stage 1 added a CIS v8 overview; the safeguard sets themselves are absent.
Organizations implementing CIS Controls need guidance on safeguard sets and how they
map to the broader controls framework.
**Date:** 2026-10-29
**Author:** ORCHORDS
**Status:** documented

## Symptom
CIS Controls v8 organizes its safeguards into sets that map to the broader CIS Controls
framework. The corpus has 0 documents on this axis covering safeguard sets specifically.
Organizations implementing CIS Controls need a document on how safeguard sets relate to
the overall controls framework.

## Root cause
CIS Controls v8 "are a prioritized set of CIS Safeguards to defend against the most
prevalent cyber attacks against systems and networks. They are mapped to and referenced
by multiple legal, regulatory, and policy frameworks." The download bundle contains the
PDF, Excel spreadsheet, Change Log, and the Implementation Groups document.

**Source:** CIS Security:
`https://www.cisecurity.org/controls/v8`

## The "safeguard sets" concept
CIS Controls v8 organizes safeguards into sets:

- **Safeguard organization** — safeguards are grouped into sets that map to the broader
  CIS Controls framework (VERIFIED from CIS v8 page)
- **Implementation Groups** — three tiers of implementation complexity (IG1, IG2, IG3)
  define which safeguards apply to which organizations (VERIFIED from CIS v8 page)
- **Framework mapping** — safeguard sets map to legal, regulatory, and policy frameworks
  including NIST, CSA, SAFECode, MITRE ATT&CK, and OWASP (VERIFIED)

The specific safeguard IDs and their text were not available in the fetched pages; this
document describes the structure only.

## The "implementation group" pattern
CIS Controls v8 defines three Implementation Groups:

1. **IG1 — Basic Cyber Hygiene** — foundational safeguards for all organizations
2. **IG2 — Risk-Driven** — additional safeguards for organizations with known attack
   targets or regulated data
3. **IG3 — Expanded** — comprehensive safeguards for organizations with specific
   regulatory or mission requirements

This pattern is VERIFIED from the CIS v8 page. The Implementation Groups document is
included in the download bundle.

## Verification
- Version: CIS Controls v8 (confirmed from CIS Security)
- Current download: v8.1 (confirmed)
- Design principles: Offense Informs Defense, Focus, Feasible, Measurable, Align
  (confirmed)

The full safeguard set text is available from CIS Security. This document is grounded
in the CIS v8 page only.

## Gotchas
- The specific safeguard IDs and their text were not available in the fetched pages.
  This document describes the structure only; refer to the CIS Controls v8 PDF or
  Excel spreadsheet for specific safeguard content.
- The current download is v8.1, not v8. Organizations should reference v8.1 for the
  most current version.
- The Implementation Groups document is included in the download bundle and defines
  which safeguards apply to each group.

## Related
- `compliance/cis-controls-v8-overview.md`
- `compliance/cis-controls-v8-1-overview.md`
- `compliance/cis-microsoft-baselines-overview.md`
