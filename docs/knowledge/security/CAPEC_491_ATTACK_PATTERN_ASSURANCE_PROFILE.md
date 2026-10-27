# Quadratic Data Expansion Attack Pattern Assurance Profile

## Reference

- Attack pattern: **491 — Quadratic Data Expansion**
- Status: Draft

## Pattern description

An adversary exploits macro-like substitution to cause a denial of service situation due to excessive memory being allocated to fully expand the data. The result of this denial of service could cause the application to freeze or crash. This involves defining a very large entity and using it multiple times in a single entity substitution. CAPEC-197 is a similar attack pattern, but it is easier to discover and defend against. This attack pattern does not perform multi-level substitution and therefore does not obviously appear to consume extensive resources.

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
- 491: https://capec.mitre.org/data/definitions/491.html
- Reviewed: 2026-10-27
