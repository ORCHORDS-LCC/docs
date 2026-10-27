# T1485.001 Lifecycle-Triggered Deletion Outcome Lesson

## Authoritative description

- Technique: **T1485.001 — Lifecycle-Triggered Deletion**
- Tactics: impact
- Platforms: IaaS

Adversaries may modify the lifecycle policies of a cloud storage bucket to destroy all objects stored within. Cloud storage buckets often allow users to set lifecycle policies to automate the migration, archival, or deletion of objects after a set period of time. If a threat actor has sufficient permissions to modify these policies, they may be able to delete all objects at once. For example, in AWS environments, an adversary with the `PutLifecycleConfiguration` permission may use the `PutBucketLifecycle` API call to apply a lifecycle policy to an S3 bucket that deletes all objects in the bucket after one day. In addition to destroying data for purposes of extortion and Financial Theft, adversaries may also perform this action on buckets storing cloud logs for Indicator Removal.

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
- T1485.001: https://attack.mitre.org/techniques/T1485/001
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
