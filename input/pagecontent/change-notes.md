
The Da Vinci Unsolicited Notifications Implementation Guide was developed under the  [Davinci Project](#)

### Changes and Updates for version 1.0.0

The first official published version of the DEQM IG for FHIR R4.

1. Applied all resolutions from STU2 Ballot

  1. Various Technical Corrections and Corrections to Typographical Errors
  1.  updated examples
  1. Remove MessageDefintion and GraphDefinition profile and references to them ([FHIR-NNNNN](https://jira.hl7.org/browse/FHIR-))
  1. Update Guidance on [Errors and ReliablDelivery](guidance.html#reliable-delivery) ([FHIR-26165](https://jira.hl7.org/browse/FHIR-26165), [FHIR-26201](https://jira.hl7.org/browse/FHIR-26201)).


### Changes and Updates for version 0.2.0

1. This Implementation Guide was originally named *Da Vinci Alerts Implementation Guide* - after review by several HL7 workgroups, it was felt that the term "alerts" has a specific meaning to many people that was not the same as the contents of this guide.  Therefore the title of this IG has been changed to *Da Vinci Unsolicited Notifications Implementation Guide*.  Be aware that there are several technical artifacts such as the canonical base, the npm package name and the history page url that cannot be changed and still retain the word "alerts" in their paths.
1. Implemented FHIR Messaging paradigm instead of using a custom operation to transact notifications.
    1. Replaced the Da Vinci Alert Bundle Profile with a message bundle, the Da Vinci Notifications Bundle.
    1. Replaced the `$notify` custom operation with the FHIR `$process-message` operation to transact the Da Vinci Notifications Bundle directly to Recipients and Intermediaries.
    1. Replaced existing Profiles with Profiles, MessagedDefinitions and GraphDefinition to support FHIR messaging and the Admit/Discharge use case.
    1. Replaced existing examples to support FHIR messaging and the Admit/Discharge use case.
    1. Replaced existing CapabilityStatements to support FHIR messaging and the Admit/Discharge use case.
    1. Various changes and updates to the documentation and figures to provide specific guidance for using FHIR messaging and implementation of the Admit/Discharge use case.

### Changes and Updates for version 0.1.0

- **DEPRECATED: Note that this version (0.1.0) should *not* be used, it was pulled from the ballot after publication and has been replaced by version 0.2.0.**
