# Analytic 1196 Technique Engineering Review

## Reference

- Technique: **AN1196 — Analytic 1196**

Abuse of bind mounts to obscure process directories. Defender perspective: detecting anomalous mount operations where a process’s /proc entry is remapped to another directory, often hiding malicious activity from native utilities (ps, top). Behavior chain includes: (1) execution of `mount` with `-o bind` or `-B` flags, (2) modification of /proc entries inconsistent with expected process lineage, and (3) subsequent anomalous activity from processes whose metadata no longer matches execution context.

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
- AN1196: https://attack.mitre.org/detectionstrategies/DET0428#AN1196
- Reviewed: 2026-10-27
