# CSA Cloud Controls Matrix (CCM) v4.1 — Overview

**Issue:** The corpus contains zero documents on the CSA Cloud Controls Matrix (CCM) v4.1, the de-facto standard for cloud security assurance and compliance.
**Date:** 2026-10-28
**Author:** ORCHORDS
**Status:** documented

## Symptom
No existing compliance document covers the CSA Cloud Controls Matrix (CCM) v4.1, which is composed of 197 control objectives structured in 17 domains covering all key aspects of cloud technology.

## Root cause
The CSA CCM v4.1 is a relatively recent version of the framework. The corpus covers ISO/IEC standards, NIST frameworks, and regulatory compliance — the CSA CCM family is not yet represented.

**Source:** CSA Cloud Controls Matrix page:
https://cloudsecurityalliance.org/research/cloud-controls-matrix

## The "CCM v4.1" concept
The CSA Cloud Controls Matrix (CCM) is a cybersecurity control framework for cloud computing. It is composed of 197 control objectives that are structured in 17 domains covering all key aspects of cloud technology.

Key aspects from the CSA page:
- **Version:** 4.1 (latest)
- **Control objectives:** 197
- **Domains:** 17
- **Status:** Active (de-facto standard for cloud security assurance and compliance)
- **Combined with:** CAIQ (Cloud Controls Assurance Questionnaire)

## The "de-facto standard" pattern
The CCM is described as: "a cybersecurity control framework for cloud computing. It is composed of 197 control objectives that are structured in 17 domains covering all key aspects of cloud technology. It can be used as a tool for the systematic assessment of a cloud implementation, and provides guidance on which security controls should be implemented by which actor within the cloud supply chain. The controls framework is aligned to the CSA Security Guidance for Cloud Computing, and is considered a de-facto standard for cloud security assurance and compliance."

Key benefits of the CCM:
- Map controls for multiple standards and regulations (ISO, NIST, PCI, DSS)
- Assess cloud providers with the CAIQ (built into CCM v4.1)
- Clarify the shared responsibility model between CSPs and customers
- Submit to the STAR Registry for self-assessment

## Verification
The CSA CCM page at https://cloudsecurityalliance.org/research/cloud-controls-matrix returns HTTP 200 with the description of CCM v4.1 as composed of 197 control objectives in 17 domains. The CSA guidance page at https://cloudsecurityalliance.org/guidance provides additional context.

## Gotchas
- CCM v4.1 combines the CCM and CAIQ in one download — this is a significant change from v3.x.
- The CCM artifact page (https://cloudsecurityalliance.org/artifacts/cloud-controls-matrix) returned 404 — the controls are available through the main CCM page and CSA membership.
- A CCM license is required for commercial use, customization, or consulting projects. Internal use does not require a license.

## Related
- `compliance/csa-ccm-v41-control-objectives-overview.md`
- `compliance/csa-ccm-v41-shared-responsibility-model.md`
- `compliance/cis-controls-v8-overview.md`
