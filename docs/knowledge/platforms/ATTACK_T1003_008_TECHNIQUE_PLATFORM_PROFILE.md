# /etc/passwd and /etc/shadow Technique Platform Profile

## Reference

- Technique: **T1003.008 — /etc/passwd and /etc/shadow**
- Platforms named in the source: Linux

Adversaries may attempt to dump the contents of <code>/etc/passwd</code> and <code>/etc/shadow</code> to enable offline password cracking. Most modern Linux operating systems use a combination of <code>/etc/passwd</code> and <code>/etc/shadow</code> to store user account information, including password hashes in <code>/etc/shadow</code>. By default, <code>/etc/shadow</code> is only readable by the root user. Linux stores user information such as user ID, group ID, home directory path, and login shell in <code>/etc/passwd</code>. A "user" on the system may belong to a person or a service. All password hashes are stored in <code>/etc/shadow</code> - including entries for users with no passwords and users with locked or disabled accounts. Adversaries may attempt to read or dump the <code>/etc/passwd</code> and <code>/etc/shadow</code> files on Linux systems via command line utilities such as the <code>cat</code> command. Additionally, the Linux utility <code>unshadow</code> can be used to combine the two files in a format suited for password cracking utilities such as John the Ripper - for example, via the command <code>/usr/bin/unshadow /etc/passwd /etc/shadow > /tmp/crack.password.db</code>. Since the user information stored in <code>/etc/passwd</code> are linked to the password hashes in <code>/etc/shadow</code>, an adversary would need to have access to both.

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
- T1003.008: https://attack.mitre.org/techniques/T1003/008
- Reviewed: 2026-10-27
