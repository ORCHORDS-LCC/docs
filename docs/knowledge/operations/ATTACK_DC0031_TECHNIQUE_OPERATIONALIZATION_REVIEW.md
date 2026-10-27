# Kernel Module Load Technique Operationalization Review

## Reference

- Technique: **DC0031 — Kernel Module Load**

The process of loading a kernel module into the operating system kernel. Kernel modules are object files that extend the kernel’s functionality, such as adding support for device drivers, new filesystems, or additional system calls. This action can be legitimate (e.g., loading a driver) or malicious (e.g., adding a rootkit). *Data Collection Measures:* - Linux: - Auditd: Enable auditing of kernel module loading. Example rule: `-a always,exit -F arch=b64 -S init_module,delete_module`. - Syslog: Monitor `/var/log/syslog` or `/var/log/messages` for entries related to kernel module loads. - Systemd Journal: Use `journalctl` to query logs for module loading events: `journalctl -k | grep "Loading kernel module"` - macOS: - Unified Logs: Use the `log` command to query kernel module events: `log show --predicate 'eventMessage contains "kextload"' --info` - Endpoint Security Framework (ESF): Monitor for `ES_EVENT_TYPE_AUTH_KEXTLOAD` (kernel extension loading events). - Kernel-Specific Tools: - Lsmod: Use `lsmod` to list loaded kernel modules in real-time. - Kprobe/eBPF: Use extended Berkeley Packet Filter (eBPF) or Kernel Probes (kprobes) to monitor kernel events, including module loading. Example using eBPF tools like BCC: `sudo python /path/to/bcc/tools/kprobe -v do_init_module` - Enable EDR Monitoring: - Configure alerts for: Suspicious kernel module loads from non-standard paths (e.g., /tmp). Unexpected or unsigned kernel modules. - Review detailed telemetry data provided by the EDR for insight into who initiated the module load, the file path, and whether the module was signed.

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
- DC0031: https://attack.mitre.org/datacomponents/DC0031
- Reviewed: 2026-10-27
