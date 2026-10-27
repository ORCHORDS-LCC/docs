# T1003.008 /etc/passwd and /etc/shadow Outcome Lesson

## Authoritative description

- Technique: **T1003.008 — /etc/passwd and /etc/shadow**
- Tactics: credential-access
- Platforms: Linux

Adversaries may attempt to dump the contents of <code>/etc/passwd</code> and <code>/etc/shadow</code> to enable offline password cracking. Most modern Linux operating systems use a combination of <code>/etc/passwd</code> and <code>/etc/shadow</code> to store user account information, including password hashes in <code>/etc/shadow</code>. By default, <code>/etc/shadow</code> is only readable by the root user. Linux stores user information such as user ID, group ID, home directory path, and login shell in <code>/etc/passwd</code>. A "user" on the system may belong to a person or a service. All password hashes are stored in <code>/etc/shadow</code> - including entries for users with no passwords and users with locked or disabled accounts. Adversaries may attempt to read or dump the <code>/etc/passwd</code> and <code>/etc/shadow</code> files on Linux systems via command line utilities such as the <code>cat</code> command. Additionally, the Linux utility <code>unshadow</code> can be used to combine the two files in a format suited for password cracking utilities such as John the Ripper - for example, via the command <code>/usr/bin/unshadow /etc/passwd /etc/shadow > /tmp/crack.password.db</code>. Since the user information stored in <code>/etc/passwd</code> are linked to the password hashes in <code>/etc/shadow</code>, an adversary would need to have access to both.

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
- T1003.008: https://attack.mitre.org/techniques/T1003/008
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
