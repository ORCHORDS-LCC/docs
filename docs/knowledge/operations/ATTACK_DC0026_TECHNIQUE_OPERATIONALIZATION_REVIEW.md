# Image Deletion Technique Operationalization Review

## Reference

- Technique: **DC0026 — Image Deletion**

Removal of a virtual machine image in a cloud infrastructure (ex: Azure Compute Service Images DELETE) Examples: - Azure Compute Service Image Deletion - Example: Deleting a virtual machine image using Azure CLI: `az image delete --name MyImage --resource-group MyResourceGroup` - AWS EC2 AMI (Amazon Machine Image) Deletion - Example: Deregistering an AMI in AWS: `aws ec2 deregister-image --image-id ami-1234567890abcdef0` - Google Cloud Compute Engine Image Deletion - Example: Deleting a custom image in Google Cloud: `gcloud compute images delete my-custom-image` - VMware vSphere - Example: Deleting a VM image/template from a vSphere environment: This data component can be collected through the following measures: Enable Cloud Platform Logging - Azure: Enable "Activity Logs" to capture DELETE requests to `Microsoft.Compute/images`. - AWS: Use AWS CloudTrail to monitor `DeregisterImage` or `DeleteSnapshot` API calls. - Google Cloud: Enable "Cloud Audit Logs" to track image deletion events under `compute.googleapis.com/images`. API Monitoring - Monitor API activity to track the deletion of images using: - AWS SDK/CLI `DeregisterImage` or `DeleteSnapshot`. - Azure REST API DELETE operations for images. - Google Cloud Compute Engine APIs for image deletion. Cloud SIEM Integration - Ingest logs into a centralized SIEM platform for monitoring and alerting: Event Correlation - Correlate image deletion events with unusual account activity or concurrent unauthorized operations.

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
- DC0026: https://attack.mitre.org/datacomponents/DC0026
- Reviewed: 2026-10-27
