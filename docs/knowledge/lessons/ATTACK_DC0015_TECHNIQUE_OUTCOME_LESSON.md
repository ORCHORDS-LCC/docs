# DC0015 Image Creation Outcome Lesson

## Authoritative description

- Technique: **DC0015 — Image Creation**

Initial construction of a virtual machine image within a cloud environment. Virtual machine images are templates containing an operating system and installed applications, which can be deployed to create new virtual machines. Monitoring the creation of these images is important because adversaries may create custom images to include malicious software or misconfigurations for later exploitation. Examples: - Azure Compute Service Image Creation - Example: Creating a virtual machine image in Azure using Azure CLI: `az image create --resource-group MyResourceGroup --name MyImage --source MyVM` - AWS EC2 AMI (Amazon Machine Image) Creation - Example: Creating an AMI from an EC2 instance: `aws ec2 create-image --instance-id i-1234567890abcdef0 --name "MyAMI" --description "An AMI for my app"` - Google Cloud Compute Engine Image Creation - Example: Creating a custom image using gcloud: `gcloud compute images create my-custom-image --source-disk my-disk --source-disk-zone us-central1-a` - VMware vSphere - Example: Exporting a VM to create an OVF (Open Virtualization Format) template: This could later be imported into other environments with potential tampering.

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
- DC0015: https://attack.mitre.org/datacomponents/DC0015
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
