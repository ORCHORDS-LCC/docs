# ISO/IEC 42001:2023 — AI Management System Overview

**Issue:** The corpus contains no document on ISO/IEC 42001:2023, the first international standard for an AI management system, even though it is the parent standard of ISO/IEC 42005 and the target of ISO/IEC 42003's implementation guidance.
**Date:** 2026-10-28
**Author:** ORCHORDS
**Status:** documented

## Symptom
An organization that wants a certifiable, auditable way to manage AI risk has no corpus document describing the standard that provides it. ISO/IEC 42001 is the reference point for AI governance in the same way that ISO/IEC 27001 is for information security, and the corpus's AI-governance coverage does not include it.

## Root cause
ISO/IEC 42001 was published in December 2023, after most of the corpus's standards material was assembled. The corpus focuses on ISO/IEC standards, NIST frameworks, and regulatory compliance, and while it holds one ISO 42001 template under `templates/`, the standards family itself carries no document on the standard.

**Source:** ISO catalogue entry:
https://www.iso.org/standard/42001

## The "AI management system" concept
ISO/IEC 42001:2023 is an international standard that specifies requirements for establishing, implementing, maintaining, and continually improving an Artificial Intelligence Management System (AIMS) within organizations. It is designed for entities providing or utilizing AI-based products or services, ensuring responsible development and use of AI systems.

As ISO defines it, an AI management system is "a set of interrelated or interacting elements of an organization intended to establish policies and objectives, as well as processes to achieve those objectives, in relation to the responsible development, provision or use of AI systems."

Key aspects from the catalogue entry:
- **Reference number:** ISO/IEC 42001:2023
- **Title:** Information technology — Artificial intelligence — Management system
- **Status:** Published
- **Edition:** 1
- **Publication date:** 2023-12
- **Price:** CHF 225

## The "first AI management system standard" pattern
ISO describes 42001 as the world's first AI management system standard. It addresses the unique challenges AI poses — ethical considerations, transparency, and continuous learning — and for organizations it "sets out a structured way to manage risks and opportunities associated with AI, balancing innovation with governance."

The benefits ISO lists are the four that distinguish a management-system standard from a technical one:
- A framework for managing risk and opportunities
- Demonstration of responsible use of AI
- Traceability, transparency, and reliability
- Cost savings and efficiency gains

The applicability is deliberately broad: ISO states the standard applies to organizations of any size involved in developing, providing, or using AI-based products and services, across all industries.

## Verification
The catalogue page at https://www.iso.org/standard/42001 returns HTTP 200 with scope, status (Published), edition (1), date (2023-12), and price (CHF 225). The full clause text is not publicly retrievable (CHF 225 purchase required); this document is grounded in the official catalogue entry and ISO's own summary text.

## Gotchas
- ISO/IEC 42001 is the **management system** standard; ISO/IEC 42005 is the **impact assessment** standard. They are separate and complementary, not the same thing.
- There is no ISO/IEC 42000 standard. The 42000 series is an informal family name; the members are 42001, 42003, 42005 and 42006.
- 42001 is a **requirements** standard, so it is certifiable. ISO/IEC 42005 is **guidance**, so it is not. Conflating the two misrepresents the conformity-assessment story.
- The full standard text is paywalled. Do not cite clause numbers you have not read.

## Related
- `compliance/iso-42005-ai-system-impact-assessment-overview.md`
- `compliance/iso-42005-ai-system-impact-assessment-scope.md`
- `compliance/iso-42003-ai-management-system-implementation-guidance.md`
- `compliance/iso-42003-ai-management-system-implementation-guidance-status.md`
- `compliance/ieee-7000-series-ai-ethics-transparency-and-bias-standards-overview.md`
