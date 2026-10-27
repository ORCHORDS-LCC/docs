# Electron Applications Technique Platform Profile

## Reference

- Technique: **T1218.015 — Electron Applications**
- Platforms named in the source: Linux, macOS, Windows

Adversaries may abuse components of the Electron framework to execute malicious code. The Electron framework hosts many common applications such as Signal, Slack, and Microsoft Teams. Originally developed by GitHub, Electron is a cross-platform desktop application development framework that employs web technologies like JavaScript, HTML, and CSS. The Chromium engine is used to display web content and Node.js runs the backend code. Due to the functional mechanics of Electron (such as allowing apps to run arbitrary commands), adversaries may also be able to perform malicious functions in the background potentially disguised as legitimate tools within the framework. For example, the abuse of `teams.exe` and `chrome.exe` may allow adversaries to execute malicious commands as child processes of the legitimate application (e.g., `chrome.exe --disable-gpu-sandbox --gpu-launcher="C:\Windows\system32\cmd.exe /c calc.exe`). Adversaries may also execute malicious content by planting malicious JavaScript within Electron applications.

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
- T1218.015: https://attack.mitre.org/techniques/T1218/015
- Reviewed: 2026-10-27
