# Execution Prevention Technique Operationalization Review

## Reference

- Technique: **M1038 — Execution Prevention**

Prevent the execution of unauthorized or malicious code on systems by implementing application control, script blocking, and other execution prevention mechanisms. This ensures that only trusted and authorized code is executed, reducing the risk of malware and unauthorized actions. This mitigation can be implemented through the following measures: Application Control: - Use Case: Use tools like AppLocker or Windows Defender Application Control (WDAC) to create whitelists of authorized applications and block unauthorized ones. On Linux, use tools like SELinux or AppArmor to define mandatory access control policies for application execution. - Implementation: Allow only digitally signed or pre-approved applications to execute on servers and endpoints. (e.g., `New-AppLockerPolicy -PolicyType Enforced -FilePath "C:\Policies\AppLocker.xml"`) Script Blocking: - Use Case: Use script control mechanisms to block unauthorized execution of scripts, such as PowerShell or JavaScript. Web Browsers: Use browser extensions or settings to block JavaScript execution from untrusted sources. - Implementation: Configure PowerShell to enforce Constrained Language Mode for non-administrator users. (e.g., `Set-ExecutionPolicy AllSigned`) Executable Blocking: - Use Case: Prevent execution of binaries from suspicious locations, such as `%TEMP%` or `%APPDATA%` directories. - Implementation: Block execution of `.exe`, `.bat`, or `.ps1` files from user-writable directories. Dynamic Analysis Prevention: - Use Case: Use behavior-based execution prevention tools to identify and block malicious activity in real time. - Implemenation: Employ EDR solutions that analyze runtime behavior and block suspicious code execution.

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
- M1038: https://attack.mitre.org/mitigations/M1038
- Reviewed: 2026-10-27
