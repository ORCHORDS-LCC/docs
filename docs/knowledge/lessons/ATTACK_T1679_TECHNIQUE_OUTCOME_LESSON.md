# T1679 Selective Exclusion Outcome Lesson

## Authoritative description

- Technique: **T1679 — Selective Exclusion**
- Tactics: stealth
- Platforms: Windows

Adversaries may intentionally exclude certain files, folders, directories, file types, or system components from encryption or tampering during a ransomware or malicious payload execution. Some file extensions that adversaries may avoid encrypting include `.dll`, `.exe`, and `.lnk`. Adversaries may perform this behavior to avoid alerting users, to evade detection by security tools and analysts, or, in the case of ransomware, to ensure that the system remains operational enough to deliver the ransom notice. Exclusions may target files and components whose corruption would cause instability, break core services, or immediately expose the attack. By carefully avoiding these areas, adversaries maintain system responsiveness while minimizing indicators that could trigger alarms or otherwise inhibit achieving their goals.

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
- T1679: https://attack.mitre.org/techniques/T1679
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
