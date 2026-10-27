# Indrik Spider Technique Response Playbook

## Target technique

**G0119 — Indrik Spider**


Indrik Spider is a Russia-based cybercriminal group that has been active since at least 2014. Indrik Spider initially started with the Dridex banking Trojan, and then by 2017 they began running ransomware operations using BitPaymer, WastedLocker, and Hades ransomware. Following U.S. sanctions and an indictment in 2019, Indrik Spider changed their tactics and diversified their toolset.

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
- G0119: https://attack.mitre.org/groups/G0119
- Reviewed: 2026-10-27
