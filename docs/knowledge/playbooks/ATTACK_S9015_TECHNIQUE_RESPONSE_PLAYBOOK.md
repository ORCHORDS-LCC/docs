# BRICKSTORM Technique Response Playbook

## Target technique

**S9015 — BRICKSTORM**

- Platforms: ESXi, Linux, Network Devices, Windows

BRICKSTORM is a cross-platform backdoor with variants written in Go and Rust that facilitates command and control, the ingress transfer of other malware, and the exfiltration of data. BRICKSTORM has also been created from a .NET application using ahead-of-time (AOT) compilation to blend in within victim environments. BRICKSTORM was first observed in April 2024. BRICKSTORM has previously been leveraged by People's Republic of China (PRC) state-nexus actors identified as UNC6201, UNC5221, WARP PANDA, PunyToad, and SYLVANITE.

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
- S9015: https://attack.mitre.org/software/S9015
- Reviewed: 2026-10-27
