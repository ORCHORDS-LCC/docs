# Shai-Hulud Technique Operationalization Review

## Reference

- Technique: **S9008 — Shai-Hulud**

Shai-Hulud is a supply chain worm, first reported in September 2025, that spreads through code repositories, including GitHub and NPM packages. It exploits CI/CD pipeline dependencies to propagate to victims and poisons the supply chain by publishing malicious packages. Once inside a victim environment, Shai-Hulud steals credentials and access tokens from compromised repository accounts and exfiltrates them to attacker-controlled servers via encoded GitHub Actions workflows.

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
- S9008: https://attack.mitre.org/software/S9008
- Reviewed: 2026-10-27
