# Device Registration Technique Operationalization Review

## Reference

- Technique: **T1098.005 — Device Registration**

Adversaries may register a device to an adversary-controlled account. Devices may be registered in a multifactor authentication (MFA) system, which handles authentication to the network, or in a device management system, which handles device access and compliance. MFA systems, such as Duo or Okta, allow users to associate devices with their accounts in order to complete MFA requirements. An adversary that compromises a user’s credentials may enroll a new device in order to bypass initial MFA requirements and gain persistent access to a network. In some cases, the MFA self-enrollment process may require only a username and password to enroll the account's first device or to enroll a device to an inactive account. Similarly, an adversary with existing access to a network may register a device or a virtual machine to Entra ID and/or its device management system, Microsoft Intune, in order to access sensitive data or resources while bypassing conditional access policies. Devices registered in Entra ID may be able to conduct Internal Spearphishing campaigns via intra-organizational emails, which are less likely to be treated as suspicious by the email client. Additionally, an adversary may be able to perform a Service Exhaustion Flood on an Entra ID tenant by registering a large number of devices.

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
- T1098.005: https://attack.mitre.org/techniques/T1098/005
- Reviewed: 2026-10-27
