# Hidden Users Technique Platform Profile

## Reference

- Technique: **T1147 — Hidden Users**
- Platforms named in the source: macOS

Every user account in macOS has a userID associated with it. When creating a user, you can specify the userID for that account. There is a property value in /Library/Preferences/com.apple.loginwindow called Hide500Users that prevents users with userIDs 500 and lower from appearing at the login screen. By using the Create Account technique with a userID under 500 and enabling this property (setting it to Yes), an adversary can hide their user accounts much more easily: sudo dscl . -create /Users/username UniqueID 401 .

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
- T1147: https://attack.mitre.org/techniques/T1147
- Reviewed: 2026-10-27
