
<!-- {% raw %}

{% include whats-new-1.1.0-snapshot.md %} 

Where possible, new and updated pre-publishing content are highlighted with green text and background - **This highlighting will be removed prior to publication**
{:.new-content}

 {% endraw %} -->

Key updates and detailed changes between this and prior versions are available on the [Change Log] page.
{:.stu-note}

This implementation guide describes a method for the communication of relevant notifications to support the real-time exchange of information that impacts patient care and value based or risk based services.  Providers and Payers may need to be notified when activities occur that impact a patient's care. This may be as traditional as a notification of an admission or transfer to or discharge from a care setting. It also includes notifications about changes in treatment such as a new or different medication, or  changes in patient status like a new diagnosis. These notifications provide information that can improve care management and care coordination as well as act as the trigger for quality programs and other patient focused activities (for example, risk adjustment).  By allowing the patient's healthcare providers to be better informed and able to take actions and intervene earlier, the twin goals of better patient care and reduced cost of care may be met.

The [2019 CMS 45 CFR Part 156 NPRM] focuses on hospitalization notifications due to significant issues that can occur if a patient is not followed appropriately after acute care. The HL7 Da Vinci Project has responded to this need by supporting the effort to provide a FHIR based standard for adoption by both providers and payers.  It is anticipated that the burden of communicating the notification is also reduced by using FHIR.   This Guide defines a FHIR messaging based paradigm and framework to establish consistently adoptable and reproducible methods to exchange notifications. This framework is applied to the patient admission, transfer, and discharge events to generate unsolicited notifications to the care team.

### About This Guide

This Implementation Guide is supported by the [Da Vinci] initiative which is a private effort to accelerate the adoption of Health Level Seven International Fast Healthcare Interoperability Resources (HL7® FHIR®) as the standard to support and integrate value-based care (VBC) data exchange across communities. Like all Da Vinci Implementation Guides, it follows the [HL7 Da Vinci Guiding Principles] for exchange of patient health information.  The guide is based upon the prior work from the [US Core] and [Da Vinci Health Record Exchange (HRex)] Implementation Guides. Changes to this specification are managed by the sponsoring HL7 [Infrastructure and Messaging (INM)] workgroup and are incorporated as part of the standard HL7 balloting process. You can suggest changes to this specification by creating a *change request tracker* by clicking on the [Propose a Change] link at the bottom of any page.



### How to read this Guide

This Guide is divided into several pages which are listed at the top of each page in the menu bar.

- **[IG Home]**\: The home page provides the introduction and background for the Da Vinci Unsolicited Notifications Project.
- **Background**\: This menu item links to:
     - The Da Vinci Overview page provides an overview of the Da Vinci project, guidance on how to get involved, and where to find the use-case-specific IGs.
    - The Da Vinci Guiding Principles page describes key principles that underlie all Da Vinci interoperability.
- **Specification**\:
  - [Scope and Usage]\: This page delineates the Da Vinci Unsolicited Notifications use case.
  - [Roles and Actors]\: This page defines the roles and actors for Da Vinci Unsolicited Notifications.
  - [Workflow]\: This page documents the general notification workflow between unsolicited notification senders and receivers.
  - [Framework]\: This page defines the set of FHIR transactions and the FHIR artifacts used in a general framework to enable unsolicited notifications to care team members.
  - [Privacy, Safety, and Security]\: General security requirements and recommendations for {{site.title}} actors.
  - [Admit/Discharge/Transfer Use Case]\: Unsolicited notifications for the Admission/Transfer/Discharge use cases are defined using the Da Vinci Unsolicited Notifications framework.
- **[FHIR Artifacts]**\: This page introduces and provides links to the profiles, Operations, ValueSets and other FHIR artifacts used in this implementation guide.
- **Base Specs**\: This menu item links to the FHIR core specification and the US core specs underlying this IG.
- **Support**\: This menu item links to support and guidance, download links for this IG, and guidance on tools and support for Da Vinci implementers.
- **[Change Log]**\: This page documents the changes across the versions of Da Vinci Unsolicited Notifications implementation guide.



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
