# Hypervisor Technique Engineering Review

## Reference

- Technique: **T1062 — Hypervisor**

**This technique has been deprecated and should no longer be used.** A type-1 hypervisor is a software layer that sits between the guest operating systems and system's hardware. It presents a virtual running environment to an operating system. An example of a common hypervisor is Xen. A type-1 hypervisor operates at a level below the operating system and could be designed with Rootkit functionality to hide its existence from the guest operating system. A malicious hypervisor of this nature could be used to persist on systems through interruption.

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
- T1062: https://attack.mitre.org/techniques/T1062
- Reviewed: 2026-10-27
