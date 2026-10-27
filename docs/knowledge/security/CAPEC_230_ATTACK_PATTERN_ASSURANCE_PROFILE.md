# Serialized Data with Nested Payloads Attack Pattern Assurance Profile

## Reference

- Attack pattern: **230 — Serialized Data with Nested Payloads**
- Status: Draft

## Pattern description

Applications often need to transform data in and out of a data format (e.g., XML and YAML) by using a parser. It may be possible for an adversary to inject data that may have an adverse effect on the parser when it is being processed. Many data format languages allow the definition of macro-like structures that can be used to simplify the creation of complex structures. By nesting these structures, causing the data to be repeatedly substituted, an adversary can cause the parser to consume more resources while processing, causing excessive memory consumption and CPU utilization.

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
- 230: https://capec.mitre.org/data/definitions/230.html
- Reviewed: 2026-10-27
