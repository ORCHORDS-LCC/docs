# T1543.002 Systemd Service Outcome Lesson

## Authoritative description

- Technique: **T1543.002 — Systemd Service**
- Tactics: persistence, privilege-escalation
- Platforms: Linux

Adversaries may create or modify systemd services to repeatedly execute malicious payloads as part of persistence. Systemd is a system and service manager commonly used for managing background daemon processes (also known as services) and other system resources. Systemd is the default initialization (init) system on many Linux distributions replacing legacy init systems, including SysVinit and Upstart, while remaining backwards compatible. Systemd utilizes unit configuration files with the `.service` file extension to encode information about a service's process. By default, system level unit files are stored in the `/systemd/system` directory of the root owned directories (`/`). User level unit files are stored in the `/systemd/user` directories of the user owned directories (`$HOME`). Inside the `.service` unit files, the following directives are used to execute commands: * `ExecStart`, `ExecStartPre`, and `ExecStartPost` directives execute when a service is started manually by `systemctl` or on system start if the service is set to automatically start. * `ExecReload` directive executes when a service restarts. * `ExecStop`, `ExecStopPre`, and `ExecStopPost` directives execute when a service is stopped. Adversaries have created new service files, altered the commands a `.service` file’s directive executes, and modified the user directive a `.service` file executes as, which could result in privilege escalation. Adversaries may also place symbolic links in these directories, enabling systemd to find these payloads regardless of where they reside on the filesystem. The `.service` file’s User directive can be used to run service as a specific user, which could result in privilege escalation based on specific user/group permissions. Systemd services can be created via systemd generators, which support the dynamic generation of unit files. Systemd generators are small executables that run during boot or configuration reloads to dynamically create or modify systemd unit files by converting non-native configurations into services, symlinks, or drop-ins (i.e., Boot or Logon Initialization Scripts).

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
- T1543.002: https://attack.mitre.org/techniques/T1543/002
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
