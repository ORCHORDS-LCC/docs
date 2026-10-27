# Use of Captured Tickets (Pass The Ticket) Attack Pattern Assurance Profile

## Reference

- Attack pattern: **645 — Use of Captured Tickets (Pass The Ticket)**
- Status: Stable

## Pattern description

An adversary uses stolen Kerberos tickets to access systems/resources that leverage the Kerberos authentication protocol. The Kerberos authentication protocol centers around a ticketing system which is used to request/grant access to services and to then access the requested services. An adversary can obtain any one of these tickets (e.g. Service Ticket, Ticket Granting Ticket, Silver Ticket, or Golden Ticket) to authenticate to a system/resource without needing the account's credentials. Depending on the ticket obtained, the adversary may be able to access a particular resource or generate TGTs for any account within an Active Directory Domain.

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
- 645: https://capec.mitre.org/data/definitions/645.html
- Reviewed: 2026-10-27
