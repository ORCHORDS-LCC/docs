# DC0028 Image Metadata Outcome Lesson

## Authoritative description

- Technique: **DC0028 — Image Metadata**

Contextual information associated with a virtual machine image, such as its name, resource group, status (active or inactive), type (custom or prebuilt), size, creation date, and permissions. This metadata is critical for understanding the state and configuration of virtual machine images in cloud environments. Examples: - Azure Compute Service Image Metadata Example: - Name: MyCustomImage - Resource Group: MyResourceGroup - State: Available - Type: Managed Image - AWS EC2 AMI Metadata Example: - Image ID: ami-1234567890abcdef0 - Name: ProdImage - State: Available - Platform: Windows - Google Cloud Compute Engine Image Metadata Example: - Image Name: webserver-image - Project: my-project-id - Family: webserver - Source Disk: my-disk-id - VMware vSphere Template Metadata Example: - Name: LinuxTemplate - Disk Size: 40GB - Network Adapter: VM Network.

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
- DC0028: https://attack.mitre.org/datacomponents/DC0028
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
