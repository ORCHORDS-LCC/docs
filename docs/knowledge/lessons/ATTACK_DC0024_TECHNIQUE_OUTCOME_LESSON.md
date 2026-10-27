# DC0024 Cloud Storage Creation Outcome Lesson

## Authoritative description

- Technique: **DC0024 — Cloud Storage Creation**

Cloud Storage Creation refers to the initial creation of a new cloud storage resource, such as buckets, containers, or directories, within a cloud environment. This action is critical to track as it might indicate the legitimate provisioning of resources or unauthorized actions taken by adversaries to stage, store, or exfiltrate data. Examples: - AWS S3 Bucket Creation: An AWS user creates a new S3 bucket using the `CreateBucket` API call. - Azure Blob Storage Container Creation: A user creates a new container in Azure Blob Storage using the `Create Container` operation. - Google Cloud Storage Bucket Creation: A Google Cloud user creates a new bucket using `storage.buckets.create`. - OpenStack Swift Container Creation: A user creates a new container in OpenStack Swift using the `PUT` method.

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
- DC0024: https://attack.mitre.org/datacomponents/DC0024
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
