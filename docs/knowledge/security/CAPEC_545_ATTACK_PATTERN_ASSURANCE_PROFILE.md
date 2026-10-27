# Pull Data from System Resources Attack Pattern Assurance Profile

## Reference

- Attack pattern: **545 — Pull Data from System Resources**
- Status: Draft

## Pattern description

An adversary who is authorized or has the ability to search known system resources, does so with the intention of gathering useful information. System resources include files, memory, and other aspects of the target system. In this pattern of attack, the adversary does not necessarily know what they are going to find when they start pulling data. This is different than CAPEC-150 where the adversary knows what they are looking for due to the common location.

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
- 545: https://capec.mitre.org/data/definitions/545.html
- Reviewed: 2026-10-27
