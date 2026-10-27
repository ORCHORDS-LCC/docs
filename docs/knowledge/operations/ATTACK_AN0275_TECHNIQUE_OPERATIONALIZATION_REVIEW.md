# Analytic 0275 Technique Operationalization Review

## Reference

- Technique: **AN0275 — Analytic 0275**

Unexpected write operations to BIOS/UEFI firmware regions or EFI boot partitions that do not correlate with legitimate vendor firmware updates. API calls or utilities such as fwupdate.exe or vendor flash tools executed from non-administrative or non-IT management accounts. Suspicious raw disk writes targeting System Firmware GUID partitions followed by abnormal reboot sequences.

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
- AN0275: https://attack.mitre.org/detectionstrategies/DET0099#AN0275
- Reviewed: 2026-10-27
