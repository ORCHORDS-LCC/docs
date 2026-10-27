# BITS Jobs Mitigation Technique Platform Profile

## Reference

- Technique: **T1197 — BITS Jobs Mitigation**
- Platforms named in the source: not stated

This type of attack technique cannot be easily mitigated with preventive controls since it is based on the abuse of operating system design features. For example, disabling all BITS functionality will likely have unintended side effects, such as preventing legitimate software patching and updating. Efforts should be focused on preventing adversary tools from running earlier in the chain of activity and on identification of subsequent malicious behavior. Modify network and/or host firewall rules, as well as other network controls, to only allow legitimate BITS traffic. Consider limiting access to the BITS interface to specific users or groups. Consider reducing the default BITS job lifetime in Group Policy or by editing the <code>JobInactivityTimeout</code> and <code>MaxDownloadTime</code> Registry values in <code> HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\BITS</code>.

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
- T1197: https://attack.mitre.org/mitigations/T1197
- Reviewed: 2026-10-27
