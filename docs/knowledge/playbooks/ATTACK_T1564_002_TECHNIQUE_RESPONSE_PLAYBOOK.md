# Hidden Users Technique Response Playbook

## Target technique

**T1564.002 — Hidden Users**

- Tactics: stealth
- Platforms: Linux, macOS, Windows

Adversaries may use hidden users to hide the presence of user accounts they create or modify. Administrators may want to hide users when there are many user accounts on a given system or if they want to hide their administrative or other management accounts from other users. In macOS, adversaries can create or modify a user to be hidden through manipulating plist files, folder attributes, and user attributes. To prevent a user from being shown on the login screen and in System Preferences, adversaries can set the userID to be under 500 and set the key value Hide500Users to TRUE in the /Library/Preferences/com.apple.loginwindow plist file. Every user has a userID associated with it. When the Hide500Users key value is set to TRUE, users with a userID under 500 do not appear on the login screen and in System Preferences. Using the command line, adversaries can use the dscl utility to create hidden user accounts by setting the IsHidden attribute to 1. Adversaries can also hide a user’s home folder by changing the chflags to hidden. Adversaries may similarly hide user accounts in Windows. Adversaries can set the HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\SpecialAccounts\UserList Registry key value to 0 for a specific user to prevent that user from being listed on the logon screen. On Linux systems, adversaries may hide user accounts from the login screen, also referred to as the greeter. The method an adversary may use depends on which Display Manager the distribution is currently using. For example, on an Ubuntu system using the GNOME Display Manger (GDM), accounts may be hidden from the greeter using the gsettings command (ex: sudo -u gdm gsettings set org.gnome.login-screen disable-user-list true). Display Managers are not anchored to specific distributions and may be changed by a user or adversary.

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
- T1564.002: https://attack.mitre.org/techniques/T1564/002
- Reviewed: 2026-10-27
