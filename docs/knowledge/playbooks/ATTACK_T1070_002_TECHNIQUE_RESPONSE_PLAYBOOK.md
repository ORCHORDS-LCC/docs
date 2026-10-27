# Clear Linux or Mac System Logs Technique Response Playbook

## Target technique

**T1070.002 — Clear Linux or Mac System Logs**

- Tactics: stealth
- Platforms: Linux, macOS

Adversaries may clear system logs to hide evidence of an intrusion. macOS and Linux both keep track of system or user-initiated actions via system logs. The majority of native system logging is stored under the <code>/var/log/</code> directory. Subfolders in this directory categorize logs by their related functions, such as: * <code>/var/log/messages:</code>: General and system-related messages * <code>/var/log/secure</code> or <code>/var/log/auth.log</code>: Authentication logs * <code>/var/log/utmp</code> or <code>/var/log/wtmp</code>: Login records * <code>/var/log/kern.log</code>: Kernel logs * <code>/var/log/cron.log</code>: Crond logs * <code>/var/log/maillog</code>: Mail server logs * <code>/var/log/httpd/</code>: Web server access and error logs.

## Preconditions

- the estate in scope is identified, with the systems the technique could apply to;
- an owner is accountable for detection and response;
- current telemetry and configuration can be inspected;
- the technique is applicable or requires an applicability decision.

## Procedure

1. Confirm the scope and owner.
2. Read the current technique description and the associated detection guidance.
3. Inventory the telemetry that would carry the technique's indicators.
4. Inspect whether the indicators are present in the environment.
5. Exercise the detection path and confirm it produces the expected signal.
6. Record gaps in detection coverage and assign remediation owners.
7. Record justified non-applicability or accepted detection gaps separately.
8. Set the next event-driven or periodic verification trigger.

## Failure handling

If the detection path does not produce the expected signal, treat the coverage as unverified, preserve the test evidence, and route the gap through the appropriate remediation or risk process.

## Completion evidence

Scope, owner, source version, telemetry inspected, tests performed, findings, exceptions, remediation links, reviewer, and next trigger.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1070.002: https://attack.mitre.org/techniques/T1070/002
- Reviewed: 2026-10-27
