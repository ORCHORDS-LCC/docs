# Firewall Disable Technique Platform Profile

## Reference

- Technique: **DC0043 — Firewall Disable**
- Platforms named in the source: not stated

The deactivation, misconfiguration, or complete stoppage of firewall services, either on a host or in a cloud control plane. Such activity may involve turning off firewalls, modifying rules to disable protection, or deleting firewall-related configurations and activity logs. Examples: - Disabling Host-Based Firewalls: Stopping the Windows Defender Firewall service or using `iptables -F` to flush all rules on a Linux system. - Cloud Firewall Modification or Deactivation: Modifying or deleting security group rules in AWS or disabling a network firewall in Azure. - Activity Log Deletion: Writing or deleting entries in Azure Firewall Activity Logs to hide unauthorized firewall changes. - Temporary Disable for Malicious Operations: Temporarily disabling a firewall to allow malicious files or traffic, then re-enabling it to avoid detection. - Using Command-Line Tools to Stop Firewalls: Running commands like `Set-NetFirewallProfile -Enabled False on Windows or systemctl stop ufw` on Linux. This data component can be collected through the following measures: Cloud Control Plane - Azure Activity Logs: - Enable logging of administrative actions, such as stopping or modifying Azure Firewall configurations. - Use Azure Monitor to track specific firewall-related actions, including disabling or rule deletion. - AWS CloudTrail Logs: - Monitor `RevokeSecurityGroupIngress` or `RevokeSecurityGroupEgress` events to detect rule changes in AWS Security Groups. - Google Cloud Platform Logs: - Collect logs from the Firewall Rules resource in Google Cloud Operations Suite to detect rule deletions or modifications. Host-Level Firewalls - Windows Firewall Event Logs: - Enable logging of firewall state changes: - Security Event ID 2004: Firewall service stopped. - Security Event ID 2005: Firewall service started. - Use Sysmon for process creation events tied to firewall commands or scripts (Sysmon Event ID 1). - Linux Firewall Logs: Use auditd to track commands like iptables, firewalld, or ufw: `auditctl -a always,exit -F arch=b64 -S execve -k firewall_disable` - macOS Firewall: Monitor changes to the macOS Application Firewall using the log show command. Network-Level Monitoring - IDS/IPS Alerts: Deploy IDS/IPS systems to monitor abnormal traffic flows that could indicate firewall disablement. - NetFlow Data: Analyze NetFlow or packet capture data for traffic patterns inconsistent with firewall enforcement. SIEM and CSPM Tools - SIEM Integration: Use tools like Splunk or QRadar to centralize and analyze firewall disablement events from both hosts and cloud platforms. - Cloud Security Posture Management (CSPM): Use CSPM solutions to monitor misconfigurations and track deactivation of critical cloud services like firewalls.

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
- DC0043: https://attack.mitre.org/datacomponents/DC0043
- Reviewed: 2026-10-27
