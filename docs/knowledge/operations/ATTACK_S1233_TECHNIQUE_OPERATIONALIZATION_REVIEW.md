# PAKLOG Technique Operationalization Review

## Reference

- Technique: **S1233 — PAKLOG**

PAKLOG is a keylogger known to be leveraged by Mustang Panda and was first observed utilized in 2024. PAKLOG is deployed via a RAR archive (e.g., key.rar), which contains two files: a signed, legitimate binary (PACLOUD.exe) and the malicious PAKLOG DLL (pa_lang2.dll). The PACLOUD.exe binary is used to side-load the PAKLOG DLL which starts with the keylogger functionality.

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
- S1233: https://attack.mitre.org/software/S1233
- Reviewed: 2026-10-27
