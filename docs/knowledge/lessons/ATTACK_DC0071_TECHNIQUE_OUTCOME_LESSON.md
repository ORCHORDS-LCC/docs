# DC0071 Active Directory Object Access Outcome Lesson

## Authoritative description

- Technique: **DC0071 — Active Directory Object Access**

Object access refers to activities where AD objects (e.g., user accounts, groups, policies) are accessed or queried. Example: Windows Event ID 4661 logs object access attempts. Examples: - Attribute Access: e.g., `userPassword`, `memberOf`, `securityDescriptor`. - Group Enumeration: Enumerating critical group members (e.g., Domain Admins). - User Attributes: Commonly accessed attributes like `samAccountName`, `lastLogonTimestamp`. - Policy Access: Accessing GPOs to understand security settings. *Data Collection Measures:* - Audit Policies: - Enable "Audit Directory Service Access" under Advanced Audit Policies (Success and Failure). - Path: `Computer Configuration > Policies > Windows Settings > Security Settings > Advanced Audit Policy Configuration > Audit Policies > Object AccessEnable: Audit Directory Service Access` (Success and Failure). - Captured Events: IDs 4661, 4662. - Event Forwarding: Use WEF to centralize logs for SIEM analysis. - SIEM Integration: Collect and parse logs (e.g., 4661, 4662) using tools like Splunk or Azure Sentinel. - Log Filtering: - Focus on sensitive objects/attributes like: - `Domain Admins` group. - `userPassword`, `ntSecurityDescriptor`. - Enable EDR Monitoring: - Detect processes accessing sensitive AD objects (e.g., samAccountName, securityDescriptor). - Log all attempts to enumerate critical groups (e.g., "Domain Admins").

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
- DC0071: https://attack.mitre.org/datacomponents/DC0071
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
