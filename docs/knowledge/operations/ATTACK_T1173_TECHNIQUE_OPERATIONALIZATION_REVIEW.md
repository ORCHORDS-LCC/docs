# Dynamic Data Exchange Mitigation Technique Operationalization Review

## Reference

- Technique: **T1173 — Dynamic Data Exchange Mitigation**

Registry keys specific to Microsoft Office feature control security can be set to disable automatic DDE/OLE execution. Microsoft also created, and enabled by default, Registry keys to completely disable DDE execution in Word and Excel. Ensure Protected View is enabled and consider disabling embedded files in Office programs, such as OneNote, not enrolled in Protected View. On Windows 10, enable Attack Surface Reduction (ASR) rules to prevent DDE attacks and spawning of child processes from Office programs.

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
- T1173: https://attack.mitre.org/mitigations/T1173
- Reviewed: 2026-10-27
