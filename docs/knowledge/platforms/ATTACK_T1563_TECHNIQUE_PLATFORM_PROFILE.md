# Remote Service Session Hijacking Technique Platform Profile

## Reference

- Technique: **T1563 — Remote Service Session Hijacking**
- Platforms named in the source: Linux, macOS, Windows

Adversaries may take control of preexisting sessions with remote services to move laterally in an environment. Users may use valid credentials to log into a service specifically designed to accept remote connections, such as telnet, SSH, and RDP. When a user logs into a service, a session will be established that will allow them to maintain a continuous interaction with that service. Adversaries may commandeer these sessions to carry out actions on remote systems. Remote Service Session Hijacking differs from use of Remote Services because it hijacks an existing session rather than creating a new session using Valid Accounts.

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
- T1563: https://attack.mitre.org/techniques/T1563
- Reviewed: 2026-10-27
