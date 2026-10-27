# Cloud API Technique Response Playbook

## Target technique

**T1059.009 — Cloud API**

- Tactics: execution
- Platforms: IaaS, Identity Provider, Office Suite, SaaS

Adversaries may abuse cloud APIs to execute malicious commands. APIs available in cloud environments provide various functionalities and are a feature-rich method for programmatic access to nearly all aspects of a tenant. These APIs may be utilized through various methods such as command line interpreters (CLIs), in-browser Cloud Shells, PowerShell modules like Azure for PowerShell, or software developer kits (SDKs) available for languages such as Python. Cloud API functionality may allow for administrative access across all major services in a tenant such as compute, storage, identity and access management (IAM), networking, and security policies. With proper permissions (often via use of credentials such as Application Access Token and Web Session Cookie), adversaries may abuse cloud APIs to invoke various functions that execute malicious actions. For example, CLI and PowerShell functionality may be accessed through binaries installed on cloud-hosted or on-premises hosts or accessed through a browser-based cloud shell offered by many cloud platforms (such as AWS, Azure, and GCP). These cloud shells are often a packaged unified environment to use CLI and/or scripting modules hosted as a container in the cloud environment.

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
- T1059.009: https://attack.mitre.org/techniques/T1059/009
- Reviewed: 2026-10-27
