# Flash Memory Attacks Attack Pattern Assurance Profile

## Reference

- Attack pattern: **458 — Flash Memory Attacks**
- Status: Draft

## Pattern description

An adversary inserts malicious logic into a product or technology via flashing the on-board memory with a code-base that contains malicious logic. Various attacks exist against the integrity of flash memory, the most direct being rootkits coded into the BIOS or chipset of a device.

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
- 458: https://capec.mitre.org/data/definitions/458.html
- Reviewed: 2026-10-27
