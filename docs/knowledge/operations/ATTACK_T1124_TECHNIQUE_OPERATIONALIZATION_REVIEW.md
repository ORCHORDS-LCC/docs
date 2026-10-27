# System Time Discovery Technique Operationalization Review

## Reference

- Technique: **T1124 — System Time Discovery**

An adversary may gather the system time and/or time zone settings from a local or remote system. The system time is set and stored by services, such as the Windows Time Service on Windows or systemsetup on macOS. These time settings may also be synchronized between systems and services in an enterprise network, typically accomplished with a network time server within a domain. System time information may be gathered in a number of ways, such as with Net on Windows by performing net time \\hostname to gather the system time on a remote system. The victim's time zone may also be inferred from the current system time or gathered by using w32tm /tz. In addition, adversaries can discover device uptime through functions such as GetTickCount() to determine how long it has been since the system booted up. On network devices, Network Device CLI commands such as `show clock detail` can be used to see the current time configuration. On ESXi servers, `esxcli system clock get` can be used for the same purpose. In addition, system calls – such as time() – have been used to collect the current time on Linux devices. On macOS systems, adversaries may use commands such as systemsetup -gettimezone or timeIntervalSinceNow to gather current time zone information or current date and time. This information could be useful for performing other techniques, such as executing a file with a Scheduled Task/Job, or to discover locality information based on time zone to assist in victim targeting (i.e. System Location Discovery). Adversaries may also use knowledge of system time as part of a time bomb, or delaying execution until a specified date/time.

## Operationalization review

1. Record the operational scope: which services, environments, and data the technique could affect.
2. Record the runbook that would be executed, and its owner.
3. Record the telemetry the runbook depends on, and whether it is retained long enough to investigate.
4. Record the detection that would surface the technique before or after it has an effect.
5. Record the recovery path, and the evidence that recovery has been rehearsed.
6. Record the residual operational risk where the runbook depends on a manual step.

## Review evidence

- the runbook and its owner;
- the telemetry retention and coverage record;
- the detection mapping;
- the exercise or rehearsal record.

## Limitations

An operationalization review describes the runbook and the evidence around it. It does not claim the technique has been prevented or detected in a live environment.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1124: https://attack.mitre.org/techniques/T1124
- Reviewed: 2026-10-27
