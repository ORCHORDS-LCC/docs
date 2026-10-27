# T1552.005 Cloud Instance Metadata API Outcome Lesson

## Authoritative description

- Technique: **T1552.005 — Cloud Instance Metadata API**
- Tactics: credential-access
- Platforms: IaaS

Adversaries may attempt to access the Cloud Instance Metadata API to collect credentials and other sensitive data. Most cloud service providers support a Cloud Instance Metadata API which is a service provided to running virtual instances that allows applications to access information about the running virtual instance. Available information generally includes name, security group, and additional metadata including sensitive data such as credentials and UserData scripts that may contain additional secrets. The Instance Metadata API is provided as a convenience to assist in managing applications and is accessible by anyone who can access the instance. A cloud metadata API has been used in at least one high profile compromise. If adversaries have a presence on the running virtual instance, they may query the Instance Metadata API directly to identify credentials that grant access to additional resources. Additionally, adversaries may exploit a Server-Side Request Forgery (SSRF) vulnerability in a public facing web proxy that allows them to gain access to the sensitive information via a request to the Instance Metadata API. The de facto standard across cloud service providers is to host the Instance Metadata API at <code>http[:]//169.254.169.254</code>.

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
- T1552.005: https://attack.mitre.org/techniques/T1552/005
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
