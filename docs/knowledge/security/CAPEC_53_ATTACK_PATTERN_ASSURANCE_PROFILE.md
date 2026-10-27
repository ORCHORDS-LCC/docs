# Postfix, Null Terminate, and Backslash Attack Pattern Assurance Profile

## Reference

- Attack pattern: **53 — Postfix, Null Terminate, and Backslash**
- Status: Draft

## Pattern description

If a string is passed through a filter of some kind, then a terminal NULL may not be valid. Using alternate representation of NULL allows an adversary to embed the NULL mid-string while postfixing the proper data so that the filter is avoided. One example is a filter that looks for a trailing slash character. If a string insertion is possible, but the slash must exist, an alternate encoding of NULL in mid-string may be used.

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
- 53: https://capec.mitre.org/data/definitions/53.html
- Reviewed: 2026-10-27
