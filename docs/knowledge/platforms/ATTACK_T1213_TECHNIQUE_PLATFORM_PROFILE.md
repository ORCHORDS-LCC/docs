# Data from Information Repositories Technique Platform Profile

## Reference

- Technique: **T1213 — Data from Information Repositories**
- Platforms named in the source: Linux, Windows, macOS, SaaS, IaaS, Office Suite

Adversaries may leverage information repositories to mine valuable information. Information repositories are tools that allow for storage of information, typically to facilitate collaboration or information sharing between users, and can store a wide variety of data that may aid adversaries in further objectives, such as Credential Access, Lateral Movement, or Defense Evasion, or direct access to the target information. Adversaries may also abuse external sharing features to share sensitive documents with recipients outside of the organization (i.e., Transfer Data to Cloud Account). The following is a brief list of example information that may hold potential value to an adversary and may also be found on an information repository: * Policies, procedures, and standards * Physical / logical network diagrams * System architecture diagrams * Technical system documentation * Testing / development credentials (i.e., Unsecured Credentials) * Work / project schedules * Source code snippets * Links to network shares and other internal resources * Contact or other sensitive information about business partners and customers, including personally identifiable information (PII) Information stored in a repository may vary based on the specific instance or environment. Specific common information repositories include the following: * Storage services such as IaaS databases, enterprise databases, and more specialized platforms such as customer relationship management (CRM) databases * Collaboration platforms such as SharePoint, Confluence, and code repositories * Messaging platforms such as Slack and Microsoft Teams In some cases, information repositories have been improperly secured, typically by unintentionally allowing for overly-broad access by all users or even public access to unauthenticated users. This is particularly common with cloud-native or cloud-hosted services, such as AWS Relational Database Service (RDS), Redis, or ElasticSearch.

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
- T1213: https://attack.mitre.org/techniques/T1213
- Reviewed: 2026-10-27
