# Analytic 0263 Technique Operationalization Review

## Reference

- Technique: **AN0263 — Analytic 0263**

Adversary uses a tool like Ruler or MFCMapi to create a malicious Outlook rule that triggers execution upon receipt of a crafted email. On email delivery, Outlook executes the rule, resulting in code execution (e.g., launching mshta.exe or PowerShell). Outlook spawns a non-standard child process, often unsanctioned, without user interaction.

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
- AN0263: https://attack.mitre.org/detectionstrategies/DET0095#AN0263
- Reviewed: 2026-10-27
