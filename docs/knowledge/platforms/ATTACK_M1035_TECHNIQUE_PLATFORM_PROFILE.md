# Limit Access to Resource Over Network Technique Platform Profile

## Reference

- Technique: **M1035 — Limit Access to Resource Over Network**
- Platforms named in the source: not stated

Restrict access to network resources, such as file shares, remote systems, and services, to only those users, accounts, or systems with a legitimate business requirement. This can include employing technologies like network concentrators, RDP gateways, and zero-trust network access (ZTNA) models, alongside hardening services and protocols. This mitigation can be implemented through the following measures: Audit and Restrict Access: - Regularly audit permissions for file shares, network services, and remote access tools. - Remove unnecessary access and enforce least privilege principles for users and services. - Use Active Directory and IAM tools to restrict access based on roles and attributes. Deploy Secure Remote Access Solutions: - Use RDP gateways, VPN concentrators, and ZTNA solutions to aggregate and secure remote access connections. - Configure access controls to restrict connections based on time, device, and user identity. - Enforce MFA for all remote access mechanisms. Disable Unnecessary Services: - Identify running services using tools like netstat (Windows/Linux) or Nmap. - Disable unused services, such as Telnet, FTP, and legacy SMB, to reduce the attack surface. - Use firewall rules to block traffic on unused ports and protocols. Network Segmentation and Isolation: - Use VLANs, firewalls, or micro-segmentation to isolate critical network resources from general access. - Restrict communication between subnets to prevent lateral movement. Monitor and Log Access: - Monitor access attempts to file shares, RDP, and remote network resources using SIEM tools. - Enable auditing and logging for successful and failed attempts to access restricted resources. *Tools for Implementation* File Share Management: - Microsoft Active Directory Group Policies - Samba (Linux/Unix file share management) - AccessEnum (Windows access auditing tool) Secure Remote Access: - Microsoft Remote Desktop Gateway - Apache Guacamole (open-source RDP/VNC gateway) - Zero Trust solutions: Tailscale, Cloudflare Zero Trust Service and Protocol Hardening: - Nmap or Nessus for network service discovery - Windows Group Policy Editor for disabling SMBv1, Telnet, and legacy protocols - iptables or firewalld (Linux) for blocking unnecessary traffic Network Segmentation: - pfSense for open-source network isolation.

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
- M1035: https://attack.mitre.org/mitigations/M1035
- Reviewed: 2026-10-27
