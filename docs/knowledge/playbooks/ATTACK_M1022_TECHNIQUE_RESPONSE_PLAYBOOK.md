# Restrict File and Directory Permissions Technique Response Playbook

## Target technique

**M1022 — Restrict File and Directory Permissions**


Restricting file and directory permissions involves setting access controls at the file system level to limit which users, groups, or processes can read, write, or execute files. By configuring permissions appropriately, organizations can reduce the attack surface for adversaries seeking to access sensitive data, plant malicious code, or tamper with system files. Enforce Least Privilege Permissions: - Remove unnecessary write permissions on sensitive files and directories. - Use file ownership and groups to control access for specific roles. Example (Windows): Right-click the shared folder → Properties → Security tab → Adjust permissions for NTFS ACLs. Harden File Shares: - Disable anonymous access to shared folders. - Enforce NTFS permissions for shared folders on Windows. Example: Set permissions to restrict write access to critical files, such as system executables (e.g., `/bin` or `/sbin` on Linux). Use tools like `chown` and `chmod` to assign file ownership and limit access. On Linux, apply: `chmod 750 /etc/sensitive.conf` `chown root:admin /etc/sensitive.conf` File Integrity Monitoring (FIM): - Use tools like Tripwire, Wazuh, or OSSEC to monitor changes to critical file permissions. Audit File System Access: - Enable auditing to track permission changes or unauthorized access attempts. - Use auditd (Linux) or Event Viewer (Windows) to log activities. Restrict Startup Directories: - Configure permissions to prevent unauthorized writes to directories like `C:\ProgramData\Microsoft\Windows\Start Menu`. Example: Restrict write access to critical directories like `/etc/`, `/usr/local/`, and Windows directories such as `C:\Windows\System32`. - On Windows, use icacls to modify permissions: `icacls "C:\Windows\System32" /inheritance:r /grant:r SYSTEM:(OI)(CI)F` - On Linux, monitor permissions using tools like `lsattr` or `auditd`.

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
- M1022: https://attack.mitre.org/mitigations/M1022
- Reviewed: 2026-10-27
