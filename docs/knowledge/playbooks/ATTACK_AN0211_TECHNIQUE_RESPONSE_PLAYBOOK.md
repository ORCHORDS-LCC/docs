# Analytic 0211 Technique Response Playbook

## Target technique

**AN0211 — Analytic 0211**

- Platforms: Linux

Detects abuse of Mono/.NET Core environments to execute VB-like scripts, often in environments with Office emulation or WINE. Focus is on rare invocations of scripting hosts like mono.exe or .NET shells, often seen in spam filtering or forensic labs with Office support.

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
- AN0211: https://attack.mitre.org/detectionstrategies/DET0076#AN0211
- Reviewed: 2026-10-27
