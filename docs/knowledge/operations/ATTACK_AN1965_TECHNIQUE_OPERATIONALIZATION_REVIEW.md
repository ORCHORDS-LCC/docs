# Analytic 1965 Technique Operationalization Review

## Reference

- Technique: **AN1965 — Analytic 1965**

Consider analyzing self-signed code signing certificates for features that may be associated with the adversary and/or their developers, such as the thumbprint, algorithm used, validity period, and common name. Malware repositories can also be used to identify additional samples associated with the adversary and identify patterns an adversary has used in crafting self-signed code signing certificates. Much of this activity will take place outside the visibility of the target organization, making detection of this behavior difficult. Detection efforts may be focused on related follow-on behavior, such as Code Signing or Install Root Certificate.

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
- AN1965: https://attack.mitre.org/detectionstrategies/DET0833#AN1965
- Reviewed: 2026-10-27
