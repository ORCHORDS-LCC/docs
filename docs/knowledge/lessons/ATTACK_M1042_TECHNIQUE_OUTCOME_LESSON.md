# M1042 Disable or Remove Feature or Program Outcome Lesson

## Authoritative description

- Technique: **M1042 — Disable or Remove Feature or Program**

Disable or remove unnecessary and potentially vulnerable software, features, or services to reduce the attack surface and prevent abuse by adversaries. This involves identifying software or features that are no longer needed or that could be exploited and ensuring they are either removed or properly disabled. This mitigation can be implemented through the following measures: Remove Legacy Software: - Use Case: Disable or remove older versions of software that no longer receive updates or security patches (e.g., legacy Java, Adobe Flash). - Implementation: A company removes Flash Player from all employee systems after it has reached its end-of-life date. Disable Unused Features: - Use Case: Turn off unnecessary operating system features like SMBv1, Telnet, or RDP if they are not required. - Implementation: Disable SMBv1 in a Windows environment to mitigate vulnerabilities like EternalBlue. Control Applications Installed by Users: - Use Case: Prevent users from installing unauthorized software via group policies or other management tools. - Implementation: Block user installations of unauthorized file-sharing applications (e.g., BitTorrent clients) in an enterprise environment. Remove Unnecessary Services: - Use Case: Identify and disable unnecessary default services running on endpoints, servers, or network devices. - Implementation: Disable unused administrative shares (e.g., C$, ADMIN$) on workstations. Restrict Add-ons and Plugins: - Use Case: Remove or disable browser plugins and add-ons that are not needed for business purposes. - Implementation: Disable Java and ActiveX plugins in web browsers to prevent drive-by attacks.

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
- M1042: https://attack.mitre.org/mitigations/M1042
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
