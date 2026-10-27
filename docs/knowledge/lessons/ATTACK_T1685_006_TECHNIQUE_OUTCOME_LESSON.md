# T1685.006 Clear Linux or Mac System Logs Outcome Lesson

## Authoritative description

- Technique: **T1685.006 — Clear Linux or Mac System Logs**
- Tactics: defense-impairment
- Platforms: Linux, macOS

Adversaries may clear system logs to hide evidence of an intrusion. macOS and Linux both keep track of system or user-initiated actions via system logs. The majority of native system logging is stored under the `/var/log/` directory. Subfolders in this directory categorize logs by their related functions, such as: * `/var/log/messages:`: General and system-related messages * `/var/log/secure or /var/log/auth.log`: Authentication logs * `/var/log/utmp or /var/log/wtmp`: Login records * `/var/log/kern.log`: Kernel logs * `/var/log/cron.log`: Crond logs * `/var/log/maillog`: Mail server logs * `/var/log/httpd/`: Web server access and error logs.

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
- T1685.006: https://attack.mitre.org/techniques/T1685/006
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
