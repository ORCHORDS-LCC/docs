# Malicious Hardware Update Attack Pattern Assurance Profile

## Reference

- Attack pattern: **534 — Malicious Hardware Update**
- Status: Stable

## Pattern description

An adversary introduces malicious hardware during an update or replacement procedure, allowing for additional compromise or site disruption at the victim location. After deployment, it is not uncommon for upgrades and replacements to occur involving hardware and various replaceable parts. These upgrades and replacements are intended to correct defects, provide additional features, and to replace broken or worn-out parts. However, by forcing or tricking the replacement of a good component with a defective or corrupted component, an adversary can leverage known defects to obtain a desired malicious impact.

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
- 534: https://capec.mitre.org/data/definitions/534.html
- Reviewed: 2026-10-27
