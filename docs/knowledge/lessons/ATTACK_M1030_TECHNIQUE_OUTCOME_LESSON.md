# M1030 Network Segmentation Outcome Lesson

## Authoritative description

- Technique: **M1030 — Network Segmentation**

Network segmentation involves dividing a network into smaller, isolated segments to control and limit the flow of traffic between devices, systems, and applications. By segmenting networks, organizations can reduce the attack surface, restrict lateral movement by adversaries, and protect critical assets from compromise. Effective network segmentation leverages a combination of physical boundaries, logical separation through VLANs, and access control policies enforced by network appliances like firewalls, routers, and cloud-based configurations. This mitigation can be implemented through the following measures: Segment Critical Systems: - Identify and group systems based on their function, sensitivity, and risk. Examples include payment systems, HR databases, production systems, and internet-facing servers. - Use VLANs, firewalls, or routers to enforce logical separation. Implement DMZ for Public-Facing Services: - Host web servers, DNS servers, and email servers in a DMZ to limit their access to internal systems. - Apply strict firewall rules to filter traffic between the DMZ and internal networks. Use Cloud-Based Segmentation: - In cloud environments, use VPCs, subnets, and security groups to isolate applications and enforce traffic rules. - Apply AWS Transit Gateway or Azure VNet peering for controlled connectivity between cloud segments. Apply Microsegmentation for Workloads: - Use software-defined networking (SDN) tools to implement workload-level segmentation and prevent lateral movement. Restrict Traffic with ACLs and Firewalls: - Apply Access Control Lists (ACLs) to network devices to enforce "deny by default" policies. - Use firewalls to restrict both north-south (external-internal) and east-west (internal-internal) traffic. Monitor and Audit Segmented Networks: - Regularly review firewall rules, ACLs, and segmentation policies. - Monitor network flows for anomalies to ensure segmentation is effective. Test Segmentation Effectiveness: - Perform periodic penetration tests to verify that unauthorized access is blocked between network segments.

## Reusable lesson

This technique should be treated as an explicit review question when it is relevant to the system or organisation, rather than assumed to be covered by a generic control statement or by tooling that reports a related signal.

## Apply the lesson

1. Define the real scope before judging coverage.
2. Inspect current technical, process, governance, or operational evidence.
3. Separate documented intent from verified behaviour.
4. Record partial coverage and unresolved gaps instead of converting them into a pass.
5. Revisit when the underlying scope, threat environment, technology, suppliers, or mission materially changes.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- M1030: https://attack.mitre.org/mitigations/M1030
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
