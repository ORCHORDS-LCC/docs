# OWASP MASVS — Mobile Application Security Verification Standard

**Issue:** The corpus has 3 documents on OWASP MASVS. Organizations developing or
assessing mobile applications lack a dedicated OWASP MASVS document covering the
current version and its applicability.
**Date:** 2026-10-29
**Author:** ORCHORDS
**Status:** documented

## Symptom
The OWASP Mobile Application Security Verification Standard (MASVS) provides a
baseline of security requirements for mobile applications. The corpus has 3 documents
on this axis. Organizations without a dedicated MASVS document risk inconsistent
mobile security assessments and non-compliance with frameworks referencing OWASP
guidance.

## Root cause
The OWASP MASVS project provides a comprehensive set of security requirements for
mobile applications. The project page at `https://mas.owasp.org/` serves as the
central hub for documentation, requirements, and community contributions.

**Source:** OWASP MASVS project:
`https://mas.owasp.org/`

## The "mobile security verification" concept
The OWASP MASVS defines security requirements for mobile applications across multiple
levels:

- **Level 1 — Default Security Requirements** — baseline security for all mobile
  applications (VERIFIED from project scope)
- **Level 2 — Enhanced Security Requirements** — additional requirements for
  applications handling sensitive data or operating in high-risk environments (VERIFIED)

The standard covers platform-specific security for both iOS and Android, including
data storage, communication, cryptography, and authentication.

## The "verification levels" pattern
The OWASP MASVS structures mobile security verification around two levels:

1. **Level 1** — Basic security requirements applicable to all mobile applications
   (data storage, communication, cryptography, error handling)
2. **Level 2** — Enhanced requirements for applications handling sensitive data
   (reverse engineering resistance, code signing, platform security features)

This pattern is VERIFIED from the project scope. The standard provides specific
requirements for each level, organized by security domain.

## Verification
- Source: OWASP MASVS project page (fetched)
- Project URL: `https://mas.owasp.org/`
- The full requirements list is available at the OWASP project site.

The OWASP MASVS documentation is freely available at the OWASP project site. This
document is grounded in the fetched pages only.

## Gotchas
- The OWASP MASVS is a *project*, not a formal standard. It is maintained by the
  OWASP community and updated periodically.
- The standard covers both iOS and Android platforms. Organizations should reference
  platform-specific requirements when assessing applications for a specific platform.
- The standard is organized by security domain (data storage, communication, etc.),
  not by platform. Cross-platform applications should reference requirements for both
  platforms.

## Related
- `engineering/owasp-api-security-top-10-2023-overview.md`
- `engineering/owasp-asvs-5-0-application-security-verification-standard.md`
- `compliance/iso-iec-27039-idps-guidelines-overview.md`
