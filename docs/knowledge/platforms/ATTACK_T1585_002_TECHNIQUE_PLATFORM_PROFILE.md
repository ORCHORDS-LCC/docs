# Email Accounts Technique Platform Profile

## Reference

- Technique: **T1585.002 — Email Accounts**
- Platforms named in the source: PRE

Adversaries may create email accounts that can be used during targeting. Adversaries can use accounts created with email providers to further their operations, such as leveraging them to conduct Phishing for Information or Phishing. Establishing email accounts may also allow adversaries to abuse free services – such as trial periods – to Acquire Infrastructure for follow-on purposes. Adversaries may also take steps to cultivate a persona around the email account, such as through use of Social Media Accounts, to increase the chance of success of follow-on behaviors. Created email accounts can also be used in the acquisition of infrastructure (ex: Domains). To decrease the chance of physically tying back operations to themselves, adversaries may make use of disposable email services.

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
- T1585.002: https://attack.mitre.org/techniques/T1585/002
- Reviewed: 2026-10-27
