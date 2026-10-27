# Hidden Window Technique Response Playbook

## Target technique

**T1564.003 — Hidden Window**

- Tactics: stealth
- Platforms: Linux, macOS, Windows

Adversaries may use hidden windows to conceal malicious activity from the plain sight of users. In some cases, windows that would typically be displayed when an application carries out an operation can be hidden. This may be utilized by system administrators to avoid disrupting user work environments when carrying out administrative tasks. Adversaries may abuse these functionalities to hide otherwise visible windows from users so as not to alert the user to adversary activity on the system. On macOS, the configurations for how applications run are listed in property list (plist) files. One of the tags in these files can be apple.awt.UIElement, which allows for Java applications to prevent the application's icon from appearing in the Dock. A common use for this is when applications run in the system tray, but don't also want to show up in the Dock. Similarly, on Windows there are a variety of features in scripting languages, such as PowerShell, Jscript, and Visual Basic to make windows hidden. One example of this is powershell.exe -WindowStyle Hidden. The Windows Registry can also be edited to hide application windows from the current user. For example, by setting the `WindowPosition` subkey in the `HKEY_CURRENT_USER\Console\%SystemRoot%_System32_WindowsPowerShell_v1.0_PowerShell.exe` Registry key to a maximum value, PowerShell windows will open off screen and be hidden. In addition, Windows supports the `CreateDesktop()` API that can create a hidden desktop window with its own corresponding explorer.exe process. All applications running on the hidden desktop window, such as a hidden VNC (hVNC) session, will be invisible to other desktops windows. Adversaries may also leverage cmd.exe as a parent process, and then utilize a LOLBin, such as DeviceCredentialDeployment.exe, to hide windows.

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
- T1564.003: https://attack.mitre.org/techniques/T1564/003
- Reviewed: 2026-10-27
