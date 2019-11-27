---
# jekyll header
active: security
title: Security and Privacy
layout: default
---

In order to be responsible stewards of data, we will need to follow the data governance laws around sensitive conditions. Sensitive conditions are defined to support masking of clinical data that protects consumer’s privacy and are subject to special disclosure rules which govern the distribution of data to external parties.

[The FHIR Security and Privacy Module] describes how to protect a patients privacy through de-Identification, pseudonymization, anonymization. FHIR does not mandate a single technical approach to security and privacy; rather, the specification provides a set of building blocks that can be applied to create secure, private systems.

<div class="note-to-balloters" markdown="1">
The DaVinci project is actively seeking input on security approaches and expectations for authentication and authorization between Senders and Receivers of sensitive patient data (e.g., will TLS, mutual-TLS, OAuth, etc. be required to interoperate?).  There are several implementation guides and ongoing initiatives to address these issues including:

- [SMART Application Launch Framework Implementation Guide Release 1.0.0]
- [FHIR Bulk Data Access (Flat FHIR)] (specifically: SMART Backend Services: Authorization Guide)
- [FHIR at Scale Taskforce (FAST)]
- [Dynamic Registration for SMART Apps]  We are aware of the planned FHIR Data Segmentation for Privacy project.

Once an approach has been agreed upon, it will be documented in the the [Da Vinci Health Record Exchange (HRex) Implementation Guide].
</div>

{% include link-list.md %}


[SMART Application Launch Framework Implementation Guide Release 1.0.0]: http://www.hl7.org/fhir/smart-app-launch/
[FHIR Bulk Data Access (Flat FHIR)]: https://hl7.org/fhir/uv/bulkdata/
[FHIR at Scale Taskforce (FAST)]: https://oncprojectracking.healthit.gov/wiki/pages/viewpage.action?pageId=43614268
[Da Vinci Health Record Exchange (HRex) Implementation Guide]: http://hl7.org/fhir/us/davinci-hrex/history.html
[Dynamic Registration for SMART Apps]: http://www.udap.org/udap-dynamic-client-registration.html
