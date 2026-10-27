# Owner Footprinting Attack Pattern Assurance Profile

## Reference

- Attack pattern: **577 — Owner Footprinting**
- Status: Draft

## Pattern description

An adversary exploits functionality meant to identify information about the primary users on the target system to an authorized user. They may do this, for example, by reviewing logins or file modification times. By knowing what owners use the target system, the adversary can inform further and more targeted malicious behavior. An example Windows command that may accomplish this is "dir /A ntuser.dat". Which will display the last modified time of a user's ntuser.dat file when run within the root folder of a user. This time is synonymous with the last time that user was logged in.

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
- 577: https://capec.mitre.org/data/definitions/577.html
- Reviewed: 2026-10-27
