---
title: Da Vinci Alerts Patient Admit/Discharge Use Case
layout: default
active: guidance
---

###  Introduction

The use case demonstrates the protocols by the Da Vinci Alerts are transacted between an Alert Sender/Intermediary and an Alert Receiver/Intermediary.

### Use Case Background

Having the ability to send a notifications to update physicians and care management teams when a patient is admitted to a hospital, transferred to another facility, or discharged from the hospital is key to improving patient care. These notifications improve post-discharge transitions, promote communication between providers and encourage follow up care.

The Provider is notified when:

- A Patient is admitted to the hospital for inpatient or emergency care
- A Patient is discharged from the hospital
- A Patient is transferred from one care unit to another

### Graph of FHIR Resources

The following resource graph defines the resources that support the admit/discharge alerts use case.  Communication, Patient, Encounter, and Condition are the primary resources which are transacted in the Alert Bundle to notify the provider of when ADT event has occurrd.  They are indicated using a black outline. The other associated resources such as Location, Practitioner and Organization can be accessed after receiving the notification through a subsequent FHIR read or search interaction.  Note that resource outlined in boxes represent a choice of one of the resources.

{% include img-portrait.html img="Alert for Admission and Discharge Resource Graph.svg" caption="Figure 1" %}

### Push Alert Notification

TODO narrative...

{% include img-portrait.html img="admit_flow.svg" caption="Figure 2" %}

{% include img-portrait.html img="admit_intermediary_flow.svg" caption="Figure 3" %}

{% include examplebutton_default.html example="push_example" b_title = "Click Here To See Example PUSH Alert Notification" %}
<br />

{% include link-list.md %}
