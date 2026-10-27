# Analytic 0021 Technique Platform Profile

## Reference

- Technique: **AN0021 — Analytic 0021**
- Platforms named in the source: Windows

Adversary manipulates dependencies/dev tools used by developers or CI: a package manager (npm/yarn/pnpm, pip/pipenv, nuget/dotnet, chocolatey/winget, maven/gradle) or a compiler/IDE downloads or restores content; files are written under project paths and execution paths (node_modules, packages, .nuget, .gradle, .m2, %AppData%\npm, %UserProfile%\.cargo\bin, temp build dirs). First run of newly written components triggers scripts (preinstall/postinstall), shell/PowerShell spawning, or loader DLLs, followed by network egress to non-approved registries/CDNs.

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
- AN0021: https://attack.mitre.org/detectionstrategies/DET0009#AN0021
- Reviewed: 2026-10-27
