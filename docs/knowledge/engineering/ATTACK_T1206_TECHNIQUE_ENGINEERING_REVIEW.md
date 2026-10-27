# Sudo Caching Technique Engineering Review

## Reference

- Technique: **T1206 — Sudo Caching**

The sudo command "allows a system administrator to delegate authority to give certain users (or groups of users) the ability to run some (or all) commands as root or another user while providing an audit trail of the commands and their arguments." Since sudo was made for the system administrator, it has some useful configuration features such as a timestamp_timeout that is the amount of time in minutes between instances of sudo before it will re-prompt for a password. This is because sudo has the ability to cache credentials for a period of time. Sudo creates (or touches) a file at /var/db/sudo with a timestamp of when sudo was last run to determine this timeout. Additionally, there is a tty_tickets variable that treats each new tty (terminal session) in isolation. This means that, for example, the sudo timeout of one tty will not affect another tty (you will have to type the password again). Adversaries can abuse poor configurations of this to escalate privileges without needing the user's password. /var/db/sudo's timestamp can be monitored to see if it falls within the timestamp_timeout range. If it does, then malware can execute sudo commands without needing to supply the user's password. When tty_tickets is disabled, adversaries can do this from any tty for that user. The OSX Proton Malware has disabled tty_tickets to potentially make scripting easier by issuing echo \'Defaults !tty_tickets\' >> /etc/sudoers . In order for this change to be reflected, the Proton malware also must issue killall Terminal. As of macOS Sierra, the sudoers file has tty_tickets enabled by default.

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
- T1206: https://attack.mitre.org/techniques/T1206
- Reviewed: 2026-10-27
