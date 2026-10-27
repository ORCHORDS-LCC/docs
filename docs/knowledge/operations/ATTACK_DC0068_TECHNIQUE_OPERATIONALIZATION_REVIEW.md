# Active Directory Object Deletion Technique Operationalization Review

## Reference

- Technique: **DC0068 — Active Directory Object Deletion**

Object deletion in AD (e.g., user accounts, groups, OUs) is logged as Event ID 5141. Examples: - User Account: Deleted user. - Group: Deleted security/distribution group. - Organizational Unit (OU): Loss of configurations or policies. - Service Account: Disrupted operations or cover tracks. - Trust Object: Removed domain trust, disrupting connectivity. *Data Collection Measures:* - Audit Policy: - Enable "Audit Directory Service Changes" (Success and Failure). - Path: `Computer Configuration > Policies > Windows Settings > Security Settings > Advanced Audit Policy Configuration > Audit Policies > Directory Service Changes`. - Key Event: Event ID 5141. - Log Forwarding: Use WEF to centralize logs for SIEM tools (e.g., Splunk). - Enable EDR Monitoring: - Detect processes or users that initiate unauthorized object deletions. - Monitor tools and scripts that may delete key directory objects.

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
- DC0068: https://attack.mitre.org/datacomponents/DC0068
- Reviewed: 2026-10-27
