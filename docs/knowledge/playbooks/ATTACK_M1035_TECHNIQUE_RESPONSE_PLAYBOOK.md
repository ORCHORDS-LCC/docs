# Limit Access to Resource Over Network Technique Response Playbook

## Target technique

**M1035 — Limit Access to Resource Over Network**


Restrict access to network resources, such as file shares, remote systems, and services, to only those users, accounts, or systems with a legitimate business requirement. This can include employing technologies like network concentrators, RDP gateways, and zero-trust network access (ZTNA) models, alongside hardening services and protocols. This mitigation can be implemented through the following measures: Audit and Restrict Access: - Regularly audit permissions for file shares, network services, and remote access tools. - Remove unnecessary access and enforce least privilege principles for users and services. - Use Active Directory and IAM tools to restrict access based on roles and attributes. Deploy Secure Remote Access Solutions: - Use RDP gateways, VPN concentrators, and ZTNA solutions to aggregate and secure remote access connections. - Configure access controls to restrict connections based on time, device, and user identity. - Enforce MFA for all remote access mechanisms. Disable Unnecessary Services: - Identify running services using tools like netstat (Windows/Linux) or Nmap. - Disable unused services, such as Telnet, FTP, and legacy SMB, to reduce the attack surface. - Use firewall rules to block traffic on unused ports and protocols. Network Segmentation and Isolation: - Use VLANs, firewalls, or micro-segmentation to isolate critical network resources from general access. - Restrict communication between subnets to prevent lateral movement. Monitor and Log Access: - Monitor access attempts to file shares, RDP, and remote network resources using SIEM tools. - Enable auditing and logging for successful and failed attempts to access restricted resources. *Tools for Implementation* File Share Management: - Microsoft Active Directory Group Policies - Samba (Linux/Unix file share management) - AccessEnum (Windows access auditing tool) Secure Remote Access: - Microsoft Remote Desktop Gateway - Apache Guacamole (open-source RDP/VNC gateway) - Zero Trust solutions: Tailscale, Cloudflare Zero Trust Service and Protocol Hardening: - Nmap or Nessus for network service discovery - Windows Group Policy Editor for disabling SMBv1, Telnet, and legacy protocols - iptables or firewalld (Linux) for blocking unnecessary traffic Network Segmentation: - pfSense for open-source network isolation.

## Preconditions

- the estate in scope is identified, with the systems the technique could apply to;
- an owner is accountable for detection and response;
- current telemetry and configuration can be inspected;
- the technique is applicable or requires an applicability decision.

## Procedure

1. Confirm the scope and owner.
2. Read the current technique description and the associated detection guidance.
3. Inventory the telemetry that would carry the technique's indicators.
4. Inspect whether the indicators are present in the environment.
5. Exercise the detection path and confirm it produces the expected signal.
6. Record gaps in detection coverage and assign remediation owners.
7. Record justified non-applicability or accepted detection gaps separately.
8. Set the next event-driven or periodic verification trigger.

## Failure handling

If the detection path does not produce the expected signal, treat the coverage as unverified, preserve the test evidence, and route the gap through the appropriate remediation or risk process.

## Completion evidence

Scope, owner, source version, telemetry inspected, tests performed, findings, exceptions, remediation links, reviewer, and next trigger.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- M1035: https://attack.mitre.org/mitigations/M1035
- Reviewed: 2026-10-27
