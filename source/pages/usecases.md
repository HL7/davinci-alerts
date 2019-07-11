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

The use case demonstrates the protocols by the Da Vinci Alerts are transacted between an Alert Sender/Intermediary and an Alert Receiver/Intermediary.

### Use Case Background

Having the ability to send a notifications to update physicians and care management teams when a patient is admitted to a hospital, transferred to another facility, or discharged from the hospital is key to improving patient care. These notifications improve post-discharge transitions, promote communication between providers and encourage follow up care.

The Provider is notified when:

- A Patient is admitted to the hospital for inpatient or emergency care
- A Patient is discharged from the hospital
- A Patient is transferred from one care unit to another

### Graph of FHIR Resources

The following resource graph in figure 1 defines the resources that support the ADT alerts use case.  Communication, Patient, Encounter, and Condition are the primary resources (indicated by the black borders) which are transacted in the Alert Bundle to notify the provider of when the event has occurred. The other associated resources such as Location, Practitioner and Organization can be accessed after receiving the notification through a subsequent FHIR read or search interaction.  Note that the boxes with several resources inside them represents a choice.

{% include img-portrait.html img="Alert for Admission and Discharge Resource Graph.svg" caption="Figure 1" %}

### Push Alert Notification

In the following interaction shown in figures 2 and 3, the HealthCare facility is acting in the role of the Alert Sender and the Alert Recipient can be any of the actors listed in figure 1 on the home page.  To notify the Alert Recipients/Intermediary of an ADT event, the Alert Sender uses a FHIR RESTful push to submit the Alert Bundle to appropiate FHIR endpoints. As shown in figure 3, when an Intermediary successfully receives the notifications, it then subsequently notifies the the Alert Recipients using the same push protocol.

Note to Balloters: We are actively seeking input on whether this guide should limit the expectations of how Alert Intermediaries forward the alerts to the Alert Recievers.  For example using existing data transport protocols such as Direct, SMS or V2 messaging.
{:.note-to-balloters}

{% include img-portrait.html img="admit_flow.svg" caption="Figure 2" %}

---

{% include img-portrait.html img="admit_intermediary_flow.svg" caption="Figure 3" %}

---

**Example Transaction**
{% include examplebutton_default.html example="push_example" b_title = "Click Here To See Example PUSH Alert Notification" %}
<br />

### FHIR Subscription Based Notification

The interaction diagram in figure 4 illustrates the sequences of events for subscribing for ADT Alerts and the subsequent notifications when the the event occurs. Figure 5 depicts the same interactions using an Alert intermediary. the HealthCare facility is acting in the role of the Alert Sender (in a subscription protocol more commonly known as a the subscription publisher) and the Alert Recipient (in a subscription protocol more commonly known as a the subscriber) can be any of the actors listed in figure 1 on the home page.

{% include img-portrait.html img="Basic.jpg" caption="Figure 4" %}

---

{% include img-portrait.html img="Generic.svg" caption="Figure 5" %}

---

**Example Transaction**
{% include examplebutton_default.html example="example" b_title = "Click Here To See Example Subscription Alert Notification" %}
<br />

{% include link-list.md %}
