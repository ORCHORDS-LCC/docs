# Cutting Edge Technique Platform Profile

## Reference

- Technique: **C0029 — Cutting Edge**
- Platforms named in the source: not stated

Cutting Edge was a campaign conducted by suspected China-nexus espionage actors, variously identified as UNC5221/UTA0178 and UNC5325, that began as early as December 2023 with the exploitation of zero-day vulnerabilities in Ivanti Connect Secure (previously Pulse Secure) VPN appliances. Cutting Edge targeted the U.S. defense industrial base and multiple sectors globally including telecommunications, financial, aerospace, and technology. Cutting Edge featured the use of defense evasion and living-off-the-land (LoTL) techniques along with the deployment of web shells and other custom malware.

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
- C0029: https://attack.mitre.org/campaigns/C0029
- Reviewed: 2026-10-27
