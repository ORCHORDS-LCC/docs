# Messaging Applications Technique Platform Profile

## Reference

- Technique: **T1213.005 — Messaging Applications**
- Platforms named in the source: Office Suite, SaaS

Adversaries may leverage chat and messaging applications, such as Microsoft Teams, Google Chat, and Slack, to mine valuable information. The following is a brief list of example information that may hold potential value to an adversary and may also be found on messaging applications: * Testing / development credentials (i.e., Chat Messages) * Source code snippets * Links to network shares and other internal resources * Proprietary data * Discussions about ongoing incident response efforts In addition to exfiltrating data from messaging applications, adversaries may leverage data from chat messages in order to improve their targeting - for example, by learning more about an environment or evading ongoing incident response efforts.

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
- T1213.005: https://attack.mitre.org/techniques/T1213/005
- Reviewed: 2026-10-27
