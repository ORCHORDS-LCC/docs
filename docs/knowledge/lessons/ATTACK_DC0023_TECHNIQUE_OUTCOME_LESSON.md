# DC0023 Cloud Storage Modification Outcome Lesson

## Authoritative description

- Technique: **DC0023 — Cloud Storage Modification**

Cloud Storage Modification involves tracking changes made to cloud storage infrastructure, including updates to settings, permissions, or stored data. Examples include modifying object access control lists (ACLs), uploading new objects, or updating bucket policies. Examples: AWS S3: An object is uploaded or its ACL is modified. - Azure Blob Storage: A blob's metadata or permissions are updated. - Google Cloud Storage: An object's lifecycle policy is updated, or a bucket policy is changed. - OpenStack Swift: Modifications to container settings or uploading of new objects.

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
- DC0023: https://attack.mitre.org/datacomponents/DC0023
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
