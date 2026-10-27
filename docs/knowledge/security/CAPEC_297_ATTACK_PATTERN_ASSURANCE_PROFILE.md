# TCP ACK Ping Attack Pattern Assurance Profile

## Reference

- Attack pattern: **297 — TCP ACK Ping**
- Status: Stable

## Pattern description

An adversary sends a TCP segment with the ACK flag set to a remote host for the purpose of determining if the host is alive. This is one of several TCP 'ping' types. The RFC 793 expected behavior for a service is to respond with a RST 'reset' packet to any unsolicited ACK segment that is not part of an existing connection. So by sending an ACK segment to a port, the adversary can identify that the host is alive by looking for a RST packet. Typically, a remote server will respond with a RST regardless of whether a port is open or closed. In this way, TCP ACK pings cannot discover the state of a remote port because the behavior is the same in either case. The firewall will look up the ACK packet in its state-table and discard the segment because it does not correspond to any active connection. A TCP ACK Ping can be used to discover if a host is alive via RST response packets sent from the host.

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
- 297: https://capec.mitre.org/data/definitions/297.html
- Reviewed: 2026-10-27
