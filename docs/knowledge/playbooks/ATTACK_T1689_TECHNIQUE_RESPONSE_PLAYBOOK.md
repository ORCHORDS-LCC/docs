# Downgrade Attack Technique Response Playbook

## Target technique

**T1689 — Downgrade Attack**

- Tactics: defense-impairment
- Platforms: macOS, Windows, Linux

Adversaries may downgrade or use a version of system features that may be outdated, vulnerable, and/or does not support updated security controls. Downgrade attacks typically take advantage of a system’s backward compatibility to force it into less secure modes of operation. Adversaries may downgrade and use various less-secure versions of features of a system, such as Command and Scripting Interpreter or even network protocols that can be abused to enable Adversary-in-the-Middle or Network Sniffing. For example, PowerShell versions 5+ includes Script Block Logging (SBL), which can record executed script content. However, adversaries may attempt to execute a previous version of PowerShell that does not support SBL with the intent to impair defenses while running malicious scripts that may have otherwise been detected. Adversaries may similarly target network traffic to downgrade from an encrypted HTTPS connection to an unsecured HTTP connection that exposes network data in clear text. On Windows systems, adversaries may downgrade the boot manager to a vulnerable version that bypasses Secure Boot, granting the ability to disable various operating system security mechanisms.

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
- T1689: https://attack.mitre.org/techniques/T1689
- Reviewed: 2026-10-27
