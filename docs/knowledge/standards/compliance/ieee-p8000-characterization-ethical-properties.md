# IEEE P8000 — Standard for Characterization and Specification of Ethical Properties in Autonomous Intelligent Systems

**Issue:** The corpus contains zero documents on IEEE P8000, the standard for characterizing and specifying ethical properties in autonomous intelligent systems.
**Date:** 2026-10-28
**Author:** ORCHORDS
**Status:** documented

## Symptom
Engineering teams routinely need to state, in a testable way, what makes an autonomous system ethically acceptable. The corpus contains no document that covers the standard for characterizing and specifying ethical properties of such systems, so that vocabulary has no home in the corpus.

## Root cause
IEEE P8000 is a project (P = proposed, under development) in the IEEE 7000 series, which addresses ethical concerns in technology design. The corpus focuses on ISO/IEC standards, NIST frameworks, and regulatory compliance, so IEEE's ethical-characterization work is not yet represented.

**Source:** IEEE AIS standards list:
https://standards.ieee.org/initiatives/autonomous-intelligence-systems/standards/

## The "ethical property characterization" concept
IEEE P8000 provides a framework for the characterization and specification of a suite of desirable and beneficial ethical properties in autonomous intelligent systems.

Key aspects from the IEEE catalogue:
- **Standard number:** IEEE P8000 (project, no year)
- **Title:** Standard for Characterization and Specification of Ethical Properties in Autonomous Intelligent Systems
- **Status:** Project (P = proposed, under development)
- **Family:** IEEE 7000 series (AI ethics, transparency, bias, ethical properties)

The word doing the work in that title is *characterization*. An ethical property has to be turned into something a system can be said to have or lack, and a specification has to be written in a form that a reviewer or an assurance case can check. That is a different job from stating a value, and it is the job this project takes on.

## The "characterize, then specify" pattern
Ethical requirements are handled in two steps:
- Characterize the desirable and beneficial ethical properties an autonomous system should exhibit
- Specify each property in a form that can be evaluated against the system

The properties this sits closest to are the ones the rest of the 7000 family also addresses:
- Transparency of the system's behaviour
- Freedom from algorithmic bias in its outputs
- Respect for human autonomy and agency
- Accountable governance of the system over its lifecycle

This pattern is critical for:
- Assurance cases that argue an autonomous system is ethically acceptable
- Procurement evaluation criteria that go beyond functional requirements
- Consistency between an ethics policy and what is actually testable
- Traceability from stated values to system requirements, the concern IEEE 7000-2021 establishes

## Verification
The IEEE AIS standards page at https://standards.ieee.org/initiatives/autonomous-intelligence-systems/standards/ lists IEEE P8000 as a project with the title given above. The IEEE Trust in Technology initiative page at https://standards.ieee.org/initiatives/digital-trust/ provides additional context. The full project text is behind IEEE's paywall.

## Gotchas
- IEEE P8000 is a *project* (P = proposed, under development), not a published standard — there is no year to cite.
- It is a single project, not a family of standards, despite the number.
- It characterizes and specifies ethical properties; it is not itself an AI management system standard. For that, see ISO/IEC 42001.
- Do not confuse it with IEEE 2800-2022, which is an unrelated power-grid standard on inverter-based resources.

## Related
- `compliance/ieee-7000-model-process-ethical-concerns-system-design.md`
- `compliance/ieee-7000-series-ai-ethics-transparency-and-bias-standards-overview.md`
- `compliance/ieee-7001-transparency-of-autonomous-systems.md`
- `compliance/ieee-7003-algorithmic-bias-considerations.md`
- `compliance/iso-42005-ai-system-impact-assessment-overview.md`
