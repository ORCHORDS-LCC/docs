# Systemd Service Mitigation Technique Response Playbook

## Target technique

**T1501 — Systemd Service Mitigation**


The creation and modification of systemd service unit files is generally reserved for administrators such as the Linux root user and other users with superuser privileges. Limit user access to system utilities such as systemctl to only users who have a legitimate need. Restrict read/write access to systemd unit files to only select privileged users who have a legitimate need to manage system services. Additionally, the installation of software commonly adds and changes systemd service unit files. Restrict software installation to trusted repositories only and be cautious of orphaned software packages. Utilize malicious code protection and application whitelisting to mitigate the ability of malware to create or modify systemd services.

## Preconditions

- the estate in scope is identified, with the systems the technique could apply to;
- an owner is accountable for detection and response;
- current telemetry and configuration can be inspected;
- the technique is applicable or requires an applicability decision.

## Procedure

1. Confirm the scope and owner.
2. Read the current technique description and the associated detection guidance.
3. Inventory the telemetry that would carry the technique's indicators.
4. Inspect whether the indicators are present in the environment.
5. Exercise the detection path and confirm it produces the expected signal.
6. Record gaps in detection coverage and assign remediation owners.
7. Record justified non-applicability or accepted detection gaps separately.
8. Set the next event-driven or periodic verification trigger.

## Failure handling

If the detection path does not produce the expected signal, treat the coverage as unverified, preserve the test evidence, and route the gap through the appropriate remediation or risk process.

## Completion evidence

Scope, owner, source version, telemetry inspected, tests performed, findings, exceptions, remediation links, reviewer, and next trigger.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1501: https://attack.mitre.org/mitigations/T1501
- Reviewed: 2026-10-27
