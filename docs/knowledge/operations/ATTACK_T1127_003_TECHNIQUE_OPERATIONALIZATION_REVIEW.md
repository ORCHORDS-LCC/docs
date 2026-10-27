# JamPlus Technique Operationalization Review

## Reference

- Technique: **T1127.003 — JamPlus**

Adversaries may use `JamPlus` to proxy the execution of a malicious script. `JamPlus` is a build utility tool for code and data build systems. It works with several popular compilers and can be used for generating workspaces in code editors such as Visual Studio. Adversaries may abuse the `JamPlus` build utility to execute malicious scripts via a `.jam` file, which describes the build process and required dependencies. Because the malicious script is executed from a reputable developer tool, it may subvert application control security systems such as Smart App Control.

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
- T1127.003: https://attack.mitre.org/techniques/T1127/003
- Reviewed: 2026-10-27
