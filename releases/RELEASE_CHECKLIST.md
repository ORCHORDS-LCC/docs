---
title: "Release Checklist"
version: "1.0.0"
last-updated: "2026-06-21"
status: "review"
---

# Release Checklist

**Project:** ORCHORDS  
**Owner:** ORCHORDS (Build & Release Engineer)  
**Reviewers:** ORCHORDS (DevOps Lead), ORCHORDS (QA Lead)  
**ISO Standards:** ISO/IEC 12207:2017 (transition), ISO/IEC 25010:2023 (functional suitability)  
**Version:** 1.0.0  
**Last Updated:** June 2026  

---


## Scope & Audience

| Aspect | Definition |
|---|---|
| **Scope** | Pre-release, release-day, and post-release checklists |
| **Diátaxis form** | How-to guide |
| **Primary audience** | ORCHORDS, ORCHORDS, ORCHORDS, ORCHORDS |
| **Secondary audience** | Future maintainers and reviewers of this document |


---

## Overview

This checklist defines every step required to ship a ORCHORDS release. Per **ISO/IEC 12207:2017 section 6.4**, transition is a controlled process -- skipping a step is not acceptable for any release, no matter how small.
## Contents

- [Pre-Release (1 Week Before)](#pre-release-1-week-before)
  - [Feature Freeze](#feature-freeze)
  - [QA Sign-Off](#qa-sign-off)
  - [Build Preparation](#build-preparation)
- [Release Day](#release-day)
  - [Build Release Candidate](#build-release-candidate)
  - [Sign Artifacts](#sign-artifacts)
  - [Final Smoke Test](#final-smoke-test)
  - [Publish](#publish)
- [Post-Release (Within 48 Hours)](#post-release-within-48-hours)
  - [Monitoring](#monitoring)
  - [Communication](#communication)
- [Hotfix Checklist](#hotfix-checklist)
- [Version History](#version-history)
  - [Change Log](#change-log)
  - [Review Cadence](#review-cadence)

---

## Pre-Release (1 Week Before)

### Feature Freeze

- [ ] **ORCHORDS confirms** all features for this release are complete and merged
- [ ] No new feature PRs merged after freeze (only bug fixes)
- [ ] `main` branch is at the feature-complete commit
- [ ] Feature freeze announced in #engineering Slack

### QA Sign-Off

- [ ] **ORCHORDS runs** the full test suite (unit + integration + smoke + regression)
- [ ] All tests pass on the feature-complete commit
- [ ] Performance benchmarks meet targets in [`PERFORMANCE_BENCHMARKS.md`](../PERFORMANCE_BENCHMARKS.md)
- [ ] Accessibility audit passes (WCAG 2.1 AA) per [`ACCESSIBILITY_COMPLIANCE.md`](../ACCESSIBILITY_COMPLIANCE.md)
- [ ] Beta testers validated the release candidate (if applicable)
- [ ] Known issues documented in release notes

### Build Preparation

- [ ] **ORCHORDS updates** `CMakeLists.txt` version to `X.Y.Z`
- [ ] **ORCHORDS updates** `CHANGELOG.md` with all changes since last release
- [ ] **ORCHORDS writes** release notes (see [`CHANGELOG_POLICY.md`](./CHANGELOG_POLICY.md))
- [ ] **ORCHORDS prepares** Store screenshots and descriptions
- [ ] **ORCHORDS verifies** code signing certificate is not expiring within 30 days
- [ ] **ORCHORDS updates** SWID tag data (see [`SWID_TAG_SPEC.md`](./SWID_TAG_SPEC.md))

---

## Release Day

### Build Release Candidate

- [ ] **ORCHORDS creates** release tag on the frozen `main` commit:
  ```bash
  git tag vX.Y.Z
  git push origin vX.Y.Z
  ```
- [ ] Forgejo Actions release workflow runs (GitHub Actions–compatible); builds complete on all platforms
- [ ] Artifacts verified: `ORCHORDSSetup.exe`, `ORCHORDS.zip`, `ORCHORDS.pdb`, `ORCHORDS.swidtag`

### Sign Artifacts

- [ ] **ORCHORDS signs** all executables and installer (Azure Artifact Signing)
- [ ] Signature verified: `signtool verify /pa ORCHORDSSetup.exe`
- [ ] SmartScreen reputation check on signed installer (if new certificate)

### Final Smoke Test

- [ ] **ORCHORDS tests** on clean Windows 10 VM:
  - [ ] Fresh install from `ORCHORDSSetup.exe`
  - [ ] Application launches
  - [ ] New project → import media → export → verify output file
- [ ] **ORCHORDS tests** on clean Windows 11 VM (same steps)
- [ ] **ORCHORDS tests** upgrade install from previous version
- [ ] All smoke tests pass

### Publish

- [ ] **ORCHORDS uploads** signed artifacts to GitHub Releases with release notes
- [ ] **ORCHORDS submits** to Microsoft Store (if this release goes to Store)
- [ ] **ORCHORDS publishes** announcement to community channels
- [ ] **ORCHORDS updates** download page on website
- [ ] **ORCHORDS sends** email to beta testers
- [ ] **ORCHORDS updates** social media
- [ ] **ORCHORDS closes** the release in Linear

---

## Post-Release (Within 48 Hours)

### Monitoring

- [ ] **ORCHORDS monitors** crash reports in Firebase Crashlytics
- [ ] **ORCHORDS monitors** Store submission status (if applicable)
- [ ] **ORCHORDS monitors** community feedback for critical issues
- [ ] **ORCHORDS monitors** download/install metrics

### Communication

- [ ] **ORCHORDS writes** launch summary for team (what shipped, metrics so far)
- [ ] **ORCHORDS schedules** post-release retrospective (within 2 weeks)

---

## Hotfix Checklist

For a critical bug (S0 severity) that requires an immediate patch release:

- [ ] Hotfix branch created from the release tag (`hotfix/description`)
- [ ] Fix implemented and tested
- [ ] ORCHORDS signs off on hotfix
- [ ] ORCHORDS builds, signs, and tests hotfix installer
- [ ] Hotfix tagged and released
- [ ] Incident report filed (see [`engineering/BACKUP_DISASTER_RECOVERY.md`](../engineering/BACKUP_DISASTER_RECOVERY.md))
- [ ] Post-incident review scheduled

---

## Version History

| Version | Date | Changes |
|---|---|---|
| 1.0.0 | June 2026 | Initial checklist — aligned with ISO/IEC 12207:2017 §6.4 |

---

*Grounded in: ISO/IEC 12207:2017 §6.4 (Transition Process), ISO/IEC 25010:2023 (Functional Suitability)*



---

## References

### Internal Documents

- [$title](./../PERFORMANCE_BENCHMARKS.md)
- [$title](././CHANGELOG_POLICY.md)
- [$title](././SWID_TAG_SPEC.md)
- [$title](./../ACCESSIBILITY_COMPLIANCE.md)

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

- **Next review:** On each release
- **Reviewer:** ORCHORDS (Build & Release Engineer)
- **Cadence:** Per STYLE_GUIDE.md defaults for this document type