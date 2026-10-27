# Analytic 1261 Technique Platform Profile

## Reference

- Technique: **AN1261 — Analytic 1261**
- Platforms named in the source: Containers

Detection of container image build activity directly on the host using Docker or Kubernetes APIs. Defenders may observe Docker build requests, anomalous Dockerfile instructions (such as downloading code from unknown IPs), or creation of new images followed by immediate deployment. This behavior chain typically consists of an unexpected image creation event correlated with outbound network communication to non-standard or untrusted destinations.

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
- AN1261: https://attack.mitre.org/detectionstrategies/DET0459#AN1261
- Reviewed: 2026-10-27
