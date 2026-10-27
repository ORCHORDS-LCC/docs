# Functionality Misuse Attack Pattern Assurance Profile

## Reference

- Attack pattern: **212 — Functionality Misuse**
- Status: Stable

## Pattern description

An adversary leverages a legitimate capability of an application in such a way as to achieve a negative technical impact. The system functionality is not altered or modified but used in a way that was not intended. This is often accomplished through the overuse of a specific functionality or by leveraging functionality with design flaws that enables the adversary to gain access to unauthorized, sensitive data.

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
- 212: https://capec.mitre.org/data/definitions/212.html
- Reviewed: 2026-10-27
