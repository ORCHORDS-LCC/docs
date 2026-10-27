# Image Deletion Technique Platform Profile

## Reference

- Technique: **DC0026 — Image Deletion**
- Platforms named in the source: not stated

Removal of a virtual machine image in a cloud infrastructure (ex: Azure Compute Service Images DELETE) Examples: - Azure Compute Service Image Deletion - Example: Deleting a virtual machine image using Azure CLI: `az image delete --name MyImage --resource-group MyResourceGroup` - AWS EC2 AMI (Amazon Machine Image) Deletion - Example: Deregistering an AMI in AWS: `aws ec2 deregister-image --image-id ami-1234567890abcdef0` - Google Cloud Compute Engine Image Deletion - Example: Deleting a custom image in Google Cloud: `gcloud compute images delete my-custom-image` - VMware vSphere - Example: Deleting a VM image/template from a vSphere environment: This data component can be collected through the following measures: Enable Cloud Platform Logging - Azure: Enable "Activity Logs" to capture DELETE requests to `Microsoft.Compute/images`. - AWS: Use AWS CloudTrail to monitor `DeregisterImage` or `DeleteSnapshot` API calls. - Google Cloud: Enable "Cloud Audit Logs" to track image deletion events under `compute.googleapis.com/images`. API Monitoring - Monitor API activity to track the deletion of images using: - AWS SDK/CLI `DeregisterImage` or `DeleteSnapshot`. - Azure REST API DELETE operations for images. - Google Cloud Compute Engine APIs for image deletion. Cloud SIEM Integration - Ingest logs into a centralized SIEM platform for monitoring and alerting: Event Correlation - Correlate image deletion events with unusual account activity or concurrent unauthorized operations.

## Platform profile

1. Record the platforms in scope and the versions actually deployed.
2. Compare the deployed platform surface against the platforms the source names.
3. Record where the platform provides a native control for the technique, and where it does not.
4. Record the configuration evidence for the native control, where one exists.
5. Record the gap where the platform provides no native control, and the compensating detection.
6. Record the platform version, because platform behaviour changes between versions.

## Evidence

- the platform and version inventory for the scoped estate;
- the configuration export or screenshot for the native control;
- the detection evidence where the platform provides none.

## Limitations

A technique entry describes a class of abuse across platforms. The platform-specific exposure is a property of the deployment, established only by inventory and configuration evidence.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- DC0026: https://attack.mitre.org/datacomponents/DC0026
- Reviewed: 2026-10-27
