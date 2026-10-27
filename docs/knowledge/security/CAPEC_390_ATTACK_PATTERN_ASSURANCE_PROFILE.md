# Bypassing Physical Security Attack Pattern Assurance Profile

## Reference

- Attack pattern: **390 — Bypassing Physical Security**
- Status: Draft

## Pattern description

Facilities often used layered models for physical security such as traditional locks, Electronic-based card entry systems, coupled with physical alarms. Hardware security mechanisms range from the use of computer case and cable locks as well as RFID tags for tracking computer assets. This layered approach makes it difficult for random physical security breaches to go unnoticed, but is less effective at stopping deliberate and carefully planned break-ins. Avoiding detection begins with evading building security and surveillance and methods for bypassing the electronic or physical locks which secure entry points.

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
- 390: https://capec.mitre.org/data/definitions/390.html
- Reviewed: 2026-10-27
