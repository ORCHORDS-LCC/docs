# Kali365 Technique Platform Profile

## Reference

- Technique: **S9044 — Kali365**
- Platforms named in the source: IaaS, macOS, Windows

Kali365 is a Phishing-as-a-Service (PHaaS) kit first observed in April 2026 that generates victim-targeted lures across multiple operating systems to induce users into copying and pasting actor-controlled commands for local execution. Kali365 incorporates on-demand device code generation and mirrors the copy-paste execution tradecraft associated with ClickFix. Operators have used Kali365 to harvest victims' OAuth tokens and session cookies through adversary-in-the-middle (AiTM) interception, enabling account takeover. Kali365 PHaaS was first observed in April 2026. Kali365 has also been affiliated with other branding to include Octopi365 and Freedom365.

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
- S9044: https://attack.mitre.org/software/S9044
- Reviewed: 2026-10-27
