# Active Directory Object Creation Technique Operationalization Review

## Reference

- Technique: **DC0087 — Active Directory Object Creation**

Creating new objects in AD, such as user accounts, groups, organizational units (OUs), or trust relationships. Logged as Event ID 5137. Examples: - User Account Creation: New user account. - Group Creation: New security/distribution group. - OU Creation: New organizational unit. - Service Account Creation: New service account for automation or malicious tasks. - Trust Object Creation: Trust relationship with another domain.

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
- DC0087: https://attack.mitre.org/datacomponents/DC0087
- Reviewed: 2026-10-27
