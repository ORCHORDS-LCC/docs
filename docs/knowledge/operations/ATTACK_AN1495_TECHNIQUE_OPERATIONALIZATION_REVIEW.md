# Analytic 1495 Technique Operationalization Review

## Reference

- Technique: **AN1495 — Analytic 1495**

Monitor registry modifications to `HKLM\SYSTEM\CurrentControlSet\Control\Lsa\Security Packages` or `...\OSConfig\Security Packages`, especially insertions of new DLL entries. Correlate this with subsequent DLL module loads into `lsass.exe`. Track unsigned or anomalous DLLs loading into LSASS using image load auditing. LSASS loads unsigned DLL due to AuditLevel=8 registry configuration or System reboot followed by DLL load into lsass.exe.

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
- AN1495: https://attack.mitre.org/detectionstrategies/DET0542#AN1495
- Reviewed: 2026-10-27
