# Rooting SIM Cards Attack Pattern Assurance Profile

## Reference

- Attack pattern: **614 — Rooting SIM Cards**
- Status: Draft

## Pattern description

SIM cards are the de facto trust anchor of mobile devices worldwide. The cards protect the mobile identity of subscribers, associate devices with phone numbers, and increasingly store payment credentials, for example in NFC-enabled phones with mobile wallets. This attack leverages over-the-air (OTA) updates deployed via cryptographically-secured SMS messages to deliver executable code to the SIM. By cracking the DES key, an attacker can send properly signed binary SMS messages to a device, which are treated as Java applets and are executed on the SIM. These applets are allowed to send SMS, change voicemail numbers, and query the phone location, among many other predefined functions. These capabilities alone provide plenty of potential for abuse.

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
- 614: https://capec.mitre.org/data/definitions/614.html
- Reviewed: 2026-10-27
