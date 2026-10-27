# T1546.018 Python Startup Hooks Outcome Lesson

## Authoritative description

- Technique: **T1546.018 — Python Startup Hooks**
- Tactics: persistence, privilege-escalation
- Platforms: Linux, macOS, Windows

Adversaries may achieve persistence by leveraging Python’s startup mechanisms, including path configuration (`.pth`) files and the `sitecustomize.py` or `usercustomize.py` modules. These files are automatically processed during the initialization of the Python interpreter, allowing for the execution of arbitrary code whenever Python is invoked. Path configuration files are designed to extend Python’s module search paths through the use of import statements. If a `.pth` file is placed in Python's `site-packages` or `dist-packages` directories, any lines beginning with `import` will be executed automatically on Python invocation. Similarly, if `sitecustomize.py` or `usercustomize.py` is present in the Python path, these files will be imported during interpreter startup, and any code they contain will be executed. Adversaries may abuse these mechanisms to establish persistence on systems where Python is widely used (e.g., for automation or scripting in production environments).

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
- T1546.018: https://attack.mitre.org/techniques/T1546/018
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
