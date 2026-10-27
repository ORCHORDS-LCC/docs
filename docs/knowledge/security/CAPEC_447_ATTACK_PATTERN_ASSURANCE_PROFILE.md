# Design Alteration Attack Pattern Assurance Profile

## Reference

- Attack pattern: **447 — Design Alteration**
- Status: Stable

## Pattern description

An adversary modifies the design of a technology, product, or component to acheive a negative impact once the system is deployed. In this type of attack, the goal of the adversary is to modify the design of the system, prior to development starting, in such a way that the negative impact can be leveraged when the system is later deployed. Design alteration attacks differ from development alteration attacks in that design alteration attacks take place prior to development and which then may or may not be developed by the adverary. Design alteration attacks include modifying system designs to degrade system performance, cause unexpected states or errors, and general design changes that may lead to additional vulnerabilities. These attacks generally require insider access to modify design documents, but they may also be spoofed via web communications. The product is then developed and delivered to the user where the negative impact can be leveraged at a later time.

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
- 447: https://capec.mitre.org/data/definitions/447.html
- Reviewed: 2026-10-27
