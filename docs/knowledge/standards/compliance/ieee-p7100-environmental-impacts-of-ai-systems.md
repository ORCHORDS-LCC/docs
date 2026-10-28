# IEEE P7100 — Standard for Measurement of Environmental Impacts of Artificial Intelligence Systems

**Issue:** The corpus contains zero documents on IEEE P7100, the standard for measuring the environmental impacts of AI systems.
**Date:** 2026-10-28
**Author:** ORCHORDS
**Status:** documented

## Symptom
AI systems consume energy and water during model training and during inference at scale, and the corpus contains no document that sets out how those impacts are measured and reported. IEEE P7100 addresses exactly that measurement problem, and the corpus's coverage of it is empty.

## Root cause
IEEE P7100 is a project (P = proposed, under development) in the IEEE 7000 series, which applies ethical and societal concerns to specific engineering domains. The corpus focuses on ISO/IEC standards, NIST frameworks, and regulatory compliance, so IEEE's environmental-measurement projects are not yet represented.

**Source:** IEEE AIS standards list:
https://standards.ieee.org/initiatives/autonomous-intelligence-systems/standards/

## The "environmental impact measurement" concept
IEEE P7100 defines a measurement framework for reporting on environmental indicators for training models and deriving inferences from them.

Key aspects from the IEEE catalogue:
- **Standard number:** IEEE P7100 (project, no year)
- **Title:** Standard for Measurement of Environmental Impacts of Artificial Intelligence Systems
- **Status:** Project (P = proposed, under development)
- **Family:** IEEE 7000 series (AI ethics, transparency, bias, environmental impact)

The scope separates two distinct sources of impact: the energy and resource consumption of **training** models, and the ongoing consumption of **inference** from serving them. A system that is cheap to train but expensive to serve at scale inverts the two, so a measurement framework has to account for both sides of the lifecycle rather than reporting a single training-time figure.

## The "lifecycle indicator reporting" pattern
Environmental indicators for an AI system are reported across the lifecycle:
- Energy consumption during training runs
- Energy and resource consumption during inference at serving scale
- The infrastructure footprint the measurement is taken against
- Consistency of reported indicators between comparable systems

This pattern is critical for:
- Voluntary environmental reporting by AI system operators
- Procurement decisions that compare AI services on more than price and capability
- Regulatory scrutiny of AI data centre energy use
- Honest sustainability claims, which require a measurement method rather than an estimate

## Verification
The IEEE AIS standards page at https://standards.ieee.org/initiatives/autonomous-intelligence-systems/standards/ lists IEEE P7100 as a project with the title given above. The IEEE Trust in Technology initiative page at https://standards.ieee.org/initiatives/digital-trust/ provides additional context on the IEEE standards ecosystem. The full project text is behind IEEE's paywall.

## Gotchas
- IEEE P7100 is a *project* (P = proposed, under development), not a published standard — there is no year to cite.
- The project concerns **measurement of** environmental impact, not the mitigation of it. It does not set emissions targets or carbon budgets.
- Do not confuse it with IEEE 2800-2022, which is an unrelated power-grid standard on inverter-based resources.

## Related
- `compliance/ieee-7000-model-process-ethical-concerns-system-design.md`
- `compliance/ieee-7000-series-ai-ethics-transparency-and-bias-standards-overview.md`
- `compliance/ieee-7010-impacts-on-human-well-being.md`
- `compliance/ieee-p7021-ethical-ai-climate-projections.md`
