# Active Directory Object Deletion Technique Response Playbook

## Target technique

**DC0068 — Active Directory Object Deletion**


Object deletion in AD (e.g., user accounts, groups, OUs) is logged as Event ID 5141. Examples: - User Account: Deleted user. - Group: Deleted security/distribution group. - Organizational Unit (OU): Loss of configurations or policies. - Service Account: Disrupted operations or cover tracks. - Trust Object: Removed domain trust, disrupting connectivity. *Data Collection Measures:* - Audit Policy: - Enable "Audit Directory Service Changes" (Success and Failure). - Path: `Computer Configuration > Policies > Windows Settings > Security Settings > Advanced Audit Policy Configuration > Audit Policies > Directory Service Changes`. - Key Event: Event ID 5141. - Log Forwarding: Use WEF to centralize logs for SIEM tools (e.g., Splunk). - Enable EDR Monitoring: - Detect processes or users that initiate unauthorized object deletions. - Monitor tools and scripts that may delete key directory objects.

## Preconditions

- the estate in scope is identified, with the systems the technique could apply to;
- an owner is accountable for detection and response;
- current telemetry and configuration can be inspected;
- the technique is applicable or requires an applicability decision.

## Procedure

1. Confirm the scope and owner.
2. Read the current technique description and the associated detection guidance.
3. Inventory the telemetry that would carry the technique's indicators.
4. Inspect whether the indicators are present in the environment.
5. Exercise the detection path and confirm it produces the expected signal.
6. Record gaps in detection coverage and assign remediation owners.
7. Record justified non-applicability or accepted detection gaps separately.
8. Set the next event-driven or periodic verification trigger.

## Failure handling

If the detection path does not produce the expected signal, treat the coverage as unverified, preserve the test evidence, and route the gap through the appropriate remediation or risk process.

## Completion evidence

Scope, owner, source version, telemetry inspected, tests performed, findings, exceptions, remediation links, reviewer, and next trigger.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- DC0068: https://attack.mitre.org/datacomponents/DC0068
- Reviewed: 2026-10-27
