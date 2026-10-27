# AcidPour Technique Response Playbook

## Target technique

**S1167 — AcidPour**

- Platforms: Linux

AcidPour is a variant of AcidRain designed to impact a wider range of x86 architecture Linux devices. AcidPour is an x86 ELF binary that expands on the targeted devices and locations in AcidRain by including items such as Unsorted Block Image (UBI), Deice Mapper (DM), and various flash memory references. Based on this expanded targeting, AcidPour can impact a variety of device types including IoT, networking, and ICS embedded device types. AcidPour is a wiping payload associated with the Sandworm Team threat actor, and potentially linked to attacks against Ukrainian internet service providers (ISPs) in 2023.

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
- S1167: https://attack.mitre.org/software/S1167
- Reviewed: 2026-10-27
