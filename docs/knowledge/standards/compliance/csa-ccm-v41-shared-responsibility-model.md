# CSA Cloud Controls Matrix (CCM) v4.1 — Shared Responsibility Model

**Issue:** The corpus contains zero documents on the CSA CCM v4.1 shared responsibility model, which clarifies which controls apply to CSPs versus customers.
**Date:** 2026-10-28
**Author:** ORCHORDS
**Status:** documented

## Symptom
No existing compliance document covers the CSA CCM v4.1 shared responsibility model, which specifies which of the 197 control objectives apply to cloud service providers (CSPs) versus customers.

## Root cause
The CSA CCM v4.1 is a relatively recent version of the framework. The corpus covers ISO/IEC standards, NIST frameworks, and regulatory compliance — the CSA CCM family is not yet represented.

**Source:** CSA Cloud Controls Matrix page:
https://cloudsecurityalliance.org/research/cloud-controls-matrix

## The "shared responsibility" concept
The CCM clarifies the shared responsibility model between cloud service providers (CSPs) and customers. Each control objective specifies which actor (CSP, customer, or both) is responsible for implementing the control.

Key aspects from the CSA page:
- **Version:** 4.1 (latest)
- **Control objectives:** 197 across 17 domains
- **Combined with:** CAIQ (Cloud Controls Assurance Questionnaire)
- **Status:** De-facto standard for cloud security assurance and compliance

## The "actor mapping" pattern
The CCM maps each control objective to one or more actors:
- **CSP (Cloud Service Provider):** Responsible for infrastructure, platform, and service-level controls
- **Customer:** Responsible for data, identity, and application-level controls
- **Both (Shared):** Controls that require collaboration between CSP and customer

This pattern is critical for:
- Understanding security boundaries in cloud deployments
- Conducting security assessments of cloud implementations
- Preparing for audits and compliance reviews
- Negotiating security requirements with CSPs

## Verification
The CSA CCM page at https://cloudsecurityalliance.org/research/cloud-controls-matrix returns HTTP 200 with the description of CCM v4.1 as composed of 197 control objectives in 17 domains. The full actor mapping is available through the CCM download (requires CSA membership or license).

## Gotchas
- The CCM v4.1 combines the CCM and CAIQ in one download — this is a significant change from v3.x.
- A CCM license is required for commercial use, customization, or consulting projects. Internal use does not require a license.
- The CCM artifact page (https://cloudsecurityalliance.org/artifacts/cloud-controls-matrix) returned 404 — the controls are available through the main CCM page and CSA membership.

## Related
- `compliance/csa-ccm-v41-overview.md`
- `compliance/csa-ccm-v41-control-objectives-overview.md`
- `compliance/cis-controls-v8-overview.md`
