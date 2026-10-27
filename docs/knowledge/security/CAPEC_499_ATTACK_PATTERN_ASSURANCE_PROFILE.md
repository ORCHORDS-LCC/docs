# Android Intent Intercept Attack Pattern Assurance Profile

## Reference

- Attack pattern: **499 — Android Intent Intercept**
- Status: Draft

## Pattern description

An adversary, through a previously installed malicious application, intercepts messages from a trusted Android-based application in an attempt to achieve a variety of different objectives including denial of service, information disclosure, and data injection. An implicit intent sent from a trusted application can be received by any application that has declared an appropriate intent filter. If the intent is not protected by a permission that the malicious application lacks, then the attacker can gain access to the data contained within the intent. Further, the intent can be either blocked from reaching the intended destination, or modified and potentially forwarded along.

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
- 499: https://capec.mitre.org/data/definitions/499.html
- Reviewed: 2026-10-27
