# Fake the Source of Data Attack Pattern Assurance Profile

## Reference

- Attack pattern: **194 — Fake the Source of Data**
- Status: Stable

## Pattern description

An adversary takes advantage of improper authentication to provide data or services under a falsified identity. The purpose of using the falsified identity may be to prevent traceability of the provided data or to assume the rights granted to another individual. One of the simplest forms of this attack would be the creation of an email message with a modified "From" field in order to appear that the message was sent from someone other than the actual sender. The root of the attack (in this case the email system) fails to properly authenticate the source and this results in the reader incorrectly performing the instructed action. Results of the attack vary depending on the details of the attack, but common results include privilege escalation, obfuscation of other attacks, and data corruption/manipulation.

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
- 194: https://capec.mitre.org/data/definitions/194.html
- Reviewed: 2026-10-27
