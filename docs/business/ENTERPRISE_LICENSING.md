# Enterprise Licensing

**Project:** ORCHORDS  
**Owner:** ORCHORDS (Business Development)  
**Reviewers:** ORCHORDS (Legal), ORCHORDS (CTO), ORCHORDS (CEO)  
**ISO Standards:** ISO/IEC 19770-2:2015 (software asset management), ISO/IEC 12207:2017 (distribution)  
**Version:** 1.0.0  
**Last Updated:** June 2026  

---


## Scope & Audience

| Aspect | Definition |
|---|---|
| **Scope** | Enterprise licensing tiers, OEM deals, and ISO/IEC 19770-2 compliance |
| **Diátaxis form** | Reference |
| **Primary audience** | ORCHORDS, ORCHORDS, ORCHORDS, ORCHORDS, enterprise customers |
| **Secondary audience** | Future maintainers and reviewers of this document |


---

## Overview

This document defines ORCHORDS's enterprise licensing model for ORCHORDS -- the sales process, licensing tiers, contract structures, and how enterprise customers receive and manage their software. Per **ISO/IEC 19770-2:2015**, software identification must be included with enterprise software.
## Contents

- [Licensing Tiers](#licensing-tiers)
  - [Consumer / Individual](#consumer-individual)
  - [Professional](#professional)
  - [Enterprise](#enterprise)
- [Software Asset Management — ISO/IEC 19770-2](#software-asset-management-isoiec-19770-2)
  - [SWID Tag for Enterprise Deployments](#swid-tag-for-enterprise-deployments)
- [Enterprise Sales Process](#enterprise-sales-process)
  - [Qualification](#qualification)
  - [Enterprise Sales Stages](#enterprise-sales-stages)
- [Enterprise Contract Terms](#enterprise-contract-terms)
  - [Standard Terms to Negotiate](#standard-terms-to-negotiate)
  - [Required Legal Documents](#required-legal-documents)
- [OEM & Bundling Deals](#oem-bundling-deals)
  - [OEM Deal Types](#oem-deal-types)
  - [OEM Requirements](#oem-requirements)
- [Version History](#version-history)
  - [Change Log](#change-log)
  - [Review Cadence](#review-cadence)

---

## Licensing Tiers

### Consumer / Individual

| Item | Detail |
|---|---|
| **Model** | Direct purchase (Windows Store or website) |
| **License** | Per seat, annual or perpetual |
| **Price** | Listed at orchords.com/pricing |
| **Support** | Community forum, knowledge base |
| **Upgrade** | Included for annual licenses |

### Professional

| Item | Detail |
|---|---|
| **Model** | Annual subscription |
| **License** | Per seat |
| **Price** | Volume pricing (5–24 seats): 15% discount |
| **Support** | Email support, priority response |
| **Upgrade** | Included |
| **Features** | All ORCHORDS features |

### Enterprise

| Item | Detail |
|---|---|
| **Model** | Annual subscription or perpetual |
| **License** | Site-wide or named-user seats |
| **Price** | Custom negotiation; volume pricing (25+ seats): 25%+ discount |
| **Support** | Dedicated account manager, SLA-backed support (24h response) |
| **Upgrade** | Included |
| **Features** | All features + early access to beta |
| **Extras** | Custom onboarding, training sessions, plugin support |

---

## Software Asset Management — ISO/IEC 19770-2

Per **ISO/IEC 19770-2:2015**, enterprise customers must be able to identify and track ORCHORDS installations via SWID tags.

### SWID Tag for Enterprise Deployments

Every ORCHORDS installer ships with a SWID tag. Enterprise IT can:

- **Discover installations** via SCCM, Intune, LANDESK, or ServiceNow
- **Track version compliance** — which machines have the current version
- **Verify license compliance** — seat count vs. license count

| Tag Field | Enterprise Value |
|---|---|
| `ProductID` | Unique per version — tracks upgrade compliance |
| `Version` | Matches SemVer — IT can query for specific version ranges |
| `SoftwareCreator > Regid` | `regid.example.com` — identifies ORCHORDS as publisher |
| `ProductName` | `ORCHORDS` — human-readable identifier |

See [`releases/SWID_TAG_SPEC.md`](../releases/SWID_TAG_SPEC.md) for the technical SWID tag specification.

---

## Enterprise Sales Process

### Qualification

| Question | Yes → Next Step | No → Close |
|---|---|---|
| Is this an organizational purchase? | Continue | → Consumer tier |
| More than 10 seats needed? | Enterprise track | → Pro tier |
| Custom requirements (SSO, MDM, plugin SDK)? | Enterprise track | → Pro tier |
| Government or regulated industry? | Enterprise track + legal review | → Pro tier |

### Enterprise Sales Stages

```
Lead → Discovery → Proposal → Negotiation → Contract → Implementation → Renewal
```

| Stage | Owner | Key Activities |
|---|---|---|
| **Lead** | ORCHORDS | Initial outreach, demo scheduling |
| **Discovery** | ORCHORDS | Understand needs, use cases, seat count, current tools |
| **Proposal** | ORCHORDS + ORCHORDS | Custom pricing, feature scoping, support SLA |
| **Negotiation** | ORCHORDS + ORCHORDS | Legal review, contract terms |
| **Contract** | ORCHORDS + ORCHORDS | EULA, MSA, DPA, SOW if applicable |
| **Implementation** | ORCHORDS + ORCHORDS | Technical onboarding, SSO setup, MDM integration |
| **Renewal** | ORCHORDS | Annual renewal conversation, seat audit |

---

## Enterprise Contract Terms

### Standard Terms to Negotiate

| Term | Standard | Negotiable |
|---|---|---|
| **Contract length** | Annual | Multi-year (discount offered) |
| **Payment** | Net 30 | Net 60 for large accounts |
| **Seat minimum** | 25 seats | Negotiable for strategic accounts |
| **Support SLA** | 24-hour email response | 4-hour response for premium |
| **Data residency** | US default | EU or custom on Enterprise+ |
| **Audit rights** | ORCHORDS may audit usage twice/year | Negotiable |

### Required Legal Documents

| Document | Purpose | Owner |
|---|---|---|
| **Master Subscription Agreement (MSA)** | Governs the commercial relationship | ORCHORDS |
| **Data Processing Agreement (DPA)** | GDPR/data handling obligations | ORCHORDS |
| **Service Level Agreement (SLA)** | Support response time guarantees | ORCHORDS |
| **Software Evaluation Agreement** | For proof-of-concept / pilot | ORCHORDS |
| **Order Form** | Seat count, pricing, term | ORCHORDS + ORCHORDS |

---

## OEM & Bundling Deals

Per **ISO/IEC 19770-2:2015**, OEM distributions require a special license agreement and must include accurate SWID tags identifying the OEM as the software creator.

### OEM Deal Types

| Deal Type | Description | Example |
|---|---|---|
| **Pre-install bundling** | ORCHORDS pre-installed on new hardware | Hardware vendor partnership |
| **SaaS bundling** | Offered as part of a SaaS platform subscription | Content creation platform |
| **Agency license** | Agency manages multiple client accounts | Video production agency |

### OEM Requirements

- Custom SWID tag with OEM's `Regid` as `SoftwareCreator`
- Custom branding option (optional)
- API access for enterprise integration
- Revenue share or flat fee structure (negotiated per deal)
- Minimum commitment volumes

---

## Version History

| Version | Date | Changes |
|---|---|---|
| 1.0.0 | June 2026 | Initial guide — aligned with ISO/IEC 19770-2:2015 and ISO/IEC 12207:2017 |

---

*Grounded in: ISO/IEC 19770-2:2015 (Software Asset Management), ISO/IEC 12207:2017 §6.4 (Distribution)*



---

## References

### Internal Documents

- [$title](./../releases/SWID_TAG_SPEC.md)

### Standards & Frameworks

- ISO/IEC 12207:2017 (Systems and software engineering — Software life cycle processes)
- ISO/IEC 25010:2023 (Systems and software engineering — Quality requirements and evaluation)
- See [STYLE_GUIDE.md](./STYLE_GUIDE.md) for the full standards catalog

---

## Document Maintenance

### Change Log

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0.0 | June 2026 | ORCHORDS | Initial version |
| 1.0.1 | June 2026 | ORCHORDS | Added Scope & Audience block and Document Maintenance section per STYLE_GUIDE.md (ISO/IEC/IEEE 82079-1:2019 compliance) |

### Review Cadence

- **Next review:** Annually or on pricing change
- **Reviewer:** ORCHORDS (Business Development)
- **Cadence:** Per STYLE_GUIDE.md defaults for this document type