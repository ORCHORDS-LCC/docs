# User Account Control Technique Platform Profile

## Reference

- Technique: **M1052 — User Account Control**
- Platforms named in the source: not stated

User Account Control (UAC) is a security feature in Microsoft Windows that prevents unauthorized changes to the operating system. UAC prompts users to confirm or provide administrator credentials when an action requires elevated privileges. Proper configuration of UAC reduces the risk of privilege escalation attacks. This mitigation can be implemented through the following measures: Enable UAC Globally: - Ensure UAC is enabled through Group Policy by setting `User Account Control: Run all administrators in Admin Approval Mode` to `Enabled`. Require Credential Prompt: - Use Group Policy to configure UAC to prompt for administrative credentials instead of just confirmation (`User Account Control: Behavior of the elevation prompt`). Restrict Built-in Administrator Account: Set `Admin Approval Mode` for the built-in Administrator account to `Enabled` in Group Policy. Secure the UAC Prompt: - Configure UAC prompts to display on the secure desktop (`User Account Control: Switch to the secure desktop when prompting for elevation`). Prevent UAC Bypass: - Block untrusted applications from triggering UAC prompts by configuring `User Account Control: Only elevate executables that are signed and validated`. - Use EDR tools to detect and block known UAC bypass techniques. Monitor UAC-Related Events: - Use Windows Event Viewer to monitor for event ID 4688 (process creation) and look for suspicious processes attempting to invoke UAC elevation. *Tools for Implementation* Built-in Windows Tools: - Group Policy Editor: Configure UAC settings centrally for enterprise environments. - Registry Editor: Modify UAC-related settings directly, such as `EnableLUA` and `ConsentPromptBehaviorAdmin`. Endpoint Security Solutions: - Microsoft Defender for Endpoint: Detects and blocks UAC bypass techniques. - Sysmon: Logs process creations and monitors UAC elevation attempts for suspicious activity. Third-Party Security Tools: - Process Monitor (Sysinternals): Tracks real-time processes interacting with UAC. - EventSentry: Monitors Windows Event Logs for UAC-related alerts.

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
- M1052: https://attack.mitre.org/mitigations/M1052
- Reviewed: 2026-10-27
