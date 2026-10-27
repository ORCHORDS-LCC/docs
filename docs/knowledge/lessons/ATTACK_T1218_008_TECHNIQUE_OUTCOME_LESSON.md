# T1218.008 Odbcconf Outcome Lesson

## Authoritative description

- Technique: **T1218.008 — Odbcconf**
- Tactics: stealth
- Platforms: Windows

Adversaries may abuse odbcconf.exe to proxy execution of malicious payloads. Odbcconf.exe is a Windows utility that allows you to configure Open Database Connectivity (ODBC) drivers and data source names. The Odbcconf.exe binary may be digitally signed by Microsoft. Adversaries may abuse odbcconf.exe to bypass application control solutions that do not account for its potential abuse. Similar to Regsvr32, odbcconf.exe has a REGSVR flag that can be misused to execute DLLs (ex: odbcconf.exe /S /A &lbrace;REGSVR "(a user home directory)file.dll"&rbrace;).

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
- T1218.008: https://attack.mitre.org/techniques/T1218/008
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
