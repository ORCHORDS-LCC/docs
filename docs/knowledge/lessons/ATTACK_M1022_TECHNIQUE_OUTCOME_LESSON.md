# M1022 Restrict File and Directory Permissions Outcome Lesson

## Authoritative description

- Technique: **M1022 — Restrict File and Directory Permissions**

Restricting file and directory permissions involves setting access controls at the file system level to limit which users, groups, or processes can read, write, or execute files. By configuring permissions appropriately, organizations can reduce the attack surface for adversaries seeking to access sensitive data, plant malicious code, or tamper with system files. Enforce Least Privilege Permissions: - Remove unnecessary write permissions on sensitive files and directories. - Use file ownership and groups to control access for specific roles. Example (Windows): Right-click the shared folder → Properties → Security tab → Adjust permissions for NTFS ACLs. Harden File Shares: - Disable anonymous access to shared folders. - Enforce NTFS permissions for shared folders on Windows. Example: Set permissions to restrict write access to critical files, such as system executables (e.g., `/bin` or `/sbin` on Linux). Use tools like `chown` and `chmod` to assign file ownership and limit access. On Linux, apply: `chmod 750 /etc/sensitive.conf` `chown root:admin /etc/sensitive.conf` File Integrity Monitoring (FIM): - Use tools like Tripwire, Wazuh, or OSSEC to monitor changes to critical file permissions. Audit File System Access: - Enable auditing to track permission changes or unauthorized access attempts. - Use auditd (Linux) or Event Viewer (Windows) to log activities. Restrict Startup Directories: - Configure permissions to prevent unauthorized writes to directories like `C:\ProgramData\Microsoft\Windows\Start Menu`. Example: Restrict write access to critical directories like `/etc/`, `/usr/local/`, and Windows directories such as `C:\Windows\System32`. - On Windows, use icacls to modify permissions: `icacls "C:\Windows\System32" /inheritance:r /grant:r SYSTEM:(OI)(CI)F` - On Linux, monitor permissions using tools like `lsattr` or `auditd`.

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
- M1022: https://attack.mitre.org/mitigations/M1022
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
