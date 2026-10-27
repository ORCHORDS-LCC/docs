# Content Spoofing Via Application API Manipulation Attack Pattern Assurance Profile

## Reference

- Attack pattern: **389 — Content Spoofing Via Application API Manipulation**
- Status: Draft

## Pattern description

An attacker manipulates either egress or ingress data from a client within an application framework in order to change the content of messages. Performing this attack allows the attacker to manipulate content in such a way as to produce messages or content that look authentic but may contain deceptive links, spam-like content, or links to the attackers' code. In general, content-spoofing within an application API can be employed to stage many different types of attacks varied based on the attackers' intent. The techniques require use of specialized software that allow the attacker to use adversary-in-the-middle (CAPEC-94) communications between the web browser and the remote system.

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
- 389: https://capec.mitre.org/data/definitions/389.html
- Reviewed: 2026-10-27
