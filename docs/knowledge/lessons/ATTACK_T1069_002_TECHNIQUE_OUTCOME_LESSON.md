# T1069.002 Domain Groups Outcome Lesson

## Authoritative description

- Technique: **T1069.002 — Domain Groups**
- Tactics: discovery
- Platforms: Linux, macOS, Windows

Adversaries may attempt to find domain-level groups and permission settings. The knowledge of domain-level permission groups can help adversaries determine which groups exist and which users belong to a particular group. Adversaries may use this information to determine which users have elevated permissions, such as domain administrators. Commands such as <code>net group /domain</code> of the Net utility, <code>dscacheutil -q group</code> on macOS, and <code>ldapsearch</code> on Linux can list domain-level groups.

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
- T1069.002: https://attack.mitre.org/techniques/T1069/002
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
