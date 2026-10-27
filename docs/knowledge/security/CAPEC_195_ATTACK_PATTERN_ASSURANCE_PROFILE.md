# Principal Spoof Attack Pattern Assurance Profile

## Reference

- Attack pattern: **195 — Principal Spoof**
- Status: Draft

## Pattern description

A Principal Spoof is a form of Identity Spoofing where an adversary pretends to be some other person in an interaction. This is often accomplished by crafting a message (either written, verbal, or visual) that appears to come from a person other than the adversary. Phishing and Pharming attacks often attempt to do this so that their attempts to gather sensitive information appear to come from a legitimate source. A Principal Spoof does not use stolen or spoofed authentication credentials, instead relying on the appearance and content of the message to reflect identity.

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
- 195: https://capec.mitre.org/data/definitions/195.html
- Reviewed: 2026-10-27
