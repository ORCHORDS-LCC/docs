# Application Isolation and Sandboxing Technique Platform Profile

## Reference

- Technique: **M1048 — Application Isolation and Sandboxing**
- Platforms named in the source: not stated

Application Isolation and Sandboxing refers to the technique of restricting the execution of code to a controlled and isolated environment (e.g., a virtual environment, container, or sandbox). This method prevents potentially malicious code from affecting the rest of the system or network by limiting access to sensitive resources and critical operations. The goal is to contain threats and minimize their impact. This mitigation can be implemented through the following measures: Browser Sandboxing: - Use Case: Implement browser sandboxing to isolate untrusted web content and prevent malicious web pages or scripts from accessing sensitive system resources or initiating unauthorized downloads. - Implementation: Use browsers with built-in sandboxing features (e.g., Google Chrome, Microsoft Edge) or deploy enhanced browser security frameworks that limit the execution scope of active content. Consider controls that monitor or restrict script-based file generation and downloads commonly abused in evasion techniques like HTML smuggling. Application Virtualization: - Use Case: Deploy critical or high-risk applications in a virtualized environment to ensure any compromise does not affect the host system. - Implementation: Use application virtualization platforms to run applications in isolated environments. Email Attachment Sandboxing: - Use Case: Route email attachments to a sandbox environment to detect and block malware before delivering emails to end-users. - Implementation: Integrate security solutions with sandbox capabilities to analyze email attachments. Endpoint Sandboxing: - Use Case: Run all downloaded files and applications in a restricted environment to monitor their behavior for malicious activity. - Implementation: Use endpoint protection tools for sandboxing at the endpoint level.

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
- M1048: https://attack.mitre.org/mitigations/M1048
- Reviewed: 2026-10-27
