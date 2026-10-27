# T1562.010 Downgrade Attack Outcome Lesson

## Authoritative description

- Technique: **T1562.010 — Downgrade Attack**
- Tactics: stealth
- Platforms: Windows, Linux, macOS

Adversaries may downgrade or use a version of system features that may be outdated, vulnerable, and/or does not support updated security controls. Downgrade attacks typically take advantage of a system’s backward compatibility to force it into less secure modes of operation. Adversaries may downgrade and use various less-secure versions of features of a system, such as Command and Scripting Interpreters or even network protocols that can be abused to enable Adversary-in-the-Middle or Network Sniffing. For example, PowerShell versions 5+ includes Script Block Logging (SBL), which can record executed script content. However, adversaries may attempt to execute a previous version of PowerShell that does not support SBL with the intent to Impair Defenses while running malicious scripts that may have otherwise been detected. Adversaries may similarly target network traffic to downgrade from an encrypted HTTPS connection to an unsecured HTTP connection that exposes network data in clear text. On Windows systems, adversaries may downgrade the boot manager to a vulnerable version that bypasses Secure Boot, granting the ability to disable various operating system security mechanisms.

## Reusable lesson

This technique should be treated as an explicit review question when it is relevant to the system or organisation, rather than assumed to be covered by a generic control statement or by tooling that reports a related signal.

## Apply the lesson

1. Define the real scope before judging coverage.
2. Inspect current technical, process, governance, or operational evidence.
3. Separate documented intent from verified behaviour.
4. Record partial coverage and unresolved gaps instead of converting them into a pass.
5. Revisit when the underlying scope, threat environment, technology, suppliers, or mission materially changes.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1562.010: https://attack.mitre.org/techniques/T1562/010
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
