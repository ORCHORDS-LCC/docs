# Do Not Mitigate Technique Platform Profile

## Reference

- Technique: **M1055 — Do Not Mitigate**
- Platforms named in the source: not stated

The Do Not Mitigate category highlights scenarios where attempting to mitigate a specific technique may inadvertently increase the organization's security risk or operational instability. This could happen due to the complexity of the system, the integration of critical processes, or the potential for introducing new vulnerabilities. Instead of direct mitigation, these situations may call for alternative strategies such as detection, monitoring, or response. The Do Not Mitigate category underscores the importance of assessing the trade-offs between mitigation efforts and overall system integrity. This mitigation can be implemented through the following measures: Complex Systems Where Mitigation is Risky: - Interpretation: In certain systems, direct mitigation could introduce new risks, especially if the system is highly interconnected or complex, such as in legacy industrial control systems (ICS). Patching or modifying these systems could result in unplanned downtime, disruptions, or even safety risks. - Use Case: In a power grid control system, attempting to patch or disable certain services related to device communications might disrupt critical operations, leading to unintended service outages. Risk of Reducing Security Coverage: - Interpretation: In some cases, mitigating a technique might reduce the visibility or effectiveness of other security controls, limiting an organization’s ability to detect broader attacks. - Use Case: Disabling script execution on a web server to mitigate potential PowerShell-based attacks could interfere with legitimate administrative operations that rely on scripting, while attackers may still find alternate ways to execute code. Introduction of New Vulnerabilities: - Interpretation: In highly sensitive or tightly controlled environments, implementing certain mitigations might create vulnerabilities in other parts of the system. For instance, disabling default security mechanisms in an attempt to resolve compatibility issues may open the system to exploitation. - Use Case: Disabling certificate validation to resolve internal communication issues in a secure environment could lead to man-in-the-middle attacks, creating a greater vulnerability than the original problem. Negative Impact on Performance and Availability: - Interpretation: Mitigations that involve removing or restricting system functionalities can have unintended consequences for system performance and availability. Some mitigations, while effective at blocking certain attacks, may introduce performance bottlenecks or compromise essential operations. - Use Case: Implementing high levels of encryption to mitigate data theft might result in significant performance degradation in systems handling large volumes of real-time transactions.

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
- M1055: https://attack.mitre.org/mitigations/M1055
- Reviewed: 2026-10-27
