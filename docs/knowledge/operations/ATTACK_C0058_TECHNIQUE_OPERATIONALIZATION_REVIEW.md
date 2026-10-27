# SharePoint ToolShell Exploitation Technique Operationalization Review

## Reference

- Technique: **C0058 — SharePoint ToolShell Exploitation**

The SharePoint ToolShell Exploitation campaign was conducted in July 2025 and encompassed the first waves of exploitation against incompletely patched spoofing (CVE-2025-49706) and remote code execution (CVE-2025-49704) vulnerabilities affecting on-premises Microsoft SharePoint servers. Later patched and updated as CVE-2025-53770 and CVE-2025-53771, the ToolShell vulnerabilities were widely exploited including by China-based ransomware actor Storm-2603 and espionage actors Threat Group-3390 and ZIRCONIUM. SharePoint ToolShell Exploitation targeted multiple regions and industries including finance, education, energy, and healthcare across Asia, Europe, and the United States.

## Operationalization review

1. Record the operational scope: which services, environments, and data the technique could affect.
2. Record the runbook that would be executed, and its owner.
3. Record the telemetry the runbook depends on, and whether it is retained long enough to investigate.
4. Record the detection that would surface the technique before or after it has an effect.
5. Record the recovery path, and the evidence that recovery has been rehearsed.
6. Record the residual operational risk where the runbook depends on a manual step.

## Review evidence

- the runbook and its owner;
- the telemetry retention and coverage record;
- the detection mapping;
- the exercise or rehearsal record.

## Limitations

An operationalization review describes the runbook and the evidence around it. It does not claim the technique has been prevented or detected in a live environment.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- C0058: https://attack.mitre.org/campaigns/C0058
- Reviewed: 2026-10-27
