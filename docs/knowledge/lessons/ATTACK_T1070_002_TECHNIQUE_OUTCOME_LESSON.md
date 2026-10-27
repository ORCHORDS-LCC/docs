# T1070.002 Clear Linux or Mac System Logs Outcome Lesson

## Authoritative description

- Technique: **T1070.002 — Clear Linux or Mac System Logs**
- Tactics: stealth
- Platforms: Linux, macOS

Adversaries may clear system logs to hide evidence of an intrusion. macOS and Linux both keep track of system or user-initiated actions via system logs. The majority of native system logging is stored under the <code>/var/log/</code> directory. Subfolders in this directory categorize logs by their related functions, such as: * <code>/var/log/messages:</code>: General and system-related messages * <code>/var/log/secure</code> or <code>/var/log/auth.log</code>: Authentication logs * <code>/var/log/utmp</code> or <code>/var/log/wtmp</code>: Login records * <code>/var/log/kern.log</code>: Kernel logs * <code>/var/log/cron.log</code>: Crond logs * <code>/var/log/maillog</code>: Mail server logs * <code>/var/log/httpd/</code>: Web server access and error logs.

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
- T1070.002: https://attack.mitre.org/techniques/T1070/002
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
