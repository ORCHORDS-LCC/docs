# Image Metadata Technique Operationalization Review

## Reference

- Technique: **DC0028 — Image Metadata**

Contextual information associated with a virtual machine image, such as its name, resource group, status (active or inactive), type (custom or prebuilt), size, creation date, and permissions. This metadata is critical for understanding the state and configuration of virtual machine images in cloud environments. Examples: - Azure Compute Service Image Metadata Example: - Name: MyCustomImage - Resource Group: MyResourceGroup - State: Available - Type: Managed Image - AWS EC2 AMI Metadata Example: - Image ID: ami-1234567890abcdef0 - Name: ProdImage - State: Available - Platform: Windows - Google Cloud Compute Engine Image Metadata Example: - Image Name: webserver-image - Project: my-project-id - Family: webserver - Source Disk: my-disk-id - VMware vSphere Template Metadata Example: - Name: LinuxTemplate - Disk Size: 40GB - Network Adapter: VM Network.

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
- DC0028: https://attack.mitre.org/datacomponents/DC0028
- Reviewed: 2026-10-27
