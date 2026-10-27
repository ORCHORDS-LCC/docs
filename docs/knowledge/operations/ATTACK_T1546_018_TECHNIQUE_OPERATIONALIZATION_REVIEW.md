# Python Startup Hooks Technique Operationalization Review

## Reference

- Technique: **T1546.018 — Python Startup Hooks**

Adversaries may achieve persistence by leveraging Python’s startup mechanisms, including path configuration (`.pth`) files and the `sitecustomize.py` or `usercustomize.py` modules. These files are automatically processed during the initialization of the Python interpreter, allowing for the execution of arbitrary code whenever Python is invoked. Path configuration files are designed to extend Python’s module search paths through the use of import statements. If a `.pth` file is placed in Python's `site-packages` or `dist-packages` directories, any lines beginning with `import` will be executed automatically on Python invocation. Similarly, if `sitecustomize.py` or `usercustomize.py` is present in the Python path, these files will be imported during interpreter startup, and any code they contain will be executed. Adversaries may abuse these mechanisms to establish persistence on systems where Python is widely used (e.g., for automation or scripting in production environments).

## Operationalization review

1. Record the operational scope: which services, environments, and data the technique could affect.
2. Record the runbook that would be executed, and its owner.
3. Record the telemetry the runbook depends on, and whether it is retained long enough to investigate.
4. Record the detection that would surface the technique before or after it has an effect.
5. Record the recovery path, and the evidence that recovery has been rehearsed.
6. Record the residual operational risk where the runbook depends on a manual step.

## Review evidence

- the runbook and its owner;
- the telemetry retention and coverage record;
- the detection mapping;
- the exercise or rehearsal record.

## Limitations

An operationalization review describes the runbook and the evidence around it. It does not claim the technique has been prevented or detected in a live environment.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1546.018: https://attack.mitre.org/techniques/T1546/018
- Reviewed: 2026-10-27
