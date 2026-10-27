# Redundant Access Technique Platform Profile

## Reference

- Technique: **T1108 — Redundant Access**
- Platforms named in the source: Windows, SaaS, IaaS, Linux, macOS, Office Suite, Identity Provider

**This technique has been deprecated. Please use Create Account, Web Shell, and External Remote Services where appropriate.** Adversaries may use more than one remote access tool with varying command and control protocols or credentialed access to remote services so they can maintain access if an access mechanism is detected or mitigated. If one type of tool is detected and blocked or removed as a response but the organization did not gain a full understanding of the adversary's tools and access, then the adversary will be able to retain access to the network. Adversaries may also attempt to gain access to Valid Accounts to use External Remote Services such as external VPNs as a way to maintain access despite interruptions to remote access tools deployed within a target network. Adversaries may also retain access through cloud-based infrastructure and applications. Use of a Web Shell is one such way to maintain access to a network through an externally accessible Web server.

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
- T1108: https://attack.mitre.org/techniques/T1108
- Reviewed: 2026-10-27
