# Analytic 1561 Technique Response Playbook

## Target technique

**AN1561 — Analytic 1561**

- Platforms: Windows

Registry access to system language keys (e.g., HKLM\SYSTEM\CurrentControlSet\Control\Nls\Language) or suspicious processes invoking locale-related APIs (e.g., GetUserDefaultUILanguage, GetSystemDefaultUILanguage, GetKeyboardLayoutList). Defender visibility focuses on anomalous or non-standard processes issuing these queries, especially when run by unknown binaries or scripts.

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
- AN1561: https://attack.mitre.org/detectionstrategies/DET0565#AN1561
- Reviewed: 2026-10-27
