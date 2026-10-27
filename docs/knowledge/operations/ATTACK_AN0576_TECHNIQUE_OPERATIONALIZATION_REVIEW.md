# Analytic 0576 Technique Operationalization Review

## Reference

- Technique: **AN0576 — Analytic 0576**

Cause→effect chain: (1) A user or service launches an indirection utility (e.g., forfiles.exe, pcalua.exe, wsl.exe, scriptrunner.exe, ssh.exe with -o ProxyCommand/LocalCommand). (2) That utility spawns a secondary program/command (PowerShell, cmd, msiexec, regsvr32, curl, arbitrary EXE) and/or opens outbound network connections. (3) Optional precursor modification of SSH config to persist LocalCommand/ProxyCommand. Correlate process creation, command/script content, file access to %USERPROFILE%\.ssh\config, and network connections from the utility or its child.

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
- AN0576: https://attack.mitre.org/detectionstrategies/DET0200#AN0576
- Reviewed: 2026-10-27
