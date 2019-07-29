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
{:.self-link}

FHIR resources can be used to transport patient information relevant to a specific event (e.g. admission, discharge, change in treatment, new diagnosis) to another provider or the health plan to communicate the details of where care was delivered and help to ensure timely follow-up as needed.  This information can be used to build an encounter record in the receiving system with appropriate provenance and make it available to CDS and other local services. *For the initial phase*, alerts are transacted using the Da Vinci [`$notify`] operation to push directly to “registered” Alert Recipient or Alert Intermediary.

This project recognizes the impact of the [Argonaut Clinical Data Subscriptions] project which is working on event based subscriptions and major revisions to the Subscription resource for FHIR R5. In a future version this guide, a subscription based notification is planned which will align with the outcomes of the Argonaut project.
{:.note-to-balloters}

### Must Support

All elements in the Da Vinci Alert profiles have a [MustSupport flag]. Systems claiming to conform to a profile must "support" the element as defined herein:

#### This guide adopts the following definitions of Must Support for all *direct* transactions between the Alert Sender and Alert Recipient or Alert Intermediary
{:.no_toc}

*Must Support* on any data element SHALL be interpreted as follows:

* As part of the alert notification or a query result as specified by the [Da Vinci Alert Sender CapabilityStatement], the Alert Sender SHALL be capable of including the data elements defined in the Da Vinci Alert profiles that have a MustSupport flag.

* Alert Recipient/Intermediary SHALL be capable of processing resource instances containing the data elements without generating an error or causing the application to fail. In other words Alert Recipient/Intermediary SHOULD be capable of processing the data elements (display, store, etc).

* In situations where information on a particular data element is not present and the reason for absence is unknown, Alert Sender SHALL NOT include the data elements in the resource instance returned as part of the query results.

* When receiving an alert notification or querying Alert Senders, the Alert Recipient/Intermediary SHALL interpret missing data elements within resource instances as data not present in the US Core Responder's systems.

* In situations where information on a particular data element is missing and the US Core Responder knows the precise reason for the absence of data, Alert Sender SHALL send the reason for the missing information using values (such as nullFlavors) from the value set where they exist or using the dataAbsentReason extension.

* Alert Recipient/Intermediary SHALL be able to process resource instances containing data elements asserting missing information.

* NOTE: *Alert Sender* = Server and *Alert Recipient/Intermediary* = Client

#### This guide adopts the following definitions of Must Support for all transactions between the Alert Intermediary and Alert Recipient
{:.no_toc}

*Must Support* on any data element SHALL be interpreted as follows:

- As part of the alert notification or a query result as specified by the [Da Vinci Intermediary Server CapabilityStatement], the Alert Sender SHALL be capable of including the data elements defined in the Da Vinci Alert profiles that have a MustSupport flag.

- The Alert Recipient SHALL be capable of processing resource instances containing the data elements the data elements defined in the Da Vinci Alert profiles that have a MustSupport flag without generating an error or causing the application to fail. In other words, the Alert Recipient SHOULD be capable of processing the data elements (displaying, storing, etc).

- In situations where information on a particular data element is not needed or considered protected information the Alert Intermediary MAY remove the data elements in the resource instance returned as part of the query results. The Alert Intermediary MAY send the reason for the missing information using values (such as nullFlavors) from the value set where they exist or using the dataAbsentReason extension.

- The Alert Recipient SHALL be able to process resource instances containing missing data elements and data elements asserting missing information.

* NOTE: *Alert Intermediary* = Server and *Alert Recipient* = Client



### Preconditions and Assumptions

#### Preconditions

- There is an event that drives the generation of the Alert.
- An Alert will be generated for each patient separately.
  - The event can be for one or more patients.
- The Alert Sender has access to the Alert Recipients/Intermediary FHIR endpoints.
- System level trust exists between the actors.
  - Clients have been authorized by the servers.
  - It is assumed that consent is managed elsewhere.
- A secure information transport mechanism exists between the actors.

#### Assumptions

- Based on FHIR R4 and US Core R4 profiles where applicable.
- Alerts are transacted to an operation endpoint ($notify).
- The Da Vinci Alerts Bundle Profile is the FHIR object that is exchanged for all alert transactions.
  - The Da Vinci Alerts Communication Profile is always part of the bundle and provides the necessary context for the alert reason.

### Alert Bundle

The FHIR resources used in Da Vinci Alert transactions form a network through their relationships with each other - either through a direct reference to another resource or through a chain of intermediate references. These groups of resources are referred to as resource graphs. The FHIR Alert resource graph for the admit and discharge use case is shown in [Figure 7].

For every alert notification, the FHIR object that is exchanged is the [Da Vinci Alert Bundle Profile]. This bundle is a [`transaction`] type bundle that is POSTed to the Alert Recipient's or Intermediary's FHIR endpoint via a the $notify operation. The complete set of content to make up an Alert Bundle includes the [Da Vinci Alerts Communication Profile] which provides the necessary context for the alert reason together with various resources pointed to or indirectly connected to the Communication profile, all gathered together into a Bundle for transport and persistence.  Resources associated with the following list of Communication references SHALL be included in the Bundle:

- `Communication.subject` (Patient resource)
- `Communication.encounter` (Encounter Resource )
-  All supporting data (resources) for each kind of alert is referenced in `Communication.payload`

The following Table summarizes the Alert Scenarios and the Resources that may be referenced in the [Da Vinci Communication Profile] payload element and included in the alert Bundle:

{% include alert_scenarios.md %}
{: .grid}

Note to Balloters: The resources listed for scenarios that are not part of the initial phase are suggestions and will be reviewed and updated when these scenarios are added in future iterations of this IG.
{:.note-to-balloters}

[Example of an Alert Bundle](Bundle-admit-01.html) for a patient admission.

### Push Alert Notification

As shown in Figure 4a and 4b, When an event or request triggers an alert, the Alert Sender creates an Alert bundle and notifies the Alert Recipient or Alert Intermediary using the [Da Vinci Notify Operation] operation. The body of this operation is a Parameter resource consisting of a single parameter with two nested parts containing:

1. The Alert Bundle containing the required Alert Communication profile and required resources for this Alert event use case. The table in the previous section lists for each alert scenario, the relevant resources to be included in the Alert Bundle and referenced in the `Communication.payload` element.

1. The [Da Vinci Alerts Endpoint Profile] which is intended only for the *direct* recipient of the operation and provides the recipient with the technical details for getting additional information from the medical record for the alert.

    Note that an authentication token may be supplied in `Endpoint.header` by the Alert Sender to allow direct recipients of the Alert (whether an Alert Recipient or Alert Intermediary) to access additional information. This and other supplied headers, if any are given, are appended to the GET request. Sending these tokens has obvious security consequences. The server and client are responsible for ensuring that the content is appropriately secured.

In the context of the `$notify` operation, the Alert Recipient/Intermediary is treated as a ["black box"] and simply accepts and processes the submitted data and there are no further expectations. The response to the operation and the transaction Bundle are defined in the FHIR specification.

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
