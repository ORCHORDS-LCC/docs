# Pretexting Attack Pattern Assurance Profile

## Reference

- Attack pattern: **407 — Pretexting**
- Status: Draft

## Pattern description

An adversary engages in pretexting behavior to solicit information from target persons, or manipulate the target into performing some action that serves the adversary's interests. During a pretexting attack, the adversary creates an invented scenario, assuming an identity or role to persuade a targeted victim to release information or perform some action. It is more than just creating a lie; in some cases it can be creating a whole new identity and then using that identity to manipulate the receipt of information.

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
- 407: https://capec.mitre.org/data/definitions/407.html
- Reviewed: 2026-10-27
