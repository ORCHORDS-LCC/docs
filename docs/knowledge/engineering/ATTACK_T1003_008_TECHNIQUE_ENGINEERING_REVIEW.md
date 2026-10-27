# /etc/passwd and /etc/shadow Technique Engineering Review

## Reference

- Technique: **T1003.008 — /etc/passwd and /etc/shadow**

Adversaries may attempt to dump the contents of /etc/passwd and /etc/shadow to enable offline password cracking. Most modern Linux operating systems use a combination of /etc/passwd and /etc/shadow to store user account information, including password hashes in /etc/shadow. By default, /etc/shadow is only readable by the root user. Linux stores user information such as user ID, group ID, home directory path, and login shell in /etc/passwd. A "user" on the system may belong to a person or a service. All password hashes are stored in /etc/shadow - including entries for users with no passwords and users with locked or disabled accounts. Adversaries may attempt to read or dump the /etc/passwd and /etc/shadow files on Linux systems via command line utilities such as the cat command. Additionally, the Linux utility unshadow can be used to combine the two files in a format suited for password cracking utilities such as John the Ripper - for example, via the command /usr/bin/unshadow /etc/passwd /etc/shadow > /tmp/crack.password.db. Since the user information stored in /etc/passwd are linked to the password hashes in /etc/shadow, an adversary would need to have access to both.

## Engineering review

1. Identify the engineering boundary where the technique would apply: the component, the service, or the deployment.
2. Review the design decision that would prevent the technique, and record the alternative considered.
3. Review the implementation evidence for the preventive control.
4. Review the test coverage that would fail if the control regressed.
5. Review the observability: which signal would show the control is not operating.
6. Record the residual risk where prevention is not achievable, and the detection that compensates.

## Review evidence

- the design record for the preventive decision;
- the implementation or configuration evidence;
- the test record showing the control is exercised;
- the observability mapping.

## Limitations

An engineering review describes what the design and the implementation evidence show. It does not claim the technique has been addressed in production.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1003.008: https://attack.mitre.org/techniques/T1003/008
- Reviewed: 2026-10-27
