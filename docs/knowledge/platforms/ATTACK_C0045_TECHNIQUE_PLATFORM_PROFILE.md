# ShadowRay Technique Platform Profile

## Reference

- Technique: **C0045 — ShadowRay**
- Platforms named in the source: not stated

ShadowRay was a campaign that began in late 2023 targeting the education, cryptocurrency, biopharma, and other sectors through a vulnerability (CVE-2023-48022) in the Ray AI framework named ShadowRay. According to security researchers ShadowRay was the first known instance of AI workloads being activley exploited in the wild through vulnerabilities in AI infrastructure. CVE-2023-48022, which allows access to compute resources and sensitive data for exposed instances, remains unpatched and has been disputed by the vendor as they maintain that Ray is not intended for use outside of a strictly controlled network environment.

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
- C0045: https://attack.mitre.org/campaigns/C0045
- Reviewed: 2026-10-27
