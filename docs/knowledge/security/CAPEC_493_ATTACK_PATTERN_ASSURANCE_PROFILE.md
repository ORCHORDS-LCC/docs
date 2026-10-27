# SOAP Array Blowup Attack Pattern Assurance Profile

## Reference

- Attack pattern: **493 — SOAP Array Blowup**
- Status: Draft

## Pattern description

An adversary may execute an attack on a web service that uses SOAP messages in communication. By sending a very large SOAP array declaration to the web service, the attacker forces the web service to allocate space for the array elements before they are parsed by the XML parser. The attacker message is typically small in size containing a large array declaration of say 1,000,000 elements and a couple of array elements. This attack targets exhaustion of the memory resources of the web service.

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
- 493: https://capec.mitre.org/data/definitions/493.html
- Reviewed: 2026-10-27
