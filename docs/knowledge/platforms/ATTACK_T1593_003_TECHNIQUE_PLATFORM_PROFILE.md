# Code Repositories Technique Platform Profile

## Reference

- Technique: **T1593.003 — Code Repositories**
- Platforms named in the source: PRE

Adversaries may search public code repositories for information about victims that can be used during targeting. Victims may store code in repositories on various third-party websites such as GitHub, GitLab, SourceForge, and BitBucket. Users typically interact with code repositories through a web application or command-line utilities such as git. Adversaries may search various public code repositories for various information about a victim. Public code repositories can often be a source of various general information about victims, such as commonly used programming languages and libraries as well as the names of employees. Adversaries may also identify more sensitive data, including accidentally leaked credentials or API keys. Information from these sources may reveal opportunities for other forms of reconnaissance (ex: Phishing for Information), establishing operational resources (ex: Compromise Accounts or Compromise Infrastructure), and/or initial access (ex: Valid Accounts or Phishing). **Note:** This is distinct from Code Repositories, which focuses on Collection from private and internally hosted code repositories.

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
- T1593.003: https://attack.mitre.org/techniques/T1593/003
- Reviewed: 2026-10-27
