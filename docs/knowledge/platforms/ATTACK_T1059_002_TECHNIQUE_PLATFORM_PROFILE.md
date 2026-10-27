# AppleScript Technique Platform Profile

## Reference

- Technique: **T1059.002 — AppleScript**
- Platforms named in the source: macOS

Adversaries may abuse AppleScript for execution. AppleScript is a macOS scripting language designed to control applications and parts of the OS via inter-application messages called AppleEvents. These AppleEvent messages can be sent independently or easily scripted with AppleScript. These events can locate open windows, send keystrokes, and interact with almost any open application locally or remotely. Scripts can be run from the command-line via <code>osascript /path/to/script</code> or <code>osascript -e "script here"</code>. Aside from the command line, scripts can be executed in numerous ways including Mail rules, Calendar.app alarms, and Automator workflows. AppleScripts can also be executed as plain text shell scripts by adding <code>#!/usr/bin/osascript</code> to the start of the script file. AppleScripts do not need to call <code>osascript</code> to execute. However, they may be executed from within mach-O binaries by using the macOS Native APIs <code>NSAppleScript</code> or <code>OSAScript</code>, both of which execute code independent of the <code>/usr/bin/osascript</code> command line utility. Adversaries may abuse AppleScript to execute various behaviors, such as interacting with an open SSH connection, moving to remote machines, and even presenting users with fake dialog boxes. These events cannot start applications remotely (they can start them locally), but they can interact with applications if they're already running remotely. On macOS 10.10 Yosemite and higher, AppleScript has the ability to execute Native APIs, which otherwise would require compilation and execution in a mach-O binary file format. Since this is a scripting language, it can be used to launch more common techniques as well such as a reverse shell via Python.

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
- T1059.002: https://attack.mitre.org/techniques/T1059/002
- Reviewed: 2026-10-27
