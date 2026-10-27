# Environment Variable Permissions Technique Response Playbook

## Target technique

**M1039 — Environment Variable Permissions**


Restrict the modification of environment variables to authorized users and processes by enforcing strict permissions and policies. This ensures the integrity of environment variables, preventing adversaries from abusing or altering them for malicious purposes. This mitigation can be implemented through the following measures: Restrict Write Access: - Use Case: Set file system-level permissions to restrict access to environment variable configuration files (e.g., `.bashrc`, `.bash_profile`, `.zshrc`, `systemd` service files). - Implementation: Configure `/etc/environment` or `/etc/profile` on Linux systems to only allow root or administrators to modify the file. Secure Access Controls: - Use Case: Limit access to environment variable settings in application deployment tools or CI/CD pipelines to authorized personnel. - Implementation: Use role-based access control (RBAC) in tools like Jenkins or GitLab to ensure only specific users can modify environment variables. Restrict Process Scope: - Use Case: Configure policies to ensure environment variables are only accessible to the processes they are explicitly intended for. - Implementation: Use containerized environments like Docker to isolate environment variables to specific containers and ensure they are not inherited by other processes. Audit Environment Variable Changes: - Use Case: Enable logging for changes to critical environment variables. - Implementation: Use `auditd` on Linux to monitor changes to files like `/etc/environment` or application-specific environment files.

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
- M1039: https://attack.mitre.org/mitigations/M1039
- Reviewed: 2026-10-27
