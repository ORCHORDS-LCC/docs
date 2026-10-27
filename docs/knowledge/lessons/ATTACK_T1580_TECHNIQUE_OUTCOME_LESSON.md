# T1580 Cloud Infrastructure Discovery Outcome Lesson

## Authoritative description

- Technique: **T1580 — Cloud Infrastructure Discovery**
- Tactics: discovery
- Platforms: IaaS

An adversary may attempt to discover infrastructure and resources that are available within an infrastructure-as-a-service (IaaS) environment. This includes compute service resources such as instances, virtual machines, and snapshots as well as resources of other services including the storage and database services. Cloud providers offer methods such as APIs and commands issued through CLIs to serve information about infrastructure. For example, AWS provides a <code>DescribeInstances</code> API within the Amazon EC2 API that can return information about one or more instances within an account, the <code>ListBuckets</code> API that returns a list of all buckets owned by the authenticated sender of the request, the <code>HeadBucket</code> API to determine a bucket’s existence along with access permissions of the request sender, or the <code>GetPublicAccessBlock</code> API to retrieve access block configuration for a bucket. Similarly, GCP's Cloud SDK CLI provides the <code>gcloud compute instances list</code> command to list all Google Compute Engine instances in a project , and Azure's CLI command <code>az vm list</code> lists details of virtual machines. In addition to API commands, adversaries can utilize open source tools to discover cloud storage infrastructure through Wordlist Scanning. An adversary may enumerate resources using a compromised user's access keys to determine which are available to that user. The discovery of these available resources may help adversaries determine their next steps in the Cloud environment, such as establishing Persistence.An adversary may also use this information to change the configuration to make the bucket publicly accessible, allowing data to be accessed without authentication. Adversaries have also may use infrastructure discovery APIs such as <code>DescribeDBInstances</code> to determine size, owner, permissions, and network ACLs of database resources. Adversaries can use this information to determine the potential value of databases and discover the requirements to access them. Unlike in Cloud Service Discovery, this technique focuses on the discovery of components of the provided services rather than the services themselves.

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
- T1580: https://attack.mitre.org/techniques/T1580
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
