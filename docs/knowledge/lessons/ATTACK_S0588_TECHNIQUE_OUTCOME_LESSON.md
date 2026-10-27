# S0588 GoldMax Outcome Lesson

## Authoritative description

- Technique: **S0588 — GoldMax**
- Platforms: Windows, Linux

GoldMax is a second-stage C2 backdoor written in Go with Windows and Linux variants that are nearly identical in functionality. GoldMax was discovered in early 2021 during the investigation into the SolarWinds Compromise, and has likely been used by APT29 since at least mid-2019. GoldMax uses multiple defense evasion techniques, including avoiding virtualization execution and masking malicious traffic.

## Reusable lesson

This technique should be treated as an explicit review question when it is relevant to the system or organisation, rather than assumed to be covered by a generic control statement or by tooling that reports a related signal.

## Apply the lesson

1. Define the real scope before judging coverage.
2. Inspect current technical, process, governance, or operational evidence.
3. Separate documented intent from verified behaviour.
4. Record partial coverage and unresolved gaps instead of converting them into a pass.
5. Revisit when the underlying scope, threat environment, technology, suppliers, or mission materially changes.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- S0588: https://attack.mitre.org/software/S0588
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
