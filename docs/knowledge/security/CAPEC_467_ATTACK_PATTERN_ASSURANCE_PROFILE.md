# Cross Site Identification Attack Pattern Assurance Profile

## Reference

- Attack pattern: **467 — Cross Site Identification**
- Status: Draft

## Pattern description

An attacker harvests identifying information about a victim via an active session that the victim's browser has with a social networking site. A victim may have the social networking site open in one tab or perhaps is simply using the "remember me" feature to keep their session with the social networking site active. An attacker induces a payload to execute in the victim's browser that transparently to the victim initiates a request to the social networking site (e.g., via available social network site APIs) to retrieve identifying information about a victim. While some of this information may be public, the attacker is able to harvest this information in context and may use it for further attacks on the user (e.g., spear phishing).

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
- 467: https://capec.mitre.org/data/definitions/467.html
- Reviewed: 2026-10-27
