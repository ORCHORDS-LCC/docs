# Application API Navigation Remapping Attack Pattern Assurance Profile

## Reference

- Attack pattern: **386 — Application API Navigation Remapping**
- Status: Draft

## Pattern description

An attacker manipulates either egress or ingress data from a client within an application framework in order to change the destination and/or content of links/buttons displayed to a user within API messages. Performing this attack allows the attacker to manipulate content in such a way as to produce messages or content that looks authentic but contains links/buttons that point to an attacker controlled destination. Some applications make navigation remapping more difficult to detect because the actual HREF values of images, profile elements, and links/buttons are masked. One example would be to place an image in a user's photo gallery that when clicked upon redirected the user to an off-site location. Also, traditional web vulnerabilities (such as CSRF) can be constructed with remapped buttons or links. In some cases navigation remapping can be used for Phishing attacks or even means to artificially boost the page view, user site reputation, or click-fraud.

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
- 386: https://capec.mitre.org/data/definitions/386.html
- Reviewed: 2026-10-27
