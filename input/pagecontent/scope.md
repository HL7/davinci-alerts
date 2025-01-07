### Scope

The goal of this Implementation Guide is to define a technical framework for sending unsolicited notifications to the appropriate actors when triggered by an event. Note that the information being communicated is a *notification* and not an *alert* which often has the expectation that something needs to be done. The assumption is that data is being transferred but not the responsibility.  The data recipient determines the action it takes based upon the information it receives.  The notifications should provide enough information to understand what the notification is about and to enable the Recipient to determine if and what additional steps they need to take in response to the notification.  For example, additional steps may include:

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

### Scenarios

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

{% include link-list.md %}