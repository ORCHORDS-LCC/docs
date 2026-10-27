# Passive OS Fingerprinting Attack Pattern Assurance Profile

## Reference

- Attack pattern: **313 — Passive OS Fingerprinting**
- Status: Stable

## Pattern description

An adversary engages in activity to detect the version or type of OS software in a an environment by passively monitoring communication between devices, nodes, or applications. Passive techniques for operating system detection send no actual probes to a target, but monitor network or client-server communication between nodes in order to identify operating systems based on observed behavior as compared to a database of known signatures or values. While passive OS fingerprinting is not usually as reliable as active methods, it is generally better able to evade detection.

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
- 313: https://capec.mitre.org/data/definitions/313.html
- Reviewed: 2026-10-27
