# Analytic 1028 Technique Operationalization Review

## Reference

- Technique: **AN1028 — Analytic 1028**

Abuse of Regsvcs.exe or Regasm.exe to execute arbitrary code embedded in .NET assemblies via [ComRegisterFunction]/[ComUnregisterFunction]. Behavioral chain: (1) Process creation of regsvcs/regasm with suspicious assembly paths/flags → (2) Assembly/DLL load inside regsvcs/regasm → (3) Registry writes to HKCR\CLSID/ProgID during COM registration → (4) Optional child process or network activity spawned by installer/registration code.

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
- AN1028: https://attack.mitre.org/detectionstrategies/DET0361#AN1028
- Reviewed: 2026-10-27
