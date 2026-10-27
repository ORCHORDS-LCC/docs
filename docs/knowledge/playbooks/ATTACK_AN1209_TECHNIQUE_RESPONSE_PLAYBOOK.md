# Analytic 1209 Technique Response Playbook

## Target technique

**AN1209 — Analytic 1209**

- Platforms: Linux

Detection focuses on identifying abuse of LD_PRELOAD and related linker variables. Defender perspective: monitor unexpected setting or modification of LD_PRELOAD in shell initialization scripts or environment exports, file creation of suspicious shared libraries, and correlation of these modifications with anomalous process execution. Key signals include execve events with LD_PRELOAD defined, newly created .so files in user directories, and processes hooking libc functions exhibiting abnormal behavior.

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
- AN1209: https://attack.mitre.org/detectionstrategies/DET0435#AN1209
- Reviewed: 2026-10-27
