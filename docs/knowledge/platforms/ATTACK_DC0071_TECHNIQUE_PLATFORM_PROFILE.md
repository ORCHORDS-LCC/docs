# Active Directory Object Access Technique Platform Profile

## Reference

- Technique: **DC0071 — Active Directory Object Access**
- Platforms named in the source: not stated

Object access refers to activities where AD objects (e.g., user accounts, groups, policies) are accessed or queried. Example: Windows Event ID 4661 logs object access attempts. Examples: - Attribute Access: e.g., `userPassword`, `memberOf`, `securityDescriptor`. - Group Enumeration: Enumerating critical group members (e.g., Domain Admins). - User Attributes: Commonly accessed attributes like `samAccountName`, `lastLogonTimestamp`. - Policy Access: Accessing GPOs to understand security settings. *Data Collection Measures:* - Audit Policies: - Enable "Audit Directory Service Access" under Advanced Audit Policies (Success and Failure). - Path: `Computer Configuration > Policies > Windows Settings > Security Settings > Advanced Audit Policy Configuration > Audit Policies > Object AccessEnable: Audit Directory Service Access` (Success and Failure). - Captured Events: IDs 4661, 4662. - Event Forwarding: Use WEF to centralize logs for SIEM analysis. - SIEM Integration: Collect and parse logs (e.g., 4661, 4662) using tools like Splunk or Azure Sentinel. - Log Filtering: - Focus on sensitive objects/attributes like: - `Domain Admins` group. - `userPassword`, `ntSecurityDescriptor`. - Enable EDR Monitoring: - Detect processes accessing sensitive AD objects (e.g., samAccountName, securityDescriptor). - Log all attempts to enumerate critical groups (e.g., "Domain Admins").

## Platform profile

1. Record the platforms in scope and the versions actually deployed.
2. Compare the deployed platform surface against the platforms the source names.
3. Record where the platform provides a native control for the technique, and where it does not.
4. Record the configuration evidence for the native control, where one exists.
5. Record the gap where the platform provides no native control, and the compensating detection.
6. Record the platform version, because platform behaviour changes between versions.

## Evidence

- the platform and version inventory for the scoped estate;
- the configuration export or screenshot for the native control;
- the detection evidence where the platform provides none.

## Limitations

A technique entry describes a class of abuse across platforms. The platform-specific exposure is a property of the deployment, established only by inventory and configuration evidence.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- DC0071: https://attack.mitre.org/datacomponents/DC0071
- Reviewed: 2026-10-27
