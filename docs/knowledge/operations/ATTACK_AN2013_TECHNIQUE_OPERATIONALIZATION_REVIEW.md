# Analytic 2013 Technique Operationalization Review

## Reference

- Technique: **AN2013 — Analytic 2013**

If infrastructure or patterns in the malicious web content related to SEO poisoning or Drive-by Target have been previously identified, internet scanning may uncover when an adversary has staged web content supporting a strategic web compromise. Much of this activity will take place outside the visibility of the target organization, making detection of this behavior difficult. Detection efforts may be focused on other phases of the adversary lifecycle, such as Drive-by Compromise or Exploitation for Client Execution.

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
- AN2013: https://attack.mitre.org/detectionstrategies/DET0881#AN2013
- Reviewed: 2026-10-27
