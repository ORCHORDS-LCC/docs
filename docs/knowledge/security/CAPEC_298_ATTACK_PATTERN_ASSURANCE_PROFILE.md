# UDP Ping Attack Pattern Assurance Profile

## Reference

- Attack pattern: **298 — UDP Ping**
- Status: Stable

## Pattern description

An adversary sends a UDP datagram to the remote host to determine if the host is alive. If a UDP datagram is sent to an open UDP port there is very often no response, so a typical strategy for using a UDP ping is to send the datagram to a random high port on the target. The goal is to solicit an 'ICMP port unreachable' message from the target, indicating that the host is alive. UDP pings are useful because some firewalls are not configured to block UDP datagrams sent to strange or typically unused ports, like ports in the 65K range. Additionally, while some firewalls may filter incoming ICMP, weaknesses in firewall rule-sets may allow certain types of ICMP (host unreachable, port unreachable) which are useful for UDP ping attempts.

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
- 298: https://capec.mitre.org/data/definitions/298.html
- Reviewed: 2026-10-27
