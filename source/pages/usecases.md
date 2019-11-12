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

This use case demonstrates how the Da Vinci Notifications IG framework is used to define the Da Vinci Notification Bundle for admissions and discharge and how to send a notification between a Sender and a Recipient/Intermediary.

### Use Case Background

Having the ability to send a notifications to update physicians and care management teams when a patient is admitted to a hospital or discharged from the hospital is key to improving patient care. The intent of these notifications is *not* to replace existing data exchange mechanisms, for example the discharge summary; but rather to notify of the discharge event and provide enough data to gather more information, if desired. These notifications improve post-discharge transitions, promote communication between providers and encourage follow up care.  Figure X illustrates how some of the admit and discharge data elements corresponded to the resource in the message bundle.

{% include img-portrait.html img="bundle_graphic.svg" caption="Figure X" %}

<!--
The Provider is notified when:

- A Patient is admitted to the hospital for inpatient or emergency care
- A Patient is discharged from the hospital
- A Patient is transferred from one care unit to another
-->

### FHIR Resources for Admission and Discharge Notification

To carry information regarding admission and discharge event messages, the required resources for the message Bundle need to be defined.  The core components of the Bundle are defined in the [Framework] page and include the *MessageHeader* and the "root" resource represented by the  `MessageHeader.focus`.  For admissions and discharge *Encounter* (US Core Encounter) is the focus of the event as shown in figure 3:

{% include img-portrait.html img="admit_message_graph1.svg" caption="Figure 3" %}

The other "required if present" resources defined in the framework are those referenced by `MessageHeader.author`, `MessageHeader.responsible`, `MessageHeader.sender` and by referenced by the US Core Encounter Profile. These combine to make up a 'generic' Encounter message bundle structure illustrated in figure 4 below:


{% include img-portrait.html img="admit_message_graph2.svg" caption="Figure 4" %}

The following additional resources (or rather profiles) have been determined to be "required if present" by the Da Vinci community to fulfill the data item requirements specific to admissions and discharge.


{: .grid}
| ﻿Notification Scenarios | Additional Resource Requirements |
|---|---|
| Emergency and Inpatient Admissions | US Core Condition,  Da Vinci HRex Coverage |
| Emergency and Inpatient Discharges |  US Core Condition, Da Vinci HRex Coverage |


Adding these additional components results in the following resource graph showing all the required resources and their relationships for the admission and discharge notification use case:

{% include img-portrait.html img="admit_message_graph3.svg" caption="Figure 5" %}

Note that an Admit/Discharge Bundle may contain more or less resources than this graph illustrates since:  
a) having additional resources in the message bundle is not prohibited as long as the resources are reference by or reference another resource in the message bundle and  
b) not all the resources listed above may be present in the source system. (For a more detailed discussion of when required resources may be absent, see the section on [Must Support])
{:.highlight-note}

MessageDefinition and GraphDefinition can be used to formally define this resource graph for the admission and discharge event:

- [Example Da Vinci Notification MessageDefinition](MessageDefinition-admit-1.html)

- [Example Da Vinci Notification GraphDefinition](GraphDefinition-admit-1.html)

Alternatively a Bundle Profile can be used to define the structure:

- [Example Da Vinci StructureDefinition Profile Admit Message Bundle](StructureDefinition-profile-admit-message-01.html)

<!--
- \* it is questionable whether Encounter.diagnosis.condition has been implemented by the EHR vendors - need to discuss with vendors.
- \** There is no Practitioner.endpoint element and an extension may be needed to implement.
- \*** MessageDefinition is used to formally define the Message content for a given event (e.g, an inpatient admission or discharge).  It defines the event and the focal and non focal Resources/Profiles that make up the message:
-->

**Example Da Vinci Notification Message Bundle**

- [Example Da Vinci Notification Message Bundle](Bundle-message-admit-01.html)

### Pushing Unsolicited Admit/Discharge Notification

In the following interaction shown in figures 8, the HealthCare facility is acting in the role of the Notification Sender and the Notification Recipient can be any of the actors listed in figure 1 on the home page.  To notify the Notification Recipients/Intermediary of an admit or discharge event, the Notification Sender uses $process-message operation to submit the Notification Message to appropriate FHIR endpoints. Not shown in figure 8 is that when the Intermediary successfully receives and processes the notifications, it subsequently forwards the data the end users.

{% include img-portrait.html img="$process_message_admit_wf.svg" caption="Figure 8" %}

---

**Example Transaction**

The following transaction show an example of using the `$process-message` operation to send a Da Vinci Admission Notification Message Bundle to a Recipient:

{% include examplebutton_default.html example="process-message-example" b_title = "Click Here To See Example Notification " %}

---

<!--{% raw %}

### FHIR Subscription Based Notification

The interaction diagram in figure 5 and 6 on the [Framework] page illustrates the sequences of events for subscribing for ADT Notifications and the subsequent notifications when the the event occurs.

{:.note-to-balloters}
Note to Balloters: We are actively seeking input on what additional work is needed to determine the best way to implement subscriptions for notification notification. See the [FHIR Subscription Based Notification] framework for further details.

{% endraw %}-->





{% include link-list.md %}
