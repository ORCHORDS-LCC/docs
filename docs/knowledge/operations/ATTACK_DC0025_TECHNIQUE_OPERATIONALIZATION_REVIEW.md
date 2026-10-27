# Cloud Storage Access Technique Operationalization Review

## Reference

- Technique: **DC0025 — Cloud Storage Access**

Cloud storage access refers to the retrieval or interaction with data stored in cloud infrastructure. This data component includes activities such as reading, downloading, or accessing files and objects within cloud storage systems. Common examples include API calls like GetObject in AWS S3, which retrieves objects from cloud buckets. Examples: - AWS S3 Access: An adversary uses the `GetObject` API to retrieve sensitive data from an AWS S3 bucket. - Azure Blob Storage Access: A user accesses a blob in Azure Storage using `Get Blob` or `Get Blob Properties`. - Google Cloud Storage Access: An adversary uses `storage.objects.get` to download objects from - OpenStack Swift Storage Access: A user retrieves an object from OpenStack Swift using the `GET` method.

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
- DC0025: https://attack.mitre.org/datacomponents/DC0025
- Reviewed: 2026-10-27
