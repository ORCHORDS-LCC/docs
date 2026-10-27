# T1027.012 LNK Icon Smuggling Outcome Lesson

## Authoritative description

- Technique: **T1027.012 — LNK Icon Smuggling**
- Tactics: stealth
- Platforms: Windows

Adversaries may smuggle commands to download malicious payloads past content filters by hiding them within otherwise seemingly benign windows shortcut files. Windows shortcut files (.LNK) include many metadata fields, including an icon location field (also known as the `IconEnvironmentDataBlock`) designed to specify the path to an icon file that is to be displayed for the LNK file within a host directory. Adversaries may abuse this LNK metadata to download malicious payloads. For example, adversaries have been observed using LNK files as phishing payloads to deliver malware. Once invoked (e.g., Malicious File), payloads referenced via external URLs within the LNK icon location field may be downloaded. These files may also then be invoked by Command and Scripting Interpreter/System Binary Proxy Execution arguments within the target path field of the LNK. LNK Icon Smuggling may also be utilized post compromise, such as malicious scripts executing an LNK on an infected host to download additional malicious payloads.

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
- T1027.012: https://attack.mitre.org/techniques/T1027/012
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
