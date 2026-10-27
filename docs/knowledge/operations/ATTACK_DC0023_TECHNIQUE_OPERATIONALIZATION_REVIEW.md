# Cloud Storage Modification Technique Operationalization Review

## Reference

- Technique: **DC0023 — Cloud Storage Modification**

Cloud Storage Modification involves tracking changes made to cloud storage infrastructure, including updates to settings, permissions, or stored data. Examples include modifying object access control lists (ACLs), uploading new objects, or updating bucket policies. Examples: AWS S3: An object is uploaded or its ACL is modified. - Azure Blob Storage: A blob's metadata or permissions are updated. - Google Cloud Storage: An object's lifecycle policy is updated, or a bucket policy is changed. - OpenStack Swift: Modifications to container settings or uploading of new objects.

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
- DC0023: https://attack.mitre.org/datacomponents/DC0023
- Reviewed: 2026-10-27
