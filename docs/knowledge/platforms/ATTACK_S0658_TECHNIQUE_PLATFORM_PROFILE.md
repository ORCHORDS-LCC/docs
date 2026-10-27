# XCSSET Technique Platform Profile

## Reference

- Technique: **S0658 — XCSSET**
- Platforms named in the source: macOS

XCSSET is a modular macOS malware family delivered through infected Xcode projects and executed when the project is compiled. Active since August 2020, it has been observed installing backdoors, spoofed browsers, collecting data, and encrypting user files. It is composed of SHC-compiled shell scripts and run-only AppleScripts, often hiding in apps that mimic system tools (such as Xcode, Mail, or Notes) or use familiar icons (like Launchpad) to avoid detection.

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
- S0658: https://attack.mitre.org/software/S0658
- Reviewed: 2026-10-27
