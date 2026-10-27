# Exfiltration to Text Storage Sites Technique Response Playbook

## Target technique

**T1567.003 — Exfiltration to Text Storage Sites**

- Tactics: exfiltration
- Platforms: Linux, macOS, Windows, ESXi

Adversaries may exfiltrate data to text storage sites instead of their primary command and control channel. Text storage sites, such as pastebin[.]com, are commonly used by developers to share code and other information. Text storage sites are often used to host malicious code for C2 communication (e.g., Stage Capabilities), but adversaries may also use these sites to exfiltrate collected data. Furthermore, paid features and encryption options may allow adversaries to conceal and store data more securely. **Note:** This is distinct from Exfiltration to Code Repository, which highlight access to code repositories via APIs.

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
- T1567.003: https://attack.mitre.org/techniques/T1567/003
- Reviewed: 2026-10-27
