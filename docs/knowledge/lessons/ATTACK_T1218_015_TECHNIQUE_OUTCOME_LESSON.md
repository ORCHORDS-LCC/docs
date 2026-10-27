# T1218.015 Electron Applications Outcome Lesson

## Authoritative description

- Technique: **T1218.015 — Electron Applications**
- Tactics: stealth
- Platforms: Linux, macOS, Windows

Adversaries may abuse components of the Electron framework to execute malicious code. The Electron framework hosts many common applications such as Signal, Slack, and Microsoft Teams. Originally developed by GitHub, Electron is a cross-platform desktop application development framework that employs web technologies like JavaScript, HTML, and CSS. The Chromium engine is used to display web content and Node.js runs the backend code. Due to the functional mechanics of Electron (such as allowing apps to run arbitrary commands), adversaries may also be able to perform malicious functions in the background potentially disguised as legitimate tools within the framework. For example, the abuse of `teams.exe` and `chrome.exe` may allow adversaries to execute malicious commands as child processes of the legitimate application (e.g., `chrome.exe --disable-gpu-sandbox --gpu-launcher="C:\Windows\system32\cmd.exe /c calc.exe`). Adversaries may also execute malicious content by planting malicious JavaScript within Electron applications.

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
- T1218.015: https://attack.mitre.org/techniques/T1218/015
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
