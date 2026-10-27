# DC0047 Snapshot Enumeration Outcome Lesson

## Authoritative description

- Technique: **DC0047 — Snapshot Enumeration**

The process of listing or retrieving metadata about existing snapshots in a cloud environment. *Data Collection Measures:* - AWS CloudTrail - Logs API calls such as `DescribeSnapshots`, `ListSnapshots`, and `GetSnapshotAttributes`. - Azure Monitor Logs - Tracks snapshot enumeration via `Microsoft.Compute/snapshots/read`. - Google Cloud Logging - Detects snapshot listing through `compute.disks.listSnapshots`.

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
- DC0047: https://attack.mitre.org/datacomponents/DC0047
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
