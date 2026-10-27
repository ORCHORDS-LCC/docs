# Enumerate Mail Exchange (MX) Records Attack Pattern Assurance Profile

## Reference

- Attack pattern: **290 — Enumerate Mail Exchange (MX) Records**
- Status: Stable

## Pattern description

An adversary enumerates the MX records for a given via a DNS query. This type of information gathering returns the names of mail servers on the network. Mail servers are often not exposed to the Internet but are located within the DMZ of a network protected by a firewall. A side effect of this configuration is that enumerating the MX records for an organization my reveal the IP address of the firewall or possibly other internal systems. Attackers often resort to MX record enumeration when a DNS Zone Transfer is not possible.

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
- 290: https://capec.mitre.org/data/definitions/290.html
- Reviewed: 2026-10-27
