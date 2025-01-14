
The Da Vinci Unsolicited Notifications Implementation Guide was supported by the [Da Vinci] initiative.

### Version {{site.data.ig.version}}

- Publication Date: 2025-1-15
- url: <https://hl7.org/fhir/us/davinci-alerts/STU1.1/>
- Based on FHIR version : 4.0.1

#### What's new in Version {{site.data.ig.version}} of Da Vinci Unsolicited Notifications:

This STU Update of the Da Vinci Unsolicited Notifications Implementation Guide is the third published version of this guide. The sponsoring HL7 International/Infrastructure And Messaging Work Group members agreed to and voted on the resolution of the community review comments and edits to this guide. There are no updates from the 1.1.0-preview version. For a detailed list of the changes for previous versions, see the 1.1.0-preview version below.

### Version 1.1.0-preview

- Publication Date: 2024-12-11
- url: <https://hl7.org/fhir/us/davinci-alerts/STU1.1-snapshot/>
- Based on FHIR version : 4.0.1

#### What's new in Version 1.1.0-preview of Da Vinci Unsolicited Notifications:

{% include whats-new-1.1.0-snapshot.md %}

#### Updates and Corrected Errata in Version 1.1.0-preview:

**Tracker Status**: **Summary** **Jira Issue** **Link to Updated Content**

1. **Applied**: Update security page [FHIR-26135](https://jira.hl7.org/browse/FHIR-26135) See change [Here](security.html)
2. **Applied**: Question on Bundle Size [FHIR-26173](https://jira.hl7.org/browse/FHIR-26173) See change [Here](guidance.html#what-is-in-the-message-bundle)
3. **Applied**: Add Device as sender and author in MessageHeader [FHIR-26209](https://jira.hl7.org/browse/FHIR-26209) See changes [Here](StructureDefinition-notifications-messageheader.html) and [Here](Bundle-admit-notification-message-bundle-02.html)
4. **Applied**: Clarify terminology migration plans [FHIR-26226](https://jira.hl7.org/browse/FHIR-26226) See change [Here](artifacts.html#4)
5. **Applied**: Correct Transfer-notification-messageheader profile name [FHIR-29684](https://jira.hl7.org/browse/FHIR-29684) See change [Here](StructureDefinition-transfer-notification-messageheader.html)
6. **Applied**: Use realistic NPI format for Practitioner example [FHIR-37495](https://jira.hl7.org/browse/FHIR-37495) See change [Here](Bundle-admit-notification-message-bundle-01.html)
7. **Applied**: Consideration of FAST's Hybrid Intermediary IG [FHIR-38032](https://jira.hl7.org/browse/FHIR-38032) See change [Here](roles.html)
8. **Applied**: Clarify that request is an event [FHIR-39546](https://jira.hl7.org/browse/FHIR-39546) See changes [Here](scope.html) and [Here](roles.html)
9. **Applied**: Fix typo and add links [FHIR-39548](https://jira.hl7.org/browse/FHIR-39548) See change [Here](guidance.html#formally-defining-the-da-vinci-notification-message)
10. **Applied**: Define Acronym HIN [FHIR-39547](https://jira.hl7.org/browse/FHIR-39547) See change [Here](roles.html)
11. **Applied**: Copy editing changes prior to comment period to ensure accuracy, clarity, and readability. [FHIR-48964](https://jira.hl7.org/browse/FHIR-48964)
11.  **Applied**: Technical QA changes change to examples and conformance artifacts to meet the ig publication validation rules [FHIR-48966](https://jira.hl7.org/browse/FHIR-48966)
12. **Applied**: Alignment with Proposed Da Vinci standard pages/menu items. [FHIR-48965](https://jira.hl7.org/browse/FHIR-48965) For example see changes [Here](index.html#how-to-read-this-guide)
13. **Applied**: Supports US-Core 3.1.1, 6.1.0, and 7.0.0 [FHIR-48963](https://jira.hl7.org/browse/FHIR-48963)

### Version 1.0.0

- Publication Date: 2020-10-15
- url: <https://hl7.org/fhir/us/davinci-alerts/STU1/>
- Based on FHIR version : 4.0.1

The first official published version of the Da Vinci Unsolicited Notifications IG for FHIR R4.

1. Applied all resolutions from STU1 Ballot

  1. Various Technical Corrections and corrections to typographical errors and grammar.
  1. Update and correct examples
  1. Remove MessageDefintion and GraphDefinition profile and references to them ([FHIR-26130](https://jira.hl7.org/browse/FHIR-26130), [FHIR-26106](https://jira.hl7.org/browse/FHIR-26106)).
  1. Update Guidance on [Errors and ReliableDeliver](https://hl7.org/fhir/us/davinci-alerts/STU1/guidance.html#reliable-delivery) ([FHIR-26165](https://jira.hl7.org/browse/FHIR-26165), [FHIR-26201](https://jira.hl7.org/browse/FHIR-26201) [FHIR-26285](https://jira.hl7.org/browse/FHIR-26285),[FHIR-26190](https://jira.hl7.org/browse/FHIR-26190),[FHIR-26176](https://jira.hl7.org/browse/FHIR-26176)).
  1. Update [Scope and Usage](https://hl7.org/fhir/us/davinci-alerts/STU1/index.html#scope-and-usage)([FHIR-26200](https://jira.hl7.org/browse/FHIR-26200), [FHIR-26182](https://jira.hl7.org/browse/FHIR-26182) #[FHIR-26132](https://jira.hl7.org/browse/FHIR-26132),#[FHIR-26129](https://jira.hl7.org/browse/FHIR-26129),[FHIR-26184](https://jira.hl7.org/browse/FHIR-26184)).
  1. Update [Precondition and Assumption](https://hl7.org/fhir/us/davinci-alerts/STU1/guidance.html#preconditions-and-assumptions)([FHIR-26200](https://jira.hl7.org/browse/FHIR-26200),#[FHIR-26132](https://jira.hl7.org/browse/FHIR-26132) #[FHIR-26129](https://jira.hl7.org/browse/FHIR-26129),#[FHIR-26117](https://jira.hl7.org/browse/FHIR-26117),[FHIR-26121](https://jira.hl7.org/browse/FHIR-26121)).
  1. Update introduction to the [The Da Vinci Notification Message Bundl](https://hl7.org/fhir/us/davinci-alerts/STU1/guidance.html#the-da-vinci-notification-message-bundle)([FHIR-26200](https://jira.hl7.org/browse/FHIR-26200)).
  1. Update [Use Case Backgroun](https://hl7.org/fhir/us/davinci-alerts/STU1/usecases.html#use-case-background)([FHIR-26182](https://jira.hl7.org/browse/FHIR-26182),[FHIR-26116](https://jira.hl7.org/browse/FHIR-26116)).
  1. Clarify how Intermediary [forwards message](https://hl7.org/fhir/us/davinci-alerts/STU1/guidance.html#forwarding-notifications-using-this-framework) within framework and add [Notification Forwarder CapabilityStatement] ([FHIR-26177](https://jira.hl7.org/browse/FHIR-26177))
  1. Clarify [Intermediary rol](https://hl7.org/fhir/us/davinci-alerts/STU1/index.html#roles-and-actors) ([FHIR-26148](https://jira.hl7.org/browse/FHIR-26148))
  1. Clarify how to [sort incoming message](https://hl7.org/fhir/us/davinci-alerts/STU1/guidance.html#sending-unsolicited-notifications) (#[FHIR-26132](https://jira.hl7.org/browse/FHIR-26132))
  1. Add [Transfer notification use cas](https://hl7.org/fhir/us/davinci-alerts/STU1/usecases.html). (#[FHIR-26909](https://jira.hl7.org/browse/FHIR-26909))
  1. Flatten and Remove child concept for admit and discharge from the [Da Vinci Notification Event CodeSystem]. ([FHIR-26268](https://jira.hl7.org/browse/FHIR-26268),[FHIR-26178](https://jira.hl7.org/browse/FHIR-26178),[FHIR-26179](https://jira.hl7.org/browse/FHIR-26179),[FHIR-26180](https://jira.hl7.org/browse/FHIR-26180), [FHIR-26136](https://jira.hl7.org/browse/FHIR-26136))
  1. Clarify why [Da Vinci Notifications Bundle Profile] has min=0 constraints. ([FHIR-26289](https://jira.hl7.org/browse/FHIR-26289))
  1. Update [Da Vinci Notifications MessageHeader Profile] to require use of references. ([FHIR-26286](https://jira.hl7.org/browse/FHIR-26286))
  1. Update section on [formal message definition] (guidance.html#formally-defining-the-da-vinci-notification-message)([FHIR-26224](https://jira.hl7.org/browse/FHIR-26224)).
  1. Updates to [Security](https://hl7.org/fhir/us/davinci-alerts/STU1/security.html) page ([FHIR-26195](https://jira.hl7.org/browse/FHIR-26195), [FHIR-26194](https://jira.hl7.org/browse/FHIR-26194),[FHIR-26134](https://jira.hl7.org/browse/FHIR-26134), (https://jira.hl7.org/browse/FHIR-26134), [FHIR-26139](https://jira.hl7.org/browse/FHIR-26139)).
  1. Add `id` element to [Da Vinci Notifications MessageHeader Profile] ([FHIR-26168](https://jira.hl7.org/browse/FHIR-26168)).
  1. Add `id` and 'timestamp element to [Da Vinci Notifications Bundle Profile] profiles. ([FHIR-26168](https://jira.hl7.org/browse/FHIR-26168), [FHIR-26156](https://jira.hl7.org/browse/FHIR-26156)).
  1. Update [Da Vinci Admit Notification MessageHeader Profile],
[Da Vinci Discharge Notification MessageHeader Profile], and
[Da Vinci Transfer Notification MessageHeader Profile] with extensible bindings instead of pattern definitions ([FHIR-26163](https://jira.hl7.org/browse/FHIR-26163)).
  1. Remove detailed summaries from profiles ([FHIR-26161](https://jira.hl7.org/browse/FHIR-26161)).
  1. Clarify for the [Da Vinci Admit/Transfer/Discharge Notification Encounter Profile] that the link is from Condition to Encounter ([FHIR-26158](https://jira.hl7.org/browse/FHIR-26158)).
  1. Added section on [Data Query](https://hl7.org/fhir/us/davinci-alerts/STU1/guidance.html#fetching-additional-data). ([FHIR-26121](https://jira.hl7.org/browse/FHIR-26121))
  1. Updated [STU Note](https://hl7.org/fhir/us/davinci-alerts/STU1/guidance.html#introduction) regarding subscriptions ([FHIR-26100](https://jira.hl7.org/browse/FHIR-26100), [FHIR-26171](https://jira.hl7.org/browse/FHIR-26171)).
  1. Added [About This Guid](https://hl7.org/fhir/us/davinci-alerts/STU1/index.html#about-this-guide) section referring to Da Vinci and Da Vinci Guiding Principles ([FHIR-26114](https://jira.hl7.org/browse/FHIR-26114),[FHIR-26127](https://jira.hl7.org/browse/FHIR-26127), [FHIR-26131](https://jira.hl7.org/browse/FHIR-26131)).
  1. Update to Must Support Section ([FHIR-26124](https://jira.hl7.org/browse/FHIR-26124), [FHIR-26155](https://jira.hl7.org/browse/FHIR-26155)).
  1. Remove Query Requester CapabilityStatement and Query Responder CapabilityStatement ([FHIR-26155](https://jira.hl7.org/browse/FHIR-26155)).
  1. Clarify intent of [future scenario](https://hl7.org/fhir/us/davinci-alerts/STU1/index.html#scenarios) ([FHIR-26133](https://jira.hl7.org/browse/FHIR-26133)).
  1. Clarify intent of MessageHeader.author ([FHIR-26138](https://jira.hl7.org/browse/FHIR-26138)).
  1. Simplify sequence diagrams ([FHIR-26147](https://jira.hl7.org/browse/FHIR-26147)).
  1. Clarify approach to messaging in Framework ([FHIR-26098](https://jira.hl7.org/browse/FHIR-26098)).
  1. Correct Conformance expectations for [Notification Sender CapabilityStatement] ([FHIR-28357](https://jira.hl7.org/browse/FHIR-28357))

### Version 0.2.0

- Publication Date: 2019-12-22
- url: <https://hl7.org/fhir/us/davinci-alerts/2020Feb/>
- Based on FHIR version : 4.0.1

1. This Implementation Guide was originally named *Da Vinci Alerts Implementation Guide* - after review by several HL7 workgroups, it was felt that the term "alerts" has a specific meaning to many people that was not the same as the contents of this guide.  Therefore the title of this IG has been changed to *Da Vinci Unsolicited Notifications Implementation Guide*.  Be aware that there are several technical artifacts such as the canonical base, the npm package name and the history page url that cannot be changed and still retain the word "alerts" in their paths.
1. Implemented FHIR Messaging paradigm instead of using a custom operation to transact notifications.
    1. Replaced the Da Vinci Alert Bundle Profile with a message bundle, the Da Vinci Notifications Bundle.
    1. Replaced the `$notify` custom operation with the FHIR `$process-message` operation to transact the Da Vinci Notifications Bundle directly to Recipients and Intermediaries.
    1. Replaced existing Profiles with Profiles, MessagedDefinitions and GraphDefinition to support FHIR messaging and the Admit/Discharge use case.
    1. Replaced existing examples to support FHIR messaging and the Admit/Discharge use case.
    1. Replaced existing CapabilityStatements to support FHIR messaging and the Admit/Discharge use case.
    1. Various changes and updates to the documentation and figures to provide specific guidance for using FHIR messaging and implementation of the Admit/Discharge use case.

### Version 0.1.0

- **DEPRECATED: Note that this version (0.1.0) should *not* be used, it was pulled from the ballot after publication and has been replaced by version 0.2.0

---

{% include link-list.md %}
