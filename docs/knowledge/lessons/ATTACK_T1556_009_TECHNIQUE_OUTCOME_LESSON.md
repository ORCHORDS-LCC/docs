# T1556.009 Conditional Access Policies Outcome Lesson

## Authoritative description

- Technique: **T1556.009 — Conditional Access Policies**
- Tactics: defense-impairment, persistence, credential-access
- Platforms: IaaS, Identity Provider

Adversaries may disable or modify conditional access policies to enable persistent access to compromised accounts. Conditional access policies are additional verifications used by identity providers and identity and access management systems to determine whether a user should be granted access to a resource. For example, in Entra ID, Okta, and JumpCloud, users can be denied access to applications based on their IP address, device enrollment status, and use of multi-factor authentication. In some cases, identity providers may also support the use of risk-based metrics to deny sign-ins based on a variety of indicators. In AWS and GCP, IAM policies can contain `condition` attributes that verify arbitrary constraints such as the source IP, the date the request was made, and the nature of the resources or regions being requested. These measures help to prevent compromised credentials from resulting in unauthorized access to data or resources, as well as limit user permissions to only those required. By modifying conditional access policies, such as adding additional trusted IP ranges, removing Multi-Factor Authentication requirements, or allowing additional Unused/Unsupported Cloud Regions, adversaries may be able to ensure persistent access to accounts and circumvent defensive measures.

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
- T1556.009: https://attack.mitre.org/techniques/T1556/009
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
