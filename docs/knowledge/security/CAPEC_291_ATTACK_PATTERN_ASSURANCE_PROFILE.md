# DNS Zone Transfers Attack Pattern Assurance Profile

## Reference

- Attack pattern: **291 — DNS Zone Transfers**
- Status: Stable

## Pattern description

An attacker exploits a DNS misconfiguration that permits a ZONE transfer. Some external DNS servers will return a list of IP address and valid hostnames. Under certain conditions, it may even be possible to obtain Zone data about the organization's internal network. When successful the attacker learns valuable information about the topology of the target organization, including information about particular servers, their role within the IT structure, and possibly information about the operating systems running upon the network. This is configuration dependent behavior so it may also be required to search out multiple DNS servers while attempting to find one with ZONE transfers allowed.

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
- 291: https://capec.mitre.org/data/definitions/291.html
- Reviewed: 2026-10-27
