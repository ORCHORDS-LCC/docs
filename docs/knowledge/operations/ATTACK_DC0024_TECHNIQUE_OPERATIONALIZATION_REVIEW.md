# Cloud Storage Creation Technique Operationalization Review

## Reference

- Technique: **DC0024 — Cloud Storage Creation**

Cloud Storage Creation refers to the initial creation of a new cloud storage resource, such as buckets, containers, or directories, within a cloud environment. This action is critical to track as it might indicate the legitimate provisioning of resources or unauthorized actions taken by adversaries to stage, store, or exfiltrate data. Examples: - AWS S3 Bucket Creation: An AWS user creates a new S3 bucket using the `CreateBucket` API call. - Azure Blob Storage Container Creation: A user creates a new container in Azure Blob Storage using the `Create Container` operation. - Google Cloud Storage Bucket Creation: A Google Cloud user creates a new bucket using `storage.buckets.create`. - OpenStack Swift Container Creation: A user creates a new container in OpenStack Swift using the `PUT` method.

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
- DC0024: https://attack.mitre.org/datacomponents/DC0024
- Reviewed: 2026-10-27
