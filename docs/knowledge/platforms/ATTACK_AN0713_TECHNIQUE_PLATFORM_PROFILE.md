# Analytic 0713 Technique Platform Profile

## Reference

- Technique: **AN0713 — Analytic 0713**
- Platforms named in the source: Linux

Defender observes unauthorized modification or creation of Python hook files such as `.pth`, `sitecustomize.py`, or `usercustomize.py` in Python `site-packages`, `dist-packages`, or user paths. This is often correlated with subsequent unexpected interpreter execution (e.g., python3 running without user interaction), changes in interpreter behavior (e.g., malicious imports), and outbound connections initiated from Python. Defender links write/modify actions on hook files with execve of python process and/or anomalous child process or network activity.

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
- AN0713: https://attack.mitre.org/detectionstrategies/DET0258#AN0713
- Reviewed: 2026-10-27
