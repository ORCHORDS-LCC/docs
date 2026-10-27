# T1027.010 Command Obfuscation Outcome Lesson

## Authoritative description

- Technique: **T1027.010 — Command Obfuscation**
- Tactics: stealth
- Platforms: Linux, macOS, Windows

Adversaries may obfuscate content during command execution to impede detection. Command-line obfuscation is a method of making strings and patterns within commands and scripts more difficult to signature and analyze. This type of obfuscation can be included within commands executed by delivered payloads (e.g., Phishing and Drive-by Compromise) or interactively via Command and Scripting Interpreter. For example, adversaries may abuse syntax that utilizes various symbols and escape characters (such as spacing, `^`, `+`. `$`, and `%`) to make commands difficult to analyze while maintaining the same intended functionality. Many languages support built-in obfuscation in the form of base64 or URL encoding. Adversaries may also manually implement command obfuscation via string splitting (`“Wor”+“d.Application”`), order and casing of characters (`rev <<<'dwssap/cte/ tac'`), globing (`mkdir -p '/tmp/:&$NiA'`), as well as various tricks involving passing strings through tokens/environment variables/input streams. Adversaries may also use tricks such as directory traversals to obfuscate references to the binary being invoked by a command (`C:\voi\pcw\..\..\Windows\tei\qs\k\..\..\..\system32\erool\..\wbem\wg\je\..\..\wmic.exe shadowcopy delete`). Tools such as <code>Invoke-Obfuscation</code> and <code>Invoke-DOSfucation</code> have also been used to obfuscate commands.

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
- T1027.010: https://attack.mitre.org/techniques/T1027/010
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
