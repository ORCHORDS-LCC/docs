# Launchd Technique Platform Profile

## Reference

- Technique: **T1053.004 — Launchd**
- Platforms named in the source: macOS

This technique is deprecated due to the inaccurate usage. The report cited did not provide technical detail as to how the malware interacted directly with launchd rather than going through known services. Other system services are used to interact with launchd rather than launchd being used by itself. Adversaries may abuse the <code>Launchd</code> daemon to perform task scheduling for initial or recurring execution of malicious code. The <code>launchd</code> daemon, native to macOS, is responsible for loading and maintaining services within the operating system. This process loads the parameters for each launch-on-demand system-level daemon from the property list (plist) files found in <code>/System/Library/LaunchDaemons</code> and <code>/Library/LaunchDaemons</code> . These LaunchDaemons have property list files which point to the executables that will be launched . An adversary may use the <code>launchd</code> daemon in macOS environments to schedule new executables to run at system startup or on a scheduled basis for persistence. <code>launchd</code> can also be abused to run a process under the context of a specified account. Daemons, such as <code>launchd</code>, run with the permissions of the root user account, and will operate regardless of which user account is logged in.

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
- T1053.004: https://attack.mitre.org/techniques/T1053/004
- Reviewed: 2026-10-27
