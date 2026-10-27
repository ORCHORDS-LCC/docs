# File Creation Technique Operationalization Review

## Reference

- Technique: **DC0039 — File Creation**

A new file is created on a system or network storage. This action often signifies an operation such as saving a document, writing data, or deploying a file. Logging these events helps identify legitimate or potentially malicious file creation activities. Examples include logging file creation events (e.g., Sysmon Event ID 11 or Linux auditd logs).

## Operationalization review

1. Record the operational scope: which services, environments, and data the technique could affect.
2. Record the runbook that would be executed, and its owner.
3. Record the telemetry the runbook depends on, and whether it is retained long enough to investigate.
4. Record the detection that would surface the technique before or after it has an effect.
5. Record the recovery path, and the evidence that recovery has been rehearsed.
6. Record the residual operational risk where the runbook depends on a manual step.

## Review evidence

- the runbook and its owner;
- the telemetry retention and coverage record;
- the detection mapping;
- the exercise or rehearsal record.

## Limitations

An operationalization review describes the runbook and the evidence around it. It does not claim the technique has been prevented or detected in a live environment.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- DC0039: https://attack.mitre.org/datacomponents/DC0039
- Reviewed: 2026-10-27
