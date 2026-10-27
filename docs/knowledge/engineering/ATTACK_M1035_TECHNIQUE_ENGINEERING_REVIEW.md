# Limit Access to Resource Over Network Technique Engineering Review

## Reference

- Technique: **M1035 — Limit Access to Resource Over Network**

Restrict access to network resources, such as file shares, remote systems, and services, to only those users, accounts, or systems with a legitimate business requirement. This can include employing technologies like network concentrators, RDP gateways, and zero-trust network access (ZTNA) models, alongside hardening services and protocols. This mitigation can be implemented through the following measures: Audit and Restrict Access: - Regularly audit permissions for file shares, network services, and remote access tools. - Remove unnecessary access and enforce least privilege principles for users and services. - Use Active Directory and IAM tools to restrict access based on roles and attributes. Deploy Secure Remote Access Solutions: - Use RDP gateways, VPN concentrators, and ZTNA solutions to aggregate and secure remote access connections. - Configure access controls to restrict connections based on time, device, and user identity. - Enforce MFA for all remote access mechanisms. Disable Unnecessary Services: - Identify running services using tools like netstat (Windows/Linux) or Nmap. - Disable unused services, such as Telnet, FTP, and legacy SMB, to reduce the attack surface. - Use firewall rules to block traffic on unused ports and protocols. Network Segmentation and Isolation: - Use VLANs, firewalls, or micro-segmentation to isolate critical network resources from general access. - Restrict communication between subnets to prevent lateral movement. Monitor and Log Access: - Monitor access attempts to file shares, RDP, and remote network resources using SIEM tools. - Enable auditing and logging for successful and failed attempts to access restricted resources. *Tools for Implementation* File Share Management: - Microsoft Active Directory Group Policies - Samba (Linux/Unix file share management) - AccessEnum (Windows access auditing tool) Secure Remote Access: - Microsoft Remote Desktop Gateway - Apache Guacamole (open-source RDP/VNC gateway) - Zero Trust solutions: Tailscale, Cloudflare Zero Trust Service and Protocol Hardening: - Nmap or Nessus for network service discovery - Windows Group Policy Editor for disabling SMBv1, Telnet, and legacy protocols - iptables or firewalld (Linux) for blocking unnecessary traffic Network Segmentation: - pfSense for open-source network isolation.

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
- M1035: https://attack.mitre.org/mitigations/M1035
- Reviewed: 2026-10-27
