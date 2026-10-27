# DC0070 Cloud Service Metadata Outcome Lesson

## Authoritative description

- Technique: **DC0070 — Cloud Service Metadata**

Cloud service metadata refers to the contextual and descriptive information about cloud services, including their name, type, purpose, configuration, and activity around them. This metadata is essential for understanding the roles and functions of cloud services, their operational status, and their potential misuse. Examples: - Azure Service Metadata: Metadata describing a resource in Azure, such as an Azure Storage Account or a Virtual Machine. - AWS Cloud Service Metadata: Metadata for an AWS EC2 instance collected using the `DescribeInstances` API call. - Google Cloud Service Metadata: Metadata for a Google Compute Engine instance collected using `gcloud compute instances describe`. - Office 365 Metadata: Metadata about an Office 365 SharePoint site.

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
- DC0070: https://attack.mitre.org/datacomponents/DC0070
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
