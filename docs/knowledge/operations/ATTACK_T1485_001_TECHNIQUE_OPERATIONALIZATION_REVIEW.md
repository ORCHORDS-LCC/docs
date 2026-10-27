# Lifecycle-Triggered Deletion Technique Operationalization Review

## Reference

- Technique: **T1485.001 — Lifecycle-Triggered Deletion**

Adversaries may modify the lifecycle policies of a cloud storage bucket to destroy all objects stored within. Cloud storage buckets often allow users to set lifecycle policies to automate the migration, archival, or deletion of objects after a set period of time. If a threat actor has sufficient permissions to modify these policies, they may be able to delete all objects at once. For example, in AWS environments, an adversary with the `PutLifecycleConfiguration` permission may use the `PutBucketLifecycle` API call to apply a lifecycle policy to an S3 bucket that deletes all objects in the bucket after one day. In addition to destroying data for purposes of extortion and Financial Theft, adversaries may also perform this action on buckets storing cloud logs for Indicator Removal.

## Operationalization review

1. Record the operational scope: which services, environments, and data the technique could affect.
2. Record the runbook that would be executed, and its owner.
3. Record the telemetry the runbook depends on, and whether it is retained long enough to investigate.
4. Record the detection that would surface the technique before or after it has an effect.
5. Record the recovery path, and the evidence that recovery has been rehearsed.
6. Record the residual operational risk where the runbook depends on a manual step.

## Review evidence

- the runbook and its owner;
- the telemetry retention and coverage record;
- the detection mapping;
- the exercise or rehearsal record.

## Limitations

An operationalization review describes the runbook and the evidence around it. It does not claim the technique has been prevented or detected in a live environment.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1485.001: https://attack.mitre.org/techniques/T1485/001
- Reviewed: 2026-10-27
