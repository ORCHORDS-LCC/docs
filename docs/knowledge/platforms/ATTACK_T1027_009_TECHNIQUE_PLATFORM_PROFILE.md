# Embedded Payloads Technique Platform Profile

## Reference

- Technique: **T1027.009 — Embedded Payloads**
- Platforms named in the source: Linux, macOS, Windows

Adversaries may embed payloads within other files to conceal malicious content from defenses. Otherwise seemingly benign files (such as scripts and executables) may be abused to carry and obfuscate malicious payloads and content. In some cases, embedded payloads may also enable adversaries to Subvert Trust Controls by not impacting execution controls such as digital signatures and notarization tickets. Adversaries may embed payloads in various file formats to hide payloads. This is similar to Steganography, though does not involve weaving malicious content into specific bytes and patterns related to legitimate digital media formats. For example, adversaries have been observed embedding payloads within or as an overlay of an otherwise benign binary. Adversaries have also been observed nesting payloads (such as executables and run-only scripts) inside a file of the same format. Embedded content may also be used as Process Injection payloads used to infect benign system processes. These embedded then injected payloads may be used as part of the modules of malware designed to provide specific features such as encrypting C2 communications in support of an orchestrator module. For example, an embedded module may be injected into default browsers, allowing adversaries to then communicate via the network.

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
- T1027.009: https://attack.mitre.org/techniques/T1027/009
- Reviewed: 2026-10-27
