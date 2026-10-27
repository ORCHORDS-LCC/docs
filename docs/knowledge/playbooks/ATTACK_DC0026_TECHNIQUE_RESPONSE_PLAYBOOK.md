# Image Deletion Technique Response Playbook

## Target technique

**DC0026 — Image Deletion**


Removal of a virtual machine image in a cloud infrastructure (ex: Azure Compute Service Images DELETE) Examples: - Azure Compute Service Image Deletion - Example: Deleting a virtual machine image using Azure CLI: `az image delete --name MyImage --resource-group MyResourceGroup` - AWS EC2 AMI (Amazon Machine Image) Deletion - Example: Deregistering an AMI in AWS: `aws ec2 deregister-image --image-id ami-1234567890abcdef0` - Google Cloud Compute Engine Image Deletion - Example: Deleting a custom image in Google Cloud: `gcloud compute images delete my-custom-image` - VMware vSphere - Example: Deleting a VM image/template from a vSphere environment: This data component can be collected through the following measures: Enable Cloud Platform Logging - Azure: Enable "Activity Logs" to capture DELETE requests to `Microsoft.Compute/images`. - AWS: Use AWS CloudTrail to monitor `DeregisterImage` or `DeleteSnapshot` API calls. - Google Cloud: Enable "Cloud Audit Logs" to track image deletion events under `compute.googleapis.com/images`. API Monitoring - Monitor API activity to track the deletion of images using: - AWS SDK/CLI `DeregisterImage` or `DeleteSnapshot`. - Azure REST API DELETE operations for images. - Google Cloud Compute Engine APIs for image deletion. Cloud SIEM Integration - Ingest logs into a centralized SIEM platform for monitoring and alerting: Event Correlation - Correlate image deletion events with unusual account activity or concurrent unauthorized operations.

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
- DC0026: https://attack.mitre.org/datacomponents/DC0026
- Reviewed: 2026-10-27
