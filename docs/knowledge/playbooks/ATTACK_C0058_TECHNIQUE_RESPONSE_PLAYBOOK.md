# SharePoint ToolShell Exploitation Technique Response Playbook

## Target technique

**C0058 — SharePoint ToolShell Exploitation**


The SharePoint ToolShell Exploitation campaign was conducted in July 2025 and encompassed the first waves of exploitation against incompletely patched spoofing (CVE-2025-49706) and remote code execution (CVE-2025-49704) vulnerabilities affecting on-premises Microsoft SharePoint servers. Later patched and updated as CVE-2025-53770 and CVE-2025-53771, the ToolShell vulnerabilities were widely exploited including by China-based ransomware actor Storm-2603 and espionage actors Threat Group-3390 and ZIRCONIUM. SharePoint ToolShell Exploitation targeted multiple regions and industries including finance, education, energy, and healthcare across Asia, Europe, and the United States.

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
- C0058: https://attack.mitre.org/campaigns/C0058
- Reviewed: 2026-10-27
