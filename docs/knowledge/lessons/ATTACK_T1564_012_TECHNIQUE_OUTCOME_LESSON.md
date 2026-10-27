# T1564.012 File/Path Exclusions Outcome Lesson

## Authoritative description

- Technique: **T1564.012 — File/Path Exclusions**
- Tactics: stealth
- Platforms: Linux, macOS, Windows

Adversaries may attempt to hide their file-based artifacts by writing them to specific folders or file names excluded from antivirus (AV) scanning and other defensive capabilities. AV and other file-based scanners often include exclusions to optimize performance as well as ease installation and legitimate use of applications. These exclusions may be contextual (e.g., scans are only initiated in response to specific triggering events/alerts), but are also often hardcoded strings referencing specific folders and/or files assumed to be trusted and legitimate. Adversaries may abuse these exclusions to hide their file-based artifacts. For example, rather than tampering with tool settings to add a new exclusion (i.e., Disable or Modify Tools), adversaries may drop their file-based payloads in default or otherwise well-known exclusions. Adversaries may also use Security Software Discovery and other Discovery/Reconnaissance activities to both discover and verify existing exclusions in a victim environment.

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
- T1564.012: https://attack.mitre.org/techniques/T1564/012
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
