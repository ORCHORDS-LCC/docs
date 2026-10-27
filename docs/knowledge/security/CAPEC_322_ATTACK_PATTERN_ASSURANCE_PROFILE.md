# TCP (ISN) Greatest Common Divisor Probe Attack Pattern Assurance Profile

## Reference

- Attack pattern: **322 — TCP (ISN) Greatest Common Divisor Probe**
- Status: Stable

## Pattern description

This OS fingerprinting probe sends a number of TCP SYN packets to an open port of a remote machine. The Initial Sequence Number (ISN) in each of the SYN/ACK response packets is analyzed to determine the smallest number that the target host uses when incrementing sequence numbers. This information can be useful for identifying an operating system because particular operating systems and versions increment sequence numbers using different values. The result of the analysis is then compared against a database of OS behaviors to determine the OS type and/or version.

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
- 322: https://capec.mitre.org/data/definitions/322.html
- Reviewed: 2026-10-27
