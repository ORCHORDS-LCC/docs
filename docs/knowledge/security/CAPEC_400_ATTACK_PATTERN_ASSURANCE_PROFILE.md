# RFID Chip Deactivation or Destruction Attack Pattern Assurance Profile

## Reference

- Attack pattern: **400 — RFID Chip Deactivation or Destruction**
- Status: Draft

## Pattern description

An attacker uses methods to deactivate a passive RFID tag for the purpose of rendering the tag, badge, card, or object containing the tag unresponsive. RFID tags are used primarily for access control, inventory, or anti-theft devices. The purpose of attacking the RFID chip is to disable or damage the chip without causing damage to the object housing it.

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
- 400: https://capec.mitre.org/data/definitions/400.html
- Reviewed: 2026-10-27
