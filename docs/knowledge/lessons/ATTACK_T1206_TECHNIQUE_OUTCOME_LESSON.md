# T1206 Sudo Caching Outcome Lesson

## Authoritative description

- Technique: **T1206 — Sudo Caching**
- Tactics: privilege-escalation
- Platforms: Linux, macOS

The sudo command "allows a system administrator to delegate authority to give certain users (or groups of users) the ability to run some (or all) commands as root or another user while providing an audit trail of the commands and their arguments." Since sudo was made for the system administrator, it has some useful configuration features such as a timestamp_timeout that is the amount of time in minutes between instances of sudo before it will re-prompt for a password. This is because sudo has the ability to cache credentials for a period of time. Sudo creates (or touches) a file at /var/db/sudo with a timestamp of when sudo was last run to determine this timeout. Additionally, there is a tty_tickets variable that treats each new tty (terminal session) in isolation. This means that, for example, the sudo timeout of one tty will not affect another tty (you will have to type the password again). Adversaries can abuse poor configurations of this to escalate privileges without needing the user's password. /var/db/sudo's timestamp can be monitored to see if it falls within the timestamp_timeout range. If it does, then malware can execute sudo commands without needing to supply the user's password. When tty_tickets is disabled, adversaries can do this from any tty for that user. The OSX Proton Malware has disabled tty_tickets to potentially make scripting easier by issuing echo \'Defaults !tty_tickets\' >> /etc/sudoers . In order for this change to be reflected, the Proton malware also must issue killall Terminal. As of macOS Sierra, the sudoers file has tty_tickets enabled by default.

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
- T1206: https://attack.mitre.org/techniques/T1206
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
