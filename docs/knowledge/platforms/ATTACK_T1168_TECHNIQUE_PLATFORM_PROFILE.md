# Local Job Scheduling Technique Platform Profile

## Reference

- Technique: **T1168 — Local Job Scheduling**
- Platforms named in the source: Linux, macOS

On Linux and macOS systems, multiple methods are supported for creating pre-scheduled and periodic background jobs: cron, at, and launchd. Unlike Scheduled Task/Job on Windows systems, job scheduling on Linux-based systems cannot be done remotely unless used in conjunction within an established remote session, like secure shell (SSH). ### cron System-wide cron jobs are installed by modifying /etc/crontab file, /etc/cron.d/ directory or other locations supported by the Cron daemon, while per-user cron jobs are installed using crontab with specifically formatted crontab files. This works on macOS and Linux systems. Those methods allow for commands or scripts to be executed at specific, periodic intervals in the background without user interaction. An adversary may use job scheduling to execute programs at system startup or on a scheduled basis for Persistence, to conduct Execution as part of Lateral Movement, to gain root privileges, or to run a process under the context of a specific account. ### at The at program is another means on POSIX-based systems, including macOS and Linux, to schedule a program or script job for execution at a later date and/or time, which could also be used for the same purposes. ### launchd Each launchd job is described by a different configuration property list (plist) file similar to Launch Daemon or Launch Agent, except there is an additional key called StartCalendarInterval with a dictionary of time values. This only works on macOS and OS X.

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
- T1168: https://attack.mitre.org/techniques/T1168
- Reviewed: 2026-10-27
