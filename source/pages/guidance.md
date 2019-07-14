---
title: General Guidance and Definitions
layout: default
active: guidance

---

{:.no_toc}

<!-- TOC  the css styling for this is \pages\assets\css\project.css under 'markdown-toc'-->

* Do not remove this line (it will not be displayed)
{:toc}

### Introduction
{:.self-link}

FHIR resources can be used to transport patient information relevant to a specific event (e.g. admission, discharge, change in treatment, new diagnosis) to another provider or the health plan to communicate the details of where care was delivered and help to ensure timely follow-up as needed.  This information can be used to build an encounter record in the receiving system with appropriate provenance and make it available to CDS and other local services. Da Vinci Alerts are transacted either using one of the following interactions:

1. A FHIR RESTful push directly to “registered” Alert Recipient or via an Alert Intermediary.  
1. A FHIR based subscription with notifications being sent to a subscriber who is the Alert Recipient or Alert Intermediary.

### Preconditions and Assumptions

#### Preconditions

- There is an event that drives the generation of the Alert.
- An Alert will be generated for each patient separately.
  - The event can be for one or more patients
- FHIR R4 RESTful endpoints exist for all actors.
  - Note that this is a requirement for FHIR RESTful Push transactions and for RestHook channel transactions when using the FHIR subscriptions.  It is not required for other type of subscription channels or FHIR messaging.
- System level trust exists between the actors.
  - Clients have been authorized by the servers.
  - It is assumed that consent is managed elsewhere.
- “Endpoint Discovery” i.e., a curated list of where to forward the data  is actively maintained and managed by the Alert Senders and Intermediaries.  These interactions are outside the scope of this specification.
   - Note that this is needed when transacting alerts using FHIR RESTful push notifications.


#### Assumptions
- Based on FHIR R4 and US Core R4 profiles where applicable
- Alerts are transacted either using a FHIR RESTful push or FHIR subscriptions.
- The “Alert Bundle” is the FHIR object that is exchanged for all alert transactions.
  - The [DaVinci Communication Resource Profile] is always part of the bundle and provides the necessary context for the alert reason.

### Alert Bundle

The FHIR resources used in Da Vinci Alert transactions form a network through their relationships with each other - either through a direct reference to another resource or through a chain of intermediate references. These groups of resources are referred to as resource graphs. The FHIR Alert resource graph for the admit and discharge use case is shown in [Figure 2-1]

Whether as a direct push based transaction or via subscription notification, a common “Alert Bundle” is the FHIR object that is exchanged. This bundle is a [`transaction`] type bundle that is POSTed to the Alert Recipient's or Intermediary's FHIR endpoint. The complete set of content to make up an Alert Bundle includes the [DaVinci Communication Resource Profile] which provides the necessary context for the alert reason together with various resources pointed to or indirectly connected to the Communication profile, all gathered together into a Bundle for transport and persistence.  Resources associated with the following list of Communication references SHALL be included in the Bundle:

- `Communication.subject` (Patient resource)
- `Communication.encounter` (Encounter Resource )
-  All supporting data (resources) for each kind of alert is referenced in `Communication.payload`

The following Table summarizes the Alert Scenarios and the Resources that may be referenced in the [Da Vinci Communication Profile] payload element and included in the alert Bundle:

{% include alert_scenarios.md %}
{: .grid}

[Example of an Alert Bundle](Bundle-admit-01.html) for a patient admission.

### Push Alert Notification

The FHIR RESTful PUSH transaction provides a way for a Alert Sender to submit data-of-interest for a particular alert to the Alert Recipient. There is no expectation that the data submitted represents all the data required by the the Alert Reveiver, only that the data is known to be relevant to the triggering event.

The table in the previous section list the relevant resources to be included in the Alert Bundle and referenced in the `Communication.payload` element for a particular Alert scenario.   The Alert Recipient simply accepts the submitted data and there is no further expectations. The response to this transaction interactions are defined in the base [FHIR specification].

Note to Balloters: We are actively seeking input on what expectations should be defined for Alert delivery. Specifically sender side error handling and receiver side error handling.
{:.note-to-balloters}

{% include img.html img="push_transaction.svg" caption="Figure 4" %}

##### Usage
{:.no_toc}

The Alert Sender notifies the Alert Recipient by pushing the Alert Bundle using the `transaction` interaction as follows:

`POST [base] {?_format=[mime-type]}`

{% include examplebutton_default.html example="push_example" b_title = "Click Here To See Example PUSH Alert Notification" %}

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



---

{% include link-list.md %}
