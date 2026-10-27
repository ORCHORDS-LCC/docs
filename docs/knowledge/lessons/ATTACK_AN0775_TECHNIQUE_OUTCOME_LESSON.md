# AN0775 Analytic 0775 Outcome Lesson

## Authoritative description

- Technique: **AN0775 — Analytic 0775**
- Platforms: Linux

Detection of writes to /boot or EFI directories outside of expected package manager updates. Monitoring kernel log and auditd events for attempts to overwrite bootloader binaries (e.g., grub, shim). Unexpected execution of efibootmgr or dd writing to /dev/sdX devices followed by boot parameter changes.

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
- AN0775: https://attack.mitre.org/detectionstrategies/DET0278#AN0775
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
