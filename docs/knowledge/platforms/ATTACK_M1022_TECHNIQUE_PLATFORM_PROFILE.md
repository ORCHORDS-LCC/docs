# Restrict File and Directory Permissions Technique Platform Profile

## Reference

- Technique: **M1022 — Restrict File and Directory Permissions**
- Platforms named in the source: not stated

Restricting file and directory permissions involves setting access controls at the file system level to limit which users, groups, or processes can read, write, or execute files. By configuring permissions appropriately, organizations can reduce the attack surface for adversaries seeking to access sensitive data, plant malicious code, or tamper with system files. Enforce Least Privilege Permissions: - Remove unnecessary write permissions on sensitive files and directories. - Use file ownership and groups to control access for specific roles. Example (Windows): Right-click the shared folder → Properties → Security tab → Adjust permissions for NTFS ACLs. Harden File Shares: - Disable anonymous access to shared folders. - Enforce NTFS permissions for shared folders on Windows. Example: Set permissions to restrict write access to critical files, such as system executables (e.g., `/bin` or `/sbin` on Linux). Use tools like `chown` and `chmod` to assign file ownership and limit access. On Linux, apply: `chmod 750 /etc/sensitive.conf` `chown root:admin /etc/sensitive.conf` File Integrity Monitoring (FIM): - Use tools like Tripwire, Wazuh, or OSSEC to monitor changes to critical file permissions. Audit File System Access: - Enable auditing to track permission changes or unauthorized access attempts. - Use auditd (Linux) or Event Viewer (Windows) to log activities. Restrict Startup Directories: - Configure permissions to prevent unauthorized writes to directories like `C:\ProgramData\Microsoft\Windows\Start Menu`. Example: Restrict write access to critical directories like `/etc/`, `/usr/local/`, and Windows directories such as `C:\Windows\System32`. - On Windows, use icacls to modify permissions: `icacls "C:\Windows\System32" /inheritance:r /grant:r SYSTEM:(OI)(CI)F` - On Linux, monitor permissions using tools like `lsattr` or `auditd`.

## Platform profile

1. Record the platforms in scope and the versions actually deployed.
2. Compare the deployed platform surface against the platforms the source names.
3. Record where the platform provides a native control for the technique, and where it does not.
4. Record the configuration evidence for the native control, where one exists.
5. Record the gap where the platform provides no native control, and the compensating detection.
6. Record the platform version, because platform behaviour changes between versions.

## Evidence

- the platform and version inventory for the scoped estate;
- the configuration export or screenshot for the native control;
- the detection evidence where the platform provides none.

## Limitations

A technique entry describes a class of abuse across platforms. The platform-specific exposure is a property of the deployment, established only by inventory and configuration evidence.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- M1022: https://attack.mitre.org/mitigations/M1022
- Reviewed: 2026-10-27
