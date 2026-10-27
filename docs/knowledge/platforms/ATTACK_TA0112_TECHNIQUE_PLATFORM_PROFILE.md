# Defense Impairment Technique Platform Profile

## Reference

- Technique: **TA0112 — Defense Impairment**
- Platforms named in the source: not stated

The adversary is trying to break security mechanisms, pipelines, and tooling so defenders can’t see or trust what’s happening. Defense Impairment consists of techniques that degrade, disable, or undermine the effectiveness and trustworthiness of security controls and monitoring mechanisms. These techniques are characterized by direct interference with defensive systems. The goal is to reduce defenders’ ability to detect, interpret, or respond to adversary activity.

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
- TA0112: https://attack.mitre.org/tactics/TA0112
- Reviewed: 2026-10-27
