# Customer Relationship Management Software Technique Platform Profile

## Reference

- Technique: **T1213.004 — Customer Relationship Management Software**
- Platforms named in the source: SaaS

Adversaries may leverage Customer Relationship Management (CRM) software to mine valuable information. CRM software is used to assist organizations in tracking and managing customer interactions, as well as storing customer data. Once adversaries gain access to a victim organization, they may mine CRM software for customer data. This may include personally identifiable information (PII) such as full names, emails, phone numbers, and addresses, as well as additional details such as purchase histories and IT support interactions. By collecting this data, an adversary may be able to send personalized Phishing emails, engage in SIM swapping, or otherwise target the organization’s customers in ways that enable financial gain or the compromise of additional organizations. CRM software may be hosted on-premises or in the cloud. Information stored in these solutions may vary based on the specific instance or environment. Examples of CRM software include Microsoft Dynamics 365, Salesforce, Zoho, Zendesk, and HubSpot.

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
- T1213.004: https://attack.mitre.org/techniques/T1213/004
- Reviewed: 2026-10-27
