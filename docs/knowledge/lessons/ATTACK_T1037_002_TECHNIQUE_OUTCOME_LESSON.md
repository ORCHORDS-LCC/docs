# T1037.002 Login Hook Outcome Lesson

## Authoritative description

- Technique: **T1037.002 — Login Hook**
- Tactics: persistence, privilege-escalation
- Platforms: macOS

Adversaries may use a Login Hook to establish persistence executed upon user logon. A login hook is a plist file that points to a specific script to execute with root privileges upon user logon. The plist file is located in the <code>/Library/Preferences/com.apple.loginwindow.plist</code> file and can be modified using the <code>defaults</code> command-line utility. This behavior is the same for logout hooks where a script can be executed upon user logout. All hooks require administrator permissions to modify or create hooks. Adversaries can add or insert a path to a malicious script in the <code>com.apple.loginwindow.plist</code> file, using the <code>LoginHook</code> or <code>LogoutHook</code> key-value pair. The malicious script is executed upon the next user login. If a login hook already exists, adversaries can add additional commands to an existing login hook. There can be only one login and logout hook on a system at a time. **Note:** Login hooks were deprecated in 10.11 version of macOS in favor of Launch Daemon and Launch Agent.

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
- T1037.002: https://attack.mitre.org/techniques/T1037/002
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
