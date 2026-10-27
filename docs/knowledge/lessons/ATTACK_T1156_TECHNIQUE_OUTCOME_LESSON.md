# T1156 Malicious Shell Modification Outcome Lesson

## Authoritative description

- Technique: **T1156 — Malicious Shell Modification**
- Tactics: persistence
- Platforms: Linux, macOS

Adversaries may establish persistence through executing malicious commands triggered by a user’s shell. User shells execute several configuration scripts at different points throughout the session based on events. For example, when a user opens a command line interface or remotely logs in (such as SSH) a login shell is initiated. The login shell executes scripts from the system (/etc) and the user’s home directory (~/) to configure the environment. All login shells on a system use /etc/profile when initiated. These configuration scripts run at the permission level of their directory and are often used to set environment variables, create aliases, and customize the user’s environment. When the shell exits or terminates, additional shell scripts are executed to ensure the shell exits appropriately. Adversaries may attempt to establish persistence by inserting commands into scripts automatically executed by shells. Using bash as an example, the default shell for most GNU/Linux systems, adversaries may add commands that launch malicious binaries into the /etc/profile and /etc/profile.d files . These files require root permissions and are executed each time any shell on a system launches. For user level permissions, adversaries can insert malicious commands into ~/.bash_profile, ~/.bash_login, or ~/.profile (Rocke) which are sourced when a user opens a command line interface or connects remotely. Adversaries often use ~/.bash_profile since the system only executes the first file that exists in the listed order. Adversaries have also leveraged the ~/.bashrc file (Tsunami, Rocke, Linux Rabbit, Magento) which is additionally executed if the connection is established remotely or an additional interactive shell is opened, such as a new tab in the command line interface. Some malware targets the termination of a program to trigger execution (Cannon), adversaries can use the ~/.bash_logout file to execute malicious commands at the end of a session(Pearl_shellbot). For macOS, the functionality of this technique is similar but leverages zsh, the default shell for macOS 10.15+. When the Terminal.app is opened, the application launches a zsh login shell and a zsh interactive shell. The login shell configures the system environment using /etc/profile, /etc/zshenv, /etc/zprofile, and /etc/zlogin. The login shell then configures the user environment with ~/.zprofile and ~/.zlogin. The interactive shell uses the ~/.zshrc to configure the user environment. Upon exiting, /etc/zlogout and ~/.zlogout are executed. For legacy programs, macOS executes /etc/bashrc on startup.

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
- T1156: https://attack.mitre.org/techniques/T1156
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
