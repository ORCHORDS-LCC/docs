# T1213 Data from Information Repositories Outcome Lesson

## Authoritative description

- Technique: **T1213 — Data from Information Repositories**
- Tactics: collection
- Platforms: Linux, Windows, macOS, SaaS, IaaS, Office Suite

Adversaries may leverage information repositories to mine valuable information. Information repositories are tools that allow for storage of information, typically to facilitate collaboration or information sharing between users, and can store a wide variety of data that may aid adversaries in further objectives, such as Credential Access, Lateral Movement, or Defense Evasion, or direct access to the target information. Adversaries may also abuse external sharing features to share sensitive documents with recipients outside of the organization (i.e., Transfer Data to Cloud Account). The following is a brief list of example information that may hold potential value to an adversary and may also be found on an information repository: * Policies, procedures, and standards * Physical / logical network diagrams * System architecture diagrams * Technical system documentation * Testing / development credentials (i.e., Unsecured Credentials) * Work / project schedules * Source code snippets * Links to network shares and other internal resources * Contact or other sensitive information about business partners and customers, including personally identifiable information (PII) Information stored in a repository may vary based on the specific instance or environment. Specific common information repositories include the following: * Storage services such as IaaS databases, enterprise databases, and more specialized platforms such as customer relationship management (CRM) databases * Collaboration platforms such as SharePoint, Confluence, and code repositories * Messaging platforms such as Slack and Microsoft Teams In some cases, information repositories have been improperly secured, typically by unintentionally allowing for overly-broad access by all users or even public access to unauthenticated users. This is particularly common with cloud-native or cloud-hosted services, such as AWS Relational Database Service (RDS), Redis, or ElasticSearch.

## Reusable lesson

This technique should be treated as an explicit review question when it is relevant to the system or organisation, rather than assumed to be covered by a generic control statement or by tooling that reports a related signal.

## Apply the lesson

1. Define the real scope before judging coverage.
2. Inspect current technical, process, governance, or operational evidence.
3. Separate documented intent from verified behaviour.
4. Record partial coverage and unresolved gaps instead of converting them into a pass.
5. Revisit when the underlying scope, threat environment, technology, suppliers, or mission materially changes.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1213: https://attack.mitre.org/techniques/T1213
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
