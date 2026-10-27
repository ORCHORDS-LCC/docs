# /etc/passwd and /etc/shadow Technique Platform Profile

## Reference

- Technique: **T1003.008 — /etc/passwd and /etc/shadow**
- Platforms named in the source: Linux

Adversaries may attempt to dump the contents of /etc/passwd and /etc/shadow to enable offline password cracking. Most modern Linux operating systems use a combination of /etc/passwd and /etc/shadow to store user account information, including password hashes in /etc/shadow. By default, /etc/shadow is only readable by the root user. Linux stores user information such as user ID, group ID, home directory path, and login shell in /etc/passwd. A "user" on the system may belong to a person or a service. All password hashes are stored in /etc/shadow - including entries for users with no passwords and users with locked or disabled accounts. Adversaries may attempt to read or dump the /etc/passwd and /etc/shadow files on Linux systems via command line utilities such as the cat command. Additionally, the Linux utility unshadow can be used to combine the two files in a format suited for password cracking utilities such as John the Ripper - for example, via the command /usr/bin/unshadow /etc/passwd /etc/shadow > /tmp/crack.password.db. Since the user information stored in /etc/passwd are linked to the password hashes in /etc/shadow, an adversary would need to have access to both.

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
