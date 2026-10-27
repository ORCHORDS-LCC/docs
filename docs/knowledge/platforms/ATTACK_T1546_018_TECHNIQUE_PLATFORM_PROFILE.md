# Python Startup Hooks Technique Platform Profile

## Reference

- Technique: **T1546.018 — Python Startup Hooks**
- Platforms named in the source: Linux, macOS, Windows

Adversaries may achieve persistence by leveraging Python’s startup mechanisms, including path configuration (`.pth`) files and the `sitecustomize.py` or `usercustomize.py` modules. These files are automatically processed during the initialization of the Python interpreter, allowing for the execution of arbitrary code whenever Python is invoked. Path configuration files are designed to extend Python’s module search paths through the use of import statements. If a `.pth` file is placed in Python's `site-packages` or `dist-packages` directories, any lines beginning with `import` will be executed automatically on Python invocation. Similarly, if `sitecustomize.py` or `usercustomize.py` is present in the Python path, these files will be imported during interpreter startup, and any code they contain will be executed. Adversaries may abuse these mechanisms to establish persistence on systems where Python is widely used (e.g., for automation or scripting in production environments).

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
- T1546.018: https://attack.mitre.org/techniques/T1546/018
- Reviewed: 2026-10-27
