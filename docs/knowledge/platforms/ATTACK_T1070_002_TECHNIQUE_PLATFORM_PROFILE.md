# Clear Linux or Mac System Logs Technique Platform Profile

## Reference

- Technique: **T1070.002 — Clear Linux or Mac System Logs**
- Platforms named in the source: Linux, macOS

Adversaries may clear system logs to hide evidence of an intrusion. macOS and Linux both keep track of system or user-initiated actions via system logs. The majority of native system logging is stored under the <code>/var/log/</code> directory. Subfolders in this directory categorize logs by their related functions, such as: * <code>/var/log/messages:</code>: General and system-related messages * <code>/var/log/secure</code> or <code>/var/log/auth.log</code>: Authentication logs * <code>/var/log/utmp</code> or <code>/var/log/wtmp</code>: Login records * <code>/var/log/kern.log</code>: Kernel logs * <code>/var/log/cron.log</code>: Crond logs * <code>/var/log/maillog</code>: Mail server logs * <code>/var/log/httpd/</code>: Web server access and error logs.

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
- T1070.002: https://attack.mitre.org/techniques/T1070/002
- Reviewed: 2026-10-27
