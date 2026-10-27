# Credential Access Protection Technique Response Playbook

## Target technique

**M1043 — Credential Access Protection**


Credential Access Protection focuses on implementing measures to prevent adversaries from obtaining credentials, such as passwords, hashes, tokens, or keys, that could be used for unauthorized access. This involves restricting access to credential storage mechanisms, hardening configurations to block credential dumping methods, and using monitoring tools to detect suspicious credential-related activity. This mitigation can be implemented through the following measures: Restrict Access to Credential Storage: - Use Case: Prevent adversaries from accessing the SAM (Security Account Manager) database on Windows systems. - Implementation: Enforce least privilege principles and restrict administrative access to credential stores such as `C:\Windows\System32\config\SAM`. Use Credential Guard: - Use Case: Isolate LSASS (Local Security Authority Subsystem Service) memory to prevent credential dumping. - Implementation: Enable Windows Defender Credential Guard on enterprise endpoints to isolate secrets and protect them from unauthorized access. Monitor for Credential Dumping Tools: - Use Case: Detect and block known tools like Mimikatz or Windows Credential Editor. - Implementation: Flag suspicious process behavior related to credential dumping. Disable Cached Credentials: - Use Case: Prevent adversaries from exploiting cached credentials on endpoints. - Implementation: Configure group policy to reduce or eliminate the use of cached credentials (e.g., set Interactive logon: Number of previous logons to cache to 0). Enable Secure Boot and Memory Protections: - Use Case: Prevent memory-based attacks used to extract credentials. - Implementation: Configure Secure Boot and enforce hardware-based security features like DEP (Data Execution Prevention) and ASLR (Address Space Layout Randomization).

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
- M1043: https://attack.mitre.org/mitigations/M1043
- Reviewed: 2026-10-27
