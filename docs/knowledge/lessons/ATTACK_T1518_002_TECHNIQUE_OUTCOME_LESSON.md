# T1518.002 Backup Software Discovery Outcome Lesson

## Authoritative description

- Technique: **T1518.002 — Backup Software Discovery**
- Tactics: discovery
- Platforms: Windows, macOS, Linux

Adversaries may attempt to get a listing of backup software or configurations that are installed on a system. Adversaries may use this information to shape follow-on behaviors, such as Data Destruction, Inhibit System Recovery, or Data Encrypted for Impact. Commands that can be used to obtain security software information are netsh, `reg query` with Reg, `dir` with cmd, and Tasklist, but other indicators of discovery behavior may be more specific to the type of software or security system the adversary is looking for, such as Veeam, Acronis, Dropbox, or Paragon.

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
- T1518.002: https://attack.mitre.org/techniques/T1518/002
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
