# Leveraging/Manipulating Configuration File Search Paths Attack Pattern Assurance Profile

## Reference

- Attack pattern: **38 — Leveraging/Manipulating Configuration File Search Paths**
- Status: Draft

## Pattern description

This pattern of attack sees an adversary load a malicious resource into a program's standard path so that when a known command is executed then the system instead executes the malicious component. The adversary can either modify the search path a program uses, like a PATH variable or classpath, or they can manipulate resources on the path to point to their malicious components. J2EE applications and other component based applications that are built from multiple binaries can have very long list of dependencies to execute. If one of these libraries and/or references is controllable by the attacker then application controls can be circumvented by the attacker.

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
- 38: https://capec.mitre.org/data/definitions/38.html
- Reviewed: 2026-10-27
