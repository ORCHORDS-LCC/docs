# Databases Technique Platform Profile

## Reference

- Technique: **T1213.006 — Databases**
- Platforms named in the source: IaaS, Linux, macOS, SaaS, Windows

Adversaries may leverage databases to mine valuable information. These databases may be hosted on-premises or in the cloud (both in platform-as-a-service and software-as-a-service environments). Examples of databases from which information may be collected include MySQL, PostgreSQL, MongoDB, Amazon Relational Database Service, Azure SQL Database, Google Firebase, and Snowflake. Databases may include a variety of information of interest to adversaries, such as usernames, hashed passwords, personally identifiable information, and financial data. Data collected from databases may be used for Lateral Movement, Command and Control, or Exfiltration. Data exfiltrated from databases may also be used to extort victims or may be sold for profit.

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
- T1213.006: https://attack.mitre.org/techniques/T1213/006
- Reviewed: 2026-10-27
