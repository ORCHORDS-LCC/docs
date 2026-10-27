# Execution Prevention Technique Response Playbook

## Target technique

**M1038 — Execution Prevention**


Prevent the execution of unauthorized or malicious code on systems by implementing application control, script blocking, and other execution prevention mechanisms. This ensures that only trusted and authorized code is executed, reducing the risk of malware and unauthorized actions. This mitigation can be implemented through the following measures: Application Control: - Use Case: Use tools like AppLocker or Windows Defender Application Control (WDAC) to create whitelists of authorized applications and block unauthorized ones. On Linux, use tools like SELinux or AppArmor to define mandatory access control policies for application execution. - Implementation: Allow only digitally signed or pre-approved applications to execute on servers and endpoints. (e.g., `New-AppLockerPolicy -PolicyType Enforced -FilePath "C:\Policies\AppLocker.xml"`) Script Blocking: - Use Case: Use script control mechanisms to block unauthorized execution of scripts, such as PowerShell or JavaScript. Web Browsers: Use browser extensions or settings to block JavaScript execution from untrusted sources. - Implementation: Configure PowerShell to enforce Constrained Language Mode for non-administrator users. (e.g., `Set-ExecutionPolicy AllSigned`) Executable Blocking: - Use Case: Prevent execution of binaries from suspicious locations, such as `%TEMP%` or `%APPDATA%` directories. - Implementation: Block execution of `.exe`, `.bat`, or `.ps1` files from user-writable directories. Dynamic Analysis Prevention: - Use Case: Use behavior-based execution prevention tools to identify and block malicious activity in real time. - Implemenation: Employ EDR solutions that analyze runtime behavior and block suspicious code execution.

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
- M1038: https://attack.mitre.org/mitigations/M1038
- Reviewed: 2026-10-27
