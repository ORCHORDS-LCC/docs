# Force the System to Reset Values Attack Pattern Assurance Profile

## Reference

- Attack pattern: **166 — Force the System to Reset Values**
- Status: Draft

## Pattern description

An attacker forces the target into a previous state in order to leverage potential weaknesses in the target dependent upon a prior configuration or state-dependent factors. Even in cases where an attacker may not be able to directly control the configuration of the targeted application, they may be able to reset the configuration to a prior state since many applications implement reset functions.

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
- 166: https://capec.mitre.org/data/definitions/166.html
- Reviewed: 2026-10-27
