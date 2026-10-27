# Login Items Technique Operationalization Review

## Reference

- Technique: **T1547.015 — Login Items**

Adversaries may add login items to execute upon user login to gain persistence or escalate privileges. Login items are applications, documents, folders, or server connections that are automatically launched when a user logs in. Login items can be added via a shared file list or Service Management Framework. Shared file list login items can be set using scripting languages such as AppleScript, whereas the Service Management Framework uses the API call <code>SMLoginItemSetEnabled</code>. Login items installed using the Service Management Framework leverage <code>launchd</code>, are not visible in the System Preferences, and can only be removed by the application that created them. Login items created using a shared file list are visible in System Preferences, can hide the application when it launches, and are executed through LaunchServices, not launchd, to open applications, documents, or URLs without using Finder. Users and applications use login items to configure their user environment to launch commonly used services or applications, such as email, chat, and music applications. Adversaries can utilize AppleScript and Native API calls to create a login item to spawn malicious executables. Prior to version 10.5 on macOS, adversaries can add login items by using AppleScript to send an Apple events to the “System Events” process, which has an AppleScript dictionary for manipulating login items. Adversaries can use a command such as <code>tell application “System Events” to make login item at end with properties /path/to/executable</code>. This command adds the path of the malicious executable to the login item file list located in <code>~/Library/Application Support/com.apple.backgroundtaskmanagementagent/backgrounditems.btm</code>. Adversaries can also use login items to launch executables that can be used to control the victim system remotely or as a means to gain privilege escalation by prompting for user credentials.

## Operationalization review

1. Record the operational scope: which services, environments, and data the technique could affect.
2. Record the runbook that would be executed, and its owner.
3. Record the telemetry the runbook depends on, and whether it is retained long enough to investigate.
4. Record the detection that would surface the technique before or after it has an effect.
5. Record the recovery path, and the evidence that recovery has been rehearsed.
6. Record the residual operational risk where the runbook depends on a manual step.

## Review evidence

- the runbook and its owner;
- the telemetry retention and coverage record;
- the detection mapping;
- the exercise or rehearsal record.

## Limitations

An operationalization review describes the runbook and the evidence around it. It does not claim the technique has been prevented or detected in a live environment.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1547.015: https://attack.mitre.org/techniques/T1547/015
- Reviewed: 2026-10-27
