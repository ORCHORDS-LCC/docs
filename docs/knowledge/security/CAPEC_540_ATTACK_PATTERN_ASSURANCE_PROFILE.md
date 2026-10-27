# Overread Buffers Attack Pattern Assurance Profile

## Reference

- Attack pattern: **540 — Overread Buffers**
- Status: Draft

## Pattern description

An adversary attacks a target by providing input that causes an application to read beyond the boundary of a defined buffer. This typically occurs when a value influencing where to start or stop reading is set to reflect positions outside of the valid memory location of the buffer. This type of attack may result in exposure of sensitive information, a system crash, or arbitrary code execution.

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
- 540: https://capec.mitre.org/data/definitions/540.html
- Reviewed: 2026-10-27
