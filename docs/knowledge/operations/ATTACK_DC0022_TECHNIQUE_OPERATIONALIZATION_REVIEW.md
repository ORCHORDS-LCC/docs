# Cloud Storage Deletion Technique Operationalization Review

## Reference

- Technique: **DC0022 — Cloud Storage Deletion**

Cloud Storage Deletion refers to the removal or destruction of cloud storage infrastructure, such as buckets, containers, or directories, within a cloud environment. Monitoring this activity is critical to detecting potential unauthorized or malicious actions, such as data destruction by adversaries or accidental deletions that may lead to data loss. Examples: - AWS S3 Bucket Deletion: An AWS user deletes an S3 bucket using the `DeleteBucket` API call. - Azure Blob Storage Container Deletion: A user deletes a container in Azure Blob Storage using the `Delete Container` operation. - Google Cloud Storage Bucket Deletion: A Google Cloud user deletes a bucket using the `storage.buckets.delete` API. - OpenStack Swift Container Deletion: A user deletes a container in OpenStack Swift using the `DELETE` method. This data component can be collected through the following measures: Enable Logging for Cloud Storage Services - AWS S3: Enable AWS CloudTrail to log DeleteBucket API actions. - Azure Blob Storage: Enable Azure Monitor and Diagnostic Logs to capture Delete Container operations. Use Azure Event Grid to capture and trigger alerts for container deletion. - Google Cloud Storage: Enable Data Access logs in Cloud Audit Logs to monitor storage.buckets.delete API calls. - OpenStack Swift: Configure Swift logging to capture DELETE requests for containers. Centralized Logging and Analysis - Use platforms like Splunk or native SIEMs to forward and analyze logs for anomalies in cloud storage deletions.

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
- DC0022: https://attack.mitre.org/datacomponents/DC0022
- Reviewed: 2026-10-27
