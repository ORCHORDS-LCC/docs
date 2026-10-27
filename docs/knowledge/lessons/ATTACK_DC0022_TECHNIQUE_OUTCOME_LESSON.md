# DC0022 Cloud Storage Deletion Outcome Lesson

## Authoritative description

- Technique: **DC0022 — Cloud Storage Deletion**

Cloud Storage Deletion refers to the removal or destruction of cloud storage infrastructure, such as buckets, containers, or directories, within a cloud environment. Monitoring this activity is critical to detecting potential unauthorized or malicious actions, such as data destruction by adversaries or accidental deletions that may lead to data loss. Examples: - AWS S3 Bucket Deletion: An AWS user deletes an S3 bucket using the `DeleteBucket` API call. - Azure Blob Storage Container Deletion: A user deletes a container in Azure Blob Storage using the `Delete Container` operation. - Google Cloud Storage Bucket Deletion: A Google Cloud user deletes a bucket using the `storage.buckets.delete` API. - OpenStack Swift Container Deletion: A user deletes a container in OpenStack Swift using the `DELETE` method. This data component can be collected through the following measures: Enable Logging for Cloud Storage Services - AWS S3: Enable AWS CloudTrail to log DeleteBucket API actions. - Azure Blob Storage: Enable Azure Monitor and Diagnostic Logs to capture Delete Container operations. Use Azure Event Grid to capture and trigger alerts for container deletion. - Google Cloud Storage: Enable Data Access logs in Cloud Audit Logs to monitor storage.buckets.delete API calls. - OpenStack Swift: Configure Swift logging to capture DELETE requests for containers. Centralized Logging and Analysis - Use platforms like Splunk or native SIEMs to forward and analyze logs for anomalies in cloud storage deletions.

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
- DC0022: https://attack.mitre.org/datacomponents/DC0022
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
