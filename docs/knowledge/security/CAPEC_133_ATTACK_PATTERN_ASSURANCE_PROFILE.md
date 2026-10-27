# Try All Common Switches Attack Pattern Assurance Profile

## Reference

- Attack pattern: **133 — Try All Common Switches**
- Status: Draft

## Pattern description

An attacker attempts to invoke all common switches and options in the target application for the purpose of discovering weaknesses in the target. For example, in some applications, adding a --debug switch causes debugging information to be displayed, which can sometimes reveal sensitive processing or configuration information to an attacker. This attack differs from other forms of API abuse in that the attacker is indiscriminately attempting to invoke options in the hope that one of them will work rather than specifically targeting a known option. Nonetheless, even if the attacker is familiar with the published options of a targeted application this attack method may still be fruitful as it might discover unpublicized functionality.

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
- 133: https://capec.mitre.org/data/definitions/133.html
- Reviewed: 2026-10-27
