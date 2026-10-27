# Cloud Storage Metadata Technique Response Playbook

## Target technique

**DC0027 — Cloud Storage Metadata**


Cloud Storage Metadata provides contextual information about cloud storage infrastructure and its associated activity. This data may include attributes such as storage name, size, owner, permissions, creation date, region, and activity metadata. It is essential for monitoring, auditing, and identifying anomalies in cloud storage environments. Examples: - AWS S3 Bucket Metadata: Metadata about an S3 bucket includes the bucket name, region, creation date, owner, storage class, and permissions. - Azure Blob Storage Metadata: Metadata for an Azure Blob container includes container name, access level (e.g., private or public), size, and tags. - Google Cloud Storage Metadata: Metadata includes bucket name, storage class, location, labels, lifecycle policies, and versioning status. - OpenStack Swift Metadata: Metadata for a Swift container includes name, access level, quota, and custom attributes.

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
- DC0027: https://attack.mitre.org/datacomponents/DC0027
- Reviewed: 2026-10-27
