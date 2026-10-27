# Image Deletion Technique Engineering Review

## Reference

- Technique: **DC0026 — Image Deletion**

Removal of a virtual machine image in a cloud infrastructure (ex: Azure Compute Service Images DELETE) Examples: - Azure Compute Service Image Deletion - Example: Deleting a virtual machine image using Azure CLI: `az image delete --name MyImage --resource-group MyResourceGroup` - AWS EC2 AMI (Amazon Machine Image) Deletion - Example: Deregistering an AMI in AWS: `aws ec2 deregister-image --image-id ami-1234567890abcdef0` - Google Cloud Compute Engine Image Deletion - Example: Deleting a custom image in Google Cloud: `gcloud compute images delete my-custom-image` - VMware vSphere - Example: Deleting a VM image/template from a vSphere environment: This data component can be collected through the following measures: Enable Cloud Platform Logging - Azure: Enable "Activity Logs" to capture DELETE requests to `Microsoft.Compute/images`. - AWS: Use AWS CloudTrail to monitor `DeregisterImage` or `DeleteSnapshot` API calls. - Google Cloud: Enable "Cloud Audit Logs" to track image deletion events under `compute.googleapis.com/images`. API Monitoring - Monitor API activity to track the deletion of images using: - AWS SDK/CLI `DeregisterImage` or `DeleteSnapshot`. - Azure REST API DELETE operations for images. - Google Cloud Compute Engine APIs for image deletion. Cloud SIEM Integration - Ingest logs into a centralized SIEM platform for monitoring and alerting: Event Correlation - Correlate image deletion events with unusual account activity or concurrent unauthorized operations.

## Engineering review

1. Identify the engineering boundary where the technique would apply: the component, the service, or the deployment.
2. Review the design decision that would prevent the technique, and record the alternative considered.
3. Review the implementation evidence for the preventive control.
4. Review the test coverage that would fail if the control regressed.
5. Review the observability: which signal would show the control is not operating.
6. Record the residual risk where prevention is not achievable, and the detection that compensates.

## Review evidence

- the design record for the preventive decision;
- the implementation or configuration evidence;
- the test record showing the control is exercised;
- the observability mapping.

## Limitations

An engineering review describes what the design and the implementation evidence show. It does not claim the technique has been addressed in production.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- DC0026: https://attack.mitre.org/datacomponents/DC0026
- Reviewed: 2026-10-27
