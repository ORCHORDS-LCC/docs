# Cloud Storage Access Technique Response Playbook

## Target technique

**DC0025 — Cloud Storage Access**


Cloud storage access refers to the retrieval or interaction with data stored in cloud infrastructure. This data component includes activities such as reading, downloading, or accessing files and objects within cloud storage systems. Common examples include API calls like GetObject in AWS S3, which retrieves objects from cloud buckets. Examples: - AWS S3 Access: An adversary uses the `GetObject` API to retrieve sensitive data from an AWS S3 bucket. - Azure Blob Storage Access: A user accesses a blob in Azure Storage using `Get Blob` or `Get Blob Properties`. - Google Cloud Storage Access: An adversary uses `storage.objects.get` to download objects from - OpenStack Swift Storage Access: A user retrieves an object from OpenStack Swift using the `GET` method.

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
- DC0025: https://attack.mitre.org/datacomponents/DC0025
- Reviewed: 2026-10-27
