# Software Configuration Technique Response Playbook

## Target technique

**M1054 — Software Configuration**


Software configuration refers to making security-focused adjustments to the settings of applications, middleware, databases, or other software to mitigate potential threats. These changes help reduce the attack surface, enforce best practices, and protect sensitive data. This mitigation can be implemented through the following measures: Conduct a Security Review of Application Settings: - Review the software documentation to identify recommended security configurations. - Compare default settings against organizational policies and compliance requirements. Implement Access Controls and Permissions: - Restrict access to sensitive features or data within the software. - Enforce least privilege principles for all roles and accounts interacting with the software. Enable Logging and Monitoring: - Configure detailed logging for key application events such as authentication failures, configuration changes, or unusual activity. - Integrate logs with a centralized monitoring solution, such as a SIEM. Update and Patch Software Regularly: - Ensure the software is kept up-to-date with the latest security patches to address known vulnerabilities. - Use automated patch management tools to streamline the update process. Disable Unnecessary Features or Services: - Turn off unused functionality or components that could introduce vulnerabilities, such as debugging interfaces or deprecated APIs. Test Configuration Changes: - Perform configuration changes in a staging environment before applying them in production. - Conduct regular audits to ensure that settings remain aligned with security policies. *Tools for Implementation* Configuration Management Tools: - Ansible: Automates configuration changes across multiple applications and environments. - Chef: Ensures consistent application settings through code-based configuration management. - Puppet: Automates software configurations and audits changes for compliance. Security Benchmarking Tools: - CIS-CAT: Provides benchmarks and audits for secure software configurations. - Aqua Security Trivy: Scans containerized applications for configuration issues. Vulnerability Management Solutions: - Nessus: Identifies misconfigurations and suggests corrective actions. Logging and Monitoring Tools: - Splunk: Aggregates and analyzes application logs to detect suspicious activity.

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
- M1054: https://attack.mitre.org/mitigations/M1054
- Reviewed: 2026-10-27
