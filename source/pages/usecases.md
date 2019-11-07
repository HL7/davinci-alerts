---
title: Da Vinci Notifications Patient Admit/Discharge Use Case
layout: default
active: usecases
---

{:.no_toc}

<!-- TOC  the css styling for this is \pages\assets\css\project.css under 'markdown-toc'-->

* Do not remove this line (it will not be displayed)
{:toc}

###  Introduction

This use case demonstrates how the Da Vinci Notifications IG framework is implemented to transact an notification between a Sender and a Recipient/Intermediary.

### Use Case Background

Having the ability to send a notifications to update physicians and care management teams when a patient is admitted to a hospital or discharged from the hospital is key to improving patient care. The intent of these notifications is not to replace existing data exchange mechanisms, for example the discharge summary; but rather to notify of the discharge event and provide enough data to gather more information, if desired. These notifications improve post-discharge transitions, promote communication between providers and encourage follow up care.

The Provider is notified when:

- A Patient is admitted to the hospital for inpatient or emergency care
- A Patient is discharged from the hospital

<!--
- A Patient is transferred from one care unit to another
-->

### Graph of FHIR Resources

the following tables summarizes the additional Resources that directly or indirectly referenced  and included in the message or available in a subsequent query by the Intermediary or Recipient

{: .grid}
| ﻿Notification Scenarios | Resources in Notification Bundle | Searchable Resources|
|---|---|---|
| Emergency and Inpatient Admissions | US Core R4 Condition |Location, Coverage, Practitioner (sender), Organization (sender), PractitionerRole (sender)|
| Emergency and Inpatient Discharges | US Core R4 Condition |Location, Coverage, Practitioner (sender), Organization (sender), PractitionerRole (sender) |


This resource graph defines the resources that support the admission and discharge alerts use case using FHIR messaging. MessageHeader, Patient, Encounter, and Condition are the primary resources (indicated by the black borders) which are messaged in the Da Vinci Notification Message Bundle to notify the provider of when the event has occurred. The Endpoint Resource can be optionally included in the bundle to allow the Recipient to optionally query other associated resources such as Location, Practitioner and Organization  through a subsequent FHIR read or search interaction (TODO this needs further testing and discussion).  Note that the boxes with several resources inside them represents a choice.

{% include img-portrait.html img="admit_message_graph.svg" caption="Figure 3" %}

- \* it is questionable whether Encounter.diagnosis.condition has been implemented by the EHR vendors - need to discuss with vendors.
- \** There is no Practitioner.endpoint element and an extension may be needed to implement.
- \*** MessageDefinition is used to formally define the Message content for a given event (e.g, an inpatient admission or discharge).  It defines the event and the focal and non focal Resources/Profiles that make up the message:

    - [Example Da Vinci Notification MessageDefinition](MessageDefinition-admit-1.html)

    The GraphDefinition is referenced by the MessageDefinition and it defines the links between the all resources that are contained within the message.

    - [Example Da Vinci Notification GraphDefinition](GraphDefinition-admit-1.html)

**Example Da Vinci Notification Message Bundle**

- [Example Da Vinci Notification Message Bundle](Bundle-message-admit-01.html)


### Push Notification Notification

In the following interaction shown in figures 8 and 9, the HealthCare facility is acting in the role of the Notification Sender and the Notification Recipient can be any of the actors listed in figure 1 on the home page.  To notify the Notification Recipients/Intermediary of an admit or discharge event, the Notification Sender uses $notify operation to submit the Notification Bundle to appropriate FHIR endpoints. As shown in figure 3, when an Intermediary successfully receives the notifications, it subsequently redistributes the data the end users.

{% include img-portrait.html img="admit_flow.svg" caption="Figure 8" %}

---

{% include img-portrait.html img="admit_intermediary_flow.svg" caption="Figure 9" %}

---

**Example Transaction**
{% include examplebutton_default.html example="process-message-example" b_title = "Click Here To See Example Notification " %}
<br />

<!--{% raw %}

### FHIR Subscription Based Notification

The interaction diagram in figure 5 and 6 on the [Framework] page illustrates the sequences of events for subscribing for ADT Notifications and the subsequent notifications when the the event occurs.

{:.note-to-balloters}
Note to Balloters: We are actively seeking input on what additional work is needed to determine the best way to implement subscriptions for notification notification. See the [FHIR Subscription Based Notification] framework for further details.

{% endraw %}-->





{% include link-list.md %}
