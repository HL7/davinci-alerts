<!-- FHIR Core Resources -->
{% include r4-link-list.md %}
<!-- IG Pages (Including IG Artifacts -->
{% include page-link-list.md %}
["black box"]: https://en.wikipedia.org/wiki/Black_box
[2019 CMS 45 CFR Part 156 NPRM]: https://www.federalregister.gov/d/2020-05050
[Admit Notification Intermediate Transmit Bundle]:Bundle-admit-notification-intermediate-transmit-bundle.html
[Alternate Reference]: http://hl7.org/fhir/StructureDefinition/alternate-reference
[Argonaut Clinical Data Subscriptions]: http://argonautwiki.hl7.org/index.php?title=Argonaut_2019_Projects#Clinical_Data_Subscriptions
[Basic Provenance for HIE Redistribution and Transformation]: {{site.data.fhir.uscore7}}/basic-provenance.html#hie-redistribution
[Bundle Admit Notification Message Bundle 01]: Bundle-admit-notification-message-bundle-01.html
[Bundle Discharge Notification Message Bundle 01]: Bundle-discharge-notification-message-bundle-01.html
[Bundle]: {{site.data.fhir.path}}bundle.html
[Capability Statements]: artifacts.html#1
[Da Vinci Admit Notification Message Definition]: MessageDefinition-notification-admit.html
[Da Vinci Discharge Notification Message Definition]: MessageDefinition-notification-discharge.html
[Da Vinci Health Record Exchange (HRex)]: http://hl7.org/fhir/us/davinci-hrex/index.html
[Da Vinci Notification Event CodeSystem]: CodeSystem-notification-event.html
[Da Vinci Notifications CapabilityStatements]: capstatements.html
[Da Vinci Notifications GraphDefinition Profile]: StructureDefinition-notifications-graphdefinition.html
[Da Vinci Notifications MessageDefinition Profile]: StructureDefinition-notifications-messagedefinition.html
[Da Vinci Notifications Must Support Extension]: StructureDefinition-extension-mustSupport.html
[Da Vinci]: http://www.hl7.org/about/davinci/index.cfm?ref=common
[Discharge disposition]: http://hl7.org/fhir/ValueSet/encounter-discharge-disposition
[Downloads]: downloads.html "Downloads Page"
[Dynamic Registration for SMART Apps]: http://www.udap.org/udap-dynamic-client-registration.html
[ElementDefinition.mustSupport]: {{site.data.fhir.path}}elementdefinition-definitions.html#ElementDefinition.mustSupport
[Endpoint]: {{site.data.fhir.path}}bundle.html
[Example Transaction]: usecases.html#example-transaction
[Examples Transactions]: usecases.html#example-transactions
[Examples]: artifacts.html#5
[FHIR Artifacts]: artifacts.html
[FHIR Bulk Data Access (Flat FHIR)]: http://hl7.org/fhir/uv/bulkdata/STU1/
[FHIR Data Segmentation for Privacy project]: https://www.hl7.org/special/Committees/projman/searchableProjectIndex.cfm?action=edit&ProjectNumber=1549
[FHIR Messaging paradigm]: {{site.data.fhir.path}}messaging.html
[FHIR R4 core]: {{site.data.fhir.path}}fhir-spec.zip
[FHIR R5 MessageHeader]: http://hl7.org/fhir/R5/messageheader.html
[FHIR RESTful operation]: {{site.data.fhir.path}}operations.html
[FHIR Subscription Based Notification]: guidance.html#fhir-subscription-based-notification
[FHIR at Scale Taskforce (FAST)]: https://confluence.hl7.org/display/FAST/FAST+Projects
[FHIR core downloads]: {{site.data.fhir.path}}downloads.html
[FHIR message Bundle]: {{site.data.fhir.path}}bundle.html#message
[FHIR messaging]: {{site.data.fhir.path}}messaging.html
[FHIR security guidance]:{{site.data.fhir.path}}security.html
[Formal Profile Definition]: #profile
[Framework]: guidance.html  "General Framework Page"
[HL7 Da Vinci Guiding Principles]: https://confluence.hl7.org/display/DVP/Da+Vinci+Clinical+Advisory+Council+Members?preview=/66940155/66942916/Guiding%20Principles%20for%20Da%20Vinci%20Implementation%20Guides.pdf
[HRex Organization Profile]: {{site.data.fhir.hrex}}/StructureDefinition-hrex-organization.html
[HRex Security and Privacy]: {{site.data.fhir.hrex}}/security.html
[Hybrid/Intermediary Exchange Implementation Guide]: http://hl7.org/fhir/us/exchange-routing/index.html
[IG Home]: index.html "Home Page"
[Infrastructure and Messaging (INM)]: http://www.hl7.org/Special/committees/inm/index.cfm
[Message Definitions]: bundles.html "Bundle Definitions Page"
[Messageheader Admit Notification Messageheader 01]: MessageHeader-admit-notification-messageheader-01.html
[Messageheader Discharge Notification Messageheader 01]: MessageHeader-discharge-notification-messageheader-01.html
[Must Support]: guidance.html#must-support
[MustSupport flag]: {{site.data.fhir.path}}profiling.html#mustsupport
[NotificationAdmitDischarge]: GraphDefinition-admit-discharge.html
[Operations]: artifacts.html
[Profiles]: artifacts.html#2
[Profiling]: {{site.data.fhir.path}}profiling.html
[Propose a Change]: https://jira.hl7.org/issues/?filter=12844&jql=project%20%3D%20FHIR%20AND%20Specification%20%3D%20%22US%20Da%20Vinci%20Alerts%20(FHIR)%20%5BFHIR-us-davinci-alerts%5D%22
[Push Alert Notification]: guidance.html#push-alert-notification
[R5 cross-version extension]: {{site.data.fhir.path}}security.html
[SMART Application Launch Framework Implementation Guide Release 1.0.0]: http://www.hl7.org/fhir/smart-app-launch/
[SMART Backend Services]: https://www.hl7.org/fhir/smart-app-launch/backend-services.html#backend-services
[Standard error responses]: {{site.data.fhir.path}}messageheader-operation-process-message.html
[Terminology]: artifacts.html#3
[US Core Condition Encounter Diagnosis Profile]: {{site.data.fhir.uscore7}}StructureDefinition-us-core-condition-encounter-diagnosis.html
[US Core Encounter Profile]: {{site.data.fhir.uscore7}}StructureDefinition-us-core-encounter.html
[US Core Location Profile]: {{site.data.fhir.uscore7}}StructureDefinition-us-core-location.html
[US Core Must Support]: {{site.data.fhir.uscore7}}/must-support.html
[US Core Patient Profile]: {{site.data.fhir.uscore7}}StructureDefinition-us-core-patient.html
[US Core Provenance Profile]: {{site.data.fhir.uscore7}}/StructureDefinition-us-core-provenance.html
[US Core guidance]: {{site.data.fhir.uscore7}}/StructureDefinition-us-core-condition-encounter-diagnosis.html#mandatory-and-must-support-data-elements
[US Core]: {{site.data.fhir.uscore7}}/index.html
[V3 Value SetActEncounterCode]: http://terminology.hl7.org/ValueSet/v3-ActEncounterCode
[`$process-message`]: {{site.data.fhir.path}}messageheader-operation-process-message.html
[`collection`]: {{site.data.fhir.path}}http.html#collection
[aggregation]: {{site.data.fhir.path}}elementdefinition-definitions.html#ElementDefinition.type.aggregation
[figure 9]: usecases.html#figure-9
[instructions on how to use it]: https://confluence.hl7.org/display/FHIR/Using+the+FHIR+Validator
[notifications by messaging]: {{site.data.fhir.path}}subscription.html#messaging
[operation]: {{site.data.fhir.path}}operations.html
[reliable delivery]: {{site.data.fhir.path}}messaging.html#reliable
[validator]: https://fhir.github.io/latest-ig-validator/org.hl7.fhir.validator.jar
