# Tool Technique Platform Profile

## Reference

- Technique: **T1588.002 — Tool**
- Platforms named in the source: PRE

Adversaries may buy, steal, or download software tools that can be used during targeting. Tools can be open or closed source, free or commercial. A tool can be used for malicious purposes by an adversary, but (unlike malware) were not intended to be used for those purposes (ex: PsExec). Adversaries may obtain tools to support their operations, including to support execution of post-compromise behaviors. Tools may also be leveraged for testing – for example, evaluating malware against commercial antivirus or endpoint detection and response (EDR) applications. Tool acquisition may involve the procurement of commercial software licenses, including for red teaming tools such as Cobalt Strike. In addition to freely downloading or purchasing software, adversaries may steal software and/or software licenses from third-party entities (including other adversaries). Threat actors may also crack trial versions of software.

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
- T1588.002: https://attack.mitre.org/techniques/T1588/002
- Reviewed: 2026-10-27
