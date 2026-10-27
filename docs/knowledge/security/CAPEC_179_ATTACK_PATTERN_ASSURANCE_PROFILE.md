# Calling Micro-Services Directly Attack Pattern Assurance Profile

## Reference

- Attack pattern: **179 — Calling Micro-Services Directly**
- Status: Draft

## Pattern description

An attacker is able to discover and query Micro-services at a web location and thereby expose the Micro-services to further exploitation by gathering information about their implementation and function. Micro-services in web pages allow portions of a page to connect to the server and update content without needing to cause the entire page to update. This allows user activity to change portions of the page more quickly without causing disruptions elsewhere.

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
- 179: https://capec.mitre.org/data/definitions/179.html
- Reviewed: 2026-10-27
