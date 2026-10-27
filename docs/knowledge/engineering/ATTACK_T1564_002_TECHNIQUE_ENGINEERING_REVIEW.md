# Hidden Users Technique Engineering Review

## Reference

- Technique: **T1564.002 — Hidden Users**

Adversaries may use hidden users to hide the presence of user accounts they create or modify. Administrators may want to hide users when there are many user accounts on a given system or if they want to hide their administrative or other management accounts from other users. In macOS, adversaries can create or modify a user to be hidden through manipulating plist files, folder attributes, and user attributes. To prevent a user from being shown on the login screen and in System Preferences, adversaries can set the userID to be under 500 and set the key value Hide500Users to TRUE in the /Library/Preferences/com.apple.loginwindow plist file. Every user has a userID associated with it. When the Hide500Users key value is set to TRUE, users with a userID under 500 do not appear on the login screen and in System Preferences. Using the command line, adversaries can use the dscl utility to create hidden user accounts by setting the IsHidden attribute to 1. Adversaries can also hide a user’s home folder by changing the chflags to hidden. Adversaries may similarly hide user accounts in Windows. Adversaries can set the HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\SpecialAccounts\UserList Registry key value to 0 for a specific user to prevent that user from being listed on the logon screen. On Linux systems, adversaries may hide user accounts from the login screen, also referred to as the greeter. The method an adversary may use depends on which Display Manager the distribution is currently using. For example, on an Ubuntu system using the GNOME Display Manger (GDM), accounts may be hidden from the greeter using the gsettings command (ex: sudo -u gdm gsettings set org.gnome.login-screen disable-user-list true). Display Managers are not anchored to specific distributions and may be changed by a user or adversary.

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
- T1564.002: https://attack.mitre.org/techniques/T1564/002
- Reviewed: 2026-10-27
