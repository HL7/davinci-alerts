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

For every notification, the FHIR object that is exchanged is the [Da Vinci Notification Message Bundle]. It consists of a Bundle identified by the type "message", with the first resource in the bundle being a MessageHeader resource. The first resource in the bundle is the MessageHeader resource. The MessageHeader resource has a code - the message event - that identifies the reason for the notification.  The MessageHeader also carries additional notification metadata. The other resources in the bundle depend on the notification scenario and form a network through their relationships with each other - either through a direct reference to another resource or through a chain of intermediate references. These groups of resources are referred to as resource graphs. The FHIR Notification resource graph for the admit and discharge use case is shown in [Figure 7].

{% include img-portrait.html img="admit_message_graph.svg" caption="Figure 7" %}

Note:

- \* it is questionable whether Encounter.diagnosis.condition has been implemented by the EHR vendors - need to discuss with vendors.
- \** There is no Practitioner.endpoint element and an extension may be needed to implement.
- \*** MessageDefinition is used to formally define the Message content for a given event (e.g, an inpatient admission or discharge).  It defines the event and the focal and non focal Resources/Profiles that make up the message:

    - [Example Da Vinci Notification MessageDefinition](MessageDefinition-admit-1.html)

    The GraphDefinition is referenced by the MessageDefinition and it defines the links between the all resources that are contained within the message.

    - [Example Da Vinci Notification GraphDefinition](GraphDefinition-admit-1.html)


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
-There is no expectation that the data submitted represents all the data required by the Notification Recipient/Intermediary, only that the data is known to be relevant to the triggering event. The Notification Recipient/Intermediary can optionally fetch additional information from the patient's medical record using FHIR RESTful searches.  The endpoint for this search may be known or supplied via the $process-message operation payload.

Seeking input on whether or not to document how to  transmit endpoint data intended only for the *direct* recipient of the operation and to provides the recipient with the technical details for getting additional information from the medical record for the alert - Note that this has serious security implications as it may contain sensitive access information.
{:.note-to-balloters}

- Not shown in figure 4, after the Intermediary successfully receives the notification, processes it and optionally searches and process the search results, it redistributes the data the end users.  It **MAY** use FHIR messagins and the `$process-message` operation to do this.  Note that the Notification Intermediary **MAY** customize the content based on the end user (for example, withholding data that a particular care team member does not need).

Note to Balloters: We are actively seeking input on whether this guide should define the expectations of how Notification Intermediaries distribute the alert information to the Notification Recipients. For example using existing data transport protocols such as Direct, SMS or V2 messaging.
{:.note-to-balloters}





Note to Balloters: We are actively seeking input on what expectations should be defined for error handling and and whether there is a need to support ["reliable delivery"]
{:.note-to-balloters}

As shown in figure 4, after the Notification Intermediary successfully receives the notification, processes the Notification Bundle and optionally searches and process the seach results, it redistributes the data the end users.  It may use the `$process-message` operation to do this, however the original Endpoint SHALL NOT be distributed.  Note that the Notification Intermediary may customize the content based on the end user (for example, withholding data that a particular care team member does not need).

Note to Balloters: We are actively seeking input on whether this guide should define the expectations of how Notification Intermediaries distribute the alert information to the Notification Recipients. For example using existing data transport protocols such as Direct, SMS or V2 messaging.
{:.note-to-balloters}




#### APIs
{:.no_toc}

The following Da Vinci Notification FHIR artifacts are used in this transaction:

- [Da Vinci Notification Message Bundle]
- [Da Vinci Notifications MessageHeader Profile]

#### Usage
{:.no_toc}

The `$process-message` operation is invoked by the Notification Sender using the `POST` syntax with Parameter resource in the request body:

`POST [base]Communication/$process-message`

{% include examplebutton_default.html example="notify-example" b_title = "Click Here To See Example PUSH Notification Notification" %}

## FHIR Messaging

An alternative consideration is to use the [FHIR Messaging paradigm] to send a Da Vinci Notification Message Bundle to the Recipient. There are several transport mechanisms that can be used. One way is to use the $process-message operation on FHIR Server Restful endpoint. This is analogous to the Notification Bundle $process-message operation above using the $process-message operation in place of the $process-message and a Da Vinci Notification Message Bundle structure instead of the Notification Bundle:



The same Da Vinci Notification Message Bundle structure can be re-used as the notification payload for FHIR Subscription based alerts since a subscriber can register to receive [notifications by messaging]:

{% include img.html img="subscription_messaging_wf.svg" caption="Figure 6" %}


### Graph of FHIR Resources for Messaging

The following resource graph in figure 8 defines the resources that support the admission and discharge alerts use case using FHIR messaging. MessageHeader, Patient, Encounter, and Condition are the primary resources (indicated by the black borders) which are messaged in the Da Vinci Notification Message Bundle to notify the provider of when the event has occurred. The Endpoint Resource can be optionally included in the bundle to allow the Recipient to optionally query other associated resources such as Location, Practitioner and Organization  through a subsequent FHIR read or search interaction (TODO this needs further testing and discussion).  Note that the boxes with several resources inside them represents a choice.

{% include img-portrait.html img="admit_message_graph.svg" caption="Figure 8" %}

Note:

- \* it is questionable whether Encounter.diagnosis.condition has been implemented by the EHR vendors - need to discuss with vendors.
- \** There is no Practitioner.endpoint element and an extension may be needed to implement.
- \*** MessageDefinition is used to formally define the Message content for a given event (e.g, an inpatient admission or discharge).  It defines the event and the focal and non focal Resources/Profiles that make up the message:

    - [Example Da Vinci Notification MessageDefinition](MessageDefinition-admit-1.html)

    The GraphDefinition is referenced by the MessageDefinition and it defines the links between the all resources that are contained within the message.

    - [Example Da Vinci Notification GraphDefinition](GraphDefinition-admit-1.html)


The Bundle can be transacted similarly to the Notification bundle by posting to an operation endpoint using a RESTful POST transaction:

- [Example Da Vinci Notification Message Bundle](Bundle-message-admit-01.html)


**Example Transaction**
The following transaction show an example of using the `$process-message` operation to send a Da Vinci Notification Message Bundle:

{% include examplebutton_default.html example="process-message-example" b_title = "Click Here To See Example Notification Notification" %}
<br />

### Comparison of the Communication Profile to the MessageHeader Profile

The Messag eHeader is the first resource in the Da Vinci Notification Message Bundle and serves the same function as Communication resources in the Notification Bundle above, providing the necessary context for the alert reason together with various resources pointed to or indirectly connected to it:

{% include img-portrait.html img="comm_msg_map.svg" caption="Figure 9" %}

- [Example Da Vinci Notification MessageHeader](MessageHeader-admit-1.html)



<!--{% raw %}
### FHIR Subscription Based Notification

{:.note-to-balloters}
Note to Balloters: We are actively seeking input on what additional work is needed to determine the best way to implement subscriptions for alert notification.  This project recognizes the impact of the Argonaut work on Subscription for R5 and is considering what approach to take to align with that work.
<br /><br />
current proposals include:
<br /><br />
\1. criteria based on searching the resource that corresponds to the alert event  (for example Encounter for admit/discharge) with the expectation that the subscriber would perform a subsequent query to fetch the supporting data.
<br /><br />
\2. criteria based on searching the resource that corresponds to the alert event  (for example Encounter for admit/discharge) **plus** a graph definition to inform the server what Notification Bundle to return with the resource using the [$graph operation]
<br /><br />
\3. criteria based on searching `Encounter.status` and/or `Encounter.class`**plus** a graph definition to inform the server what Notification Bundle to return with the resource using the [$graph operation]
<br /><br />
\4. criteria based on searching `Communication.topic` **plus** a graph definition to inform the server what Notification Bundle to return with the resource using the [$graph operation]

<br />

The interaction diagram in figure 5 illustrates the sequences of events for subscribing for alerts and the subsequent notifications when the the event occurs.  The server (in a subscription protocol more commonly known as a the subscription publisher) can be either the Notification Sender or the Notification Intermediary. The client (in a subscription protocol more commonly known as a the subscriber) can be either the Notification Recipient or the Notification Intermediary.

{% include img-portrait-med.html img="basic_sub.svg" caption="Figure 5" %}

---

Figure 6 depicts additional subscription interactions for the Notification Intermediary when transacting with multiple servers.

{% include img-portrait-med.html img="add_intermediary_interactions.svg" caption="Figure 6" %}

---

**Example Transaction**
{% include examplebutton_default.html example="example" b_title = "Click Here To See Example Subscription Notification Notification" %}
<br />


{% endraw %}-->
---

{% include link-list.md %}
