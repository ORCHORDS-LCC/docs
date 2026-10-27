# Customer Relationship Management Software Technique Operationalization Review

## Reference

- Technique: **T1213.004 — Customer Relationship Management Software**

Adversaries may leverage Customer Relationship Management (CRM) software to mine valuable information. CRM software is used to assist organizations in tracking and managing customer interactions, as well as storing customer data. Once adversaries gain access to a victim organization, they may mine CRM software for customer data. This may include personally identifiable information (PII) such as full names, emails, phone numbers, and addresses, as well as additional details such as purchase histories and IT support interactions. By collecting this data, an adversary may be able to send personalized Phishing emails, engage in SIM swapping, or otherwise target the organization’s customers in ways that enable financial gain or the compromise of additional organizations. CRM software may be hosted on-premises or in the cloud. Information stored in these solutions may vary based on the specific instance or environment. Examples of CRM software include Microsoft Dynamics 365, Salesforce, Zoho, Zendesk, and HubSpot.

## Operationalization review

1. Record the operational scope: which services, environments, and data the technique could affect.
2. Record the runbook that would be executed, and its owner.
3. Record the telemetry the runbook depends on, and whether it is retained long enough to investigate.
4. Record the detection that would surface the technique before or after it has an effect.
5. Record the recovery path, and the evidence that recovery has been rehearsed.
6. Record the residual operational risk where the runbook depends on a manual step.

## Review evidence

- the runbook and its owner;
- the telemetry retention and coverage record;
- the detection mapping;
- the exercise or rehearsal record.

## Limitations

An operationalization review describes the runbook and the evidence around it. It does not claim the technique has been prevented or detected in a live environment.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1213.004: https://attack.mitre.org/techniques/T1213/004
- Reviewed: 2026-10-27
