# Financial Theft Technique Platform Profile

## Reference

- Technique: **T1657 — Financial Theft**
- Platforms named in the source: Linux, macOS, Office Suite, SaaS, Windows

Adversaries may steal monetary resources from targets through extortion, social engineering, technical theft, or other methods aimed at their own financial gain at the expense of the availability of these resources for victims. Financial theft is the ultimate objective of several popular campaign types including extortion by ransomware, business email compromise (BEC) and fraud, "pig butchering," bank hacking, and exploiting cryptocurrency networks. Adversaries may Compromise Accounts to conduct unauthorized transfers of funds. In the case of business email compromise or email fraud, an adversary may utilize Impersonation of a trusted entity. Once the social engineering is successful, victims can be deceived into sending money to financial accounts controlled by an adversary. This creates the potential for multiple victims (i.e., compromised accounts as well as the ultimate monetary loss) in incidents involving financial theft. Extortion by ransomware may occur, for example, when an adversary demands payment from a victim after Data Encrypted for Impact and Exfiltration of data, followed by threatening to leak sensitive data to the public unless payment is made to the adversary. Adversaries may use dedicated leak sites to distribute victim data. Due to the potentially immense business impact of financial theft, an adversary may abuse the possibility of financial theft and seeking monetary gain to divert attention from their true goals such as Data Destruction and business disruption.

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
- T1657: https://attack.mitre.org/techniques/T1657
- Reviewed: 2026-10-27
