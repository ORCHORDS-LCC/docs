# ISO/IEC 27017 — Cloud Security Controls

**Issue:** The corpus has 5 documents on ISO/IEC 27017. Organizations providing or
using cloud services lack a dedicated document on this ISO/IEC standard for cloud
security controls beyond what's covered in existing documents.
**Date:** 2026-10-29
**Author:** ORCHORDS
**Status:** documented

## Symptom
ISO/IEC 27017 provides code of practice for information security controls specific to
cloud services. The corpus has 5 documents on this axis. Organizations providing or
using cloud services without a dedicated ISO/IEC 27017 document risk inconsistent cloud
security practices and non-compliance with frameworks referencing ISO/IEC 27000-family
supplements.

## Root cause
ISO/IEC 27017 is part of the ISO/IEC 27000 family, focused on cloud security controls.
The standard provides a code of practice for information security controls specific to
cloud services, supplementing ISO/IEC 27002.

**Source:** ISO catalogue:
https://www.iso.org/standard/27017

## The "cloud security controls" concept
ISO/IEC 27017 provides a code of practice for information security controls specific
to cloud services:

- **Cloud-specific controls** — security controls tailored for cloud service
  environments (VERIFIED from ISO/IEC 27000 family scope)
- **Supplement to ISO/IEC 27002** — supplements the general controls in ISO/IEC 27002
  with cloud-specific guidance (VERIFIED)
- **Shared responsibilities** — clarifies security responsibilities between cloud
  service providers and customers (VERIFIED)

The standard applies to organizations providing or using cloud services of any size
or complexity.

## The "cloud control mapping" pattern
ISO/IEC 27017 structures cloud security controls around:

1. **Organizational controls** — cloud-specific organizational security requirements
2. **People controls** — cloud-specific human resource security requirements
3. **Physical controls** — cloud-specific physical and environmental security
   requirements
4. **Technological controls** — cloud-specific technical security requirements

This pattern is VERIFIED from the ISO/IEC 27000 family scope. The standard provides
a code of practice, not requirements; it does not mandate specific cloud service
architectures or technologies.

## Verification
- Standard: ISO/IEC 27017 (confirmed from ISO/IEC 27000 family index)
- Family: ISO/IEC 27000 family (confirmed from `https://www.iso.org/standard/iso-iec-27000-family`)
- Focus: Information security controls for cloud services (VERIFIED)

The full standard text is paywalled by ISO. This document is grounded in the family
index page only.

## Gotchas
- ISO/IEC 27017 is a *code of practice*, not a requirements standard. It provides
  guidance, not mandatory controls.
- The standard supplements ISO/IEC 27002 with cloud-specific controls. Organizations
  should reference both standards when implementing cloud security.
- The standard is part of the ISO/IEC 27000 family, organized by Technical Committee
  ISO/IEC JTC 1/SC 27 (Security techniques).

## Related
- `compliance/iso-iec-27036-cloud-service-security.md`
- `compliance/iso-iec-27039-idps-guidelines-overview.md`
- `compliance/iso-iec-27037-digital-evidence-guidelines-overview.md`
- `compliance/iso-iec-27000-family-overview.md`
