# GlassWorm Technique Response Playbook

## Target technique

**S9010 — GlassWorm**

- Platforms: macOS, Windows

GlassWorm is a worm that propagated through supply chain attacks by compromising repository credentials from victim environments and having malicious payloads added to those compromised accounts for distribution to victims across the various development ecosystems. GlassWorm has numerous variants, including Rust binaries, encrypted JavaScript and a variant leveraging invisible Unicode characters that made reverse engineering difficult. GlassWorm has employed a unique command and control (C2) methodology using Solana blockchain. GlassWorm was first reported in October 2025.

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
- S9010: https://attack.mitre.org/software/S9010
- Reviewed: 2026-10-27
