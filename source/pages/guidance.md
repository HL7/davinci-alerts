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

All elements in the Da Vinci Alert profiles have a [MustSupport flag]. Systems claiming to conform to a profile must "support" the element as defined herein:

#### This guide adopts the following definitions of Must Support for all *direct* transactions between the Alert Sender and Alert Recipient or Alert Intermediary
{:.no_toc}

*Must Support* on any data element SHALL be interpreted as follows:

* As part of the alert notification or a query result as specified by the [Da Vinci Alerts CapabilityStatements], the Alert Sender SHALL be capable of including the data elements defined in the Da Vinci Alert profiles that have a MustSupport flag.

* Alert Recipient/Intermediary SHALL be capable of processing resource instances containing the data elements without generating an error or causing the application to fail. In other words Alert Recipient/Intermediary SHOULD be capable of processing the data elements (display, store, etc).

* In situations where information on a particular data element is not present and the reason for absence is unknown, Alert Sender SHALL NOT include the data elements in the resource instance returned as part of a $notify alert notification or a query response.

* When receiving an alert notification or a query response from the Alert Sender, the Alert Recipient/Intermediary SHALL interpret missing data elements within resource instances as data not present in the Alert Sender's systems.

* In situations where information on a particular data element is missing and the Alert Sender knows the precise reason for the absence of data, Alert Sender SHALL provide the reason for the missing information using values (such as nullFlavors) from the value set where they exist or using the dataAbsentReason extension.

* Alert Recipient/Intermediary SHALL be able to process resource instances containing data elements asserting missing information without generating an error or causing the application to fail.

<!-- * NOTE: *Alert Sender* = Server and *Alert Recipient/Intermediary* = Client -->

#### This guide adopts the following definitions of Must Support for all transactions between the Alert Intermediary and Alert Recipient
{:.no_toc}

*Must Support* on any data element SHALL be interpreted as follows:

- As part of the alert notification or a query result as specified by the [Da Vinci Intermediary Server CapabilityStatement], the Alert Sender SHALL be capable of including the data elements defined in the Da Vinci Alert profiles that have a MustSupport flag.

- The Alert Recipient SHALL be capable of processing resource instances containing the data elements the data elements defined in the Da Vinci Alert profiles that have a MustSupport flag without generating an error or causing the application to fail. In other words, the Alert Recipient SHOULD be capable of processing the data elements (displaying, storing, etc).

- In situations where information on a particular data element is not needed or considered protected information the Alert Intermediary MAY remove the data elements in the resource instance when distributing the alert notification or responding to an Alert Recipient's query. The Alert Intermediary MAY provide the reason for the missing information using values (such as nullFlavors) from the value set where they exist or using the dataAbsentReason extension.

- The Alert Recipient SHALL be able to process resource instances containing missing data elements and data elements asserting missing information without generating an error or causing the application to fail.

<!-- * NOTE: *Alert Intermediary* = Server and *Alert Recipient* = Client -->



### Preconditions and Assumptions

#### Preconditions

- There is an event that drives the generation of the Alert.
- An Alert will be generated for each patient separately.
  - The event can be for one or more patients.
- The Alert Sender has access to the Alert Recipients/Intermediary FHIR endpoints.
- System level trust exists between the actors.
  - Clients have been authorized by the servers.
  - It is assumed that consent is managed elsewhere.
  - Patient consent allows exchange of data between the relevant systems.
- A secure information transport mechanism exists between the actors.

#### Assumptions

- Based on FHIR R4 and US Core R4 profiles where applicable.
- Alerts are transacted to an operation endpoint ($notify).
- The Da Vinci Alerts Bundle Profile is the FHIR object that is exchanged for all alert transactions.
  - The Da Vinci Alerts Communication Profile is always part of the bundle and provides the necessary context for the alert reason.

### Alert Bundle

The FHIR resources used in Da Vinci Alert transactions form a network through their relationships with each other - either through a direct reference to another resource or through a chain of intermediate references. These groups of resources are referred to as resource graphs. The FHIR Alert resource graph for the admit and discharge use case is shown in [Figure 7].

{:.note-to-balloters}
Note to Balloters: We are seeking input on the Bundle type to use this context.   Both `transaction`, and `collection` were considered.  Although `transaction` (and `transaction-response`) provides some additional confirmation of delivery, the required .request.method element places additional expectations on the server responding to the `$notify` transaction.  In contrast, the `collection` type imposes no processing obligations or behavioral rules beyond persistence, including any confirmation confirmation of delivery beyond the http status.

For every alert notification, the FHIR object that is exchanged is the [Da Vinci Alert Bundle Profile]. This bundle is a [`collection`] type bundle that is POSTed to the Alert Recipient's or Intermediary's FHIR endpoint via a the $notify operation. The complete set of content to make up an Alert Bundle includes the [Da Vinci Alerts Communication Profile] which provides the necessary context for the alert reason together with various resources pointed to or indirectly connected to the Communication profile, all gathered together into a Bundle for transport and persistence.  Resources associated with the following list of Communication references SHALL be included in the Bundle:

- `Communication.subject` (Patient resource)
- `Communication.encounter` (Encounter Resource )
-  All supporting data (resources) for each kind of alert is referenced in `Communication.payload`

The following Table summarizes the Alert Scenarios and the Resources that may be referenced in the [Da Vinci Communication Profile] payload element and included in the alert Bundle:

{: .grid}
| ﻿Alert Scenarios | Resources in Alert Bundle<sup>(1)</sup> | Searchable Resources<sup>(2)</sup> |
|---|---|---|
| Emergency and Inpatient Admissions | US Core R4 Condition |Location, Coverage, Practitioner (sender), Organization (sender), PractitionerRole (sender)|
| Emergency and Inpatient Discharges | US Core R4 Condition |Location, Coverage, Practitioner (sender), Organization (sender), PractitionerRole (sender) |

---

[Example of an Alert Bundle](Bundle-communication-alert-admit-01.html) for a patient admission.

---

{:.note-to-balloters}
Note to Balloters: These scenarios may be added in future iterations of this IG.

{:.note-to-balloters .grid}
| ﻿Alert Scenarios | Resources in Alert Bundle<sup>(1)</sup> | Searchable Resources<sup>(2)</sup> |
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

---

footnotes:

(1): In addition to Patient and Encounter which are included in all Alert Bundles.

(2): Minimum set of the patient's Resources that are Available for Optional Subsequent Queries.


### Push Alert Notification

As shown in Figure 4a and 4b, When an event or request triggers an alert, the Alert Sender creates an Alert bundle and notifies the Alert Recipient or Alert Intermediary using the [Da Vinci Notify Operation] operation. The body of this operation is a Parameter resource consisting of a single parameter with two nested parts containing:

1. The Alert Bundle containing the required Alert Communication profile and required resources for this Alert event use case. The table in the previous section lists for each alert scenario, the relevant resources to be included in the Alert Bundle and referenced in the `Communication.payload` element.

1. The [Da Vinci Alerts Endpoint Profile] which is intended only for the *direct* recipient of the operation and provides the recipient with the technical details for getting additional information from the medical record for the alert.

    Note that an authentication token may be supplied in `Endpoint.header` by the Alert Sender to allow direct recipients of the Alert (whether an Alert Recipient or Alert Intermediary) to access additional information. This and other supplied headers, if any are given, are appended to the GET request. Sending these tokens has obvious security consequences. The server and client are responsible for ensuring that the content is appropriately secured.

In the context of the `$notify` operation, the Alert Recipient/Intermediary is treated as a ["black box"] and simply accepts and processes the submitted data and there are no further expectations. The response to the operation and the collection Bundle are defined in the FHIR specification.

Note to Balloters: We are actively seeking input on what expectations should be defined for error handling and and whether there is a need to support ["reliable delivery"]
{:.note-to-balloters}

Since the parameter can repeat a single operation transaction may contain multiple alerts. There is no expectation that the data submitted represents all the data required by the Alert Recipient/Intermediary, only that the data is known to be relevant to the triggering event. The Alert Recipient/Intermediary can optionally fetch additional information from the patient's medical record using FHIR RESTful searches.  The endpoint for this search may be known or supplied via the $notify operation payload.

As shown in figure 4b, after the Alert Intermediary successfully receives the notification, processes the Alert Bundle and optionally searches and process the seach results, it redistributes the data the end users.  It may use the `$notify` operation to do this, however the original Endpoint SHALL NOT be distributed.  Note that the Alert Intermediary may customize the content based on the end user (for example, withholding data that a particular care team member does not need).

Note to Balloters: We are actively seeking input on whether this guide should define the expectations of how Alert Intermediaries distribute the alert information to the Alert Recipients.  For example using existing data transport protocols such as Direct, SMS or V2 messaging.
{:.note-to-balloters}

{% include img.html img="push_alert_1.svg" caption="Figure 4a" %}
{% include img.html img="push_alert_2.svg" caption="Figure 4b" %}

#### APIs
{:.no_toc}

The following Da Vinci Alert FHIR artifacts are used in this transaction:

- [Da Vinci Alerts Bundle Profile]
- [Da Vinci Alerts Communication Profile]
- [Da Vinci Alerts Endpoint Profile]
- [Da Vinci Notify Operation]

#### Usage
{:.no_toc}

The `$notify` operation is invoked by the Alert Sender using the `POST` syntax with Parameter resource in the request body:

`POST [base]Communication/$notify`

{% include examplebutton_default.html example="notify-example" b_title = "Click Here To See Example PUSH Alert Notification" %}

## FHIR Messaging

An alternative consideration is to use the [FHIR Messaging paradigm] to send a Da Vinci Alert Message Bundle to the Recipient. There are several transport mechanisms that can be used. One way is to use the $process-message operation on FHIR Server Restful endpoint. This is analogous to the Alert Bundle $notify operation above using the $process-message operation in place of the $notify and a Da Vinci Alert Message Bundle structure instead of the Alert Bundle:

{% include img.html img="$process_message_wf.svg" caption="Figure 5" %}

The same Da Vinci Alert Message Bundle structure can be re-used as the notification payload for FHIR Subscription based alerts since a subscriber can register to receive [notifications by messaging]:

{% include img.html img="subscription_messaging_wf.svg" caption="Figure 6" %}


### Graph of FHIR Resources for Messaging

The following resource graph in figure 8 defines the resources that support the admission and discharge alerts use case using FHIR messaging. MessageHeader, Patient, Encounter, and Condition are the primary resources (indicated by the black borders) which are messaged in the Da Vinci Alert Message Bundle to notify the provider of when the event has occurred. The Endpoint Resource can be optionally included in the bundle to allow the Recipient to optionally query other associated resources such as Location, Practitioner and Organization  through a subsequent FHIR read or search interaction (TODO this needs further testing and discussion).  Note that the boxes with several resources inside them represents a choice.

{% include img-portrait.html img="admit_message_graph.svg" caption="Figure 8" %}

Note:

- \* it is questionable whether Encounter.diagnosis.condition has been implemented by the EHR vendors - need to discuss with vendors.
- \** There is no Practitioner.endpoint element and an extension may be needed to implement.
- \*** MessageDefinition is used to formally define the Message content for a given event (e.g, an inpatient admission or discharge).  It defines the event and the focal and non focal Resources/Profiles that make up the message:

    - [Example Da Vinci Alert MessageDefinition](MessageDefinition-admit-1.html)

    The GraphDefinition is referenced by the MessageDefinition and it defines the links between the all resources that are contained within the message.

    - [Example Da Vinci Alert GraphDefinition](GraphDefinition-admit-1.html)


The Bundle can be transacted similarly to the Alert bundle by posting to an operation endpoint using a RESTful POST transaction:

- [Example Da Vinci Alert Message Bundle](Bundle-message-admit-01.html)


**Example Transaction**
The following transaction show an example of using the `$process-message` operation to send a Da Vinci Alert Message Bundle:

{% include examplebutton_default.html example="process-message-example" b_title = "Click Here To See Example Alert Notification" %}
<br />

### Comparison of the Communication Profile to the MessageHeader Profile

The Messag eHeader is the first resource in the Da Vinci Alert Message Bundle and serves the same function as Communication resources in the Alert Bundle above, providing the necessary context for the alert reason together with various resources pointed to or indirectly connected to it:

{% include img-portrait.html img="comm_msg_map.svg" caption="Figure 9" %}

- [Example Da Vinci Alert MessageHeader](MessageHeader-admit-1.html)



<!--{% raw %}
### FHIR Subscription Based Notification

{:.note-to-balloters}
Note to Balloters: We are actively seeking input on what additional work is needed to determine the best way to implement subscriptions for alert notification.  This project recognizes the impact of the Argonaut work on Subscription for R5 and is considering what approach to take to align with that work.
<br /><br />
current proposals include:
<br /><br />
\1. criteria based on searching the resource that corresponds to the alert event  (for example Encounter for admit/discharge) with the expectation that the subscriber would perform a subsequent query to fetch the supporting data.
<br /><br />
\2. criteria based on searching the resource that corresponds to the alert event  (for example Encounter for admit/discharge) **plus** a graph definition to inform the server what Alert Bundle to return with the resource using the [$graph operation]
<br /><br />
\3. criteria based on searching `Encounter.status` and/or `Encounter.class`**plus** a graph definition to inform the server what Alert Bundle to return with the resource using the [$graph operation]
<br /><br />
\4. criteria based on searching `Communication.topic` **plus** a graph definition to inform the server what Alert Bundle to return with the resource using the [$graph operation]

<br />

The interaction diagram in figure 5 illustrates the sequences of events for subscribing for alerts and the subsequent notifications when the the event occurs.  The server (in a subscription protocol more commonly known as a the subscription publisher) can be either the Alert Sender or the Alert Intermediary. The client (in a subscription protocol more commonly known as a the subscriber) can be either the Alert Recipient or the Alert Intermediary.

{% include img-portrait-med.html img="basic_sub.svg" caption="Figure 5" %}

---

Figure 6 depicts additional subscription interactions for the Alert Intermediary when transacting with multiple servers.

{% include img-portrait-med.html img="add_intermediary_interactions.svg" caption="Figure 6" %}

---

**Example Transaction**
{% include examplebutton_default.html example="example" b_title = "Click Here To See Example Subscription Alert Notification" %}
<br />


{% endraw %}-->
---

{% include link-list.md %}
