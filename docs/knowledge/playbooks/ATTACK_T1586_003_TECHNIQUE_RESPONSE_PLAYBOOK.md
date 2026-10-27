# Cloud Accounts Technique Response Playbook

## Target technique

**T1586.003 — Cloud Accounts**

- Tactics: resource-development
- Platforms: PRE

Adversaries may compromise cloud accounts that can be used during targeting. Adversaries can use compromised cloud accounts to further their operations, including leveraging cloud storage services such as Dropbox, Microsoft OneDrive, or AWS S3 buckets for Exfiltration to Cloud Storage or to Upload Tools. Cloud accounts can also be used in the acquisition of infrastructure, such as Virtual Private Servers or Serverless infrastructure. Additionally, cloud-based messaging services such as Twilio, SendGrid, AWS End User Messaging, AWS SNS (Simple Notification Service), or AWS SES (Simple Email Service) may be leveraged for spam or Phishing. Compromising cloud accounts may allow adversaries to develop sophisticated capabilities without managing their own servers. A variety of methods exist for compromising cloud accounts, such as gathering credentials via Phishing for Information, purchasing credentials from third-party sites, conducting Password Spraying attacks, or attempting to Steal Application Access Tokens. Prior to compromising cloud accounts, adversaries may conduct Reconnaissance to inform decisions about which accounts to compromise to further their operation. In some cases, adversaries may target privileged service provider accounts with the intent of leveraging a Trusted Relationship between service providers and their customers.

## Preconditions

- the estate in scope is identified, with the systems the technique could apply to;
- an owner is accountable for detection and response;
- current telemetry and configuration can be inspected;
- the technique is applicable or requires an applicability decision.

## Procedure

1. Confirm the scope and owner.
2. Read the current technique description and the associated detection guidance.
3. Inventory the telemetry that would carry the technique's indicators.
4. Inspect whether the indicators are present in the environment.
5. Exercise the detection path and confirm it produces the expected signal.
6. Record gaps in detection coverage and assign remediation owners.
7. Record justified non-applicability or accepted detection gaps separately.
8. Set the next event-driven or periodic verification trigger.

## Failure handling

If the detection path does not produce the expected signal, treat the coverage as unverified, preserve the test evidence, and route the gap through the appropriate remediation or risk process.

## Completion evidence

Scope, owner, source version, telemetry inspected, tests performed, findings, exceptions, remediation links, reviewer, and next trigger.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1586.003: https://attack.mitre.org/techniques/T1586/003
- Reviewed: 2026-10-27
