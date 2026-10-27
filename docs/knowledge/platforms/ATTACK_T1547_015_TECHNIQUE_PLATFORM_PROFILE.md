# Login Items Technique Platform Profile

## Reference

- Technique: **T1547.015 — Login Items**
- Platforms named in the source: macOS

Adversaries may add login items to execute upon user login to gain persistence or escalate privileges. Login items are applications, documents, folders, or server connections that are automatically launched when a user logs in. Login items can be added via a shared file list or Service Management Framework. Shared file list login items can be set using scripting languages such as AppleScript, whereas the Service Management Framework uses the API call <code>SMLoginItemSetEnabled</code>. Login items installed using the Service Management Framework leverage <code>launchd</code>, are not visible in the System Preferences, and can only be removed by the application that created them. Login items created using a shared file list are visible in System Preferences, can hide the application when it launches, and are executed through LaunchServices, not launchd, to open applications, documents, or URLs without using Finder. Users and applications use login items to configure their user environment to launch commonly used services or applications, such as email, chat, and music applications. Adversaries can utilize AppleScript and Native API calls to create a login item to spawn malicious executables. Prior to version 10.5 on macOS, adversaries can add login items by using AppleScript to send an Apple events to the “System Events” process, which has an AppleScript dictionary for manipulating login items. Adversaries can use a command such as <code>tell application “System Events” to make login item at end with properties /path/to/executable</code>. This command adds the path of the malicious executable to the login item file list located in <code>~/Library/Application Support/com.apple.backgroundtaskmanagementagent/backgrounditems.btm</code>. Adversaries can also use login items to launch executables that can be used to control the victim system remotely or as a means to gain privilege escalation by prompting for user credentials.

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
- T1547.015: https://attack.mitre.org/techniques/T1547/015
- Reviewed: 2026-10-27
