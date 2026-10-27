# Lifecycle-Triggered Deletion Technique Response Playbook

## Target technique

**T1485.001 — Lifecycle-Triggered Deletion**

- Tactics: impact
- Platforms: IaaS

Adversaries may modify the lifecycle policies of a cloud storage bucket to destroy all objects stored within. Cloud storage buckets often allow users to set lifecycle policies to automate the migration, archival, or deletion of objects after a set period of time. If a threat actor has sufficient permissions to modify these policies, they may be able to delete all objects at once. For example, in AWS environments, an adversary with the `PutLifecycleConfiguration` permission may use the `PutBucketLifecycle` API call to apply a lifecycle policy to an S3 bucket that deletes all objects in the bucket after one day. In addition to destroying data for purposes of extortion and Financial Theft, adversaries may also perform this action on buckets storing cloud logs for Indicator Removal.

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
- T1485.001: https://attack.mitre.org/techniques/T1485/001
- Reviewed: 2026-10-27
