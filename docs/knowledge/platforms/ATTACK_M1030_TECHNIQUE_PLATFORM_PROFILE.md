# Network Segmentation Technique Platform Profile

## Reference

- Technique: **M1030 — Network Segmentation**
- Platforms named in the source: not stated

Network segmentation involves dividing a network into smaller, isolated segments to control and limit the flow of traffic between devices, systems, and applications. By segmenting networks, organizations can reduce the attack surface, restrict lateral movement by adversaries, and protect critical assets from compromise. Effective network segmentation leverages a combination of physical boundaries, logical separation through VLANs, and access control policies enforced by network appliances like firewalls, routers, and cloud-based configurations. This mitigation can be implemented through the following measures: Segment Critical Systems: - Identify and group systems based on their function, sensitivity, and risk. Examples include payment systems, HR databases, production systems, and internet-facing servers. - Use VLANs, firewalls, or routers to enforce logical separation. Implement DMZ for Public-Facing Services: - Host web servers, DNS servers, and email servers in a DMZ to limit their access to internal systems. - Apply strict firewall rules to filter traffic between the DMZ and internal networks. Use Cloud-Based Segmentation: - In cloud environments, use VPCs, subnets, and security groups to isolate applications and enforce traffic rules. - Apply AWS Transit Gateway or Azure VNet peering for controlled connectivity between cloud segments. Apply Microsegmentation for Workloads: - Use software-defined networking (SDN) tools to implement workload-level segmentation and prevent lateral movement. Restrict Traffic with ACLs and Firewalls: - Apply Access Control Lists (ACLs) to network devices to enforce "deny by default" policies. - Use firewalls to restrict both north-south (external-internal) and east-west (internal-internal) traffic. Monitor and Audit Segmented Networks: - Regularly review firewall rules, ACLs, and segmentation policies. - Monitor network flows for anomalies to ensure segmentation is effective. Test Segmentation Effectiveness: - Perform periodic penetration tests to verify that unauthorized access is blocked between network segments.

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
- M1030: https://attack.mitre.org/mitigations/M1030
- Reviewed: 2026-10-27
