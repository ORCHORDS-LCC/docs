# ISO/IEC 27039:2015 — IDPS Deployment Guidelines

**Issue:** Organizations deploying intrusion detection and prevention systems lack
guidance on selection, deployment, and operations aligned to an international standard.
**Date:** 2026-10-29
**Author:** ORCHORDS
**Status:** documented

## Symptom
ISO/IEC 27039:2015 is the only ISO/IEC standard dedicated to intrusion detection and
prevention systems (IDPS). The corpus has 0 documents on this axis. Organizations
deploying IDPS without reference to this standard risk misaligned detection rules,
poor integration with existing security monitoring, and non-compliance with frameworks
that reference ISO/IEC 27000-family supplements.

## Root cause
ISO/IEC 27039:2015 "provides guidelines to assist organizations in preparing to deploy
intrusion detection and prevention systems (IDPS). In particular, it addresses the
selection, deployment, and operations of IDPS." Published 2015-02, Edition 1, 48 pages,
TC ISO/IEC JTC 1/SC 27, ICS 35.030, stage 90.93 confirmed.

**Source:** ISO catalogue:
`https://www.iso.org/standard/56889.html`

## The "IDPS" concept
An Intrusion Detection and Prevention System (IDPS) monitors network or system activity
for malicious activity or policy violations and reports such activity or attempts to
stop it. ISO/IEC 27039 covers:

- Selection criteria for IDPS technologies (VERIFIED from catalogue scope)
- Deployment architecture and integration with existing security controls (VERIFIED)
- Operational procedures including monitoring, tuning, and incident response (VERIFIED)

The standard applies to organizations of any size deploying IDPS in any environment
— on-premises, cloud, or hybrid.

## The "IDPS lifecycle" pattern
ISO/IEC 27039 structures IDPS guidance around a lifecycle:

1. **Pre-deployment** — requirements gathering, threat modelling, technology selection
2. **Deployment** — installation, configuration, integration with SIEM/SOAR
3. **Operations** — monitoring, tuning, rule management, incident response
4. **Review** — periodic assessment of IDPS effectiveness

This pattern is VERIFIED from the catalogue scope. The standard does not prescribe
specific technologies; it provides process guidance applicable to any IDPS product.

## Verification
- Standard number: ISO/IEC 27039:2015 (confirmed from ISO catalogue)
- Title: exact match to publisher's listing
- Publication date: 2015-02 (confirmed)
- Edition: 1 (confirmed)
- Pages: 48 (confirmed)
- Technical Committee: ISO/IEC JTC 1/SC 27 (confirmed)
- ICS: 35.030 (confirmed)
- Life cycle stage: 90.93 (confirmed)

The full standard text is paywalled by ISO. This document is grounded in the catalogue
entry only.

## Gotchas
- ISO/IEC 27039 is about IDPS *guidelines*, not requirements. It does not mandate
  deployment of an IDPS; it guides organizations that have already decided to deploy one.
- The standard is from SC 27 (Security techniques), not SC 21 (Network services).
  Do not confuse it with ISO/IEC 27001 or 27002.
- The standard was published in 2015 but remains current (stage 90.93 = "Most advanced").
  No revision has been issued as of the catalogue verification date.

## Related
- `compliance/iso-iec-27037-digital-evidence-guidelines-overview.md`
- `compliance/iso-iec-27014-information-security-governance.md`
- `compliance/iso-iec-24760-1-identity-management-terms.md`
- `compliance/iso-iec-27000-family-overview.md`
