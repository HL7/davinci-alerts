
<div class="strike" markdown="1">

### Roles

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

### Actors

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

{% include link-list.md %}