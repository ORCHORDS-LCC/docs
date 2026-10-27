# T1564.003 Hidden Window Outcome Lesson

## Authoritative description

- Technique: **T1564.003 — Hidden Window**
- Tactics: stealth
- Platforms: Linux, macOS, Windows

Adversaries may use hidden windows to conceal malicious activity from the plain sight of users. In some cases, windows that would typically be displayed when an application carries out an operation can be hidden. This may be utilized by system administrators to avoid disrupting user work environments when carrying out administrative tasks. Adversaries may abuse these functionalities to hide otherwise visible windows from users so as not to alert the user to adversary activity on the system. On macOS, the configurations for how applications run are listed in property list (plist) files. One of the tags in these files can be <code>apple.awt.UIElement</code>, which allows for Java applications to prevent the application's icon from appearing in the Dock. A common use for this is when applications run in the system tray, but don't also want to show up in the Dock. Similarly, on Windows there are a variety of features in scripting languages, such as PowerShell, Jscript, and Visual Basic to make windows hidden. One example of this is <code>powershell.exe -WindowStyle Hidden</code>. The Windows Registry can also be edited to hide application windows from the current user. For example, by setting the `WindowPosition` subkey in the `HKEY_CURRENT_USER\Console\%SystemRoot%_System32_WindowsPowerShell_v1.0_PowerShell.exe` Registry key to a maximum value, PowerShell windows will open off screen and be hidden. In addition, Windows supports the `CreateDesktop()` API that can create a hidden desktop window with its own corresponding <code>explorer.exe</code> process. All applications running on the hidden desktop window, such as a hidden VNC (hVNC) session, will be invisible to other desktops windows. Adversaries may also leverage cmd.exe as a parent process, and then utilize a LOLBin, such as DeviceCredentialDeployment.exe, to hide windows.

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
- T1564.003: https://attack.mitre.org/techniques/T1564/003
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
