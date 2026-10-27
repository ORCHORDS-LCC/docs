# Disable or Remove Feature or Program Technique Response Playbook

## Target technique

**M1042 — Disable or Remove Feature or Program**


Disable or remove unnecessary and potentially vulnerable software, features, or services to reduce the attack surface and prevent abuse by adversaries. This involves identifying software or features that are no longer needed or that could be exploited and ensuring they are either removed or properly disabled. This mitigation can be implemented through the following measures: Remove Legacy Software: - Use Case: Disable or remove older versions of software that no longer receive updates or security patches (e.g., legacy Java, Adobe Flash). - Implementation: A company removes Flash Player from all employee systems after it has reached its end-of-life date. Disable Unused Features: - Use Case: Turn off unnecessary operating system features like SMBv1, Telnet, or RDP if they are not required. - Implementation: Disable SMBv1 in a Windows environment to mitigate vulnerabilities like EternalBlue. Control Applications Installed by Users: - Use Case: Prevent users from installing unauthorized software via group policies or other management tools. - Implementation: Block user installations of unauthorized file-sharing applications (e.g., BitTorrent clients) in an enterprise environment. Remove Unnecessary Services: - Use Case: Identify and disable unnecessary default services running on endpoints, servers, or network devices. - Implementation: Disable unused administrative shares (e.g., C$, ADMIN$) on workstations. Restrict Add-ons and Plugins: - Use Case: Remove or disable browser plugins and add-ons that are not needed for business purposes. - Implementation: Disable Java and ActiveX plugins in web browsers to prevent drive-by attacks.

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
- M1042: https://attack.mitre.org/mitigations/M1042
- Reviewed: 2026-10-27
