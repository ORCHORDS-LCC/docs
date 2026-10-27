# AN0462 Analytic 0462 Outcome Lesson

## Authoritative description

- Technique: **AN0462 — Analytic 0462**
- Platforms: Windows

Adversary installs/uses packet-capture or raw-socket capability (WinPcap/Npcap, wpcap/packet DLLs or raw socket attach) and sets a filter. A crafted inbound packet is observed; within a short window the host process that loaded capture libraries initiates an outbound connection (e.g., reverse shell) to the packet origin.

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
- AN0462: https://attack.mitre.org/detectionstrategies/DET0162#AN0462
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
