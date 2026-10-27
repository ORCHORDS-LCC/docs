# DC0049 Snapshot Deletion Outcome Lesson

## Authoritative description

- Technique: **DC0049 — Snapshot Deletion**

The removal of a point-in-time backup of a cloud storage volume, virtual machine (VM), or database. *Data Collection Measures:* - AWS CloudTrail - Logs `DeleteSnapshot` API calls in EC2, RDS, and EBS services. - Azure Monitor Logs - Tracks snapshot deletions via `Microsoft.Compute/snapshots/delete` API calls. - Google Cloud Logging - Detects snapshot removal through `compute.disks.deleteSnapshot` events.

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
- DC0049: https://attack.mitre.org/datacomponents/DC0049
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
