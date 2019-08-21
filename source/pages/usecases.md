---
title: Da Vinci Alerts Patient Admit/Discharge Use Case
layout: default
active: usecases
---

{:.no_toc}

<!-- TOC  the css styling for this is \pages\assets\css\project.css under 'markdown-toc'-->

* Do not remove this line (it will not be displayed)
{:toc}

###  Introduction

This use case demonstrates how the Da Vinci Alerts IG framework is implemented to transact an alert between an Alert Sender/Intermediary and an Alert Recipient/Intermediary.

### Use Case Background

Having the ability to send a notifications to update physicians and care management teams when a patient is admitted to a hospital or discharged from the hospital is key to improving patient care. The intent of these alerts is not to replace existing data exchange mechanisms, for example the discharge summary; but rather to notify of the discharge event and provide enough data to gather more information, if desired. These notifications improve post-discharge transitions, promote communication between providers and encourage follow up care.

The Provider is notified when:

- A Patient is admitted to the hospital for inpatient or emergency care
- A Patient is discharged from the hospital

<!--
- A Patient is transferred from one care unit to another
-->

### Graph of FHIR Resources

The following resource graph in figure 7 defines the resources that support the admission and discharge alerts use case.  Communication, Patient, Encounter, and Condition are the primary resources (indicated by the black borders) which are transacted in the Alert Bundle to notify the provider of when the event has occurred. The other associated resources such as Location, Practitioner and Organization can be accessed after receiving the notification through a subsequent FHIR read or search interaction.  Note that the boxes with several resources inside them represents a choice.

{% include img-portrait.html img="Alert for Admission and Discharge Resource Graph.svg" caption="Figure 7" %}

### Push Alert Notification

In the following interaction shown in figures 8 and 9, the HealthCare facility is acting in the role of the Alert Sender and the Alert Recipient can be any of the actors listed in figure 1 on the home page.  To notify the Alert Recipients/Intermediary of an admit or discharge event, the Alert Sender uses $notify operation to submit the Alert Bundle to appropriate FHIR endpoints. As shown in figure 3, when an Intermediary successfully receives the notifications, it subsequently redistributes the data the end users.

{% include img-portrait.html img="admit_flow.svg" caption="Figure 8" %}

---

{% include img-portrait.html img="admit_intermediary_flow.svg" caption="Figure 9" %}

---

**Example Transaction**
{% include examplebutton_default.html example="notify-example" b_title = "Click Here To See Example PUSH Alert Notification" %}
<br />

<!--{% raw %}

### FHIR Subscription Based Notification

The interaction diagram in figure 5 and 6 on the [Framework] page illustrates the sequences of events for subscribing for ADT Alerts and the subsequent notifications when the the event occurs.

{:.note-to-balloters}
Note to Balloters: We are actively seeking input on what additional work is needed to determine the best way to implement subscriptions for alert notification. See the [FHIR Subscription Based Notification] framework for further details.

{% endraw %}-->

## FHIR Messaging

Using the [FHIR Messaging paradigm] to send a *Da Vinci Alert Message Bundle* to the Recipient.  There are several transport mechanisms that can be used.  One way is to use the [`$process-message`] operation on FHIR Server Restful endpoint.

### Graph of FHIR Resources

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

- [Example Da Vinci Alert Message Bundle](Bundle-201908201155.55-admit-01.html)


**Example Transaction**
The following transaction show an example of using the `$process-message` operation to send a Da Vinci Alert Message Bundle:

{% include examplebutton_default.html example="process-message-example" b_title = "Click Here To See Example Alert Notification" %}
<br />

### Comparison of the Communication Profile to the MessageHeader Profile

The MessageHeader is the first resource in the Da Vinci Alert Message Bundle and serves the same function as Communication resources in the Alert Bundle above, providing the necessary context for the alert reason together with various resources pointed to or indirectly connected to it:

- [Example Da Vinci Alert MessageHeader](MessageHeader-admit-1.html)

In the figure below the key elements in the Da Vinci Communication Profile are mapped to their equivalent elements in the MessageHeader resource in order to compare and contrast these FHIR object for this use case.

{% include img-portrait.html img="comm_msg_map.svg" caption="Figure 9" %}



{% include link-list.md %}
