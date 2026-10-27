# APT42 Technique Response Playbook

## Target technique

**G1044 — APT42**


APT42 is an Iranian-sponsored threat group that conducts cyber espionage and surveillance. The group primarily focuses on targets in the Middle East region, but has targeted a variety of industries and countries since at least 2015. APT42 starts cyber operations through spearphishing emails and/or the PINEFLOWER Android malware, then monitors and collects information from the compromised systems and devices. Finally, APT42 exfiltrates data using native features and open-source tools. APT42 activities have been linked to Magic Hound by other commercial vendors. While there are behavior and software overlaps between Magic Hound and APT42, they appear to be distinct entities and are tracked as separate entities by their originating vendor.

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
- G1044: https://attack.mitre.org/groups/G1044
- Reviewed: 2026-10-27
