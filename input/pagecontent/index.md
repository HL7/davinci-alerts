{% include note-to-balloters.md %} 

Where possible, new and updated pre-publishing content are highlighted with green text and background - **This highlighting will be removed prior to publication**
{:.new-content}

Key updates and detailed changes between this and prior versions are available on the [Change Log] page.
{:.stu-note}

This implementation guide describes a method for the communication of relevant notifications to support the real-time exchange of information that impacts patient care and value based or risk based services.  Providers and Payers may need to be notified when activities occur that impact a patient's care. This may be as traditional as a notification of an admission or transfer to or discharge from a care setting. It also includes notifications about changes in treatment such as a new or different medication, or  changes in patient status like a new diagnosis. These notifications provide information that can improve care management and care coordination as well as act as the trigger for quality programs and other patient focused activities (for example, risk adjustment).  By allowing the patient's healthcare providers to be better informed and able to take actions and intervene earlier, the twin goals of better patient care and reduced cost of care may be met.

The [2019 CMS 45 CFR Part 156 NPRM] focuses on hospitalization notifications due to significant issues that can occur if a patient is not followed appropriately after acute care. The HL7 Da Vinci Project has responded to this need by supporting the effort to provide a FHIR based standard for adoption by both providers and payers.  It is anticipated that the burden of communicating the notification is also reduced by using FHIR.   This Guide defines a FHIR messaging based paradigm and framework to establish consistently adoptable and reproducible methods to exchange notifications. This framework is applied to the patient admission, transfer, and discharge events to generate unsolicited notifications to the care team.

### About This Guide

This Implementation Guide is supported by the [Da Vinci] initiative which is a private effort to accelerate the adoption of Health Level Seven International Fast Healthcare Interoperability Resources (HL7® FHIR®) as the standard to support and integrate value-based care (VBC) data exchange across communities. Like all Da Vinci Implementation Guides, it follows the [HL7 Da Vinci Guiding Principles] for exchange of patient health information.  The guide is based upon the prior work from the [US Core] and [Da Vinci Health Record Exchange (HRex)] Implementation Guides. Changes to this specification are managed by the sponsoring HL7 [Infrastructure and Messaging (INM)] workgroup and are incorporated as part of the standard HL7 balloting process. You can suggest changes to this specification by creating a *change request tracker* by clicking on the [Propose a Change] link at the bottom of any page.

#### How to read this Guide
{: .no_toc}

This Guide is divided into several pages which are listed at the top of each page in the menu bar.

- [Home]\: The home page provides the introduction and background for the Da Vinci Unsolicited Notifications Project.
- [Framework]\: These pages provide guidance on the set of FHIR transactions and the FHIR artifacts used in a general framework to enable unsolicited notifications to care team members.
- [Admit/Discharge/Transfer Use Case]\: Unsolicited notifications for the Admission/Transfer/Discharge use cases are defined using the framework.
- [FHIR Artifacts]\: These pages provide detailed descriptions and formal definitions for all the FHIR objects defined in this guide.
  - [Profiles]\: This page lists the set of Profiles that are defined in this guide.
  - [Terminology]\: This page lists the value sets and code system defined for this guide.
  - [Examples]\: List of links to all the examples used in this guide.
  - [CapabilityStatements]\: This set of pages describes the expected FHIR capabilities of the various Da Vinci Notification actors.
- [Security]\: General security requirements and recommendations for {{site.title}} actors.

- [Downloads]\: This page provides links to downloadable artifacts.

### Scope and Usage

<span class="bg-success" markdown="1">The goal of this Implementation Guide is to define a technical framework for sending unsolicited notifications to the appropriate actors when triggered by an event.</span><!-- new-content --> Note that the information being communicated is a *notification* and not an *alert* which often has the expectation that something needs to be done. The assumption is that data is being transferred but not the responsibility.  The data recipient determines the action it takes based upon the information it receives.  The notifications should provide enough information to understand what the notification is about and to enable the Recipient to determine if and what additional steps they need to take in response to the notification.  For example, additional steps may include:

- a request for more information from the Sender through a FHIR RESTful query
- creation of an encounter record in the receiving system with appropriate provenance
- making the information available to CDS and other local services.

The following table summarizes the technical scope of this guide:

<div class="row">
<div class="col-sm-6" markdown="1" style="background-color: Lightcyan;">
**In Scope**

---

-  Define a common FHIR messaging Bundle that is exchanged for all Notifications.
-  Define the FHIR transactions and minimum operational behavior for the relevant Actors
- Define how to define and share the minimal data elements needed to support the information needs for an initial set of notifications and use cases starting with the patient admission and discharge event.  
-  Define how users requiring more data may follow up with additional queries.
- Describe basic Security and Privacy considerations

----

</div>
<div class="col-sm-6" markdown = "1" style="background-color: WhiteSmoke;">
**Out Of Scope**

---

- The business rules and workflow surrounding when a notification is triggered  
   - These are considered implementation specific details and include both what and exactly when an event occurs and who it is about and who gets the notification.
   - This includes notifications that are not associated with a particular event
- Creation and Management of the list of Recipients/Intermediaries[^1]
- How the Intermediary determines further processing of notification data
- Creation of the FHIR equivalent of v2 Messaging
- Distribution beyond FHIR Endpoints (e.g. SMS, email)
- Bidirectional Work, such as Gaps in Care
- Any notification that requires workflow management such as Task
- Complex content such as image files or scanned documents
- Besides the standard http response, the Recipient's workflow upon receipt of the notification.


---

</div>

</div>

<!--
The triggering of a notification allow for the appropriate notification to be sent at the appropriate time to provide important information to the end users without overwhelming the them causing "notification fatigue".
-->

#### Scenarios

Notifications can be generated for many scenarios.

This Implementation Guide focus is the *Admission Transfer and Discharge* Scenario.  However, the framework defined in this guide is intended to support other scenarios such as those listed below.  There is no plan to publish additional use cases in this implementation guide. Additional scenarios may be published as supplemental non-balloted informative documents or use case specific Implementation Guides.

<div class="row">
<div class="col-sm-6" markdown="1" style="background-color: Lightcyan;">
**Initial Scenarios**

- Emergency and Inpatient Admissions
- Admission for Observation
- Admission for special services, such as outpatient surgery
- Encounter/Visit Notification for ambulatory services
- Transfer From emergency room to an inpatient status
- Transfer from inpatient to another facility like an inpatient rehab facility
- Discharges/Visit ends

---

</div>
<div class="col-sm-6" markdown = "1" style="background-color: WhiteSmoke;">
**Potential Future Scenarios**

---

-   Lab Results
-   Problem with Treatment -- such as drug recall, device recall/issue
-   Public Health Notification
-   Scheduled Appointment/Pre-Admit
-   Referral
-   Ordered Device/Biometric/Patient (i.e. Fit Bit)
-   Treatment Start/End
-   Change in Social Determinants of Health
-   Birth/Death
-   Coverage Start/End
-   Notification of Prior Authorization (Pended to Approved/Denied)
-   Pharmacy (Pickup, Restock, Dispense)
-   Notification of New Condition
-   Worker's Compensation Visits and Services
-   Changes in Care Team

---

</div>

</div>

### Roles and Actors

<div class="strike" markdown="1">

#### Roles

- **Sender** - the system responsible for sending the notifications, typically operated by the facility or organization where the event occurred
  - <span class="bg-success" markdown="1">Events may include requests or orders (for example, ordering a test for an infectious disease).</span><!-- new-content -->
- **Recipient** – the system responsible for receiving generated notifications from Senders
  - It is the responsibility of the Receiver to filter and sort the Da Vinci notifications it receives
<!-- - **Interested Entity** – a system that is interested in receiving notificationss for specific events, providers, patients or other predefined criteria -->
- **Intermediary** (e.g. ClearingHouse or HIE/HIN)– a system that can act as a central point to receive notifications from multiple Senders and distribute them to Recipients based on previously defined forwarding policies.
  - The Intermediary has the role and functional requirements of a Da Vinci Notifications Recipient
  - The Intermediary has the role and functional requirements of a Da Vinci Notifications Sender if it is forwarding messages using the framework defined in this guide.
  - <span class="bg-success" markdown="1">The FAST project's [Hybrid/Intermediary Exchange Implementation Guide] is out of scope for this guide. Although it provides guidance for enabling FHIR REST interactions across one or more intermediaries, it *does not* provide guidance for the use of FHIR Messaging.</span><!-- new-content -->

See the Da Vinci Notifications [Capability Statements] for details on the RESTful transactions and specific profiles applicable to each of these actors.

#### Actors

</div>

There are many potential actors for the roles listed above:

<div class="row">
<div class="col-sm-4" markdown="1" style="background-color: Lightcyan;">

**Sender** - the system responsible for sending the notifications, typically operated by the facility or organization where the event occurred

---

- Hospital Information System (HIS) at Acute/Inpatient Facility
- EHR or Practice Management (PM) system at an Ambulatory/Outpatient (Specialist/PCP) office
- Post Acute Facility EHR or PM
- Health Plan and Contracted Entities

---
</div>

<div class="col-sm-4" markdown = "1" style="background-color: WhiteSmoke;">

**Intermediary**  – the system responsible for receiving generated notifications from Senders

---

- Health Information Exchange (HIE)
- <span class="bg-success" markdown="1">Health Information Network (HIN)</span><!-- new-content -->
- Clinically Integrated Network (CIN) systems
- National Networks (CareQuality, CommonWell, etc.)
- Specialized Notification Aggregators
- Health Plan and Contracted Entities

---

</div>
<div class="col-sm-4" markdown = "1" style="background-color: Lightcyan;">

**Recipient**  – the system responsible for receiving generated notifications from Senders

---

- Hospital Information System (HIS) at Acute/Inpatient Facility
- EHR or Practice Management (PM) system at an Ambulatory/Outpatient (Specialist/PCP) office
- Post Acute Facility EHR or PM
- Population Health Management systems
- Care Management/Care Coordination systems
- Health Plan and Contracted Entities

---

</div>

</div>

### Workflow Overview

See the [Framework] page for a detailed description of the technical workflow and API guidance.
{:.highlight-note}

Figure 1 below illustrates the general notification workflow of a Sender sending an unsolicited notification to a Receiver or Intermediary when triggered by an event or request.

{% include img.html img="notification_wf1.svg" caption="Figure 1" %}

1. An event or request triggers a notification to be sent from a Sender (aka source application) to a Recipient or Intermediary (aka destination application).  The notification includes common information shared across all Da Vinci notifications and use case dependent information.
2. The Sender notifies the Recipient by sending an "unsolicited" notification to the Recipient's FHIR endpoint.
3. The notification is processed according the Receiver or Intermediary internal business rules.

Figure 2 shows the process where an Intermediary, having previously received a notification, forwards the notification to the Recipient. In this case, the Intermediary is responsible for the redistribution of the data.  Note that it may customize the data based on end user needs.  Although not represented in the figure, there may be multiple Intermediaries.

{% include img.html img="notification_wf2.svg"
 caption="Figure 2" %}

<br/>
<br/>
 ---

 **This Implementation Guide was made possible by the thoughtful contributions of the following people and organizations:**

 - *The twenty-two founding [Da Vinci Project](http://www.hl7.org/about/davinci/index.cfm?ref=common) member organizations.*

 - *Eric Haas, Health eData Inc*
 - *Riki Merrick Vernetzt, LLC*
 - *Linda Michaelsen, Optum*
 - *Lloyd Mckenzie, Gevity*
 - *Robert Dieterle, EnableCare*
 - *Viet Nguyen, Stratametrics*
 - *Jocelyn Keegan, Point of Care Partners*

 ---

[^1]: [FHIR at Scale Taskforce (FAST)] is an ongoing initiatives to address how to define this secure infrastructure.

<br />

{% include link-list.md %}
