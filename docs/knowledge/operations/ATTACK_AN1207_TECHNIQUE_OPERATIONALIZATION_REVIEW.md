# Analytic 1207 Technique Operationalization Review

## Reference

- Technique: **AN1207 — Analytic 1207**

Abuse of mavinject.exe to inject DLLs or import descriptors into another running process. Chain: (1) mavinject.exe starts with /INJECTRUNNING or /HMODULE → (2) mavinject obtains high-access handles to a target process (VM_WRITE/CREATE_THREAD) → (3) target process loads attacker DLL (module load) → (4) optional follow-on child activity or network egress from the target process.

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
- AN1207: https://attack.mitre.org/detectionstrategies/DET0433#AN1207
- Reviewed: 2026-10-27
