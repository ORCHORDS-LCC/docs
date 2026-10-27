# Phishing Technique Platform Profile

## Reference

- Technique: **T1566 — Phishing**
- Platforms named in the source: Identity Provider, Linux, macOS, Office Suite, SaaS, Windows

Adversaries may send phishing messages to gain access to victim systems. All forms of phishing are electronically delivered social engineering. Phishing can be targeted, known as spearphishing. In spearphishing, a specific individual, company, or industry will be targeted by the adversary. More generally, adversaries can conduct non-targeted phishing, such as in mass malware spam campaigns. Adversaries may send victims emails containing malicious attachments or links, typically to execute malicious code on victim systems. Phishing may also be conducted via third-party services (like social media platforms) or delivered via calendar invites. Phishing may also involve social engineering techniques, such as posing as a trusted source, as well as evasive techniques such as removing or manipulating emails or metadata/headers from compromised accounts being abused to send messages (e.g., Email Hiding Rules). Another way to accomplish this is by Email Spoofing the identity of the sender, which can be used to fool both the human recipient as well as automated security tools, or by including the intended target as a party to an existing email thread that includes malicious files or links (i.e., "thread hijacking"). Victims may also receive phishing messages that instruct them to call a phone number where they are directed to visit a malicious URL, download malware, or install adversary-accessible remote management tools onto their computer (i.e., User Execution).

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
- T1566: https://attack.mitre.org/techniques/T1566
- Reviewed: 2026-10-27
