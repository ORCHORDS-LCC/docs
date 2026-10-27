# T1569.003 Systemctl Outcome Lesson

## Authoritative description

- Technique: **T1569.003 — Systemctl**
- Tactics: execution
- Platforms: Linux

Adversaries may abuse systemctl to execute commands or programs. Systemctl is the primary interface for systemd, the Linux init system and service manager. Typically invoked from a shell, Systemctl can also be integrated into scripts or applications. Adversaries may use systemctl to execute commands or programs as Systemd Services. Common subcommands include: `systemctl start`, `systemctl stop`, `systemctl enable`, `systemctl disable`, and `systemctl status`.

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
- T1569.003: https://attack.mitre.org/techniques/T1569/003
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
