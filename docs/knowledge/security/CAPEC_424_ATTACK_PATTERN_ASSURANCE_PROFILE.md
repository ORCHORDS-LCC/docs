# Influence Perception of Consensus or Social Proof Attack Pattern Assurance Profile

## Reference

- Attack pattern: **424 — Influence Perception of Consensus or Social Proof**
- Status: Draft

## Pattern description

The adversary influences the target's actions by leveraging the inherent human nature to assume behavior of others is appropriate. In situations of uncertainty, people tend to behave in ways they see others behaving. The adversary convinces the target of adopting behavior or actions that is advantageous to the adversary.

## Assurance profile

1. Determine whether the attack pattern is in scope for the systems and data being protected, and record the reason.
2. Review the pattern's prerequisites: the access, position, or precondition it requires.
3. Identify the observable indicators the pattern would produce in logs, telemetry, or configuration.
4. Define the control that prevents the pattern and the control that would detect it.
5. Define the verification method and the evidence that would demonstrate either prevention or detection.
6. Record the residual risk where only detection, not prevention, can be achieved.

## Verification evidence

- a scope decision recording why the pattern is or is not applicable;
- the indicator list mapped to the telemetry that would carry it;
- the control mapping with the evidence that supports it;
- a test or exercise record for the detection path.

## Limitations

An attack-pattern entry describes a class of abuse. Applicability and exposure are properties of a system, established only by evidence.

## Source

- MITRE CAPEC catalog: https://capec.mitre.org/data/xml/capec_latest.xml
- 424: https://capec.mitre.org/data/definitions/424.html
- Reviewed: 2026-10-27
