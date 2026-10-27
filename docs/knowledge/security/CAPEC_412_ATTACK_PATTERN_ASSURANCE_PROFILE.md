# Pretexting via Customer Service Attack Pattern Assurance Profile

## Reference

- Attack pattern: **412 — Pretexting via Customer Service**
- Status: Draft

## Pattern description

An adversary engages in pretexting behavior, assuming the role of someone who works for Customer Service, to solicit information from target persons, or manipulate the target into performing an action that serves the adversary's interests. One example of a scenario such as this would be to call an individual, articulate your false affiliation with a credit card company, and then attempt to get the individual to verify their credit card number.

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
- 412: https://capec.mitre.org/data/definitions/412.html
- Reviewed: 2026-10-27
