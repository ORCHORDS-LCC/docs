# Source Technique Platform Profile

## Reference

- Technique: **T1153 — Source**
- Platforms named in the source: Linux, macOS

**This technique has been deprecated and should no longer be used.** The source command loads functions into the current shell or executes files in the current context. This built-in command can be run in two different ways source /path/to/filename [arguments] or .**This technique has been deprecated and should no longer be used.** /path/to/filename [arguments]. Take note of the space after the ".". Without a space, a new shell is created that runs the program instead of running the program within the current context. This is often used to make certain features or functions available to a shell or to update a specific shell's environment. Adversaries can abuse this functionality to execute programs. The file executed with this technique does not need to be marked executable beforehand.

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
- T1153: https://attack.mitre.org/techniques/T1153
- Reviewed: 2026-10-27
