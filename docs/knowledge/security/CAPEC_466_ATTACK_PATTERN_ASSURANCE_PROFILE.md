# Leveraging Active Adversary in the Middle Attacks to Bypass Same Origin Policy Attack Pattern Assurance Profile

## Reference

- Attack pattern: **466 — Leveraging Active Adversary in the Middle Attacks to Bypass Same Origin Policy**
- Status: Draft

## Pattern description

An attacker leverages an adversary in the middle attack (CAPEC-94) in order to bypass the same origin policy protection in the victim's browser. This active adversary in the middle attack could be launched, for instance, when the victim is connected to a public WIFI hot spot. An attacker is able to intercept requests and responses between the victim's browser and some non-sensitive website that does not use TLS.

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
- 466: https://capec.mitre.org/data/definitions/466.html
- Reviewed: 2026-10-27
