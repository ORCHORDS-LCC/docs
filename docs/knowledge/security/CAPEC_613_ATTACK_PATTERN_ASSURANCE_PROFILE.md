# WiFi SSID Tracking Attack Pattern Assurance Profile

## Reference

- Attack pattern: **613 — WiFi SSID Tracking**
- Status: Draft

## Pattern description

In this attack scenario, the attacker passively listens for WiFi management frame messages containing the Service Set Identifier (SSID) for the WiFi network. These messages are frequently transmitted by WiFi access points (e.g., the retransmission device) as well as by clients that are accessing the network (e.g., the handset/mobile device). Once the attacker is able to associate an SSID with a particular user or set of users (for example, when attending a public event), the attacker can then scan for this SSID to track that user in the future.

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
- 613: https://capec.mitre.org/data/definitions/613.html
- Reviewed: 2026-10-27
