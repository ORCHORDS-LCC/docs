# T1564.002 Hidden Users Outcome Lesson

## Authoritative description

- Technique: **T1564.002 — Hidden Users**
- Tactics: stealth
- Platforms: Linux, macOS, Windows

Adversaries may use hidden users to hide the presence of user accounts they create or modify. Administrators may want to hide users when there are many user accounts on a given system or if they want to hide their administrative or other management accounts from other users. In macOS, adversaries can create or modify a user to be hidden through manipulating plist files, folder attributes, and user attributes. To prevent a user from being shown on the login screen and in System Preferences, adversaries can set the userID to be under 500 and set the key value <code>Hide500Users</code> to <code>TRUE</code> in the <code>/Library/Preferences/com.apple.loginwindow</code> plist file. Every user has a userID associated with it. When the <code>Hide500Users</code> key value is set to <code>TRUE</code>, users with a userID under 500 do not appear on the login screen and in System Preferences. Using the command line, adversaries can use the <code>dscl</code> utility to create hidden user accounts by setting the <code>IsHidden</code> attribute to <code>1</code>. Adversaries can also hide a user’s home folder by changing the <code>chflags</code> to hidden. Adversaries may similarly hide user accounts in Windows. Adversaries can set the <code>HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\SpecialAccounts\UserList</code> Registry key value to <code>0</code> for a specific user to prevent that user from being listed on the logon screen. On Linux systems, adversaries may hide user accounts from the login screen, also referred to as the greeter. The method an adversary may use depends on which Display Manager the distribution is currently using. For example, on an Ubuntu system using the GNOME Display Manger (GDM), accounts may be hidden from the greeter using the <code>gsettings</code> command (ex: <code>sudo -u gdm gsettings set org.gnome.login-screen disable-user-list true</code>). Display Managers are not anchored to specific distributions and may be changed by a user or adversary.

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
- T1564.002: https://attack.mitre.org/techniques/T1564/002
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
