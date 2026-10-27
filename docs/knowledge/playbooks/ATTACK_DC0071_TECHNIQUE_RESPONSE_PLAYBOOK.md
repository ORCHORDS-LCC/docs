# Active Directory Object Access Technique Response Playbook

## Target technique

**DC0071 — Active Directory Object Access**


Object access refers to activities where AD objects (e.g., user accounts, groups, policies) are accessed or queried. Example: Windows Event ID 4661 logs object access attempts. Examples: - Attribute Access: e.g., `userPassword`, `memberOf`, `securityDescriptor`. - Group Enumeration: Enumerating critical group members (e.g., Domain Admins). - User Attributes: Commonly accessed attributes like `samAccountName`, `lastLogonTimestamp`. - Policy Access: Accessing GPOs to understand security settings. *Data Collection Measures:* - Audit Policies: - Enable "Audit Directory Service Access" under Advanced Audit Policies (Success and Failure). - Path: `Computer Configuration > Policies > Windows Settings > Security Settings > Advanced Audit Policy Configuration > Audit Policies > Object AccessEnable: Audit Directory Service Access` (Success and Failure). - Captured Events: IDs 4661, 4662. - Event Forwarding: Use WEF to centralize logs for SIEM analysis. - SIEM Integration: Collect and parse logs (e.g., 4661, 4662) using tools like Splunk or Azure Sentinel. - Log Filtering: - Focus on sensitive objects/attributes like: - `Domain Admins` group. - `userPassword`, `ntSecurityDescriptor`. - Enable EDR Monitoring: - Detect processes accessing sensitive AD objects (e.g., samAccountName, securityDescriptor). - Log all attempts to enumerate critical groups (e.g., "Domain Admins").

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
- DC0071: https://attack.mitre.org/datacomponents/DC0071
- Reviewed: 2026-10-27
