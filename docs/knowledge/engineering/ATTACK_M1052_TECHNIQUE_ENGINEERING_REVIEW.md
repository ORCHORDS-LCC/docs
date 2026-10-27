# User Account Control Technique Engineering Review

## Reference

- Technique: **M1052 — User Account Control**

User Account Control (UAC) is a security feature in Microsoft Windows that prevents unauthorized changes to the operating system. UAC prompts users to confirm or provide administrator credentials when an action requires elevated privileges. Proper configuration of UAC reduces the risk of privilege escalation attacks. This mitigation can be implemented through the following measures: Enable UAC Globally: - Ensure UAC is enabled through Group Policy by setting `User Account Control: Run all administrators in Admin Approval Mode` to `Enabled`. Require Credential Prompt: - Use Group Policy to configure UAC to prompt for administrative credentials instead of just confirmation (`User Account Control: Behavior of the elevation prompt`). Restrict Built-in Administrator Account: Set `Admin Approval Mode` for the built-in Administrator account to `Enabled` in Group Policy. Secure the UAC Prompt: - Configure UAC prompts to display on the secure desktop (`User Account Control: Switch to the secure desktop when prompting for elevation`). Prevent UAC Bypass: - Block untrusted applications from triggering UAC prompts by configuring `User Account Control: Only elevate executables that are signed and validated`. - Use EDR tools to detect and block known UAC bypass techniques. Monitor UAC-Related Events: - Use Windows Event Viewer to monitor for event ID 4688 (process creation) and look for suspicious processes attempting to invoke UAC elevation. *Tools for Implementation* Built-in Windows Tools: - Group Policy Editor: Configure UAC settings centrally for enterprise environments. - Registry Editor: Modify UAC-related settings directly, such as `EnableLUA` and `ConsentPromptBehaviorAdmin`. Endpoint Security Solutions: - Microsoft Defender for Endpoint: Detects and blocks UAC bypass techniques. - Sysmon: Logs process creations and monitors UAC elevation attempts for suspicious activity. Third-Party Security Tools: - Process Monitor (Sysinternals): Tracks real-time processes interacting with UAC. - EventSentry: Monitors Windows Event Logs for UAC-related alerts.

## Engineering review

1. Identify the engineering boundary where the technique would apply: the component, the service, or the deployment.
2. Review the design decision that would prevent the technique, and record the alternative considered.
3. Review the implementation evidence for the preventive control.
4. Review the test coverage that would fail if the control regressed.
5. Review the observability: which signal would show the control is not operating.
6. Record the residual risk where prevention is not achievable, and the detection that compensates.

## Review evidence

- the design record for the preventive decision;
- the implementation or configuration evidence;
- the test record showing the control is exercised;
- the observability mapping.

## Limitations

An engineering review describes what the design and the implementation evidence show. It does not claim the technique has been addressed in production.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- M1052: https://attack.mitre.org/mitigations/M1052
- Reviewed: 2026-10-27
