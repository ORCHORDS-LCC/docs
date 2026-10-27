# Influence via Psychological Principles Attack Pattern Assurance Profile

## Reference

- Attack pattern: **427 — Influence via Psychological Principles**
- Status: Draft

## Pattern description

The adversary shapes the target's actions or behavior by focusing on the ways human interact and learn, leveraging such elements as cognitive and social psychology. In a variety of ways, a target can be influenced to behave or perform an action through capitalizing on what scholarship and research has learned about how and why humans react to specific scenarios and cues.

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
- 427: https://capec.mitre.org/data/definitions/427.html
- Reviewed: 2026-10-27
