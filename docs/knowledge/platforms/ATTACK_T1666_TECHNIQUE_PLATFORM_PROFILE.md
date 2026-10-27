# Modify Cloud Resource Hierarchy Technique Platform Profile

## Reference

- Technique: **T1666 — Modify Cloud Resource Hierarchy**
- Platforms named in the source: IaaS

Adversaries may attempt to modify hierarchical structures in infrastructure-as-a-service (IaaS) environments in order to evade defenses. IaaS environments often group resources into a hierarchy, enabling improved resource management and application of policies to relevant groups. Hierarchical structures differ among cloud providers. For example, in AWS environments, multiple accounts can be grouped under a single organization, while in Azure environments, multiple subscriptions can be grouped under a single management group. Adversaries may add, delete, or otherwise modify resource groups within an IaaS hierarchy. For example, in Azure environments, an adversary who has gained access to a Global Administrator account may create new subscriptions in which to deploy resources. They may also engage in subscription hijacking by transferring an existing pay-as-you-go subscription from a victim tenant to an adversary-controlled tenant. This will allow the adversary to use the victim’s compute resources without generating logs on the victim tenant. In AWS environments, adversaries with appropriate permissions in a given account may call the `LeaveOrganization` API, causing the account to be severed from the AWS Organization to which it was tied and removing any Service Control Policies, guardrails, or restrictions imposed upon it by its former Organization. Alternatively, adversaries may call the `CreateAccount` API in order to create a new account within an AWS Organization. This account will use the same payment methods registered to the payment account but may not be subject to existing detections or Service Control Policies.

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
- T1666: https://attack.mitre.org/techniques/T1666
- Reviewed: 2026-10-27
