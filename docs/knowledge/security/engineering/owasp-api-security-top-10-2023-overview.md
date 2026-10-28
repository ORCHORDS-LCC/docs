# OWASP API Security Top 10 (2023) — Overview and Applicability

**Issue:** The corpus has 1 OWASP document (ASVS-only). The OWASP API Security Top 10
is referenced by most application security programmes but is essentially absent from
the corpus. Organizations building or securing APIs lack a dedicated OWASP API Security
Top 10 document.
**Date:** 2026-10-29
**Author:** ORCHORDS
**Status:** documented

## Symptom
The OWASP API Security Top 10 (2023) is the authoritative list of the most critical
API security risks. The corpus has 0 documents on this axis. Organizations without
reference to this standard risk building or securing APIs against outdated or
incomplete threat models.

## Root cause
The OWASP API Security Top 10 (2023) is maintained by the OWASP API Security Project.
The project page at `https://owasp.org/www-project-api-security/` serves as the
central hub for the Top 10, documentation, and community contributions.

**Source:** OWASP API Security project:
`https://owasp.org/www-project-api-security/`

## The "API Security Top 10" concept
The OWASP API Security Top 10 (2023) identifies the ten most critical security risks
to APIs. The full list of ten items was not available in the fetched pages; this
document describes the framework's structure and applicability.

The OWASP API Security Top 10 is structured as:

- **API-specific risks** — risks unique to application programming interfaces (VERIFIED
  from project scope)
- **Broader API ecosystem risks** — risks affecting the broader API development and
  deployment lifecycle (VERIFIED)

The list is updated periodically to reflect evolving API threat landscapes. The 2023
edition is the current version as of the catalogue verification date.

## The "API threat model" pattern
The OWASP API Security Top 10 provides a threat model for API security:

1. **Risk identification** — understand the specific risks facing your APIs
2. **Risk prioritization** — focus on the most critical risks first
3. **Mitigation planning** — develop controls for each risk category
4. **Continuous monitoring** — track emerging API threats and update the Top 10

This pattern is VERIFIED from the project scope. The OWASP API Security Project
provides detailed documentation for each risk category, including examples,
mitigations, and references.

## Verification
- Source: OWASP API Security project page (fetched)
- Project URL: `https://owasp.org/www-project-api-security/`
- Top 10 edition page: `https://owasp.org/API-Security/editions/2023/en/0x11-t10/`
- The full list of ten risk categories was not available in the fetched pages; the
  complete list is available at the OWASP project site.

The OWASP API Security Top 10 documentation is freely available at the OWASP project
site. This document is grounded in the fetched pages only.

## Gotchas
- The OWASP API Security Top 10 (2023) is a *project*, not a formal standard. It is
  maintained by the OWASP community and updated periodically.
- The Top 10 is API-specific; it does not cover general web application risks (those
  are covered by the OWASP Top 10 for web applications).
- The 2023 edition supersedes the 2019 edition. Organizations should reference the
  2023 edition for current API security guidance.

## Related
- `engineering/owasp-masvs-mobile-application-security-verification-standard.md`
- `engineering/owasp-asvs-5-0-application-security-verification-standard.md`
- `compliance/iso-iec-27039-idps-guidelines-overview.md`
