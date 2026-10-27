# Operation Digital Eye Technique Engineering Review

## Reference

- Technique: **C0061 — Operation Digital Eye**

Operation Digital Eye was conducted in June and July of 2024 by suspected People's Republic of China (PRC)-nexus threat actors targeting business-to-business IT service providers in Southern Europe. Operation Digital Eye activity included the use of Visual Studio Code tunnels for command and control (C2) and custom lateral movement capabilities. Overlaps in tooling between Digital Eye and previous China-nexus campaigns, Operation Soft Cell and Operation Tainted Love, indicate the potential use of shared vendors or digital quartermasters.

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
- C0061: https://attack.mitre.org/campaigns/C0061
- Reviewed: 2026-10-27
