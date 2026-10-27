# AcidRain Technique Engineering Review

## Reference

- Technique: **S1125 — AcidRain**

AcidRain is an ELF binary targeting modems and routers using MIPS architecture. AcidRain is associated with the ViaSat KA-SAT communication outage that took place during the initial phases of the 2022 full-scale invasion of Ukraine. Analysis indicates overlap with another network device-targeting malware, VPNFilter, associated with Sandworm Team. US and European government sources linked AcidRain to Russian government entities, while Ukrainian government sources linked AcidRain specifically to Sandworm Team.

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
- S1125: https://attack.mitre.org/software/S1125
- Reviewed: 2026-10-27
