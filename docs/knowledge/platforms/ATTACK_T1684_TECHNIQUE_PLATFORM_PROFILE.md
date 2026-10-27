# Social Engineering Technique Platform Profile

## Reference

- Technique: **T1684 — Social Engineering**
- Platforms named in the source: Linux, macOS, Office Suite, SaaS, Windows

Adversaries may use social engineering techniques to influence users to take actions that result in unauthorized access, approval of changes, disclosure of sensitive information, or execution of adversary-supplied instructions (i.e., introduction of malicious payloads or software), while minimizing technical indicators. Adversaries may leverage trust-building methods across multiple channels (e.g., executive, vendor, or help desk scenarios, including AI-enabled voice interactions) to prompt user-authorized actions such as password resets, MFA changes, financial approvals, or the disclosure of sensitive information. Adversaries may also leverage common business communications and workflows such as email, collaboration platforms, voice communications, recruiting processes, help desk interactions, and SaaS consent mechanisms to make malicious requests appear routine and legitimate. Additionally, adversaries have persuaded victims to take actions through references of current events, harnessing relevant themes to the work role or the organizations mission. For example, adversaries may use scare tactics (i.e., threaten repercussions for non-compliance) or otherwise incite victims’ emotions in order to generate a sense of urgency to take action. This technique may include common social engineering patterns such as Phishing and Spearphishing Voice, often supported by convincing and targeted narratives.

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
- T1684: https://attack.mitre.org/techniques/T1684
- Reviewed: 2026-10-27
