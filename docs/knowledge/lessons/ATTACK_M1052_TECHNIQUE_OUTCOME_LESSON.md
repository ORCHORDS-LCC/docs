# M1052 User Account Control Outcome Lesson

## Authoritative description

- Technique: **M1052 — User Account Control**

User Account Control (UAC) is a security feature in Microsoft Windows that prevents unauthorized changes to the operating system. UAC prompts users to confirm or provide administrator credentials when an action requires elevated privileges. Proper configuration of UAC reduces the risk of privilege escalation attacks. This mitigation can be implemented through the following measures: Enable UAC Globally: - Ensure UAC is enabled through Group Policy by setting `User Account Control: Run all administrators in Admin Approval Mode` to `Enabled`. Require Credential Prompt: - Use Group Policy to configure UAC to prompt for administrative credentials instead of just confirmation (`User Account Control: Behavior of the elevation prompt`). Restrict Built-in Administrator Account: Set `Admin Approval Mode` for the built-in Administrator account to `Enabled` in Group Policy. Secure the UAC Prompt: - Configure UAC prompts to display on the secure desktop (`User Account Control: Switch to the secure desktop when prompting for elevation`). Prevent UAC Bypass: - Block untrusted applications from triggering UAC prompts by configuring `User Account Control: Only elevate executables that are signed and validated`. - Use EDR tools to detect and block known UAC bypass techniques. Monitor UAC-Related Events: - Use Windows Event Viewer to monitor for event ID 4688 (process creation) and look for suspicious processes attempting to invoke UAC elevation. *Tools for Implementation* Built-in Windows Tools: - Group Policy Editor: Configure UAC settings centrally for enterprise environments. - Registry Editor: Modify UAC-related settings directly, such as `EnableLUA` and `ConsentPromptBehaviorAdmin`. Endpoint Security Solutions: - Microsoft Defender for Endpoint: Detects and blocks UAC bypass techniques. - Sysmon: Logs process creations and monitors UAC elevation attempts for suspicious activity. Third-Party Security Tools: - Process Monitor (Sysinternals): Tracks real-time processes interacting with UAC. - EventSentry: Monitors Windows Event Logs for UAC-related alerts.

## Reusable lesson

This technique should be treated as an explicit review question when it is relevant to the system or organisation, rather than assumed to be covered by a generic control statement or by tooling that reports a related signal.

## Apply the lesson

1. Define the real scope before judging coverage.
2. Inspect current technical, process, governance, or operational evidence.
3. Separate documented intent from verified behaviour.
4. Record partial coverage and unresolved gaps instead of converting them into a pass.
5. Revisit when the underlying scope, threat environment, technology, suppliers, or mission materially changes.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- M1052: https://attack.mitre.org/mitigations/M1052
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
