# Analytic 0864 Technique Response Playbook

## Target technique

**AN0864 — Analytic 0864**

- Platforms: macOS

A tampered app/pkg/notarized update is installed via installer, softwareupdated, Homebrew, or vendor updater; new Mach-O or bundle contents appear in /Applications, /Library, /usr/local or /opt/homebrew; first run spawns sh/zsh/osascript/curl and makes egress to unfamiliar domains; AMFI/Gatekeeper may log signature/notarization problems.

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
- AN0864: https://attack.mitre.org/detectionstrategies/DET0309#AN0864
- Reviewed: 2026-10-27
