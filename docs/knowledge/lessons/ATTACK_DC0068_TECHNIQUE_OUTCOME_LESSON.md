# DC0068 Active Directory Object Deletion Outcome Lesson

## Authoritative description

- Technique: **DC0068 — Active Directory Object Deletion**

Object deletion in AD (e.g., user accounts, groups, OUs) is logged as Event ID 5141. Examples: - User Account: Deleted user. - Group: Deleted security/distribution group. - Organizational Unit (OU): Loss of configurations or policies. - Service Account: Disrupted operations or cover tracks. - Trust Object: Removed domain trust, disrupting connectivity. *Data Collection Measures:* - Audit Policy: - Enable "Audit Directory Service Changes" (Success and Failure). - Path: `Computer Configuration > Policies > Windows Settings > Security Settings > Advanced Audit Policy Configuration > Audit Policies > Directory Service Changes`. - Key Event: Event ID 5141. - Log Forwarding: Use WEF to centralize logs for SIEM tools (e.g., Splunk). - Enable EDR Monitoring: - Detect processes or users that initiate unauthorized object deletions. - Monitor tools and scripts that may delete key directory objects.

## Reusable lesson

This technique should be treated as an explicit review question when it is relevant to the system or organisation, rather than assumed to be covered by a generic control statement or by tooling that reports a related signal.

## Apply the lesson

1. Define the real scope before judging coverage.
2. Inspect current technical, process, governance, or operational evidence.
3. Separate documented intent from verified behaviour.
4. Record partial coverage and unresolved gaps instead of converting them into a pass.
5. Revisit when the underlying scope, threat environment, technology, suppliers, or mission materially changes.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- DC0068: https://attack.mitre.org/datacomponents/DC0068
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
