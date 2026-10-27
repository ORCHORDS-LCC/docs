# Image Metadata Technique Response Playbook

## Target technique

**DC0028 — Image Metadata**


Contextual information associated with a virtual machine image, such as its name, resource group, status (active or inactive), type (custom or prebuilt), size, creation date, and permissions. This metadata is critical for understanding the state and configuration of virtual machine images in cloud environments. Examples: - Azure Compute Service Image Metadata Example: - Name: MyCustomImage - Resource Group: MyResourceGroup - State: Available - Type: Managed Image - AWS EC2 AMI Metadata Example: - Image ID: ami-1234567890abcdef0 - Name: ProdImage - State: Available - Platform: Windows - Google Cloud Compute Engine Image Metadata Example: - Image Name: webserver-image - Project: my-project-id - Family: webserver - Source Disk: my-disk-id - VMware vSphere Template Metadata Example: - Name: LinuxTemplate - Disk Size: 40GB - Network Adapter: VM Network.

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
- DC0028: https://attack.mitre.org/datacomponents/DC0028
- Reviewed: 2026-10-27
