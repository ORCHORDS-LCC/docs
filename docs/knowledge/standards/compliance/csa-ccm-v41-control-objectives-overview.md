# CSA Cloud Controls Matrix (CCM) v4.1 — Control Objectives Overview

**Issue:** The corpus contains zero documents on the 197 control objectives in the CSA CCM v4.1, structured across 17 domains.
**Date:** 2026-10-28
**Author:** ORCHORDS
**Status:** documented

## Symptom
No existing compliance document covers the 197 control objectives in the CSA CCM v4.1, which are structured across 17 domains covering all key aspects of cloud technology.

## Root cause
The CSA CCM v4.1 is a relatively recent version of the framework. The corpus covers ISO/IEC standards, NIST frameworks, and regulatory compliance — the CSA CCM family is not yet represented.

**Source:** CSA Cloud Controls Matrix page:
https://cloudsecurityalliance.org/research/cloud-controls-matrix

## The "17 domains" concept
The CSA CCM v4.1 is composed of 197 control objectives structured in 17 domains covering all key aspects of cloud technology. The domains cover:

- **Application Security:** Controls for securing cloud applications
- **Business Information Management:** Controls for managing business information in the cloud
- **Change Control:** Controls for managing changes to cloud environments
- **Cloud Infrastructure Security:** Controls for securing cloud infrastructure
- **Data Security:** Controls for protecting data in the cloud
- **Encryption and Key Management:** Controls for encryption and key management
- **Governance and Strategy:** Controls for cloud governance and strategy
- **Human Resources:** Controls for human resources in cloud environments
- **Information Security Policy:** Controls for information security policy
- **Legal and Regulatory:** Controls for legal and regulatory compliance
- **Organizational Risk Management:** Controls for organizational risk management
- **Security Incident Management:** Controls for managing security incidents
- **Security and Configuration Management:** Controls for security and configuration management
- **Supply Chain Management:** Controls for supply chain security
- **Threat and Vulnerability Management:** Controls for managing threats and vulnerabilities
- **Use of Cryptography:** Controls for the use of cryptography
- **Vendor Relationship Management:** Controls for managing vendor relationships

## The "shared responsibility" pattern
The CCM clarifies the shared responsibility model between cloud service providers (CSPs) and customers. Each control objective specifies which actor (CSP, customer, or both) is responsible for implementing the control.

Key aspects:
- **CSP responsibilities:** Infrastructure, platform, and service-level controls
- **Customer responsibilities:** Data, identity, and application-level controls
- **Shared responsibilities:** Controls that require collaboration between CSP and customer

## Verification
The CSA CCM page at https://cloudsecurityalliance.org/research/cloud-controls-matrix returns HTTP 200 with the description of CCM v4.1 as composed of 197 control objectives in 17 domains. The full list of control objectives is available through the CCM download (requires CSA membership or license).

## Gotchas
- The CCM v4.1 combines the CCM and CAIQ in one download — this is a significant change from v3.x.
- A CCM license is required for commercial use, customization, or consulting projects. Internal use does not require a license.
- The CCM artifact page (https://cloudsecurityalliance.org/artifacts/cloud-controls-matrix) returned 404 — the controls are available through the main CCM page and CSA membership.

## Related
- `compliance/csa-ccm-v41-overview.md`
- `compliance/csa-ccm-v41-shared-responsibility-model.md`
- `compliance/cis-controls-v8-overview.md`
