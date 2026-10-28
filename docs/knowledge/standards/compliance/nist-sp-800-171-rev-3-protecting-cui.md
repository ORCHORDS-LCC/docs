# NIST SP 800-171 Rev. 3 — Protecting Controlled Unclassified Information

**Issue:** The corpus has 4 documents on NIST SP 800-171 but none specifically covering
Rev. 3, the current version published May 2024. Organizations handling Controlled
Unclassified Information (CUI) in nonfederal systems lack a dedicated document on
the latest revision.
**Date:** 2026-10-29
**Author:** ORCHORDS
**Status:** documented

## Symptom
NIST Special Publication 800-171 Rev. 3 provides the current security requirements for
protecting Controlled Unclassified Information (CUI) in nonfederal systems and
organizations. The corpus has 4 documents on NIST SP 800-171 but none specifically
covering Rev. 3. Organizations without a dedicated Rev. 3 document risk non-compliance
with the latest federal security requirements for CUI.

## Root cause
NIST SP 800-171 Rev. 3, "Protecting Controlled Unclassified Information in Nonfederal
Systems and Organizations", was published May 2024. It supersedes SP 800-171 Rev. 2
(01/28/2021). Authors: Ron Ross (NIST), Victoria Pillitteri (NIST).
The publication "provides federal agencies with recommended security requirements for
protecting the confidentiality of CUI when the information is resident in nonfederal
systems and organizations. The requirements apply to components of nonfederal systems
that process, store, or transmit CUI or that provide protection for such components.
The security requirements are intended for use by federal agencies in contractual
vehicles or other agreements established between those agencies and nonfederal
organizations."

**Source:** NIST CSRC:
`https://csrc.nist.gov/pubs/sp/800/171/r3/final`

## The "CUI" concept
Controlled Unclassified Information (CUI) is information that the Federal Government
has designated as requiring safeguarding or dissemination controls. NIST SP 800-171
Rev. 3 covers:

- **CUI protection requirements** — security requirements for protecting CUI in
  nonfederal systems (VERIFIED from publication abstract)
- **Applicability** — applies to components of nonfederal systems that process, store,
  or transmit CUI (VERIFIED)
- **Companion publication** — NIST SP 800-171A provides assessment procedures (VERIFIED)

The publication is grounded in Executive Order 13556, FIPS Publication 199, FIPS
Publication 200, and FISMA.

## The "security requirements" pattern
NIST SP 800-171 Rev. 3 structures security requirements around control families:

1. **Access Control** — limiting system access to authorized users
2. **Awareness and Training** — ensuring personnel understand security responsibilities
3. **Audit and Accountability** — monitoring and recording system activity
4. **Identification and Authentication** — verifying user identities
5. **Configuration Management** — managing system configurations securely
6. **Risk Assessment** — identifying and mitigating security risks

These control families are VERIFIED from the publication's listed families. The
specific requirements within each family were not available in the fetched pages.

## Verification
- Publication: NIST SP 800-171 Rev. 3 (confirmed from CSRC)
- Title: "Protecting Controlled Unclassified Information in Nonfederal Systems and
  Organizations" (confirmed)
- Publication date: May 2024 (confirmed)
- Supersedes: SP 800-171 Rev. 2 (01/28/2021) (confirmed)
- Authors: Ron Ross (NIST), Victoria Pillitteri (NIST) (confirmed)
- HTML version available as of 06/25/2024 (confirmed)

The full publication text is available from NIST. This document is grounded in the
CSRC listing and abstract only.

## Gotchas
- NIST SP 800-171 Rev. 3 is the current version (May 2024). Organizations should
  reference Rev. 3, not earlier revisions, for current CUI protection requirements.
- The publication is intended for use by federal agencies in contractual vehicles or
  other agreements with nonfederal organizations. Nonfederal organizations should
  reference their contractual obligations to determine applicability.
- The companion publication, NIST SP 800-171A, provides assessment procedures and
  should be referenced alongside Rev. 3.

## Related
- `compliance/nist-sp-800-53-rev-5-security-and-privacy-controls.md`
- `compliance/nist-sp-800-53-rev-5-release-announcement.md`
- `compliance/iso-iec-27039-idps-guidelines-overview.md`
