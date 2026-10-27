# T1070.010 Relocate Malware Outcome Lesson

## Authoritative description

- Technique: **T1070.010 — Relocate Malware**
- Tactics: stealth
- Platforms: Linux, macOS, Network Devices, Windows

Once a payload is delivered, adversaries may reproduce copies of the same malware on the victim system to remove evidence of their presence and/or avoid defenses. Copying malware payloads to new locations may also be combined with File Deletion to cleanup older artifacts. Relocating malware may be a part of many actions intended to evade defenses. For example, adversaries may copy and rename payloads to better blend into the local environment (i.e., Match Legitimate Resource Name or Location). Payloads may also be repositioned to target File/Path Exclusions as well as specific locations associated with establishing Persistence. Relocating malicious payloads may also hinder defensive analysis, especially to separate these payloads from earlier events (such as User Execution and Phishing) that may have generated alerts or otherwise drawn attention from defenders. Moving payloads into target directories does not alter the Creation timestamp, thereby evading detection logic reliant on modifications to this artifact (i.e., Timestomp).

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
- T1070.010: https://attack.mitre.org/techniques/T1070/010
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
