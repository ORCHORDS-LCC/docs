# T1070.009 Clear Persistence Outcome Lesson

## Authoritative description

- Technique: **T1070.009 — Clear Persistence**
- Tactics: stealth
- Platforms: ESXi, Linux, macOS, Windows

Adversaries may clear artifacts associated with previously established persistence on a host system to remove evidence of their activity. This may involve various actions, such as removing services, deleting executables, Modify Registry, Plist File Modification, or other methods of cleanup to prevent defenders from collecting evidence of their persistent presence. Adversaries may also delete accounts previously created to maintain persistence (i.e. Create Account). In some instances, artifacts of persistence may also be removed once an adversary’s persistence is executed in order to prevent errors with the new instance of the malware.

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
- T1070.009: https://attack.mitre.org/techniques/T1070/009
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
