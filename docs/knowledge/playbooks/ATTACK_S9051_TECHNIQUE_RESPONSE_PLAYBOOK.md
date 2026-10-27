# The Gentlemen Ransomware Technique Response Playbook

## Target technique

**S9051 — The Gentlemen Ransomware**

- Platforms: macOS, Linux, Windows, IaaS, ESXi, Network Devices

The Gentlemen Ransomware is a ransomware-as-a-service (RaaS). The Gentlemen Ransomware has been written in Go programming language and has utilized Garble to obfuscate its code to target Windows environments. The Gentlemen Ransomware is capable of executing its’ OS lockers in Windows, Linux, NAS, BSD and ESXi environments. The Gentlemen Ransomware was first observed in mid-2025 as a closed ransomware and shortly later emerged as a RaaS to affiliates in September 2025. The Gentlemen Ransomware has been affiliated with the threat group The Gentlemen.

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
- S9051: https://attack.mitre.org/software/S9051
- Reviewed: 2026-10-27
