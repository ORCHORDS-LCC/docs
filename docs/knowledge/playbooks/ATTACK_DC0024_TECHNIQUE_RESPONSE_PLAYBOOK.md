# Cloud Storage Creation Technique Response Playbook

## Target technique

**DC0024 — Cloud Storage Creation**


Cloud Storage Creation refers to the initial creation of a new cloud storage resource, such as buckets, containers, or directories, within a cloud environment. This action is critical to track as it might indicate the legitimate provisioning of resources or unauthorized actions taken by adversaries to stage, store, or exfiltrate data. Examples: - AWS S3 Bucket Creation: An AWS user creates a new S3 bucket using the `CreateBucket` API call. - Azure Blob Storage Container Creation: A user creates a new container in Azure Blob Storage using the `Create Container` operation. - Google Cloud Storage Bucket Creation: A Google Cloud user creates a new bucket using `storage.buckets.create`. - OpenStack Swift Container Creation: A user creates a new container in OpenStack Swift using the `PUT` method.

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
- DC0024: https://attack.mitre.org/datacomponents/DC0024
- Reviewed: 2026-10-27
