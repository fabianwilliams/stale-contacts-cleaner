# Building Stale Contacts Cleaner: From Idea to App Store in One Day

**Published:** February 7, 2026
**Author:** Fabian Williams, Adotob LLC
**App Status:** Submitted to Apple App Store, Awaiting Review

---

## Introduction

This article documents the development journey of Stale Contacts Cleaner, a privacy-first iOS app that went from initial concept to App Store submission in approximately 8 hours of focused work.

---

## The Problem

After years of using an iPhone, contact lists become cluttered with:

- Old contacts from previous jobs
- Duplicates from merged accounts
- People not contacted in years
- Outdated business contacts

Existing solutions either required cloud sync (privacy concerns) or had confusing interfaces.

---

## The Solution

**Stale Contacts Cleaner** provides an intuitive swipe interface for quickly reviewing and cleaning contacts:

- **Right swipe** - Keep contact
- **Left swipe** - Mark for deletion
- **Batch deletion** - Review before permanent removal
- **100% private** - All processing happens on device

---

## Development Timeline

| Phase | Duration | Key Deliverables |
|-------|----------|------------------|
| **Foundation** | 2 hours | Project setup, Contacts integration, MVVM architecture |
| **Core Features** | 2 hours | Swipe interface, contact cards, actions |
| **Polish** | 2 hours | Animations, progress tracking, alphabetical navigation |
| **Testing** | 1 hour | Real device testing, bug fixes |
| **Assets** | 0.25 hours | App icons (all iOS sizes) |
| **Submission** | 1.5 hours | Screenshots, marketing copy, App Store Connect |
| **Total** | **8 hours** | Production-ready app submitted to Apple |

---

## Technical Stack

| Component | Technology |
|-----------|------------|
| **Language** | Swift 6.0 |
| **UI Framework** | SwiftUI |
| **Architecture** | MVVM |
| **Minimum iOS** | 18.0+ |
| **Dependencies** | None (native iOS only) |
| **Data Storage** | UserDefaults, iOS Contacts |

---

## Key Features

### Privacy First

All contact processing happens entirely on device. The app:

- Does not collect any data
- Does not transmit data to external servers
- Does not use analytics or tracking
- Does not require an account
- Does not use third-party services

### Intuitive Interface

Familiar swipe gestures make the app immediately usable without tutorial or instructions.

### Alphabetical Navigation

Jump to any letter in your contact list instantly, saving time when reviewing hundreds of contacts.

### Undo Support

Made a mistake? Undo immediately before final deletion.

### Batch Operations

Review all marked contacts before permanent deletion. Final confirmation required.

---

## Development Approach

### Methodology

The project used a combination of:

1. **Clear requirements** - Well-defined problem and solution
2. **Iterative development** - Build, test, refine in small increments
3. **Quality gates** - Each phase must work before moving forward
4. **Real device testing** - Physical iPhone testing caught issues simulators missed
5. **Strategic decisions** - Human judgment on product direction

### AI-Augmented Development

Modern AI tools assisted with:

- **Code generation** - Rapid implementation of UI components and logic
- **Asset creation** - App icons generated and automatically resized
- **Documentation** - Comprehensive guides and marketing copy
- **Problem solving** - Quick debugging and issue resolution

Human contribution focused on:

- **Strategic decisions** - Product direction, feature prioritization
- **Quality validation** - Testing, bug discovery, UX refinement
- **Platform expertise** - App Store requirements, compliance questions

---

## Challenges and Solutions

### Challenge 1: Alphabetical Navigation Bug

**Issue:** Jump feature searched by first name while contacts were sorted by last name.

**Discovery:** Real device testing with actual contact list.

**Resolution:** Aligned both search and sort to use last name consistently.

**Lesson:** Real device testing is critical for finding user-facing issues.

### Challenge 2: App Store Screenshot Requirements

**Issue:** Multiple dimension mismatches with Apple's exact requirements.

**Resolution:** Automated resizing to exact specifications (1284 x 2778 for iPhone, 2732 x 2048 for iPad).

**Lesson:** Apple's submission requirements are strict but well-documented.

### Challenge 3: Export Compliance

**Issue:** App Store requires declaration about encryption usage.

**Resolution:** Confirmed app uses only standard iOS encryption (HTTPS), no custom cryptography.

**Lesson:** Understanding platform requirements prevents submission delays.

---

## Metrics and Results

### Time Investment

| Activity | Traditional Estimate | Actual Time | Efficiency Gain |
|----------|---------------------|-------------|-----------------|
| Development | 12-16 hours | 6 hours | 62% |
| Assets & Branding | 3-4 hours | 0.25 hours | 94% |
| Documentation | 2-3 hours | 0.5 hours | 80% |
| Submission | 2-3 hours | 1.5 hours | 40% |
| **Total** | **19-26 hours** | **8 hours** | **69%** |

### Code Metrics

| Metric | Value |
|--------|-------|
| Lines of Code | ~2,500 |
| Swift Files | 15 |
| External Dependencies | 0 |
| Third-Party SDKs | 0 |
| Crashes in Testing | 0 |

---

## Strategic Decisions

### Decision: Skip TestFlight Beta

**Rationale:**
- TestFlight adds friction (invitations, separate app download)
- App is simple with clear functionality
- Real device testing already completed
- Direct App Store submission provides professional presence from launch

**Result:** Faster time to market, lower user friction.

### Decision: Zero Data Collection

**Rationale:**
- Contacts are sensitive personal data
- On-device processing simpler and more secure
- Builds user trust
- Eliminates server costs and compliance overhead

**Result:** Simplified privacy declaration, differentiation from competitors.

### Decision: Free Pricing

**Rationale:**
- Maximize adoption for initial launch
- Build user base and gather feedback
- Demonstrate capability

**Result:** Broader market appeal, simpler App Store approval.

---

## Architecture Overview

### MVVM Pattern

```
View (SwiftUI)
    ↓
ViewModel (ObservableObject)
    ↓
Model (Data) + Services (Business Logic)
    ↓
iOS Contacts Framework
```

**Views:**
- ContentView - App entry point and navigation
- SwipeView - Main swipe interface
- ContactCardView - Individual contact display
- SettingsView - App preferences

**ViewModels:**
- SwipeViewModel - Swipe interface state and logic

**Services:**
- ContactsManager - iOS Contacts framework integration
- ContactActionService - Deletion queue and undo management

**Models:**
- ReviewableContact - Contact data wrapper

---

## Lessons Learned

### 1. Real Device Testing is Non-Negotiable

Simulators cannot replicate all real-world conditions. Physical device testing caught a navigation bug that would have impacted user experience.

### 2. Privacy Simplifies Architecture

Zero data collection eliminated need for:
- Backend servers
- Database design
- API development
- Authentication system
- Privacy compliance overhead

### 3. Modern Tools Enable Rapid Development

Combination of:
- Declarative UI (SwiftUI)
- Modern language features (Swift 6.0)
- AI-assisted development
- Automated asset generation

Together these compressed timeline by approximately 70%.

### 4. Clear Requirements Enable Fast Execution

Well-defined problem and solution eliminated ambiguity and enabled focused implementation.

---

## What's Next

### Immediate (1-3 days)

Awaiting Apple App Review. Typical review time is 1-3 days.

### Short-Term

Post-launch monitoring and iteration:
- User feedback via GitHub issues
- Bug fixes if needed
- Feature requests consideration

### Long-Term Possibilities

If user adoption is strong:
- Smart suggestions using on-device ML
- Duplicate detection and merging
- Export functionality for backups
- Premium features (optional)

---

## Technical Implementation Details

### Contacts Permission Flow

```swift
1. App requests Contacts permission on first launch
2. User grants or denies access
3. If granted: Load contacts for review
4. If denied: Show explanation and settings link
```

### Deletion Architecture

```swift
1. User swipes left → Contact marked for deletion (in memory)
2. User continues reviewing → State persisted locally
3. User taps "Done" → Review screen shows marked contacts
4. User confirms → Batch deletion via CNSaveRequest
5. Success → Contacts removed from iOS Contacts
```

All operations are atomic - either all deletions succeed or none occur.

### Performance Considerations

- Contact loading: Asynchronous to prevent UI blocking
- Image loading: Lazy with placeholder for missing photos
- State management: Efficient SwiftUI @Published properties
- Memory: Contact objects released after review

---

## Conclusion

Stale Contacts Cleaner demonstrates that production-quality iOS apps can be developed and submitted in remarkably compressed timeframes when combining:

1. Clear requirements and focused scope
2. Modern development tools and frameworks
3. AI-augmented implementation
4. Strategic human decision-making
5. Rigorous quality validation

The 8-hour timeline from idea to App Store submission represents a significant compression compared to traditional development timelines, while maintaining production quality standards.

---

## Resources

**Public Repository:** [github.com/fabianwilliams/stale-contacts-cleaner](https://github.com/fabianwilliams/stale-contacts-cleaner)

**Privacy Policy:** [View Privacy Policy](./PRIVACY.md)

**Issue Tracking:** [GitHub Issues](https://github.com/fabianwilliams/stale-contacts-cleaner/issues)

**Support:** support@adotob.com

---

**Status:** Submitted to Apple App Store on February 7, 2026 at 8:56 PM
**Submission ID:** 52f8b783-cec7-4497-b3b5-642296c7694c
**Expected Review:** 1-3 days

---

*This article documents a real development project. All metrics and timelines are accurate.*
