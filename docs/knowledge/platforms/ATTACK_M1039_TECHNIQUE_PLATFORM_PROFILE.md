# Environment Variable Permissions Technique Platform Profile

## Reference

- Technique: **M1039 — Environment Variable Permissions**
- Platforms named in the source: not stated

Restrict the modification of environment variables to authorized users and processes by enforcing strict permissions and policies. This ensures the integrity of environment variables, preventing adversaries from abusing or altering them for malicious purposes. This mitigation can be implemented through the following measures: Restrict Write Access: - Use Case: Set file system-level permissions to restrict access to environment variable configuration files (e.g., `.bashrc`, `.bash_profile`, `.zshrc`, `systemd` service files). - Implementation: Configure `/etc/environment` or `/etc/profile` on Linux systems to only allow root or administrators to modify the file. Secure Access Controls: - Use Case: Limit access to environment variable settings in application deployment tools or CI/CD pipelines to authorized personnel. - Implementation: Use role-based access control (RBAC) in tools like Jenkins or GitLab to ensure only specific users can modify environment variables. Restrict Process Scope: - Use Case: Configure policies to ensure environment variables are only accessible to the processes they are explicitly intended for. - Implementation: Use containerized environments like Docker to isolate environment variables to specific containers and ensure they are not inherited by other processes. Audit Environment Variable Changes: - Use Case: Enable logging for changes to critical environment variables. - Implementation: Use `auditd` on Linux to monitor changes to files like `/etc/environment` or application-specific environment files.

## Platform profile

1. Record the platforms in scope and the versions actually deployed.
2. Compare the deployed platform surface against the platforms the source names.
3. Record where the platform provides a native control for the technique, and where it does not.
4. Record the configuration evidence for the native control, where one exists.
5. Record the gap where the platform provides no native control, and the compensating detection.
6. Record the platform version, because platform behaviour changes between versions.

## Evidence

- the platform and version inventory for the scoped estate;
- the configuration export or screenshot for the native control;
- the detection evidence where the platform provides none.

## Limitations

A technique entry describes a class of abuse across platforms. The platform-specific exposure is a property of the deployment, established only by inventory and configuration evidence.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- M1039: https://attack.mitre.org/mitigations/M1039
- Reviewed: 2026-10-27
