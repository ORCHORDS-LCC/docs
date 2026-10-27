# BitSquatting Attack Pattern Assurance Profile

## Reference

- Attack pattern: **611 — BitSquatting**
- Status: Draft

## Pattern description

An adversary registers a domain name one bit different than a trusted domain. A BitSquatting attack leverages random errors in memory to direct Internet traffic to adversary-controlled destinations. BitSquatting requires no exploitation or complicated reverse engineering, and is operating system and architecture agnostic. Experimental observations show that BitSquatting popular websites could redirect non-trivial amounts of Internet traffic to a malicious entity.

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
- 611: https://capec.mitre.org/data/definitions/611.html
- Reviewed: 2026-10-27
