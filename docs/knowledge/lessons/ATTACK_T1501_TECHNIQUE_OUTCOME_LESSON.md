# T1501 Systemd Service Mitigation Outcome Lesson

## Authoritative description

- Technique: **T1501 — Systemd Service Mitigation**

The creation and modification of systemd service unit files is generally reserved for administrators such as the Linux root user and other users with superuser privileges. Limit user access to system utilities such as systemctl to only users who have a legitimate need. Restrict read/write access to systemd unit files to only select privileged users who have a legitimate need to manage system services. Additionally, the installation of software commonly adds and changes systemd service unit files. Restrict software installation to trusted repositories only and be cautious of orphaned software packages. Utilize malicious code protection and application whitelisting to mitigate the ability of malware to create or modify systemd services.

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
- T1501: https://attack.mitre.org/mitigations/T1501
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
