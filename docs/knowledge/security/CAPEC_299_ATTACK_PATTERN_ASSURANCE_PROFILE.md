# TCP SYN Ping Attack Pattern Assurance Profile

## Reference

- Attack pattern: **299 — TCP SYN Ping**
- Status: Stable

## Pattern description

An adversary uses TCP SYN packets as a means towards host discovery. Typical RFC 793 behavior specifies that when a TCP port is open, a host must respond to an incoming SYN "synchronize" packet by completing stage two of the 'three-way handshake' - by sending an SYN/ACK in response. When a port is closed, RFC 793 behavior is to respond with a RST "reset" packet. This behavior can be used to 'ping' a target to see if it is alive by sending a TCP SYN packet to a port and then looking for a RST or an ACK packet in response.

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
- 299: https://capec.mitre.org/data/definitions/299.html
- Reviewed: 2026-10-27
