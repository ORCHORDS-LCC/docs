# Fooder Technique Platform Profile

## Reference

- Technique: **S9033 — Fooder**
- Platforms named in the source: Windows

Fooder is a custom 64-bit C/C++ loader used by MuddyWater that can decrypt and reflectively load embedded payloads such as a go-socks5 proxy utility, the open-source HackBrowserData infostealer, or the MuddyViper backdoor. Fooder has frequently masqueraded as an entertainment executable, such as the Snake game (e.g., `Snake_Game.exe`).

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
- S9033: https://attack.mitre.org/software/S9033
- Reviewed: 2026-10-27
