# Local Job Scheduling Technique Engineering Review

## Reference

- Technique: **T1168 — Local Job Scheduling**

On Linux and macOS systems, multiple methods are supported for creating pre-scheduled and periodic background jobs: cron, at, and launchd. Unlike Scheduled Task/Job on Windows systems, job scheduling on Linux-based systems cannot be done remotely unless used in conjunction within an established remote session, like secure shell (SSH). ### cron System-wide cron jobs are installed by modifying /etc/crontab file, /etc/cron.d/ directory or other locations supported by the Cron daemon, while per-user cron jobs are installed using crontab with specifically formatted crontab files. This works on macOS and Linux systems. Those methods allow for commands or scripts to be executed at specific, periodic intervals in the background without user interaction. An adversary may use job scheduling to execute programs at system startup or on a scheduled basis for Persistence, to conduct Execution as part of Lateral Movement, to gain root privileges, or to run a process under the context of a specific account. ### at The at program is another means on POSIX-based systems, including macOS and Linux, to schedule a program or script job for execution at a later date and/or time, which could also be used for the same purposes. ### launchd Each launchd job is described by a different configuration property list (plist) file similar to Launch Daemon or Launch Agent, except there is an additional key called StartCalendarInterval with a dictionary of time values. This only works on macOS and OS X.

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
- T1168: https://attack.mitre.org/techniques/T1168
- Reviewed: 2026-10-27
