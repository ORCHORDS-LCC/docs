# Command Obfuscation Technique Engineering Review

## Reference

- Technique: **T1027.010 — Command Obfuscation**

Adversaries may obfuscate content during command execution to impede detection. Command-line obfuscation is a method of making strings and patterns within commands and scripts more difficult to signature and analyze. This type of obfuscation can be included within commands executed by delivered payloads (e.g., Phishing and Drive-by Compromise) or interactively via Command and Scripting Interpreter. For example, adversaries may abuse syntax that utilizes various symbols and escape characters (such as spacing, `^`, `+`. `$`, and `%`) to make commands difficult to analyze while maintaining the same intended functionality. Many languages support built-in obfuscation in the form of base64 or URL encoding. Adversaries may also manually implement command obfuscation via string splitting (`“Wor”+“d.Application”`), order and casing of characters (`rev <<<'dwssap/cte/ tac'`), globing (`mkdir -p '/tmp/:&$NiA'`), as well as various tricks involving passing strings through tokens/environment variables/input streams. Adversaries may also use tricks such as directory traversals to obfuscate references to the binary being invoked by a command (`C:\voi\pcw\..\..\Windows\tei\qs\k\..\..\..\system32\erool\..\wbem\wg\je\..\..\wmic.exe shadowcopy delete`). Tools such as Invoke-Obfuscation and Invoke-DOSfucation have also been used to obfuscate commands.

## Engineering review

1. Identify the engineering boundary where the technique would apply: the component, the service, or the deployment.
2. Review the design decision that would prevent the technique, and record the alternative considered.
3. Review the implementation evidence for the preventive control.
4. Review the test coverage that would fail if the control regressed.
5. Review the observability: which signal would show the control is not operating.
6. Record the residual risk where prevention is not achievable, and the detection that compensates.

## Review evidence

- the design record for the preventive decision;
- the implementation or configuration evidence;
- the test record showing the control is exercised;
- the observability mapping.

## Limitations

An engineering review describes what the design and the implementation evidence show. It does not claim the technique has been addressed in production.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1027.010: https://attack.mitre.org/techniques/T1027/010
- Reviewed: 2026-10-27
