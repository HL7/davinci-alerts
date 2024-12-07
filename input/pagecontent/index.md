<div class="note-to-balloters" markdown="1">

**The January 2025 ballot addresses the following**

{% include whats-new-1.1.0-snapshot.md %}

</div><!-- note-to-balloters -->

Where possible, new and updated pre-publishing content is highlighted with green text and background- **This highlighting will be removed prior to publication.**
{:.new-content}

Key updates and detailed changes between this and prior versions are available on the US Core [Change Log] and [Changes Between Versions] pages.
{:.stu-note} 

Where possible, new and updated pre-publishing content are highlighted with green text and background - **This highlighting will be removed prior to publication**
{:.new-content}

Key updates and detailed changes between this and prior versions are available on the [Change Log] page.
{:.stu-note}

This implementation guide describes a method for the communication of relevant notifications to support the real-time exchange of information that impacts patient care and value based or risk based services.  Providers and Payers may need to be notified when activities occur that impact a patient's care. This may be as traditional as a notification of an admission or transfer to or discharge from a care setting. It also includes notifications about changes in treatment such as a new or different medication, or  changes in patient status like a new diagnosis. These notifications provide information that can improve care management and care coordination as well as act as the trigger for quality programs and other patient focused activities (for example, risk adjustment).  By allowing the patient's healthcare providers to be better informed and able to take actions and intervene earlier, the twin goals of better patient care and reduced cost of care may be met.

The [2019 CMS 45 CFR Part 156 NPRM] focuses on hospitalization notifications due to significant issues that can occur if a patient is not followed appropriately after acute care. The HL7 Da Vinci Project has responded to this need by supporting the effort to provide a FHIR based standard for adoption by both providers and payers.  It is anticipated that the burden of communicating the notification is also reduced by using FHIR.   This Guide defines a FHIR messaging based paradigm and framework to establish consistently adoptable and reproducible methods to exchange notifications. This framework is applied to the patient admission, transfer, and discharge events to generate unsolicited notifications to the care team.

### About This Guide

This Implementation Guide is supported by the [Da Vinci] initiative which is a private effort to accelerate the adoption of Health Level Seven International Fast Healthcare Interoperability Resources (HL7® FHIR®) as the standard to support and integrate value-based care (VBC) data exchange across communities. Like all Da Vinci Implementation Guides, it follows the [HL7 Da Vinci Guiding Principles] for exchange of patient health information.  The guide is based upon the prior work from the [US Core] and [Da Vinci Health Record Exchange (HRex)] Implementation Guides. Changes to this specification are managed by the sponsoring HL7 [Infrastructure and Messaging (INM)] workgroup and are incorporated as part of the standard HL7 balloting process. You can suggest changes to this specification by creating a *change request tracker* by clicking on the [Propose a Change] link at the bottom of any page.

### How to read this Guide (TODO! - Rewrite)

This Guide is divided into several pages which are listed at the top of each page in the menu bar.

- [Home]\: The home page provides the introduction and background for the Da Vinci Unsolicited Notifications Project.
- [Background]\: 
- [Specification]:
  - [Security]\: General security requirements and recommendations for {{site.title}} actors.
  - [Framework]\: These pages provide guidance on the set of FHIR transactions and the FHIR artifacts used in a general framework to enable unsolicited notifications to care team members.
  - [Admit/Discharge/Transfer Use Case]\: Unsolicited notifications for the Admission/Transfer/Discharge use cases are defined using the framework.
- [FHIR Artifacts]\: These pages provide detailed descriptions and formal definitions for all the FHIR objects defined in this guide.
  - [Profiles]\: This page lists the set of Profiles that are defined in this guide.
  - [Terminology]\: This page lists the value sets and code system defined for this guide.
  - [Examples]\: List of links to all the examples used in this guide.
  - [CapabilityStatements]\: This set of pages describes the expected FHIR capabilities of the various Da Vinci Notification actors.
- [Support]:
  - [Downloads]\: This page provides links to downloadable artifacts.
- [Change Log]:


### Credits

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
