# Cloud Application Integration Technique Platform Profile

## Reference

- Technique: **T1671 — Cloud Application Integration**
- Platforms named in the source: Office Suite, SaaS

Adversaries may achieve persistence by leveraging OAuth application integrations in a software-as-a-service environment. Adversaries may create a custom application, add a legitimate application into the environment, or even co-opt an existing integration to achieve malicious ends. OAuth is an open standard that allows users to authorize applications to access their information on their behalf. In a SaaS environment such as Microsoft 365 or Google Workspace, users may integrate applications to improve their workflow and achieve tasks. Leveraging application integrations may allow adversaries to persist in an environment – for example, by granting consent to an application from a high-privileged adversary-controlled account in order to maintain access to its data, even in the event of losing access to the account. In some cases, integrations may remain valid even after the original consenting user account is disabled. Application integrations may also allow adversaries to bypass multi-factor authentication requirements through the use of Application Access Tokens. Finally, they may enable persistent Automated Exfiltration over time. Creating or adding a new application may require the adversary to create a dedicated Cloud Account for the application and assign it Additional Cloud Roles – for example, in Microsoft 365 environments, an application can only access resources via an associated service principal.

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
- T1671: https://attack.mitre.org/techniques/T1671
- Reviewed: 2026-10-27
