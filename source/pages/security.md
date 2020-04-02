---
# jekyll header
active: security
title: Security and Privacy
layout: default
---

In order to be responsible stewards of data, we will need to follow the data governance laws around sensitive conditions. Sensitive conditions are defined to support masking of clinical data that protects consumer’s privacy and are subject to special disclosure rules which govern the distribution of data to external parties.

<del>
[The FHIR Security and Privacy Module] describes how to protect a patient's privacy through de-Identification, pseudonymization, and and/or anonymization. FHIR does not mandate a single technical approach to security and privacy; rather, the specification provides a set of building blocks that can be applied to create secure, private systems.
</del>

[The FHIR Security and Privacy Module] describes how to protect a patient's privacy through de-Identification, pseudonymization, and and/or anonymization.  For FHIR RESTful transactions the defacto security layer is SMART's profile of OAuth2:

- [SMART Application Launch Framework Implementation Guide Release 1.0.0]
- [FHIR Bulk Data Access (Flat FHIR)] (specifically: SMART Backend Services: Authorization Guide)

<div class="stu-note" markdown="1">
There are several ongoing initiatives to address various security and privacy issues including:

- [FHIR Data Segmentation for Privacy project]
- [FHIR at Scale Taskforce (FAST)]
- [Dynamic Registration for SMART Apps]

Once a suitable approach has been agreed upon and published, it will be referenced in a future version of this guide.
</div>


<div class="note-to-balloters strike" markdown="1">

The DaVinci project is actively seeking input on security approaches and expectations for authentication and authorization between Senders and Receivers of sensitive patient data (e.g., will TLS, mutual-TLS, OAuth, etc. be required to interoperate?).  There are several implementation guides and ongoing initiatives to address these issues including:


- [FHIR Data Segmentation for Privacy project]
Services: Authorization Guide)
- [SMART Application Launch Framework Implementation Guide Release 1.0.0]
- [FHIR Bulk Data Access (Flat FHIR)] (specifically: SMART Backend Services: Authorization Guide)
- [FHIR at Scale Taskforce (FAST)]
- [Dynamic Registration for SMART Apps]


Once an approach has been agreed upon, it will be documented in the the [Da Vinci Health Record Exchange (HRex) Implementation Guide].

</div>


{% include link-list.md %}


[SMART Application Launch Framework Implementation Guide Release 1.0.0]: http://www.hl7.org/fhir/smart-app-launch/
[FHIR Bulk Data Access (Flat FHIR)]: https://hl7.org/fhir/uv/bulkdata/
[FHIR at Scale Taskforce (FAST)]: https://oncprojectracking.healthit.gov/wiki/pages/viewpage.action?pageId=43614268
[Da Vinci Health Record Exchange (HRex) Implementation Guide]: http://hl7.org/fhir/us/davinci-hrex/history.html
[Dynamic Registration for SMART Apps]: http://www.udap.org/udap-dynamic-client-registration.html
