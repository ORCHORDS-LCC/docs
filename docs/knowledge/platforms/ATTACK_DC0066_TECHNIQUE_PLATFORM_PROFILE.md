# Active Directory Object Modification Technique Platform Profile

## Reference

- Technique: **DC0066 — Active Directory Object Modification**
- Platforms named in the source: not stated

Changes to AD objects (e.g., users, groups, OUs) are logged as Event ID 5136 (Object Modification) or 5163 (Attribute Changes). Examples: - User Account: Modifying attributes (e.g., group membership, enabling/disabling accounts). - Group Membership: Adding/removing members. - OU: Changing properties/permissions (e.g., delegation). - Service Account: Modifying SPNs or other attributes. - Object Attributes: Changes to passwords, logon hours, or control flags.

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
- DC0066: https://attack.mitre.org/datacomponents/DC0066
- Reviewed: 2026-10-27
