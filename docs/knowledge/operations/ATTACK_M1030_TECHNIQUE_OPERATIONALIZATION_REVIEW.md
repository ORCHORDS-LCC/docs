# Network Segmentation Technique Operationalization Review

## Reference

- Technique: **M1030 — Network Segmentation**

Network segmentation involves dividing a network into smaller, isolated segments to control and limit the flow of traffic between devices, systems, and applications. By segmenting networks, organizations can reduce the attack surface, restrict lateral movement by adversaries, and protect critical assets from compromise. Effective network segmentation leverages a combination of physical boundaries, logical separation through VLANs, and access control policies enforced by network appliances like firewalls, routers, and cloud-based configurations. This mitigation can be implemented through the following measures: Segment Critical Systems: - Identify and group systems based on their function, sensitivity, and risk. Examples include payment systems, HR databases, production systems, and internet-facing servers. - Use VLANs, firewalls, or routers to enforce logical separation. Implement DMZ for Public-Facing Services: - Host web servers, DNS servers, and email servers in a DMZ to limit their access to internal systems. - Apply strict firewall rules to filter traffic between the DMZ and internal networks. Use Cloud-Based Segmentation: - In cloud environments, use VPCs, subnets, and security groups to isolate applications and enforce traffic rules. - Apply AWS Transit Gateway or Azure VNet peering for controlled connectivity between cloud segments. Apply Microsegmentation for Workloads: - Use software-defined networking (SDN) tools to implement workload-level segmentation and prevent lateral movement. Restrict Traffic with ACLs and Firewalls: - Apply Access Control Lists (ACLs) to network devices to enforce "deny by default" policies. - Use firewalls to restrict both north-south (external-internal) and east-west (internal-internal) traffic. Monitor and Audit Segmented Networks: - Regularly review firewall rules, ACLs, and segmentation policies. - Monitor network flows for anomalies to ensure segmentation is effective. Test Segmentation Effectiveness: - Perform periodic penetration tests to verify that unauthorized access is blocked between network segments.

## Operationalization review

1. Record the operational scope: which services, environments, and data the technique could affect.
2. Record the runbook that would be executed, and its owner.
3. Record the telemetry the runbook depends on, and whether it is retained long enough to investigate.
4. Record the detection that would surface the technique before or after it has an effect.
5. Record the recovery path, and the evidence that recovery has been rehearsed.
6. Record the residual operational risk where the runbook depends on a manual step.

## Review evidence

- the runbook and its owner;
- the telemetry retention and coverage record;
- the detection mapping;
- the exercise or rehearsal record.

## Limitations

An operationalization review describes the runbook and the evidence around it. It does not claim the technique has been prevented or detected in a live environment.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- M1030: https://attack.mitre.org/mitigations/M1030
- Reviewed: 2026-10-27
