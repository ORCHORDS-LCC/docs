# UDP Flood Attack Pattern Assurance Profile

## Reference

- Attack pattern: **486 — UDP Flood**
- Status: Draft

## Pattern description

An adversary may execute a flooding attack using the UDP protocol with the intent to deny legitimate users access to a service by consuming the available network bandwidth. Additionally, firewalls often open a port for each UDP connection destined for a service with an open UDP port, meaning the firewalls in essence save the connection state thus the high packet nature of a UDP flood can also overwhelm resources allocated to the firewall. UDP attacks can also target services like DNS or VoIP which utilize these protocols. Additionally, due to the session-less nature of the UDP protocol, the source of a packet is easily spoofed making it difficult to find the source of the attack.

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
- 486: https://capec.mitre.org/data/definitions/486.html
- Reviewed: 2026-10-27
