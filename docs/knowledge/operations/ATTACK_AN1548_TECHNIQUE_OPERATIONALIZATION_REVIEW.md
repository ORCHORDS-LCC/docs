# Analytic 1548 Technique Operationalization Review

## Reference

- Technique: **AN1548 — Analytic 1548**

Adversary installs or side-loads an IDE extension (VS Code, IntelliJ/JetBrains, Eclipse) or enables IDE tunneling. Chain: (1) IDE binary starts on a non-developer endpoint or server, often with install/force/tunnel flags → (2) extension files/registrations appear under user profile → (3) browser/IDE initiates outbound connections to extension marketplaces, update endpoints, or IDE remote/tunnel services → (4) optional child tools (ssh, node, powershell) execute under the IDE context.

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
- AN1548: https://attack.mitre.org/detectionstrategies/DET0561#AN1548
- Reviewed: 2026-10-27
