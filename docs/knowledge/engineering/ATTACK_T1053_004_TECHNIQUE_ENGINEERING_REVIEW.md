# Launchd Technique Engineering Review

## Reference

- Technique: **T1053.004 — Launchd**

This technique is deprecated due to the inaccurate usage. The report cited did not provide technical detail as to how the malware interacted directly with launchd rather than going through known services. Other system services are used to interact with launchd rather than launchd being used by itself. Adversaries may abuse the Launchd daemon to perform task scheduling for initial or recurring execution of malicious code. The launchd daemon, native to macOS, is responsible for loading and maintaining services within the operating system. This process loads the parameters for each launch-on-demand system-level daemon from the property list (plist) files found in /System/Library/LaunchDaemons and /Library/LaunchDaemons . These LaunchDaemons have property list files which point to the executables that will be launched . An adversary may use the launchd daemon in macOS environments to schedule new executables to run at system startup or on a scheduled basis for persistence. launchd can also be abused to run a process under the context of a specified account. Daemons, such as launchd, run with the permissions of the root user account, and will operate regardless of which user account is logged in.

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
- T1053.004: https://attack.mitre.org/techniques/T1053/004
- Reviewed: 2026-10-27
