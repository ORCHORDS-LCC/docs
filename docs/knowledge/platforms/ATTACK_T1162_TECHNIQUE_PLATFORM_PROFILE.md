# Login Item Technique Platform Profile

## Reference

- Technique: **T1162 — Login Item**
- Platforms named in the source: macOS

MacOS provides the option to list specific applications to run when a user logs in. These applications run under the logged in user's context, and will be started every time the user logs in. Login items installed using the Service Management Framework are not visible in the System Preferences and can only be removed by the application that created them . Users have direct control over login items installed using a shared file list which are also visible in System Preferences . These login items are stored in the user's ~/Library/Preferences/ directory in a plist file called com.apple.loginitems.plist . Some of these applications can open visible dialogs to the user, but they don’t all have to since there is an option to ‘Hide’ the window. If an adversary can register their own login item or modified an existing one, then they can use it to execute their code for a persistence mechanism each time the user logs in . The API method SMLoginItemSetEnabled can be used to set Login Items, but scripting languages like AppleScript can do this as well .

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
- T1162: https://attack.mitre.org/techniques/T1162
- Reviewed: 2026-10-27
