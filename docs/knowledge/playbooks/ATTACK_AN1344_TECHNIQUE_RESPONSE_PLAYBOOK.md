# Analytic 1344 Technique Response Playbook

## Target technique

**AN1344 — Analytic 1344**

- Platforms: Windows

Behavioral chain: (1) a login from a third-party account or untrusted source network establishes an interactive/remote session; (2) the session acquires elevated privileges or accesses sensitive resources atypical for that account; (3) subsequent lateral movement or data access occurs from the same session/device. Correlate Windows logon events, token elevation/privileged use, and resource access with third-party context.

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
- AN1344: https://attack.mitre.org/detectionstrategies/DET0488#AN1344
- Reviewed: 2026-10-27
