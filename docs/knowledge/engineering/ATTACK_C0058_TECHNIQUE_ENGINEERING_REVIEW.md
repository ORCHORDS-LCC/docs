# SharePoint ToolShell Exploitation Technique Engineering Review

## Reference

- Technique: **C0058 — SharePoint ToolShell Exploitation**

The SharePoint ToolShell Exploitation campaign was conducted in July 2025 and encompassed the first waves of exploitation against incompletely patched spoofing (CVE-2025-49706) and remote code execution (CVE-2025-49704) vulnerabilities affecting on-premises Microsoft SharePoint servers. Later patched and updated as CVE-2025-53770 and CVE-2025-53771, the ToolShell vulnerabilities were widely exploited including by China-based ransomware actor Storm-2603 and espionage actors Threat Group-3390 and ZIRCONIUM. SharePoint ToolShell Exploitation targeted multiple regions and industries including finance, education, energy, and healthcare across Asia, Europe, and the United States.

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
- C0058: https://attack.mitre.org/campaigns/C0058
- Reviewed: 2026-10-27
