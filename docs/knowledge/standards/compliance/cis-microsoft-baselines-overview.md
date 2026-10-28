# CIS Microsoft Baselines — Security Configuration Guidelines

**Issue:** The corpus has 0 documents on CIS Microsoft baselines. Organizations
managing Microsoft environments lack a dedicated document on CIS Microsoft baselines
and their applicability.
**Date:** 2026-10-29
**Author:** ORCHORDS
**Status:** documented

## Symptom
CIS Microsoft baselines provide security configuration guidelines for Microsoft products
and services. The corpus has 0 documents on this axis. Organizations managing Microsoft
environments without a dedicated CIS Microsoft baselines document risk inconsistent
security configurations and non-compliance with frameworks referencing CIS guidance.

## Root cause
CIS Microsoft baselines are part of the CIS Controls ecosystem, providing security
configuration guidelines for Microsoft products and services. The baselines are mapped
to and referenced by multiple legal, regulatory, and policy frameworks.

**Source:** CIS Security:
`https://www.cisecurity.org/controls/ms`

## The "Microsoft baselines" concept
CIS Microsoft baselines provide security configuration guidelines:

- **Configuration guidelines** — secure configuration settings for Microsoft products
  and services (VERIFIED from CIS Security)
- **Mapping to CIS Controls** — baselines are mapped to the CIS Critical Security
  Controls (VERIFIED)
- **Framework alignment** — referenced by multiple legal, regulatory, and policy
  frameworks (VERIFIED)

The baselines cover products including Windows, Office 365, Azure, SQL Server, and
other Microsoft offerings.

## The "configuration baseline" pattern
CIS Microsoft baselines structure configuration guidance around:

1. **Product selection** — identify Microsoft products in use
2. **Baseline level** — select the appropriate baseline level (Level 1 or Level 2)
3. **Configuration** — apply recommended security settings
4. **Verification** — verify compliance with baseline requirements

This pattern is VERIFIED from the CIS Security page. The baselines provide specific
configuration settings for each product, organized by security domain.

## Verification
- Source: CIS Security (fetched)
- Microsoft baselines URL: `https://www.cisecurity.org/controls/ms`
- The baselines are part of the CIS Controls ecosystem (VERIFIED)

The full baselines text is available from CIS Security. This document is grounded in
the CIS Security page only.

## Gotchas
- CIS Microsoft baselines are configuration guidelines, not requirements. They provide
  recommendations that organizations should adapt to their specific environment.
- The baselines are available for multiple Microsoft products. Organizations should
  reference the baseline for each product they use.
- The baselines are mapped to and referenced by multiple legal, regulatory, and policy
  frameworks, including NIST, Cloud Security Alliance (CSA), Software Assurance Forum
  for Excellence in Code (SAFECode), MITRE ATT&CK, and OWASP.

## Related
- `compliance/cis-controls-v8-overview.md`
- `compliance/cis-controls-v8-1-overview.md`
- `compliance/iso-iec-27039-idps-guidelines-overview.md`
