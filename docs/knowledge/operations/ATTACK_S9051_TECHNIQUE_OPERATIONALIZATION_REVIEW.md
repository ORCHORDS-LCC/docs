# The Gentlemen Ransomware Technique Operationalization Review

## Reference

- Technique: **S9051 — The Gentlemen Ransomware**

The Gentlemen Ransomware is a ransomware-as-a-service (RaaS). The Gentlemen Ransomware has been written in Go programming language and has utilized Garble to obfuscate its code to target Windows environments. The Gentlemen Ransomware is capable of executing its’ OS lockers in Windows, Linux, NAS, BSD and ESXi environments. The Gentlemen Ransomware was first observed in mid-2025 as a closed ransomware and shortly later emerged as a RaaS to affiliates in September 2025. The Gentlemen Ransomware has been affiliated with the threat group The Gentlemen.

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
- S9051: https://attack.mitre.org/software/S9051
- Reviewed: 2026-10-27
