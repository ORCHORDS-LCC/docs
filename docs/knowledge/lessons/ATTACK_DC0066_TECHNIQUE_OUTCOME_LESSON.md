# DC0066 Active Directory Object Modification Outcome Lesson

## Authoritative description

- Technique: **DC0066 — Active Directory Object Modification**

Changes to AD objects (e.g., users, groups, OUs) are logged as Event ID 5136 (Object Modification) or 5163 (Attribute Changes). Examples: - User Account: Modifying attributes (e.g., group membership, enabling/disabling accounts). - Group Membership: Adding/removing members. - OU: Changing properties/permissions (e.g., delegation). - Service Account: Modifying SPNs or other attributes. - Object Attributes: Changes to passwords, logon hours, or control flags.

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
- DC0066: https://attack.mitre.org/datacomponents/DC0066
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
