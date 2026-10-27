# Spearphishing Voice Technique Platform Profile

## Reference

- Technique: **T1566.004 — Spearphishing Voice**
- Platforms named in the source: Linux, macOS, Windows, Identity Provider

Adversaries may use voice communications to ultimately gain access to victim systems. Spearphishing voice is a specific variant of spearphishing. It is different from other forms of spearphishing in that it employs the use of manipulating a user into providing access to systems through a phone call or other forms of voice communications. Spearphishing frequently involves social engineering techniques, such as posing as a trusted source (ex: Impersonation) and/or creating a sense of urgency or alarm for the recipient. All forms of phishing are electronically delivered social engineering. In this scenario, adversaries are not directly sending malware to a victim vice relying on User Execution for delivery and execution. For example, victims may receive phishing messages that instruct them to call a phone number where they are directed to visit a malicious URL, download malware, or install adversary-accessible remote management tools (Remote Access Tools) onto their computer. Adversaries may also combine voice phishing with Multi-Factor Authentication Request Generation in order to trick users into divulging MFA credentials or accepting authentication prompts.

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
- T1566.004: https://attack.mitre.org/techniques/T1566/004
- Reviewed: 2026-10-27
