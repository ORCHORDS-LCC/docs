# Cross Frame Scripting (XFS) Attack Pattern Assurance Profile

## Reference

- Attack pattern: **587 — Cross Frame Scripting (XFS)**
- Status: Draft

## Pattern description

This attack pattern combines malicious Javascript and a legitimate webpage loaded into a concealed iframe. The malicious Javascript is then able to interact with a legitimate webpage in a manner that is unknown to the user. This attack usually leverages some element of social engineering in that an attacker must convinces a user to visit a web page that the attacker controls.

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
- 587: https://capec.mitre.org/data/definitions/587.html
- Reviewed: 2026-10-27
