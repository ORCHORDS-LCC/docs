# BOLDMOVE Technique Response Playbook

## Target technique

**S1184 — BOLDMOVE**

- Platforms: Linux, Network Devices

BOLDMOVE is a type of backdoor malware written in C linked to People’s Republic of China operations from 2022 through 2023. BOLDMOVE includes both Windows and Linux variants, with some Linux variants specifically designed for FortiGate Firewall devices. BOLDMOVE is linked to zero-day exploitation of CVE-2022-42475 in FortiOSS SSL-VPNs. The record for BOLDMOVE only covers known Linux variants.

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
- S1184: https://attack.mitre.org/software/S1184
- Reviewed: 2026-10-27
