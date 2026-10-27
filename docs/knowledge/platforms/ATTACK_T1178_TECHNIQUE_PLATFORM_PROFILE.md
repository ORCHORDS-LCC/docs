# SID-History Injection Mitigation Technique Platform Profile

## Reference

- Technique: **T1178 — SID-History Injection Mitigation**
- Platforms named in the source: not stated

Clean up SID-History attributes after legitimate account migration is complete. Consider applying SID Filtering to interforest trusts, such as forest trusts and external trusts, to exclude SID-History from requests to access domain resources. SID Filtering ensures that any authentication requests over a trust only contain SIDs of security principals from the trusted domain (i.e. preventing the trusted domain from claiming a user has membership in groups outside of the domain). SID Filtering of forest trusts is enabled by default, but may have been disabled in some cases to allow a child domain to transitively access forest trusts. SID Filtering of external trusts is automatically enabled on all created external trusts using Server 2003 or later domain controllers. However note that SID Filtering is not automatically applied to legacy trusts or may have been deliberately disabled to allow inter-domain access to resources. SID Filtering can be applied by: * Disabling SIDHistory on forest trusts using the netdom tool (<code>netdom trust <TrustingDomainName> /domain:<TrustedDomainName> /EnableSIDHistory:no</code> on the domain controller). * Applying SID Filter Quarantining to external trusts using the netdom tool (<code>netdom trust <TrustingDomainName> /domain:<TrustedDomainName> /quarantine:yes</code> on the domain controller) Applying SID Filtering to domain trusts within a single forest is not recommended as it is an unsupported configuration and can cause breaking changes. If a domain within a forest is untrustworthy then it should not be a member of the forest. In this situation it is necessary to first split the trusted and untrusted domains into separate forests where SID Filtering can be applied to an interforest trust.

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
- T1178: https://attack.mitre.org/mitigations/T1178
- Reviewed: 2026-10-27
