---
title: Framework
layout: default
active: guidance

---

{:.no_toc}

<!-- TOC  the css styling for this is \pages\assets\css\project.css under 'markdown-toc'-->

* Do not remove this line (it will not be displayed)
{:toc}

### Introduction

FHIR resources can be used to transport patient information relevant to a specific event (e.g. admission, discharge, change in treatment, new diagnosis) to another provider or the health plan to communicate the details of where care was delivered and help to ensure timely follow-up as needed.  The intent is to provide the minimally required information in the notification, for the Receiver to know, if the notification is of interest and give enough information to be able to request more from the Sender, if desired. This information can be used to build an encounter record in the receiving system with appropriate provenance and make it available to CDS and other local services. The following framework documents how notifications are transacted using [FHIR messaging] and the [`$process-message`] operation to push directly to “registered” Recipients and Intermediaries.

This project recognizes the impact of the [Argonaut Clinical Data Subscriptions] project which is working on event based subscriptions and major revisions to the Subscription resource for FHIR R5.  it is anticipated that an equivalent subscription based notification paradigm can be implemented as an alternate to the messsaging based approach documented in this guide.
{:.note-to-balloters}

### Must Support

All elements in the Da Vinci Notification profiles have a [MustSupport flag]. Systems claiming to conform to a profile must "support" the element as defined herein:

#### This guide adopts the following definitions of Must Support for all *direct* transactions between the Sender and Recipient or Intermediary
{:.no_toc}

*Must Support* on any data element SHALL be interpreted as follows:

* As part of the notification message or a query result as specified by the [Da Vinci Notifications CapabilityStatements], the  Sender SHALL be capable of including the data elements defined in the Da Vinci Notification profiles that have a MustSupport flag.

* The Recipient/Intermediary SHALL be capable of processing resource instances containing the data elements without generating an error or causing the application to fail. In other words Recipient/Intermediary SHOULD be capable of processing the data elements (display, store, etc).

* In situations where information on a particular data element is not present and the reason for absence is unknown, the Sender SHALL NOT include the data elements in the resource instance as part of a $process-message operation or a query response.

* When receiving a notification or a query response from the Sender, the  Recipient/Intermediary SHALL interpret missing data elements within resource instances as data not present in the Sender's systems.

* In situations where information on a particular data element is missing and the  Sender knows the precise reason for the absence of data, the Sender SHALL provide the reason for the missing information using values (such as nullFlavors) from the value set where they exist or using the dataAbsentReason extension.

* Notification Recipient/Intermediary SHALL be able to process resource instances containing data elements asserting missing information without generating an error or causing the application to fail.


#### This guide adopts the following definitions of Must Support for all transactions between the Intermediary and Recipient
{:.no_toc}

*Must Support* on any data element SHALL be interpreted as follows:

- As part of the alert notification or a query result as specified by the [Da Vinci Intermediary Server CapabilityStatement], the  Sender SHALL be capable of including the data elements defined in the Da Vinci Notification profiles that have a MustSupport flag.

- The  Recipient SHALL be capable of processing resource instances containing the data elements the data elements defined in the Da Vinci Notification profiles that have a MustSupport flag without generating an error or causing the application to fail. In other words, the Recipient SHOULD be capable of processing the data elements (displaying, storing, etc).

- In situations where information on a particular data element is not needed or considered protected information the Intermediary MAY remove the data elements in the resource instance when distributing the alert notification or responding to an n Recipient's query. The Intermediary MAY provide the reason for the missing information using values (such as nullFlavors) from the value set where they exist or using the dataAbsentReason extension.

- The Recipient SHALL be able to process resource instances containing missing data elements and data elements asserting missing information without generating an error or causing the application to fail.


### Preconditions and Assumptions

#### Preconditions

- There is an event that drives the generation of the Notification.
- An Notification will be generated for each patient separately.
  - The event can be for one or more patients.
- The Sender has access to the Recipients/Intermediary FHIR endpoints.
- System level trust exists between the actors.
  - Clients have been authorized by the servers.
  - It is assumed that consent is managed elsewhere.
  - Patient consent allows exchange of data between the relevant systems.
- A secure information transport mechanism exists between the actors.

#### Assumptions

- Based on FHIR R4 and US Core R4 profiles where applicable.
- Notifications are transacted to teh process-message operation endpoint.
- The Da Vinci Notification Message Bundle Profile is the FHIR object that is exchanged for all alert transactions.


### The Da Vinci Notification Message Bundle

For every notification, the FHIR object that is exchanged is the [Da Vinci Notification Message Bundle]. It consists of a Bundle identified by the type "message", with the first resource in the bundle being a MessageHeader resource. The first resource in the bundle is the MessageHeader resource. The MessageHeader resource has a code - the message event - that identifies the reason for the notification.  The MessageHeader also carries additional notification metadata. The other resources in the bundle depend on the notification scenario and form a network through their relationships with each other - either through a direct reference to another resource or through a chain of intermediate references. These groups of resources are referred to as resource graphs. The FHIR Notification resource graph for the admit and discharge use case is shown in [Figure 3].

{% include img-portrait.html img="admit_message_graph.svg" caption="Figure 3" %}

Note:

This resource graph defines the resources that support the admission and discharge alerts use case using FHIR messaging. MessageHeader, Patient, Encounter, and Condition are the primary resources (indicated by the black borders) which are messaged in the Da Vinci Notification Message Bundle to notify the provider of when the event has occurred. The Endpoint Resource can be optionally included in the bundle to allow the Recipient to optionally query other associated resources such as Location, Practitioner and Organization  through a subsequent FHIR read or search interaction (TODO this needs further testing and discussion).  Note that the boxes with several resources inside them represents a choice.

- \* it is questionable whether Encounter.diagnosis.condition has been implemented by the EHR vendors - need to discuss with vendors.
- \** There is no Practitioner.endpoint element and an extension may be needed to implement.
- \*** MessageDefinition is used to formally define the Message content for a given event (e.g, an inpatient admission or discharge).  It defines the event and the focal and non focal Resources/Profiles that make up the message:

    - [Example Da Vinci Notification MessageDefinition](MessageDefinition-admit-1.html)

    The GraphDefinition is referenced by the MessageDefinition and it defines the links between the all resources that are contained within the message.

    - [Example Da Vinci Notification GraphDefinition](GraphDefinition-admit-1.html)

**Example Da Vinci Notification Message Bundle**

- [Example Da Vinci Notification Message Bundle](Bundle-message-admit-01.html)

#### Associated Resources for Notification Scenarios
{:.no_toc}

Resources that associated SHALL be included in *all* Da Vinci Notification Message Bundles:

- *MessageHeader*
- *Encounter* referenced by `MessageHeader.focus`
- *Patient* referenced by `Encounter.subject`
-  All supporting data (resources) for each kind of notification that is referenced in `MessageHeader.focus`

 In addition to Patient and Encounter which are included in all Notification Bundles, the following tables summarizes the additional Resources that directly or indirectly referenced  and included in the message or avialable in a subsequent query by the Intermediary or Recipient

{: .grid}
| ﻿Notification Scenarios | Resources in Notification Bundle | Searchable Resources|
|---|---|---|
| Emergency and Inpatient Admissions | US Core R4 Condition |Location, Coverage, Practitioner (sender), Organization (sender), PractitionerRole (sender)|
| Emergency and Inpatient Discharges | US Core R4 Condition |Location, Coverage, Practitioner (sender), Organization (sender), PractitionerRole (sender) |

---


{:.note-to-balloters}
Note to Balloters: These scenarios may be added in future iterations of this IG.

{:.note-to-balloters .grid}
| ﻿Notification Scenarios | Resources in Notification Bundle<sup>(1)</sup> | Searchable Resources<sup>(2)</sup> |
|---|---|---|
| Lab Results | US Core R4 DiagnosticReport, US Core R4 Observation, US Core R4 DocumentReference |TBD... |
| Problem with Treatment – such as drug recall, device recall/issue | US Core R4 Medication, US Core R4 AdverseEvent, US Core R4 Device | TBD... |
| Encounter/Visit Notification | no additional |TBD...  |
| Public Health Notification | US Core R4 Condition |TBD...  |
| Scheduled Appointment/Pre-Admit | R4 Appointment |TBD...  |
| Referral | R4 ServiceRequest, R4 Practitioner |TBD...  |
| Ordered Device/Biometric/Patient (i.e. Fit Bit) | R4 DeviceRequest |TBD...  |
| Treatment Start/End | US Core R4 MedicationAdministration |TBD...  |
| Change in Social Determinants of Health | R4 Observation |TBD...  |
| Birth/Death | No additional resource |TBD... |
| Coverage Start/End | DEQM Coverage |TBD...  |
| Notification of Prior Authorization (Pended to Approved/Denied) | R4 ClaimResponse |TBD...  |
| Pharmacy (Pickup, Restock, Dispense) | US Core R4 Medication, US Core R4 MedicationDispense, R4 SupplyDelivery, R4 SupplyRequest |TBD...  |
| Notification of New Condition | US Core R4 Condition |TBD...  |
| Work Comp Initial/Visits/Services | US Core R4 Condition, R4 Coverage |TBD...  |
| Changes in Care Team | US Core R4 Practitioner, R4 RelatedPerson, R4 CareTeam | TBD... |




### Pushing Notifications to the Sender or Intermediary

As shown in Figure 4, When an event or request triggers a notification, the Sender creates a Da Vinci Notification Message Bundle and notifies the Recipient or Intermediary using the `$process-message` operation.

{% include img.html img="$process_message_wf.svg" caption="Figure 4" %}

- For this guide there is no expectation for a notification response message to be returned from the Recipient or Intermediary to the Sender. Therefore, the $process-message input parameters "async" and "response-url" are not used and the body of this operation is the message bundle itself.
- In the context of the `$process-message` operation, the Recipient/Intermediary is treated as a ["black box"] and simply accepts and processes the submitted data and there are no further expectations beyond the http level response as defined in the in the FHIR specification.
- There is no expectation that the data submitted represents all the data required by the Notification Recipient/Intermediary, only that the data is known to be relevant to the triggering event. The Notification Recipient/Intermediary can optionally fetch additional information from the patient's medical record using FHIR RESTful searches.  The endpoint for this search may be known or supplied via the $process-message operation payload.

Seeking input on whether or not to document how to  transmit endpoint data intended only for the *direct* recipient of the operation and to provides the recipient with the technical details for getting additional information from the medical record for the alert - Note that this has serious security implications as it may contain sensitive access information.
{:.note-to-balloters}

- Not shown in figure 4, after the Intermediary successfully receives the notification, processes it and optionally searches and process the search results, it redistributes the data the end users.  It **MAY** use FHIR messaging and the `$process-message` operation to do this or some other messaging protocol such as Direct, SMS or V2 messaging.  Note that the Notification Intermediary **MAY** customize the content based on the end user (for example, withholding data that a particular care team member does not need).

#### APIs
{:.no_toc}

The following Da Vinci Notification FHIR artifacts are used in this transaction:

- [Da Vinci Notification Message Bundle]
- [Da Vinci Notifications MessageHeader Profile]

#### Usage
{:.no_toc}

The `$process-message` operation is invoked by the  Sender using the `POST` syntax with notification message bundle resource in the request body:

`POST [base]$process-message`

**Example Transaction**
The following transaction show an example of using the `$process-message` operation to send a Da Vinci Notification Message Bundle:

{% include examplebutton_default.html example="process-message-example" b_title = "Click Here To See Example Notification Notification" %}

### Reliable Delivery

Note to Balloters: We are actively seeking input on what expectations should be defined for error handling and and whether there is a need to support ["reliable delivery"]
{:.note-to-balloters}

---

{% include link-list.md %}
