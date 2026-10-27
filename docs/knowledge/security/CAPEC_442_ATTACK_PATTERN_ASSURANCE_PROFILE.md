# Infected Software Attack Pattern Assurance Profile

## Reference

- Attack pattern: **442 — Infected Software**
- Status: Stable

## Pattern description

An adversary adds malicious logic, often in the form of a computer virus, to otherwise benign software. This logic is often hidden from the user of the software and works behind the scenes to achieve negative impacts. Many times, the malicious logic is inserted into empty space between legitimate code, and is then called when the software is executed. This pattern of attack focuses on software already fielded and used in operation as opposed to software that is still under development and part of the supply chain.

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
- 442: https://capec.mitre.org/data/definitions/442.html
- Reviewed: 2026-10-27
