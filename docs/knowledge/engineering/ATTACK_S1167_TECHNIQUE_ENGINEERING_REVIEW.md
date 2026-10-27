# AcidPour Technique Engineering Review

## Reference

- Technique: **S1167 — AcidPour**

AcidPour is a variant of AcidRain designed to impact a wider range of x86 architecture Linux devices. AcidPour is an x86 ELF binary that expands on the targeted devices and locations in AcidRain by including items such as Unsorted Block Image (UBI), Deice Mapper (DM), and various flash memory references. Based on this expanded targeting, AcidPour can impact a variety of device types including IoT, networking, and ICS embedded device types. AcidPour is a wiping payload associated with the Sandworm Team threat actor, and potentially linked to attacks against Ukrainian internet service providers (ISPs) in 2023.

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
- S1167: https://attack.mitre.org/software/S1167
- Reviewed: 2026-10-27
