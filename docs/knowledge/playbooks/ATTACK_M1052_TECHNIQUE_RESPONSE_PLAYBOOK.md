# User Account Control Technique Response Playbook

## Target technique

**M1052 — User Account Control**


User Account Control (UAC) is a security feature in Microsoft Windows that prevents unauthorized changes to the operating system. UAC prompts users to confirm or provide administrator credentials when an action requires elevated privileges. Proper configuration of UAC reduces the risk of privilege escalation attacks. This mitigation can be implemented through the following measures: Enable UAC Globally: - Ensure UAC is enabled through Group Policy by setting `User Account Control: Run all administrators in Admin Approval Mode` to `Enabled`. Require Credential Prompt: - Use Group Policy to configure UAC to prompt for administrative credentials instead of just confirmation (`User Account Control: Behavior of the elevation prompt`). Restrict Built-in Administrator Account: Set `Admin Approval Mode` for the built-in Administrator account to `Enabled` in Group Policy. Secure the UAC Prompt: - Configure UAC prompts to display on the secure desktop (`User Account Control: Switch to the secure desktop when prompting for elevation`). Prevent UAC Bypass: - Block untrusted applications from triggering UAC prompts by configuring `User Account Control: Only elevate executables that are signed and validated`. - Use EDR tools to detect and block known UAC bypass techniques. Monitor UAC-Related Events: - Use Windows Event Viewer to monitor for event ID 4688 (process creation) and look for suspicious processes attempting to invoke UAC elevation. *Tools for Implementation* Built-in Windows Tools: - Group Policy Editor: Configure UAC settings centrally for enterprise environments. - Registry Editor: Modify UAC-related settings directly, such as `EnableLUA` and `ConsentPromptBehaviorAdmin`. Endpoint Security Solutions: - Microsoft Defender for Endpoint: Detects and blocks UAC bypass techniques. - Sysmon: Logs process creations and monitors UAC elevation attempts for suspicious activity. Third-Party Security Tools: - Process Monitor (Sysinternals): Tracks real-time processes interacting with UAC. - EventSentry: Monitors Windows Event Logs for UAC-related alerts.

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
- M1052: https://attack.mitre.org/mitigations/M1052
- Reviewed: 2026-10-27
