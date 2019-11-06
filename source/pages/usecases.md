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

The following resource graph in figure 7 defines the resources that support the admission and discharge notifications use case.  Communication, Patient, Encounter, and Condition are the primary resources (indicated by the black borders) which are transacted in the Notification Bundle to notify the provider of when the event has occurred. The other associated resources such as Location, Practitioner and Organization can be accessed after receiving the notification through a subsequent FHIR read or search interaction.  Note that the boxes with several resources inside them represents a choice.

{% include img-portrait.html img="Notification for Admission and Discharge Resource Graph.svg" caption="Figure 7" %}

### Push Notification Notification

In the following interaction shown in figures 8 and 9, the HealthCare facility is acting in the role of the Notification Sender and the Notification Recipient can be any of the actors listed in figure 1 on the home page.  To notify the Notification Recipients/Intermediary of an admit or discharge event, the Notification Sender uses $notify operation to submit the Notification Bundle to appropriate FHIR endpoints. As shown in figure 3, when an Intermediary successfully receives the notifications, it subsequently redistributes the data the end users.

{% include img-portrait.html img="admit_flow.svg" caption="Figure 8" %}

---

{% include img-portrait.html img="admit_intermediary_flow.svg" caption="Figure 9" %}

---

**Example Transaction**
{% include examplebutton_default.html example="notify-example" b_title = "Click Here To See Example PUSH Notification Notification" %}
<br />

<!--{% raw %}

### FHIR Subscription Based Notification

The interaction diagram in figure 5 and 6 on the [Framework] page illustrates the sequences of events for subscribing for ADT Notifications and the subsequent notifications when the the event occurs.

{:.note-to-balloters}
Note to Balloters: We are actively seeking input on what additional work is needed to determine the best way to implement subscriptions for notification notification. See the [FHIR Subscription Based Notification] framework for further details.

{% endraw %}-->





{% include link-list.md %}
