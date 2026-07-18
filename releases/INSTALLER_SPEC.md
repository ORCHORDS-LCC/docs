---
title: "Installer Specification"
version: "1.0.0"
last-updated: "2026-06-21"
status: "review"
---

# Installer Specification

**Project:** ORCHORDS  
**Owner:** ORCHORDS (Build & Release Engineer)  
**Reviewers:** ORCHORDS (CTO), ORCHORDS (DevOps)  
**ISO Standards:** ISO/IEC 12207:2017 (transition, development), ISO/IEC 25010:2023 (installability, portability)  
**Version:** 1.0.0  
**Last Updated:** June 2026  

---


## Scope & Audience

| Aspect | Definition |
|---|---|
| **Scope** | Inno Setup installer, features, and upgrade behavior |
| **Diátaxis form** | Reference |
| **Primary audience** | ORCHORDS, ORCHORDS, QA team |
| **Secondary audience** | Future maintainers and reviewers of this document |


---

## Overview

This document defines the ORCHORDS installer for Windows. Per **ISO/IEC 12207:2017 §6.4**, the transition process includes packaging and distribution. The installer must be reliable, secure, and user-friendly. It must also satisfy **ISO/IEC 25010:2023**'s installability and portability characteristics.
## Contents

- [Technology](#technology)
- [Installer Features](#installer-features)
  - [1. Welcome Screen](#1-welcome-screen)
  - [2. License Agreement](#2-license-agreement)
  - [3. Component Selection](#3-component-selection)
  - [4. Installation Location](#4-installation-location)
  - [5. Additional Tasks](#5-additional-tasks)
  - [6. Installing Screen](#6-installing-screen)
  - [7. Completion Screen](#7-completion-screen)
- [Inno Setup Script Structure](#inno-setup-script-structure)
- [Installation Artifacts](#installation-artifacts)
- [File Associations](#file-associations)
- [Upgrade & Uninstall Behavior](#upgrade-uninstall-behavior)
  - [Upgrade from Previous Version](#upgrade-from-previous-version)
  - [Uninstall](#uninstall)
- [Code Signing](#code-signing)
- [Testing Checklist](#testing-checklist)
- [Version History](#version-history)
  - [Change Log](#change-log)
  - [Review Cadence](#review-cadence)

---

## Technology

| Component | Technology |
|---|---|
| Installer | Inno Setup 6.x |
| Script | `installer/docs-setup.iss` |
| Output | `ORCHORDSSetup.exe` (signed) |
| Target OS | Windows 10 (1903+) and Windows 11 |
| Architecture | x64 only |

---

## Installer Features

### 1. Welcome Screen

| Element | Content |
|---|---|
| Title | "ORCHORDS Setup" |
| Product name | "ORCHORDS vX.Y.Z" |
| Company | "ORCHORDS" |
| Icon | ORCHORDS logo |

### 2. License Agreement

- Full MIT license text (or EULA)
- "I accept" / "I do not accept" radio buttons

### 3. Component Selection

| Component | Default | Size | Notes |
|---|---|---|---|
| **ORCHORDS Core** | Required | ~150 MB | Main application |
| **Codecs** | Required | ~80 MB | FFmpeg, hardware codecs |
| **Effects & Templates** | Default | ~50 MB | Built-in effects, title templates |
| **VST Support** | Default | ~10 MB | VST plugin hosting |
| **Documentation** | Optional | ~20 MB | User guide, tutorials |
| **Desktop Shortcut** | Optional | — | Shortcut on desktop |
| **Start Menu Shortcut** | Optional | — | Shortcut in Start Menu |

### 4. Installation Location

| Location | Default |
|---|---|
| Program Files | `%PROGRAMFILES%\ORCHORDS\` |
| AppData | `%APPDATA%\ORCHORDS\ORCHORDS\` |
| Temp files | `%TEMP%\ORCHORDSSetup\` |

### 5. Additional Tasks

- [ ] Create desktop shortcut
- [ ] Create Start Menu shortcut
- [ ] Launch ORCHORDS after installation
- [ ] Create file association for `.orchords` project files

### 6. Installing Screen

| Feature | Implementation |
|---|---|
| Progress bar | Inno Setup built-in |
| File extraction progress | Inno Setup built-in |
| Custom branding | ORCHORDS banner image |

### 7. Completion Screen

- "Installation complete" message
- "Launch ORCHORDS now" checkbox (default: checked)
- "View release notes" link

---

## Inno Setup Script Structure

```pascal
[Setup]
AppName=ORCHORDS
AppVersion={#Version}
AppPublisher=ORCHORDS
AppPublisherURL=https://www.orchords.com
DefaultDirName={autopf}\ORCHORDS
DefaultGroupName=ORCHORDS
OutputBaseFilename=ORCHORDSSetup-{#Version}
Compression=lzma2/ultra64
SolidCompression=yes

[Files]
Source: "..\build\Release\ORCHORDS.exe"; DestDir: "{app}"
Source: "..\build\Release\ORCHORDSEngine.dll"; DestDir: "{app}"
Source: "..\build\Release\*.dll"; DestDir: "{app}"; Flags: recursesubdirs

[Icons]
Name: "{group}\ORCHORDS"; Filename: "{app}\ORCHORDS.exe"
Name: "{autodesktop}\ORCHORDS"; Filename: "{app}\ORCHORDS.exe"

[Registry]
Root: HKCR; Subkey: ".orchords"; ValueType: string; ValueData: "ORCHORDS.Project"
Root: HKCR; Subkey: "ORCHORDS.Project\shell\open\command"; ValueType: string; ValueData: "{app}\ORCHORDS.exe ""%1"""
```

---

## Installation Artifacts

| Artifact | Location | Signed? |
|---|---|---|
| `ORCHORDSSetup.exe` | CI artifact | ✅ (required) |
| `ORCHORDS.zip` (portable) | CI artifact | ❌ (no installer needed) |
| `ORCHORDS.pdb` (symbols) | CI artifact | ❌ (internal use) |
| `ORCHORDS.swidtag` | Inside installer | ✅ (part of installer) |

---

## File Associations

| Extension | Associated Action | Description |
|---|---|---|
| `.orchords` | Open with ORCHORDS | ORCHORDS project file |
| `.orchords-template` | Open with ORCHORDS | Project template file |

---

## Upgrade & Uninstall Behavior

### Upgrade from Previous Version

| Scenario | Behavior |
|---|---|
| Same version | "Already installed" — repair or uninstall options |
| Newer version | Upgrade — preserves settings, projects, plugins |
| Older version | Downgrade blocked — requires uninstall first |
| Install over existing | Clean install — old files removed |

### Uninstall

| Behavior | Detail |
|---|---|
| Remove program files | All files in `%PROGRAMFILES%\ORCHORDS\` |
| Remove AppData | `%APPDATA%\ORCHORDS\ORCHORDS\` (prompt user) |
| Remove registry entries | File associations, uninstall entry |
| Preserve projects | `%USERPROFILE%\Documents\ORCHORDS\` never removed |
| Leave shortcut | Removed (Start Menu and Desktop) |

---

## Code Signing

The installer **must be signed** before distribution. See [`CODE_SIGNING_CERTIFICATE_MANAGEMENT.md`](./CODE_SIGNING_CERTIFICATE_MANAGEMENT.md) for the signing process.

Unsigned installers trigger Windows SmartScreen warnings. Signed installers pass SmartScreen within ~1,000–5,000 installs.

---

## Testing Checklist

Before every release:

- [ ] Fresh install on Windows 10 (1903+)
- [ ] Fresh install on Windows 11
- [ ] Upgrade from previous version
- [ ] Uninstall → clean reinstall
- [ ] Verify all components installed
- [ ] Verify file associations work
- [ ] Verify SmartScreen doesn't block (or verify signed)
- [ ] Verify app launches after install
- [ ] Verify all shortcuts work
- [ ] Verify no leftover files after uninstall
- [ ] Verify installer size is reasonable (< 500 MB)

---

## Version History

| Version | Date | Changes |
|---|---|---|
| 1.0.0 | June 2026 | Initial spec — aligned with ISO/IEC 12207:2017 §6.4 and ISO/IEC 25010:2023 |

---

*Grounded in: ISO/IEC 12207:2017 §6.4 (Transition), ISO/IEC 25010:2023 (Installability, Portability)*



---

## References

### Internal Documents

- [$title](././CODE_SIGNING_CERTIFICATE_MANAGEMENT.md)

### Standards & Frameworks

- ISO/IEC 12207:2017 (Systems and software engineering — Software life cycle processes)
- ISO/IEC 25010:2023 (Systems and software engineering — Quality requirements and evaluation)
- See [STYLE_GUIDE.md](./STYLE_GUIDE.md) for the full standards catalog

---

## Document Maintenance

### Change Log

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0.0 | June 2026 | ORCHORDS | Initial version |
| 1.0.1 | June 2026 | ORCHORDS | Added Scope & Audience block and Document Maintenance section per STYLE_GUIDE.md (ISO/IEC/IEEE 82079-1:2019 compliance) |

### Review Cadence

- **Next review:** On each installer major change
- **Reviewer:** ORCHORDS (Build & Release Engineer)
- **Cadence:** Per STYLE_GUIDE.md defaults for this document type