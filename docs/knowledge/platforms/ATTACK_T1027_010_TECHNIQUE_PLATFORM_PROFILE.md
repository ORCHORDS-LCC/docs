# Command Obfuscation Technique Platform Profile

## Reference

- Technique: **T1027.010 — Command Obfuscation**
- Platforms named in the source: Linux, macOS, Windows

Adversaries may obfuscate content during command execution to impede detection. Command-line obfuscation is a method of making strings and patterns within commands and scripts more difficult to signature and analyze. This type of obfuscation can be included within commands executed by delivered payloads (e.g., Phishing and Drive-by Compromise) or interactively via Command and Scripting Interpreter. For example, adversaries may abuse syntax that utilizes various symbols and escape characters (such as spacing, `^`, `+`. `$`, and `%`) to make commands difficult to analyze while maintaining the same intended functionality. Many languages support built-in obfuscation in the form of base64 or URL encoding. Adversaries may also manually implement command obfuscation via string splitting (`“Wor”+“d.Application”`), order and casing of characters (`rev <<<'dwssap/cte/ tac'`), globing (`mkdir -p '/tmp/:&$NiA'`), as well as various tricks involving passing strings through tokens/environment variables/input streams. Adversaries may also use tricks such as directory traversals to obfuscate references to the binary being invoked by a command (`C:\voi\pcw\..\..\Windows\tei\qs\k\..\..\..\system32\erool\..\wbem\wg\je\..\..\wmic.exe shadowcopy delete`). Tools such as Invoke-Obfuscation and Invoke-DOSfucation have also been used to obfuscate commands.

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
- T1027.010: https://attack.mitre.org/techniques/T1027/010
- Reviewed: 2026-10-27
