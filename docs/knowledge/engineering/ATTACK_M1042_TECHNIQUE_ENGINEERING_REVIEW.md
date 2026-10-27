# Disable or Remove Feature or Program Technique Engineering Review

## Reference

- Technique: **M1042 — Disable or Remove Feature or Program**

Disable or remove unnecessary and potentially vulnerable software, features, or services to reduce the attack surface and prevent abuse by adversaries. This involves identifying software or features that are no longer needed or that could be exploited and ensuring they are either removed or properly disabled. This mitigation can be implemented through the following measures: Remove Legacy Software: - Use Case: Disable or remove older versions of software that no longer receive updates or security patches (e.g., legacy Java, Adobe Flash). - Implementation: A company removes Flash Player from all employee systems after it has reached its end-of-life date. Disable Unused Features: - Use Case: Turn off unnecessary operating system features like SMBv1, Telnet, or RDP if they are not required. - Implementation: Disable SMBv1 in a Windows environment to mitigate vulnerabilities like EternalBlue. Control Applications Installed by Users: - Use Case: Prevent users from installing unauthorized software via group policies or other management tools. - Implementation: Block user installations of unauthorized file-sharing applications (e.g., BitTorrent clients) in an enterprise environment. Remove Unnecessary Services: - Use Case: Identify and disable unnecessary default services running on endpoints, servers, or network devices. - Implementation: Disable unused administrative shares (e.g., C$, ADMIN$) on workstations. Restrict Add-ons and Plugins: - Use Case: Remove or disable browser plugins and add-ons that are not needed for business purposes. - Implementation: Disable Java and ActiveX plugins in web browsers to prevent drive-by attacks.

## Engineering review

1. Identify the engineering boundary where the technique would apply: the component, the service, or the deployment.
2. Review the design decision that would prevent the technique, and record the alternative considered.
3. Review the implementation evidence for the preventive control.
4. Review the test coverage that would fail if the control regressed.
5. Review the observability: which signal would show the control is not operating.
6. Record the residual risk where prevention is not achievable, and the detection that compensates.

## Review evidence

- the design record for the preventive decision;
- the implementation or configuration evidence;
- the test record showing the control is exercised;
- the observability mapping.

## Limitations

An engineering review describes what the design and the implementation evidence show. It does not claim the technique has been addressed in production.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- M1042: https://attack.mitre.org/mitigations/M1042
- Reviewed: 2026-10-27
