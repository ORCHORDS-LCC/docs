# Development Alteration Attack Pattern Assurance Profile

## Reference

- Attack pattern: **444 — Development Alteration**
- Status: Stable

## Pattern description

An adversary modifies a technology, product, or component during its development to acheive a negative impact once the system is deployed. The goal of the adversary is to modify the system in such a way that the negative impact can be leveraged when the system is later deployed. Development alteration attacks may include attacks that insert malicious logic into the system's software, modify or replace hardware components, and other attacks which negatively impact the system during development. These attacks generally require insider access to modify source code or to tamper with hardware components. The product is then delivered to the user where the negative impact can be leveraged at a later time.

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
- 444: https://capec.mitre.org/data/definitions/444.html
- Reviewed: 2026-10-27
