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

FHIR resources can be used to transport patient information relevant to a specific event (e.g. admission, discharge, change in treatment, new diagnosis) to another provider or the health plan to communicate the details of where care was delivered and help to ensure timely follow-up as needed.  This information can be used to build an encounter record in the receiving system with appropriate provenance and make it available to CDS and other local services. *For the initial phase*, alerts are transacted using the Da Vinci [`$notify`] operation to to push directly to “registered” Alert Recipient or Alert Intermediary.

This project recognizes the impact of the [Argonaut Clinical Data Subscriptions] project which is working on event based subscriptions and major revisions to the Subscription resource for FHIR R5. In a future version this guide, a subscription based notification is planned which will align with the outcomes of the Argonaut project.
{:.note-to-balloters}

### Preconditions and Assumptions

#### Preconditions

- There is an event that drives the generation of the Alert.
- An Alert will be generated for each patient separately.
  - The event can be for one or more patients
- The Alert Sender has access to the Alert Recipients/Intermediary FHIR endpoints.
- System level trust exists between the actors.
  - Clients have been authorized by the servers.
  - It is assumed that consent is managed elsewhere.
- A secure information transport mechanism exists between the actors.

#### Assumptions
- Based on FHIR R4 and US Core R4 profiles where applicable
- Alerts are transacted to an operation endpoint ($notify).
- The Da Vinci Alerts Bundle Profile is the FHIR object that is exchanged for all alert transactions.
  - The Da Vinci Alerts Communication Profile is always part of the bundle and provides the necessary context for the alert reason.

### Alert Bundle

The FHIR resources used in Da Vinci Alert transactions form a network through their relationships with each other - either through a direct reference to another resource or through a chain of intermediate references. These groups of resources are referred to as resource graphs. The FHIR Alert resource graph for the admit and discharge use case is shown in [Figure 7]

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

The [`$notify`] operation provides a way for an Alert Sender to submit data-of-interest in an Alert Bundle to the Alert Recipient. There is no expectation that the data submitted represents all the data required by the the Alert Recipient, only that the data is known to be relevant to the triggering event.

The table in the previous section list the relevant resources to be included in the Alert Bundle and referenced in the `Communication.payload` element for a particular Alert scenario.   The Alert Recipient simply accepts and process the submitted data and there is no further expectations. The response to the `$notify` operation and the transaction Bundle are defined in the FHIR specification.

Note to Balloters: We are actively seeking input on what expectations should be defined for error handling and and whether there is a need to support "Guaranteed Delivery"
{:.note-to-balloters}

{% include img.html img="push_transaction.svg" caption="Figure 4" %}

##### Usage
{:.no_toc}

The `$notify` operation is invoked by the Alert Sender using the `POST` syntax with Alert Bundle in the request body:

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
