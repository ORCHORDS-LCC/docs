# Malicious Automated Software Update via Spoofing Attack Pattern Assurance Profile

## Reference

- Attack pattern: **657 — Malicious Automated Software Update via Spoofing**
- Status: Draft

## Pattern description

An attackers uses identify or content spoofing to trick a client into performing an automated software update from a malicious source. A malicious automated software update that leverages spoofing can include content or identity spoofing as well as protocol spoofing. Content or identity spoofing attacks can trigger updates in software by embedding scripted mechanisms within a malicious web page, which masquerades as a legitimate update source. Scripting mechanisms communicate with software components and trigger updates from locations specified by the attackers' server. The result is the client believing there is a legitimate software update available but instead downloading a malicious update from the attacker.

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
- 657: https://capec.mitre.org/data/definitions/657.html
- Reviewed: 2026-10-27
