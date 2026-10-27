# Analytic 1196 Technique Platform Profile

## Reference

- Technique: **AN1196 — Analytic 1196**
- Platforms named in the source: Linux

Abuse of bind mounts to obscure process directories. Defender perspective: detecting anomalous mount operations where a process’s /proc entry is remapped to another directory, often hiding malicious activity from native utilities (ps, top). Behavior chain includes: (1) execution of `mount` with `-o bind` or `-B` flags, (2) modification of /proc entries inconsistent with expected process lineage, and (3) subsequent anomalous activity from processes whose metadata no longer matches execution context.

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
- AN1196: https://attack.mitre.org/detectionstrategies/DET0428#AN1196
- Reviewed: 2026-10-27
