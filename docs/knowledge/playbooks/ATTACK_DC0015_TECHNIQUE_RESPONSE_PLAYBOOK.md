# Image Creation Technique Response Playbook

## Target technique

**DC0015 — Image Creation**


Initial construction of a virtual machine image within a cloud environment. Virtual machine images are templates containing an operating system and installed applications, which can be deployed to create new virtual machines. Monitoring the creation of these images is important because adversaries may create custom images to include malicious software or misconfigurations for later exploitation. Examples: - Azure Compute Service Image Creation - Example: Creating a virtual machine image in Azure using Azure CLI: `az image create --resource-group MyResourceGroup --name MyImage --source MyVM` - AWS EC2 AMI (Amazon Machine Image) Creation - Example: Creating an AMI from an EC2 instance: `aws ec2 create-image --instance-id i-1234567890abcdef0 --name "MyAMI" --description "An AMI for my app"` - Google Cloud Compute Engine Image Creation - Example: Creating a custom image using gcloud: `gcloud compute images create my-custom-image --source-disk my-disk --source-disk-zone us-central1-a` - VMware vSphere - Example: Exporting a VM to create an OVF (Open Virtualization Format) template: This could later be imported into other environments with potential tampering.

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
- DC0015: https://attack.mitre.org/datacomponents/DC0015
- Reviewed: 2026-10-27
