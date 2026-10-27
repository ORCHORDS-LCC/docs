# Playcrypt Technique Response Playbook

## Target technique

**S1162 — Playcrypt**

- Platforms: Windows

Playcrypt is a ransomware that has been used by Play since at least 2022 in attacks against against the business, government, critical infrastructure, healthcare, and media sectors in North America, South America, and Europe. Playcrypt derives its name from adding the .play extension to encrypted files and has overlap with tactics and tools associated with Hive and Nokoyawa ransomware and infrastructure associated with Quantum ransomware.

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
- S1162: https://attack.mitre.org/software/S1162
- Reviewed: 2026-10-27
