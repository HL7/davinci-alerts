---
title: Da Vinci Alerts
layout: default
active: home
---

<!-- TOC  the css styling for this is \pages\assets\css\project.css under 'markdown-toc'-->

* Do not remove this line (it will not be displayed)
{:toc}


<!-- end TOC -->

The HL7 Da Vinci Project has recognized a need for communication of
Alerts between payers, providers and other actors in the healthcare
space. Alerts are defined as a need to notify another party of an event
that would affect one or more patient's care. Alerts allow actors in the
patient's healthcare to take actions and intervene earlier to assure the
patient is better cared for. This can also result in reduced costs

It is important that the framework allow for only appropriate alerts to
be sent at the appropriate time and with just the right amount of
information. This will serve to reduce alert fatigue. Because FHIR is a
web standard, the burden of communicating the alert is also reduced.

The work of this Implementation Guide is to define a FHIR framework for

1.  Identifying that an event/trigger has occurred
1.  Using a FHIR bundle to relay the alert to an interested actor

While an alert may generate workflow on the receiver's part, the Alert
is not a part of that workflow. As such, the sender of an Alert, should
not expect any additional response outside of the standard FHIR
functionality.

## How to read this Guide

This Guide is divided into several pages which are listed at the top of each page in the menu bar.

- [Home]\: The home page provides the introduction and background for the Da Vinci Alert Project.

- [Framework]\: These pages provide guidance on the set of FHIR transactions and the FHIR artifacts used in to provide a general framework to enable alert notifications.
- [Use cases]\: Exemplar use cases are presented to demonstrate how to implement the framework for a particular event notification.
    - [Admission/Discharge]\: This example shows how to implement an alert for a patient admission.
- [Profiles and Extensions]\: This page lists the set of Profile and Extension that are defined in this guide to exchange quality data.
- [Operations]\: This page lists the standard FHIR and DEQM defined Operations that are used in the DEQM transactions to exchange quality data.
- [Capability Statements]\: This set of pages describes the expected FHIR capabilities of the various DEQM actors.
- [Security]\: General security requirements and recommendations for {{site.title}} actors.
- [Examples]\: List of links to all the examples used in this guide.
- [Downloads]\: This page provides links to downloadable artifacts.


## Background


### *In Scope* for the Initial Version of Alert Implementation Guide

- There must be an event that drives the generation of the Alert
- The event can be for one or more patients but the Alert will be
generated for each patient separately
- The Alert will be based on FHIR R4 and where possible US Core
Implementation of FHIR R4

### *Out Of Scope* for the Alert Implementation Guide
- “Endpoint Discovery” and maintenance
- Creation of the FHIR equivalent of v2 Messaging
- Distribution beyond FHIR Endpoints (e.g. SMS, email)
- Bidirectional Work, such as Gaps in Care
- Alerts without an event
- Any notification that requires workflow management such as Task
- Complex content

### Scenarios

Alerts can be generated for many scenarios. The [2019 CMS (need full name)NPRM]
focuses on hospitalization due to significant issues that can occur if a patient
is not followed appropriately after acute care. The initial version of the Alert
Implementation Guide will focus on the Admission and Discharge Scenarios. The
framework as defined may support the other scenarios as listed below and work
will continue on this in future versions of the Implementation Guide.

-   Emergency and Inpatient Admissions
-   Emergency and Inpatient Discharges
-   Lab Results
-   Problem with Treatment -- such as drug recall, device recall/issue
-   Encounter/Visit Notification
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

### Roles and Actors

#### Alert Roles

- **Alert Sender** - the system responsible for sending the alert, typically operated by the facility or organization where the event occurred
- **Alert Recipient** – the system responsible for receiving generated alerts from Alert Senders
-  **Interested Entity** – a system that is interested in receiving alerts for specific events, providers, patients or other predefined criteria
- **Alert Intermediary** (aka ClearingHouse)– a system that can act a a central point to receive alerts from multiple Alert Senders and distribute alerts to Alert Recipients based on previously defined subscription policies

#### Alert Actors

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

### Workflow Overview

-  *See the [Framework] page for a detailed description of the technical workflow and API guidance*

An event or request triggers an Alert Sender to notify either an Alert Intermediary or Recipient by pushing an "Alert Bundle" object.  This guide defines 2 types of push notifications: 1) a FHIR RESTful POST/PUT to a FHIR endpoint. 2) a FHIR subscription publisher notification to a subscriber endpoint. The basic process diagrams in figure 2 shows the process where the Alert Sender transact directly with the Alert Recipient.  Figure 3 shows the process where the the Alert Sender transact with the Alert Intermediary (aka clearinghouse) which in turn interacts with the Alert Recipient.  Although not represented in the figure, there may be multiple Alert Intermediaries.

{% include img-portrait.html img="basic_process.svg" caption="Figure 2" %}

1. Event or request by patient or Healthcare Facility triggers an alert to be sent to an Alert Recipient.
1. The Alert Sender notifies the Alert Recipient by pushing an "Alert" bundle which includes the Da Vinci Communication Profile and use case dependent supporting resources.

{% include img-portrait.html img="basic_process_int.svg"
 caption="Figure 3" %}

1. Event or request by patient or Healthcare Facility triggers an alert to be sent to an Alert Intermediary ( e.g. clearinghouse).
1. The Alert Sender notifies the Alert Intermediary by pushing an "Alert" bundle which includes the Da Vinci Communication Profile and use case dependent supporting resources.
1. The Alert Intermediary subsequently notifies the Alert Recipient by pushing the "Alert" bundle to them.


---

{% include link-list.md %}
