# Kernel Modules and Extensions Mitigation Technique Engineering Review

## Reference

- Technique: **T1215 — Kernel Modules and Extensions Mitigation**

Common tools for detecting Linux rootkits include: rkhunter , chrootkit , although rootkits may be designed to evade certain detection tools. LKMs and Kernel extensions require root level permissions to be installed. Limit access to the root account and prevent users from loading kernel modules and extensions through proper privilege separation and limiting Privilege Escalation opportunities. Application whitelisting and software restriction tools, such as SELinux, can also aide in restricting kernel module loading.

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
- T1215: https://attack.mitre.org/mitigations/T1215
- Reviewed: 2026-10-27
