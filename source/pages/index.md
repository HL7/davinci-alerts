---
title: Da Vinci Unsolicited Notifications
layout: default
active: home
---

<!-- TOC  the css styling for this is \pages\assets\css\project.css under 'markdown-toc'-->

* Do not remove this line (it will not be displayed)
{:toc}


<!-- end TOC -->

The communication of relevant notifications to support the real-time exchange of information that impacts patient care and value based or risk based services.  Providers (members of a care team) and Payers may need to be alerted when activities occur that impact a patients care. This may be as traditional as admission to or discharge from a care setting (ED, Hospital, etc.) but may also include changes in treatment (e.g. medications) or patient status (new diagnosis). This information will improve care management and care coordination as well as act as the trigger for quality programs and other patient focused activities (e.g. risk adjustment).  It would allow actors participating in the patient's healthcare to take actions and intervene earlier to assure the patient is better cared for and can also result in reduced costs.

The [2019 CMS 45 CFR Part 156 NPRM] focuses on hospitalization notifications due to significant issues that can occur if a patient is not followed appropriately after acute care. The HL7 Da Vinci Project has responded to this need by supporting the effort to provide a FHIR based standard for adoption by both providers and payers.  It is anticipated that the burden of communicating the notification is also reduced by using FHIR.   This Guide defines a FHIR messaging based paradigm and framework to establish consistently adoptable and reproducible methods to exchange notifications. This framework is demonstrated using the patient admission and discharge event use case to generate unsolicited notifications to the care team.

## How to read this Guide

This Guide is divided into several pages which are listed at the top of each page in the menu bar.

- [Home]\: The home page provides the introduction and background for the Da Vinci Alert Project.

- [Framework]\: These pages provide guidance on the set of FHIR transactions and the FHIR artifacts used in a general framework to enable unsolicited notifications to careteam members.
- [Use cases]\: The Admission/Discharge use case is used to show how to implement an unsolicited notification using the framework.
- [FHIR Artifacts]\: These pages provides detailed descriptions and formal definitions for all the FHIR objects defined in this guide.
  - [Profiles]\: This page lists the set of Profiles that are defined in this guide to exchange quality data.
  - [Terminology]\: This page lists the value sets and code system defined for this guide.
  - [Capability Statements]\: This set of pages describes the expected FHIR capabilities of the various DEQM actors.
- [Security]\: General security requirements and recommendations for {{site.title}} actors.
- [Examples]\: List of links to all the examples used in this guide.
- [Downloads]\: This page provides links to downloadable artifacts.

## Scope and Usage

The work of this Implementation Guide is to:

1.  Define a technical framework for sending unsolicited notifications to the appropriate actors when triggered by an event or request.
    -  Define a common FHIR messaging Bundle that is exchanged for all Notifications.
    -  Define the FHIR transactions and minimum operational behavior for the relevant Actors
1.  Define how to define and share the minimal data elements needed to support the information needs for an initial set of Use Case starting with the patient admission and discharge event use case.  
1.  Define a how users requiring more data may follow up with additional queries.
1. Describe basic Security and Privacy considerations

It is important that the framework allow for only appropriate notification to
be sent at the appropriate time and with just the right amount of
information. This will serve to avoid "notification fatigue".

### Out Of Scope

The following items are out of scope for this implementation guide:
- What constitutes a trigger (nature of the event as defined in
your organization)
   - Including alerts without an event
- “Endpoint Discovery” and maintenance
- Creation of the FHIR equivalent of v2 Messaging
- Distribution beyond FHIR Endpoints (e.g. SMS, email)
- Bidirectional Work, such as Gaps in Care
- Any notification that requires workflow management such as Task
- Complex content
- Besides the standard http response, the Alert Recipient's workflow upon receipt of alert.
   - Note, the Notification Recipient may initiate a FHIR RESTful query for additional data.

### Scenarios

Notifications can be generated for many scenarios.

#### Initial Phase
{:.no_toc}

The initial version of this
Implementation Guide will focus on these Admission and Discharge Scenarios, basically anything that would create an encounter in a patient care record.

- Emergency and Inpatient Admissions
- Admission for Observation
- Admission for special services, such as outpatient surgery
- Encounter/Visit Notification for ambulatory services
- Discharges/Visit ends

#### Potential Future Scenarios

The framework as defined can support the other scenarios as listed below.  Work is planned to document them in future publications in collaboration with domain experts such as public health.:

{:.no_toc}

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
-   Work Comp Initial/Visits/Services
-   Changes in Care Team

## Roles and Actors

### Roles

- **Sender** - the system responsible for sending the notifications, typically operated by the facility or organization where the event occurred
- **Recipient** – the system responsible for receiving generated notifications from Senders
<!-- - **Interested Entity** – a system that is interested in receiving notificationss for specific events, providers, patients or other predefined criteria -->
- **Intermediary** (e.g. ClearingHouse or HIE/HIN)– a system that can act as a central point to receive notifications from multiple Senders and distribute them to Recipients based on previously defined forwarding policies

### Actors

There are many potential actors for the roles listed above:

{% include img-portrait.html img="alert_actors.svg" caption="Figure 1" %}

<!--
-   Patient/Caregivers
-   Care Team - Provider defined treatment relationship
-   Post-Acute Care Facilities
     - Inpatient
     - Outpatient
-   Pharmacy
-   Payer/Payer Partners
-   Hospitals
-   Ambulatory Care
    - Primary Care Provider
    - Specialty Provider
-   Labs
-   HIE/HIN
-   Social Services
-   Community Care
-->

## Workflow Overview

See the [Framework] page for a detailed description of the technical workflow and API guidance
{:. stu-note}


{% include img-portrait.html img="basic_process.svg" caption="Figure 2" %}

1. An event or request triggers a [FHIR message] to be sent from a Sender (aka source application) to a Intermediary or Recipient (aka destination application).  The notification message includes common resources across all notifications and use case dependent supporting resources.
2. The Sender notifies the  Recipient by pushing a notification message to a FHIR endpoint using the [$process-message] operation. The operation accepts the notification message and processes it according the Sender or Intermediary internal business rules.

Figure 3 shows the process where the  Sender transacts with the  Intermediary which in turn interacts with the  Recipient.  The  Intermediary is responsible for the redistribution of the data.  Note that it may customize the data based on end user needs.  Although not represented in the figure, there may be multiple Intermediaries.

{% include img-portrait.html img="basic_process_int.svg"
 caption="Figure 3" %}

---
<br />

{% include link-list.md %}
