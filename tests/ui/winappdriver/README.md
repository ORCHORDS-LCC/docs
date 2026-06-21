---
title: "WinAppDriver UI Test Suite"
version: "1.0.0"
last-updated: "2026-06-21"
status: "review"
---

# WinAppDriver UI Test Suite

**Project:** ORCHORDS
**Owner:** ORCHORDS (QA Lead)
**Reviewers:** ORCHORDS (CTO), ORCHORDS (UI/UX Lead)
**Version:** 1.0.0
**Last Updated:** June 2026

---

## Overview

Automated UI tests for ORCHORDS using Microsoft WinAppDriver. These tests validate the desktop application's UI behavior, accessibility, and user workflows on Windows.

---

## Prerequisites

| Requirement | Version | Notes |
|---|---|---|
| Windows 10/11 | 1809+ | Developer Mode enabled |
| WinAppDriver | 1.2+ | [github.com/microsoft/WinAppDriver](https://github.com/microsoft/WinAppDriver) |
| .NET SDK | 6.0+ | For test runner |
| ORCHORDS | Latest build | Installed or portable |

---

## Setup Instructions

1. **Enable Developer Mode:** Settings → Update & Security → For developers → Developer Mode
2. **Install WinAppDriver:** Download and install from the GitHub releases page
3. **Start WinAppDriver:** Run C:\Program Files\Windows Application Driver\WinAppDriver.exe
4. **Build tests:** dotnet build tests/ui/winappdriver/ORCHORDS.UITests.csproj

---

## Running Tests

`ash
# Run all UI tests
dotnet test tests/ui/winappdriver/ --logger "console;verbosity=detailed"

# Run specific test category
dotnet test --filter "Category=Timeline"

# Run with screenshots on failure
dotnet test --settings tests/ui/winappdriver/runsettings.xml
`

---

## Test Structure

`
tests/ui/winappdriver/
├── ORCHORDS.UITests.csproj
├── runsettings.xml
├── Helpers/
│   ├── AppSession.cs          # App launch and session management
│   ├── ElementExtensions.cs   # Custom element helpers
│   └── ScreenshotCapture.cs   # Failure screenshot capture
├── Tests/
│   ├── LaunchTests.cs         # App startup and splash screen
│   ├── TimelineTests.cs       # Timeline panel interactions
│   ├── EffectsPanelTests.cs   # Effects panel drag-and-drop
│   ├── ExportTests.cs         # Export dialog workflows
│   ├── MenuTests.cs           # Menu navigation
│   └── AccessibilityTests.cs  # WCAG compliance checks
└── Screenshots/               # Failure screenshots (gitignored)
`

---

## CI Integration

- Tests run on the windows-ui runner (native Windows host, not Docker)
- WinAppDriver must be started before test execution
- Runner label: ui-tests:host
- Tests require a display — use the native desktop session, not headless

---

## Document Maintenance

### Change Log

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0.0 | June 2026 | ORCHORDS | Initial document creation |