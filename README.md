# davinci-alerts
## Da Vinci Alerts

### Background

Current ADT exchange approaches typically use an HL7 V2 ADT message. This is a legacy EDI-style technology that uses HL7 specific protocols over ports that are not typically exposed to the internet. While HL7 V2 works well within the confines of a hospital system's intranet, it is not particularly well suited to cross-enterprise data exchange.

FHIR resources can be use to transport patient admission and discharge information can be used to improve care coordination, in the form of ADT alerts. An ADT alert from the provider to the health plan can help track where care has been delivered and help ensure timely follow-up care is delivered as needed since healthcare stakeholders are increasingly responsible for knowing what care their patients have received and what care they need, regardless of where their patients sought care. FHIR-enable provider systems can support functionality to send admission, discharge, and transfer information to a system with a FHIR API to receive the notification via an Encounter Resource and its associated resources. The information can be sent to a pre-determined end-point or, optionally, an end-point or Direct Address that is determined by looking up the information recipients.

Since this is a push transaction, the solution may require some additional work to define the appropriate endpoint for a specific patient's ADT notification.

---

### Meeting Artifacts

http://confluence.hl7.org:8090/pages/viewpage.action?pageId=51225446

---
