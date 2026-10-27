# T1546.004 Unix Shell Configuration Modification Outcome Lesson

## Authoritative description

- Technique: **T1546.004 — Unix Shell Configuration Modification**
- Tactics: privilege-escalation, persistence
- Platforms: Linux, macOS

Adversaries may establish persistence through executing malicious commands triggered by a user’s shell. User Unix Shells execute several configuration scripts at different points throughout the session based on events. For example, when a user opens a command-line interface or remotely logs in (such as via SSH) a login shell is initiated. The login shell executes scripts from the system (<code>/etc</code>) and the user’s home directory (<code>~/</code>) to configure the environment. All login shells on a system use /etc/profile when initiated. These configuration scripts run at the permission level of their directory and are often used to set environment variables, create aliases, and customize the user’s environment. When the shell exits or terminates, additional shell scripts are executed to ensure the shell exits appropriately. Adversaries may attempt to establish persistence by inserting commands into scripts automatically executed by shells. Using bash as an example, the default shell for most GNU/Linux systems, adversaries may add commands that launch malicious binaries into the <code>/etc/profile</code> and <code>/etc/profile.d</code> files. These files typically require root permissions to modify and are executed each time any shell on a system launches. For user level permissions, adversaries can insert malicious commands into <code>~/.bash_profile</code>, <code>~/.bash_login</code>, or <code>~/.profile</code> which are sourced when a user opens a command-line interface or connects remotely. Since the system only executes the first existing file in the listed order, adversaries have used <code>~/.bash_profile</code> to ensure execution. Adversaries have also leveraged the <code>~/.bashrc</code> file which is additionally executed if the connection is established remotely or an additional interactive shell is opened, such as a new tab in the command-line interface. Some malware targets the termination of a program to trigger execution, adversaries can use the <code>~/.bash_logout</code> file to execute malicious commands at the end of a session. For macOS, the functionality of this technique is similar but may leverage zsh, the default shell for macOS 10.15+. When the Terminal.app is opened, the application launches a zsh login shell and a zsh interactive shell. The login shell configures the system environment using <code>/etc/profile</code>, <code>/etc/zshenv</code>, <code>/etc/zprofile</code>, and <code>/etc/zlogin</code>. The login shell then configures the user environment with <code>~/.zprofile</code> and <code>~/.zlogin</code>. The interactive shell uses the <code>~/.zshrc</code> to configure the user environment. Upon exiting, <code>/etc/zlogout</code> and <code>~/.zlogout</code> are executed. For legacy programs, macOS executes <code>/etc/bashrc</code> on startup.

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
- T1546.004: https://attack.mitre.org/techniques/T1546/004
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
