# Mini Shai-Hulud Technique Operationalization Review

## Reference

- Technique: **S9043 — Mini Shai-Hulud**

Mini Shai-Hulud is a credential stealer and self-replicating supply chain worm, derived from Shai-Hulud, that has been used by TeamPCP to target Continuous Integration and Continuous Delivery/Deployment (CI/CD) workflows since at least 2026. Mini Shai-Hulud can compromise credentials across multiple cloud, container, and AI configuration file paths and can use stolen npm and GitHub OIDC tokens to spread to other packages maintained by the compromised user. Mini Shai-Hulud also has a targeted wiper component and has used multiple C2 and data exfiltration mechanisms.

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
- S9043: https://attack.mitre.org/software/S9043
- Reviewed: 2026-10-27
