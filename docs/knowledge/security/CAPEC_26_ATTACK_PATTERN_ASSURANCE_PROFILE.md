# Leveraging Race Conditions Attack Pattern Assurance Profile

## Reference

- Attack pattern: **26 — Leveraging Race Conditions**
- Status: Stable

## Pattern description

The adversary targets a race condition occurring when multiple processes access and manipulate the same resource concurrently, and the outcome of the execution depends on the particular order in which the access takes place. The adversary can leverage a race condition by "running the race", modifying the resource and modifying the normal execution flow. For instance, a race condition can occur while accessing a file: the adversary can trick the system by replacing the original file with their version and cause the system to read the malicious file.

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
- 26: https://capec.mitre.org/data/definitions/26.html
- Reviewed: 2026-10-27
