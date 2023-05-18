
###  Introduction

This use case demonstrates how the Da Vinci Notifications IG framework is used to define the Da Vinci Notification Bundle for admissions, transfers, and discharges and how to send a notification between a Sender and a Recipient/Intermediary.

### Use Case Background

The intent of this use case is to focus on the beginning and end of patient encounters.  The following list illustrates the type of events that this use case covers.[^2]

- admission to the emergency department
- admission to a hospital or equivalent facility as an inpatient
- admission to to a health care facility for a predetermined length of time, usually less than 24 hours
- admission to a hospital or equivalent facility for observation
- admission to a healthcare facility on a nonresident basis for example, for an outpatient medical procedure or surgery
- transfer from the emergency room to an inpatient status
- discharge to the patient's home environment
- discharge or transfer to a long-term care facility
- discharge or transfer to a post-acute care rehabilitation facility
- notification that the patient expired during the encounter

Having the ability to send notifications to update physicians and care management teams when a patient has a significant encounters (such as inpatient, ER visits, surgery etc.) is key to improving patient care.  The intent of these notifications is *not* to replace existing data exchange mechanisms, for example the discharge summary; but rather to notify of the event and provide enough data to gather more information, if desired. These notifications improve post-discharge transitions, promote communication between providers and encourage follow up care. The expectation for this use case is that the business rules for triggering the notification is the same that is used for an HL7 V2 ADT A01 message.  Figure 6 illustrates how some of the admit, transfer and discharge data elements corresponded to the resource in the message bundle.

<div markdown ="1" class="bg-info">
Transfer notifications should only be used if:
- Your organization calls it a "transfer" when the patient moves from the emergency room to an inpatient status
- Your organizations calls it a "transfer" when a patient moves from inpatient to another facility like an inpatient rehab facility.

You should not use transfer notifications:
- If your facility only uses *admit* and *discharge* transactions for the above scenarios
- For bed changes within the same facility, i.e. ICU to a step-down.
</div>

{% include img-portrait.html img="bundle_graphic.svg" caption="Figure 6" %}

<!--
The Provider is notified when:

- A Patient is admitted to the hospital for inpatient or emergency care
- A Patient is discharged from the hospital
- A Patient is transferred from one care unit to another
-->

### FHIR Resources for Admission, Transfer, and Discharge Notifications

To carry information regarding admission, transfer, and discharge event messages, the required resources for the message Bundle need to be defined.  The core components of the Bundle are defined in the [Framework] page and include the *MessageHeader* and the "root" resource represented by the  `MessageHeader.focus`.  For admission, transfer and discharge, the *Encounter* is the focus of the event as shown in {{ foo | filter: bar }}igure 7. For this scenario, the Da Vinci Admit/Discharge/Transfer Notification Encounter Profile - which is based on the US Core Encounter Profile - is used:

{% include img-portrait.html img="admit_message_graph1.svg" caption="Figure 7" %}

The other "required if present" resources defined in the framework are those referenced by `MessageHeader.author`, `MessageHeader.responsible`, `MessageHeader.sender` and those referenced by the Da Vinci Admit/Discharge/Transfer Notification Encounter Profile. These combine to make up a 'generic' Encounter message bundle structure illustrated in Figure 8 below:


{% include img-portrait.html img="admit_message_graph2.svg" caption="Figure 8" %}

The following additional resources (or rather profiles) have been determined to be "required if present" by the Da Vinci community to fulfill the data item requirements specific to admissions and discharge.

- US Core Condition
- Da Vinci Admit/Discharge/Transfer Notification Coverage

{: #figure-9}
Adding these additional components results in the following resource graph showing all the required resources and their relationships for the admission and discharge notification use case shown in Figure 9:

{% include img-portrait.html img="admit_message_graph3.svg" caption="Figure 9" %}

An alternate representation of this graph is a table with each row representing an "edge" - an ordered pair of the form (source profile, target profile):

{:.grid}
{% include graphdefinition-adt-narrative-table.md %}


Note that an Admit/Discharge/Transfer Bundle may contain more or less resources than this graph illustrates since:  
a) having additional resources in the message bundle is not prohibited as long as the resources are reference by or reference another resource in the message bundle and  
b) not all the resources listed above may be present in the source system. For example, including a diagnosis on an admit/transfer/discharge notification allows the recipient to determine if additional action is required, but an encounter diagnosis may not be available until well after discharge. (For a more detailed discussion of when required resources may be absent, see the section on [Must Support])
{:.highlight-note}

### Admit/Discharge/Transfer Message Profiles

The following FHIR Profiles can be used to formally define this resource graph for the admission, transfer, and discharge events.  Note that except for the first profile listed below, these profiles constrain their references to other profiles within the same bundle.

- [Da Vinci Notifications Bundle Profile]
- [Da Vinci Admit Notification MessageHeader Profile]
- [Da Vinci Transfer Notification MessageHeader Profile]
- [Da Vinci Discharge Notification MessageHeader Profile]
- [Da Vinci Admit/Discharge/Transfer Notification Condition Profile]
- [Da Vinci Admit/Discharge/Transfer Notification Coverage Profile]
- [Da Vinci Admit/Discharge/Transfer Notification Encounter Profile]

<!--
#### MessageDefinition and GraphDefinition
{:.no_toc}

The Following MessageDefinition and GraphDefinition can be used to formally define this resource graph for the admission, transfer and discharge event:

**MessageDefinition**

{% include list-simple-messagedefinitions.xhtml %}

**GraphDefinition**

{% include list-simple-graphdefinitions.xhtml %}

-->
<!--
- \* it is questionable whether Encounter.diagnosis.condition has been implemented by the EHR vendors - need to discuss with vendors.
- \** There is no Practitioner.endpoint element and an extension may be needed to implement.
- \*** MessageDefinition is used to formally define the Message content for a given event (e.g, an inpatient admission, transfer, or discharge).  It defines the event and the focal and non focal Resources/Profiles that make up the message:
-->

### Examples

Da Vinci Notification Bundles such as these examples can be assembled based on any of the above definitions.

{% include list-simple-bundles.xhtml %}

### Pushing Unsolicited Admit/Discharge/Transfer Notification

In the interaction shown in Figure 10, the HealthCare facility is acting in the role of the Notification Sender and the Notification Recipient can be any of the actors listed on the home page.  To notify the Notification Recipients/Intermediary of an admit or discharge event, the Notification Sender uses $process-message operation to submit the Notification Message to appropriate FHIR endpoints. Not shown in Figure 10 is that when the Intermediary successfully receives and processes the notifications, it subsequently forwards the data to the end users.

{% include img-portrait.html img="$process_message_admit_wf.svg" caption="Figure 10" %}

---

#### Example Transactions

The following example transactions show examples of using the `$process-message` operation to send a notification messages.

{% include examplebutton_default.html example="process-message-admit-example" b_title = "Click Here To See Example Da Vinci Admission Notification Message" %}

{% include examplebutton_default.html example="process-message-transfer-example" b_title = "Click Here To See Example Da Vinci Transfer Notification Message" %}

{% include examplebutton_default.html example="process-message-discharge-example" b_title = "Click Here To See Example Da Vinci Discharge Notification Message" %}

---

[^2]: Based on the [V3 Value SetActEncounterCode]  and [Discharge disposition] value sets.

{% include link-list.md %}
