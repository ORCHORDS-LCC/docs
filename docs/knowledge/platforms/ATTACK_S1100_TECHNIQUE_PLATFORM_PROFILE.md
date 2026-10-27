# Ninja Technique Platform Profile

## Reference

- Technique: **S1100 — Ninja**
- Platforms named in the source: Windows

Ninja is a malware developed in C++ that has been used by ToddyCat to penetrate networks and control remote systems since at least 2020. Ninja is possibly part of a post exploitation toolkit exclusively used by ToddyCat and allows multiple operators to work simultaneously on the same machine. Ninja has been used against government and military entities in Europe and Asia and observed in specific infection chains being deployed by Samurai.

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
- S1100: https://attack.mitre.org/software/S1100
- Reviewed: 2026-10-27
