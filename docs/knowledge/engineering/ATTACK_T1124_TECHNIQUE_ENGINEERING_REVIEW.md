# System Time Discovery Technique Engineering Review

## Reference

- Technique: **T1124 — System Time Discovery**

An adversary may gather the system time and/or time zone settings from a local or remote system. The system time is set and stored by services, such as the Windows Time Service on Windows or systemsetup on macOS. These time settings may also be synchronized between systems and services in an enterprise network, typically accomplished with a network time server within a domain. System time information may be gathered in a number of ways, such as with Net on Windows by performing net time \\hostname to gather the system time on a remote system. The victim's time zone may also be inferred from the current system time or gathered by using w32tm /tz. In addition, adversaries can discover device uptime through functions such as GetTickCount() to determine how long it has been since the system booted up. On network devices, Network Device CLI commands such as `show clock detail` can be used to see the current time configuration. On ESXi servers, `esxcli system clock get` can be used for the same purpose. In addition, system calls – such as time() – have been used to collect the current time on Linux devices. On macOS systems, adversaries may use commands such as systemsetup -gettimezone or timeIntervalSinceNow to gather current time zone information or current date and time. This information could be useful for performing other techniques, such as executing a file with a Scheduled Task/Job, or to discover locality information based on time zone to assist in victim targeting (i.e. System Location Discovery). Adversaries may also use knowledge of system time as part of a time bomb, or delaying execution until a specified date/time.

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
- T1124: https://attack.mitre.org/techniques/T1124
- Reviewed: 2026-10-27
