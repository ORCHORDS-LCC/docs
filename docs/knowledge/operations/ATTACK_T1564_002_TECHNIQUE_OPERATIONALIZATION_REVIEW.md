# Hidden Users Technique Operationalization Review

## Reference

- Technique: **T1564.002 — Hidden Users**

Adversaries may use hidden users to hide the presence of user accounts they create or modify. Administrators may want to hide users when there are many user accounts on a given system or if they want to hide their administrative or other management accounts from other users. In macOS, adversaries can create or modify a user to be hidden through manipulating plist files, folder attributes, and user attributes. To prevent a user from being shown on the login screen and in System Preferences, adversaries can set the userID to be under 500 and set the key value <code>Hide500Users</code> to <code>TRUE</code> in the <code>/Library/Preferences/com.apple.loginwindow</code> plist file. Every user has a userID associated with it. When the <code>Hide500Users</code> key value is set to <code>TRUE</code>, users with a userID under 500 do not appear on the login screen and in System Preferences. Using the command line, adversaries can use the <code>dscl</code> utility to create hidden user accounts by setting the <code>IsHidden</code> attribute to <code>1</code>. Adversaries can also hide a user’s home folder by changing the <code>chflags</code> to hidden. Adversaries may similarly hide user accounts in Windows. Adversaries can set the <code>HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\SpecialAccounts\UserList</code> Registry key value to <code>0</code> for a specific user to prevent that user from being listed on the logon screen. On Linux systems, adversaries may hide user accounts from the login screen, also referred to as the greeter. The method an adversary may use depends on which Display Manager the distribution is currently using. For example, on an Ubuntu system using the GNOME Display Manger (GDM), accounts may be hidden from the greeter using the <code>gsettings</code> command (ex: <code>sudo -u gdm gsettings set org.gnome.login-screen disable-user-list true</code>). Display Managers are not anchored to specific distributions and may be changed by a user or adversary.

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
- T1564.002: https://attack.mitre.org/techniques/T1564/002
- Reviewed: 2026-10-27
