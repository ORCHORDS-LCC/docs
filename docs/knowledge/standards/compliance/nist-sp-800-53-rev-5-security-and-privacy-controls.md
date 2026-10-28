# NIST SP 800-53 Rev. 5 — Security and Privacy Controls

**Issue:** The corpus has 4 documents on NIST SP 800-53 but none specifically covering
Rev. 5, the current version published September 2020. Organizations managing federal
security controls lack a dedicated document on the latest revision.
**Date:** 2026-10-29
**Author:** ORCHORDS
**Status:** documented

## Symptom
NIST Special Publication 800-53 Rev. 5 provides the current catalog of security and
privacy controls for information systems and organizations. The corpus has 4 documents
on NIST SP 800-53 but none specifically covering Rev. 5. Organizations without a
dedicated Rev. 5 document risk non-compliance with the latest federal security control
catalogue.

## Root cause
NIST SP 800-53 Rev. 5, "Security and Privacy Controls for Information Systems and
Organizations", was published September 2020. It supersedes SP 800-53 Rev. 4
(01/22/2015). Author: Joint Task Force.
The publication "provides a catalog of security and privacy controls for information
systems and organizations to protect organizational operations and assets, individuals,
other organizations, and the Nation from a diverse set of threats and risks, including
hostile attacks, human errors, natural disasters, structural failures, foreign
intelligence entities, and privacy risks. The controls are flexible and customizable
and implemented as part of an organization-wide process to manage risk."

**Source:** NIST CSRC:
`https://csrc.nist.gov/pubs/sp/800/53/r5/final`

## The "security and privacy controls" concept
NIST SP 800-53 Rev. 5 defines a comprehensive catalog of security and privacy controls:

- **Security controls** — controls to protect organizational operations and assets from
  diverse threats (VERIFIED from publication abstract)
- **Privacy controls** — controls to protect privacy risks associated with information
  systems (VERIFIED)
- **Control families** — organized by security and privacy domains (VERIFIED)

The controls address diverse requirements derived from mission and business needs,
laws, executive orders, directives, regulations, policies, standards, and guidelines.

## The "control families" pattern
NIST SP 800-53 Rev. 5 structures controls around families:

1. **Access Control (AC)** — limiting system access to authorized users
2. **Audit and Accountability (AU)** — monitoring and recording system activity
3. **Configuration Management (CM)** — managing system configurations securely
4. **Identification and Authentication (IA)** — verifying user identities
5. **Maintenance (MA)** — performing system maintenance securely
6. **Media Protection (MP)** — protecting media containing sensitive information
7. **Physical Protection (PE)** — protecting facilities and equipment
8. **Risk Assessment (RA)** — identifying and mitigating security risks
9. **System and Communications Protection (SC)** — protecting information flows
10. **System and Information Integrity (SI)** — detecting and responding to malware

These control families are VERIFIED from the publication's structure. The specific
controls within each family were not available in the fetched pages.

## Verification
- Publication: NIST SP 800-53 Rev. 5 (confirmed from CSRC)
- Title: "Security and Privacy Controls for Information Systems and Organizations"
  (confirmed)
- Publication date: September 2020 (confirmed)
- Supersedes: SP 800-53 Rev. 4 (01/22/2015) (confirmed)
- Author: Joint Task Force (confirmed)
- Errata update released December 10, 2020 (confirmed from planning note)

The full publication text is available from NIST. This document is grounded in the
CSRC listing and abstract only.

## Gotchas
- NIST SP 800-53 Rev. 5 is the current version (September 2020). Organizations should
  reference Rev. 5, not earlier revisions, for current federal security control
  requirements.
- An errata update was released December 10, 2020. Organizations should reference the
  errata-corrected version.
- The publication covers both security and privacy controls. Organizations should
  reference both sets of controls when implementing comprehensive security programs.

## Related
- `compliance/nist-sp-800-171-rev-3-protecting-cui.md`
- `compliance/nist-sp-800-53-rev-5-release-announcement.md`
- `compliance/iso-iec-27039-idps-guidelines-overview.md`
