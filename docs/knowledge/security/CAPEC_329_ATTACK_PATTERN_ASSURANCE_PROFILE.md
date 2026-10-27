# ICMP Error Message Quoting Probe Attack Pattern Assurance Profile

## Reference

- Attack pattern: **329 — ICMP Error Message Quoting Probe**
- Status: Stable

## Pattern description

An adversary uses a technique to generate an ICMP Error message (Port Unreachable, Destination Unreachable, Redirect, Source Quench, Time Exceeded, Parameter Problem) from a target and then analyze the amount of data returned or "Quoted" from the originating request that generated the ICMP error message.

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
- 329: https://capec.mitre.org/data/definitions/329.html
- Reviewed: 2026-10-27
