# Reflection Injection Attack Pattern Assurance Profile

## Reference

- Attack pattern: **138 — Reflection Injection**
- Status: Draft

## Pattern description

An adversary supplies a value to the target application which is then used by reflection methods to identify a class, method, or field. For example, in the Java programming language the reflection libraries permit an application to inspect, load, and invoke classes and their components by name. If an adversary can control the input into these methods including the name of the class/method/field or the parameters passed to methods, they can cause the targeted application to invoke incorrect methods, read random fields, or even to load and utilize malicious classes that the adversary created. This can lead to the application revealing sensitive information, returning incorrect results, or even having the adversary take control of the targeted application.

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
- 138: https://capec.mitre.org/data/definitions/138.html
- Reviewed: 2026-10-27
