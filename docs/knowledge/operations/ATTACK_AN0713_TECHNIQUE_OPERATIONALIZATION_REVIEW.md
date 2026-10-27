# Analytic 0713 Technique Operationalization Review

## Reference

- Technique: **AN0713 — Analytic 0713**

Defender observes unauthorized modification or creation of Python hook files such as `.pth`, `sitecustomize.py`, or `usercustomize.py` in Python `site-packages`, `dist-packages`, or user paths. This is often correlated with subsequent unexpected interpreter execution (e.g., python3 running without user interaction), changes in interpreter behavior (e.g., malicious imports), and outbound connections initiated from Python. Defender links write/modify actions on hook files with execve of python process and/or anomalous child process or network activity.

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
- AN0713: https://attack.mitre.org/detectionstrategies/DET0258#AN0713
- Reviewed: 2026-10-27
