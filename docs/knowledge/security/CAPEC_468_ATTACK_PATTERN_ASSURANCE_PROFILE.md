# Generic Cross-Browser Cross-Domain Theft Attack Pattern Assurance Profile

## Reference

- Attack pattern: **468 — Generic Cross-Browser Cross-Domain Theft**
- Status: Draft

## Pattern description

An attacker makes use of Cascading Style Sheets (CSS) injection to steal data cross domain from the victim's browser. The attack works by abusing the standards relating to loading of CSS: 1. Send cookies on any load of CSS (including cross-domain) 2. When parsing returned CSS ignore all data that does not make sense before a valid CSS descriptor is found by the CSS parser.

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
- 468: https://capec.mitre.org/data/definitions/468.html
- Reviewed: 2026-10-27
