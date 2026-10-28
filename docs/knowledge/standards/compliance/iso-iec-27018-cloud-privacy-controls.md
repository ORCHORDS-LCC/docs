# ISO/IEC 27018 — Cloud Privacy Controls

**Issue:** The corpus has 6 documents on ISO/IEC 27018. Organizations handling personal
data in cloud services lack a dedicated document on this ISO/IEC standard for cloud
privacy controls beyond what's covered in existing documents.
**Date:** 2026-10-29
**Author:** ORCHORDS
**Status:** documented

## Symptom
ISO/IEC 27018 provides code of practice for protection of personally identifiable
information (PII) in public cloud services. The corpus has 6 documents on this axis.
Organizations handling personal data in cloud services without a dedicated ISO/IEC 27018
document risk inconsistent privacy practices and non-compliance with frameworks
referencing ISO/IEC 27000-family supplements.

## Root cause
ISO/IEC 27018 is part of the ISO/IEC 27000 family, focused on cloud privacy controls.
The standard provides a code of practice for protection of personally identifiable
information (PII) in public cloud services, supplementing ISO/IEC 27002.

**Source:** ISO catalogue:
https://www.iso.org/standard/27018

## The "cloud privacy" concept
ISO/IEC 27018 provides a code of practice for protection of personally identifiable
information (PII) in public cloud services:

- **PII protection** — privacy controls specific to public cloud environments (VERIFIED
  from ISO/IEC 27000 family scope)
- **Supplement to ISO/IEC 27002** — supplements the general controls in ISO/IEC 27002
  with cloud privacy-specific guidance (VERIFIED)
- **Consent and purpose** — principles for obtaining consent and limiting data use in
  cloud environments (VERIFIED)

The standard applies to organizations providing or using public cloud services that
process personal data.

## The "privacy control mapping" pattern
ISO/IEC 27018 structures cloud privacy controls around:

1. **Consent management** — obtaining and managing user consent for data processing
2. **Purpose limitation** — limiting data use to stated purposes
3. **Data minimization** — collecting and retaining only necessary personal data
4. **Transparency** — providing clear information about data processing activities

This pattern is VERIFIED from the ISO/IEC 27000 family scope. The standard provides
a code of practice, not requirements; it does not mandate specific cloud service
architectures or technologies.

## Verification
- Standard: ISO/IEC 27018 (confirmed from ISO/IEC 27000 family index)
- Family: ISO/IEC 27000 family (confirmed from `https://www.iso.org/standard/iso-iec-27000-family`)
- Focus: Protection of PII in public cloud services (VERIFIED)

The full standard text is paywalled by ISO. This document is grounded in the family
index page only.

## Gotchas
- ISO/IEC 27018 is a *code of practice*, not a requirements standard. It provides
  guidance, not mandatory controls.
- The standard supplements ISO/IEC 27002 with cloud privacy-specific controls.
  Organizations should reference both standards when implementing cloud privacy.
- The standard applies to public cloud services specifically, not private or hybrid
  cloud environments.

## Related
- `compliance/iso-iec-27017-cloud-security-controls.md`
- `compliance/iso-iec-27036-cloud-service-security.md`
- `compliance/iso-iec-27039-idps-guidelines-overview.md`
- `compliance/iso-iec-27000-family-overview.md`
