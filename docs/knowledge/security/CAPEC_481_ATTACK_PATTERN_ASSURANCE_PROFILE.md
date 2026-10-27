# Contradictory Destinations in Traffic Routing Schemes Attack Pattern Assurance Profile

## Reference

- Attack pattern: **481 — Contradictory Destinations in Traffic Routing Schemes**
- Status: Draft

## Pattern description

Adversaries can provide contradictory destinations when sending messages. Traffic is routed in networks using the domain names in various headers available at different levels of the OSI model. In a Content Delivery Network (CDN) multiple domains might be available, and if there are contradictory domain names provided it is possible to route traffic to an inappropriate destination. The technique, called Domain Fronting, involves using different domain names in the SNI field of the TLS header and the Host field of the HTTP header. An alternative technique, called Domainless Fronting, is similar, but the SNI field is left blank.

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
- 481: https://capec.mitre.org/data/definitions/481.html
- Reviewed: 2026-10-27
