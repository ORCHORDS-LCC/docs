# AN1475 Analytic 1475 Outcome Lesson

## Authoritative description

- Technique: **AN1475 — Analytic 1475**
- Platforms: ESXi

Malicious VIB installation for persistence via `esxcli software vib install` using `--force` or `--no-sig-check`, enabling custom startup scripts or firewall rules. Behavior chain: (1) unsigned/suspicious VIB installation → (2) startup script or binary placed in persistent boot path → (3) persistence across reboot via /etc/rc.local.d or other boot hook).

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
- AN1475: https://attack.mitre.org/detectionstrategies/DET0535#AN1475
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
