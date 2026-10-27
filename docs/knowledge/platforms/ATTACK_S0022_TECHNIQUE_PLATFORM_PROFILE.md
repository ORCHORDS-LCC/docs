# Uroburos Technique Platform Profile

## Reference

- Technique: **S0022 — Uroburos**
- Platforms named in the source: Linux, Windows, macOS

Uroburos is a sophisticated cyber espionage tool written in C that has been used by units within Russia's Federal Security Service (FSB) associated with the Turla toolset to collect intelligence on sensitive targets worldwide. Uroburos has several variants and has undergone nearly constant upgrade since its initial development in 2003 to keep it viable after public disclosures. Uroburos is typically deployed to external-facing nodes on a targeted network and has the ability to leverage additional tools and TTPs to further exploit an internal network. Uroburos has interoperable implants for Windows, Linux, and macOS, employs a high level of stealth in communications and architecture, and can easily incorporate new or replacement components.

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
- S0022: https://attack.mitre.org/software/S0022
- Reviewed: 2026-10-27
