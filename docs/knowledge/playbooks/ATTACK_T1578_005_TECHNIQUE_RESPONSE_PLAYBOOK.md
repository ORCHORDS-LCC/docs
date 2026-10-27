# Modify Cloud Compute Configurations Technique Response Playbook

## Target technique

**T1578.005 — Modify Cloud Compute Configurations**

- Tactics: defense-impairment
- Platforms: IaaS

Adversaries may modify settings that directly affect the size, locations, and resources available to cloud compute infrastructure in order to evade defenses. These settings may include service quotas, subscription associations, tenant-wide policies, or other configurations that impact available compute. Such modifications may allow adversaries to abuse the victim’s compute resources to achieve their goals, potentially without affecting the execution of running instances and/or revealing their activities to the victim. For example, cloud providers often limit customer usage of compute resources via quotas. Customers may request adjustments to these quotas to support increased computing needs, though these adjustments may require approval from the cloud provider. Adversaries who compromise a cloud environment may similarly request quota adjustments in order to support their activities, such as enabling additional Resource Hijacking without raising suspicion by using up a victim’s entire quota. Adversaries may also increase allowed resource usage by modifying any tenant-wide policies that limit the sizes of deployed virtual machines. Adversaries may also modify settings that affect where cloud resources can be deployed, such as enabling Unused/Unsupported Cloud Regions.

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
- T1578.005: https://attack.mitre.org/techniques/T1578/005
- Reviewed: 2026-10-27
