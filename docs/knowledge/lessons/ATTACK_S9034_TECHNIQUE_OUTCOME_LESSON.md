# S9034 Tsundere Botnet Outcome Lesson

## Authoritative description

- Technique: **S9034 — Tsundere Botnet**
- Platforms: Linux, macOS, Windows

Tsundere Botnet is a botnet first reported in mid-2025 that is delivered via MSI installer or a PowerShell script. It leverages Node.js and JavaScript for payload delivery and execution, and uses smart contracts on the blockchain to host command and control (C2) addresses. Tsundere Botnet is attributed to a likely Russian-speaking threat actor. A variant named DinDoor has been linked to MuddyWater operations and uses the Deno runtime for execution rather than Node.js.

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
- S9034: https://attack.mitre.org/software/S9034
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
