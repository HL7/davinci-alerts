---
title: Framework
layout: default
active: guidance
topofpage: true
---

{:.no_toc}

<!-- TOC  the css styling for this is \pages\assets\css\project.css under 'markdown-toc'-->

* Do not remove this line (it will not be displayed)
{:toc}

### Introduction

FHIR resources can be used to transport patient information relevant to a specific event (e.g. admission, discharge, change in treatment, new diagnosis) to another provider or the health plan. These resources can communicate the details of who, when, what and where care was delivered and help to ensure timely follow-up as needed.  To reiterate, the intent of this guide is to provide a framework to create notifications that can provide enough information to Recipient and/or Intermediary for them to be able understand what the notification is about and complete enough to enable them to determine if and what additional steps they need to take in response to the notification.   The following framework documents how to use [FHIR messaging] to define the contents of the notification and how to "push" these unrequested notification messages using the [`$process-message`] operation directly to Recipients and Intermediaries.  The [Admit/Discharge Use case] demonstrates how to implement an unsolicited notification scenario using the framework.

This project recognizes the impact of the [Argonaut Clinical Data Subscriptions] project which is working on event based subscriptions and major revisions to the Subscription resource for FHIR R5.  it is anticipated that an equivalent subscription based notification paradigm can be implemented as an alternate to the unsolicited messsaging based approach documented in this guide.
{:.stu-note}

### Preconditions and Assumptions


<div class="row">
<div class="col-sm-6" markdown="1" style="background-color: Lightcyan;">
**Preconditions**

- There is an event or request that drives the generation of the Notification.
- A Notification will be generated for each patient separately.
  - The event can be for one or more patients.
- The Sender has access to the Recipients/Intermediary FHIR endpoints.
- System level trust exists between the actors (refer to the [Security] Page for additional guidance).
  - Clients have been authorized by the servers.
  - It is assumed that consent is managed elsewhere.
  - Patient consent allows exchange of data between the relevant systems.
- A secure information transport mechanism exists between the actors(refer to the [Security] Page for additional guidance).

----

</div>
<div class="col-sm-6" markdown = "1" style="background-color: WhiteSmoke;">
**Assumptions**

---

- Based on FHIR R4 and US Core R4 profiles where applicable.
- Notifications are transacted to the `$process-message` operation endpoint.
- The Da Vinci Notification Message Bundle Profile is the FHIR object that is exchanged for all alert transactions.

---

</div>

</div>
<br/>

### The Da Vinci Notification Message Bundle

For every notification, the object that is exchanged is a [FHIR message Bundle]. It consists of a Bundle identified by the type "message", with the first resource in the bundle being a [MessageHeader] resource. The MessageHeader resource has a code - the message event - that identifies the reason for the notification.  The MessageHeader also carries additional notification metadata. The other resources in the bundle depend on the notification scenario and form a network through their relationships with each other - either through a direct reference to another resource or through a chain of intermediate references.

#### The Da Vinci Notification Message Event Code
{:.no_toc}

The message event codes identify the reason for the notification.  For this framework a set of concepts describing the purpose of the Da Vinci unsolicited notification has been created.

{% include list-simple-codesystems.xhtml %}

These concepts represent a 'starter set' and will be supplemented with additional concept in the future. Note that there is no HL7 v2 messaging equivalent to these codes. However when available, a relationship between concepts in the notification event codes and concepts used in the notification "focus" resource is documented. For example in the admission and discharge scenarios the message event codes are notification concepts that correspond to the concepts defining the events in the `encounter.class` and `encounter.hospitalization.dischargeDisposition` codes.

#### What is in the Message Bundle
{:.no_toc}

<!--
The message bundle **SHALL** include the MessageHeader resource and the resources referenced by `MessageHeader.focus` element. It **SHOULD** include all resources needed for the Receiver or Intermediary to be able to process the message as expected by the the message event *provided that all included resources have a traversal path following Reference or canonical links either to or from the MessageHeader*.
-->
For all Da Vinci Notification Message Bundles, the following resources are mandatory (i.e., data MUST be present) or must be supported if the data if present in the source system (see [Must Support] definition below).  These requirements are illustrated in figure 3 below.  See the [Admit/Discharge Use Case] for an example of the required resources for a particular scenario.

**Each Bundle must have:**

1. *MessageHeader*
1. The event or request resource referenced by `MessageHeader.focus`
  - For example, the *Encounter* for admissions notification

**Each Bundle must support:**

1. US Core *Organization*, *Practitioner*, or *PractionerRole* referenced by `MessageHeader.sender`
1. US Core *Organization*, *Practitioner*, or *PractionerRole* referenced by `MessageHeader.responsible`
1. US Core *Practitioner*, or *PractionerRole* referenced by `MessageHeader.author`
1. *All* resources directly referenced by the `MessageHeader.focus` resource. Implementers should carefully consider what information they are willing to share and only include those reference elements for the use case in the focus resources. This can be formally defined by profiling the focus resource.  For example the admit/discharge use case focal resource is the [US Core Encounter Profile].

   Implementers that use FHIR as their persistence layer may need to modify those resources before assembling the message bundle to avoid sending sensitive or unnecessary data.
   {:.highlight-note}

1.  *All* resources needed for the Receiver or Intermediary to be able to interpret the notification and process the message *provided* that the resources have a traversal path to or from `MessageHeader.focus` resource.  These requirements are use case specific and need to be determined by the implementation community based on their data requirements.

#### How to define the Message Bundle
{:.no_toc}

The set of resources within the message and their relationship to each other can be represented as an interconnected graph of resources as Figure 3 below illustrates (note that this a simplified and incomplete representation of the possible resources in message. See figure 8 for an example of resource graph for the admission/discharge scenario):  

{% include img-portrait.html img="generic_message_graph.svg" caption="Figure 3" %}

#### Formally Defining the Da Vinci Notification Message
{:.no_toc}

The Da Vinci Notification Message can be formally defined in FHIR using two alternate ways:

1. a set of FHIR Profiles that constrain links to the message Bundle
1. MessageDefinition and GraphDefinition

In both methods the base [Da Vinci Notifications MessageHeader Profile]
and [Da Vinci Notifications Bundle Profile] are used to define the base constraints for all notification scenarios.

##### FHIR Profiles
{:.no_toc}

In this method all the profiles that populate the Bundle get enforced by their references and the fact that their [aggregation] is constrained to 'bundled'.  This means that these references are only to resources that populate the same bundle.  Therefore, starting with the MessageHeader profile, the profiled resources within the bundle form a chain of links that define the bundle.

Use case specific Da Vinci Notification Bundles can be derived from the:

  - [Da Vinci Notifications Bundle Profile]
  - Use case specific MessageHeader Profile and other Resource Profiles

See the Admit/Discharge use case for an example of defining a Bundle using this method.

FHIR profiling is more mature mechanism and broadly supported by the implementation community, reference implementations, and validation tooling.  However,there is no mechanism to enforce profiles in a message on a reverse link because “reverse links” cannot be traversed forward from the MessageHeader. It may also require more artifacts than using MessageDefintion/GraphDefinition.
{:.highlight-note}


##### MessageDefinition and GraphDefinition
{:.no_toc}

The [MessageDefinition] defines the event and focus resource of the Message as well as other metadata. The [GraphDefinition] is referenced by the MessageDefinition and it defines the forward and reverse links (paths) between the resources (profiles) that populate the messaging Bundle. This guide defines the following profiles to be used as "blueprints" to create MessageDefinition and GraphDefinition instances for Da Vinci Notifications:

- [Da Vinci Notifications MessageDefinition Profile]
- [Da Vinci Notifications GraphDefinition Profile]

Use case specific Da Vinci Notification Bundles can be derived from the:

  - [Da Vinci Notifications Bundle Profile]
  - Use case specific MessageDefinition and GraphDefinition instances

See the Admit/Discharge use case for an example of defining a Bundle using this method.

MessageDefinition and GraphDefinition are immature resources and may have breaking changes in future version of FHIR.  At the time of this publication, the implementation community, reference implementations, and validation tooling does not fully support them.
{:.highlight-note}


<!--

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

-->



### Pushing Unsolicited Notifications to the Receiver or Intermediary

As shown in Figure 4, when an event or request triggers a notification, the Sender creates a Da Vinci Notification Message Bundle and notifies the Recipient or Intermediary using the `$process-message` operation.

{% include img-portrait.html img="$process_message_wf.svg" caption="Figure 4" %}

- For this guide there is no expectation for a notification response message to be returned from the Recipient or Intermediary to the Sender. Therefore, the $process-message input parameters "async" and "response-url" are not used and the body of this operation is the message bundle itself.
- In the context of the `$process-message` operation, the Recipient/Intermediary is treated as a ["black box"] and simply accepts and processes the submitted data and there are no further expectations beyond the http level response as defined in the FHIR specification.
- There is no expectation that the data submitted represents all the data required by the Notification Recipient/Intermediary, only that the data is known to be relevant to the triggering event. The Notification Recipient/Intermediary can optionally fetch additional information from the patient's medical record using FHIR RESTful searches.  The endpoint for this search may be known or supplied via the $process-message operation payload.

We are actively seeking input on whether or not to document how to  transmit endpoint data intended only for the immediate  (which may be the final recipient or an intermediary)  and to provide the recipient with the technical details for getting additional information from the medical record for the alert - Note that this has serious security implications as it may contain sensitive access information.
{:.note-to-balloters}

- Not shown in figure 4, after the Intermediary successfully receives the notification, processes it and optionally searches and process the search results, it redistributes the data the end users.  It **MAY** use FHIR messaging and the `$process-message` operation to do this or some other messaging protocol such as Direct, SMS or V2 messaging.  Note that the Notification Intermediary **MAY** customize the content based on the end user (for example, withholding data that a particular care team member does not need).

#### Usage
{:.no_toc}

The `$process-message` operation is invoked by the Sender using the `POST` syntax:

`POST [base]$process-message`

The body of the operation is the Da Vinci Notification Message Bundle containing:

  1. The MessageHeader which is the first resource in the bundle and contains the the message event code - that identifies the nature of the notification.
  1. The other resources in the bundle depend on the notification use case and are defined by either the MessageDefinition and GraphDefinition or FHIR Profiles as described above.

An HTTP Status success code is returned on successful submission.


See the Admit/Discharge scenario [Example Transaction] for an example of using the `$process-message` operation to send a Da Vinci Notification Message Bundle.

### Reliable Delivery

Upon receiving a message, the Receiver/Intermediary may return one of several status codes which is documented in [`$process-message`] definition.

<div class="note-to-balloters" markdown="1">
We are actively seeking input on whether additional guidance should be documented in this guide on FHIR-related errors (in addition to normal HTTP errors related to security, header and content type negotiation issues). For example, whether to define a minimum set of error response code, such as those listed [here]({{site.data.fhir.path}}http.html#rejecting-updates). Additionally, what additional guidance should be provided to specify how the Sender can provide a more reliable delivery of notifications to the intended recipient(s).  For example, defining what actions the Sender must take when it receives a particular error response code.

At the Dec 11-12 Da Vinci Connectathon we polled the participants and determined that the following codes and guidance could be added:

- `200`,`202`,`204`+/- OperationOutcome all ok for successful transactions
   - *Issue : what does widely use Java client want?*
- `401`,`404`+/- OperationOutcome no point in retry
- `429` +/- OperationOutcome  retry but slow down traffic
- `500+` +/- OperationOutcome - server issues  may retry a few times
</div>

### Must Support

#### Profiles
All elements in the Da Vinci Notification profiles have a [MustSupport flag]. Systems claiming to conform to a profile must "support" the element as defined below:

##### This guide adopts the following definitions of Must Support for all *direct* transactions between the Sender and Recipient or Intermediary
{:.no_toc}

*Must Support* on any data element SHALL be interpreted as follows:

* As part of the notification message or a query result as specified by the [Da Vinci Notifications CapabilityStatements], the  Sender SHALL be capable of including the data elements defined in the Da Vinci Notification profiles that have a MustSupport flag.

* The Recipient/Intermediary SHALL be capable of processing resource instances containing the data elements without generating an error or causing the application to fail. In other words Recipient/Intermediary SHOULD be capable of processing the data elements (display, store, etc).

* In situations where information on a particular data element is not present and the reason for absence is unknown, the Sender SHALL NOT include the data elements in the resource instance as part of a $process-message operation or a query response.

* When receiving a notification or a query response from the Sender, the  Recipient/Intermediary SHALL interpret missing data elements within resource instances as data not present in the Sender's systems.

* In situations where information on a particular data element is missing and the  Sender knows the precise reason for the absence of data, the Sender SHALL provide the reason for the missing information using values (such as nullFlavors) from the value set where they exist or using the dataAbsentReason extension.

* Notification Recipient/Intermediary SHALL be able to process resource instances containing data elements asserting missing information without generating an error or causing the application to fail.


##### This guide adopts the following definitions of Must Support for all transactions between the Intermediary and Recipient
{:.no_toc}

*Must Support* on any data element SHALL be interpreted as follows:

- As part of the alert notification or a query result as specified by the [Da Vinci Intermediary Server CapabilityStatement], the  Sender SHALL be capable of including the data elements defined in the Da Vinci Notification profiles that have a MustSupport flag.

- The  Recipient SHALL be capable of processing resource instances containing the data elements defined in the Da Vinci Notification profiles that have a MustSupport flag without generating an error or causing the application to fail. In other words, the Recipient SHOULD be capable of processing the data elements (displaying, storing, etc).

- In situations where information on a particular data element is not needed or considered protected information the Intermediary MAY remove the data elements in the resource instance when distributing the alert notification or responding to an n Recipient's query. The Intermediary MAY provide the reason for the missing information using values (such as nullFlavors) from the value set where they exist or using the dataAbsentReason extension.

- The Recipient SHALL be able to process resource instances containing missing data elements and data elements asserting missing information without generating an error or causing the application to fail.

#### GraphDefinition

All elements in the Da Vinci Notification GraphDefinition have a [Da Vinci Notifications Must Support Extension]. Systems claiming to conform to a GraphDefinition must "support" the link as defined below:

##### This guide adopts the following definitions of Must Support for all *direct* transactions between the Sender and Recipient or Intermediary
{:.no_toc}

*Must Support* on any link SHALL be interpreted as follows:

* The Sender SHALL be capable of including the profile defined by the link in the Da Vinci GraphDefinition that have a MustSupport flag in the bundle instance as part of a $process-message operation.

* The Recipient/Intermediary SHALL be capable of processing the profile instances referred to by the link without generating an error or causing the application to fail. In other words Recipient/Intermediary SHOULD be capable of processing the profile (display, store, etc).

* In situations where information on a particular link profile is not present and the reason for absence is unknown, the Sender SHALL NOT include the profile in the bundle instance as part of a $process-message operation.

##### This guide adopts the following definitions of Must Support for all transactions between the Intermediary and Recipient
{:.no_toc}

*Must Support* on any link SHALL be interpreted as follows:

* The Intermediary SHALL be capable of including the profile defined by the link in the Da Vinci GraphDefinition that have a MustSupport flag in the bundle instance as part of a $process-message operation.

* The Recipient SHALL be capable of processing the profile instances referred to by the link without generating an error or causing the application to fail. In other words Recipient/Intermediary SHOULD be capable of processing the profile (display, store, etc).

- In situations where information on a particular data element is not needed or considered protected information the Intermediary MAY remove the profile instance from the bundle when distributing the notification. The Intermediary MAY provide the reason for the missing information using the dataAbsentReason extension.

- The Recipient SHALL be able to process bundle instances containing missing profiles and data elements asserting missing information without generating an error or causing the application to fail.

---

{% include link-list.md %}
