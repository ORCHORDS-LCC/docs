# DEPRECATED: Linux Terminal Injection Attack Pattern Assurance Profile

## Reference

- Attack pattern: **249 — DEPRECATED: Linux Terminal Injection**
- Status: Deprecated

## Pattern description

This attack pattern has been deprecated as it is covered by "CAPEC-40 : Manipulating Writeable Terminal Devices". Please refer to this CAPEC going forward.

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
- 249: https://capec.mitre.org/data/definitions/249.html
- Reviewed: 2026-10-27
