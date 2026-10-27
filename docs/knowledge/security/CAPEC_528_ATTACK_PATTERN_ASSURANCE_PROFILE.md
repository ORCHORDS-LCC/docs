# XML Flood Attack Pattern Assurance Profile

## Reference

- Attack pattern: **528 — XML Flood**
- Status: Draft

## Pattern description

An adversary may execute a flooding attack using XML messages with the intent to deny legitimate users access to a web service. These attacks are accomplished by sending a large number of XML based requests and letting the service attempt to parse each one. In many cases this type of an attack will result in a XML Denial of Service (XDoS) due to an application becoming unstable, freezing, or crashing.

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
- 528: https://capec.mitre.org/data/definitions/528.html
- Reviewed: 2026-10-27
