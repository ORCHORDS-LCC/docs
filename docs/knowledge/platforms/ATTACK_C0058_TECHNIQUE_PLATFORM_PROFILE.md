# SharePoint ToolShell Exploitation Technique Platform Profile

## Reference

- Technique: **C0058 — SharePoint ToolShell Exploitation**
- Platforms named in the source: not stated

The SharePoint ToolShell Exploitation campaign was conducted in July 2025 and encompassed the first waves of exploitation against incompletely patched spoofing (CVE-2025-49706) and remote code execution (CVE-2025-49704) vulnerabilities affecting on-premises Microsoft SharePoint servers. Later patched and updated as CVE-2025-53770 and CVE-2025-53771, the ToolShell vulnerabilities were widely exploited including by China-based ransomware actor Storm-2603 and espionage actors Threat Group-3390 and ZIRCONIUM. SharePoint ToolShell Exploitation targeted multiple regions and industries including finance, education, energy, and healthcare across Asia, Europe, and the United States.

## Platform profile

1. Record the platforms in scope and the versions actually deployed.
2. Compare the deployed platform surface against the platforms the source names.
3. Record where the platform provides a native control for the technique, and where it does not.
4. Record the configuration evidence for the native control, where one exists.
5. Record the gap where the platform provides no native control, and the compensating detection.
6. Record the platform version, because platform behaviour changes between versions.

## Evidence

- the platform and version inventory for the scoped estate;
- the configuration export or screenshot for the native control;
- the detection evidence where the platform provides none.

## Limitations

A technique entry describes a class of abuse across platforms. The platform-specific exposure is a property of the deployment, established only by inventory and configuration evidence.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- C0058: https://attack.mitre.org/campaigns/C0058
- Reviewed: 2026-10-27
