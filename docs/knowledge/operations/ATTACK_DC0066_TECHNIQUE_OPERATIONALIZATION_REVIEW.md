# Active Directory Object Modification Technique Operationalization Review

## Reference

- Technique: **DC0066 — Active Directory Object Modification**

Changes to AD objects (e.g., users, groups, OUs) are logged as Event ID 5136 (Object Modification) or 5163 (Attribute Changes). Examples: - User Account: Modifying attributes (e.g., group membership, enabling/disabling accounts). - Group Membership: Adding/removing members. - OU: Changing properties/permissions (e.g., delegation). - Service Account: Modifying SPNs or other attributes. - Object Attributes: Changes to passwords, logon hours, or control flags.

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
- DC0066: https://attack.mitre.org/datacomponents/DC0066
- Reviewed: 2026-10-27
