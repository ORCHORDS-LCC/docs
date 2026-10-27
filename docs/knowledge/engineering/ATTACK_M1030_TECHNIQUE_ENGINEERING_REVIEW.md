# Network Segmentation Technique Engineering Review

## Reference

- Technique: **M1030 — Network Segmentation**

Network segmentation involves dividing a network into smaller, isolated segments to control and limit the flow of traffic between devices, systems, and applications. By segmenting networks, organizations can reduce the attack surface, restrict lateral movement by adversaries, and protect critical assets from compromise. Effective network segmentation leverages a combination of physical boundaries, logical separation through VLANs, and access control policies enforced by network appliances like firewalls, routers, and cloud-based configurations. This mitigation can be implemented through the following measures: Segment Critical Systems: - Identify and group systems based on their function, sensitivity, and risk. Examples include payment systems, HR databases, production systems, and internet-facing servers. - Use VLANs, firewalls, or routers to enforce logical separation. Implement DMZ for Public-Facing Services: - Host web servers, DNS servers, and email servers in a DMZ to limit their access to internal systems. - Apply strict firewall rules to filter traffic between the DMZ and internal networks. Use Cloud-Based Segmentation: - In cloud environments, use VPCs, subnets, and security groups to isolate applications and enforce traffic rules. - Apply AWS Transit Gateway or Azure VNet peering for controlled connectivity between cloud segments. Apply Microsegmentation for Workloads: - Use software-defined networking (SDN) tools to implement workload-level segmentation and prevent lateral movement. Restrict Traffic with ACLs and Firewalls: - Apply Access Control Lists (ACLs) to network devices to enforce "deny by default" policies. - Use firewalls to restrict both north-south (external-internal) and east-west (internal-internal) traffic. Monitor and Audit Segmented Networks: - Regularly review firewall rules, ACLs, and segmentation policies. - Monitor network flows for anomalies to ensure segmentation is effective. Test Segmentation Effectiveness: - Perform periodic penetration tests to verify that unauthorized access is blocked between network segments.

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
- M1030: https://attack.mitre.org/mitigations/M1030
- Reviewed: 2026-10-27
