# PUBLOAD Technique Operationalization Review

## Reference

- Technique: **S1228 — PUBLOAD**

PUBLOAD is a stager malware that has been observed installing itself in existing directories such as `C:\Users\Public` or creating new directories to stage the malware and its components. PUBLOAD malware collects details of the victim host, establishes persistence, encrypts victim details using RC4 and communicates victim details back to C2. PUBLOAD malware has previously been leveraged by China-affiliated actors identified as Mustang Panda. PUBLOAD is also known as “NoFive” and some public reporting identifies the loader component as CLAIMLOADER.

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
- S1228: https://attack.mitre.org/software/S1228
- Reviewed: 2026-10-27
