# davinci-alerts repository
## [Da Vinci Unsolicited Notifications Implementation Guide](http://hl7.org/fhir/us/davinci-alerts/history.html)

### Background

Current ADT exchange approaches typically use an HL7 V2 ADT message. This is a legacy EDI-style technology that uses HL7 specific protocols over ports that are not typically exposed to the internet. While HL7 V2 works well within the confines of a hospital system's intranet, it is not particularly well suited to cross-enterprise data exchange.

FHIR Messaging paradigm can be use to notify providers of patient admission and discharge information to improve care coordination. An unsolicited notification from the provider to the health plan can help track where care has been delivered and help ensure timely follow-up care is delivered as needed since healthcare stakeholders are increasingly responsible for knowing what care their patients have received and what care they need, regardless of where their patients sought care. FHIR-enable provider systems can support functionality to send admission, discharge, and transfer information to a system with a FHIR API to receive the notification via an Encounter Resource and its associated resources. The information can be sent to a pre-determined end-point or, optionally, an end-point or Direct Address that is determined by looking up the information recipients.

Since this is a push transaction, the solution may require some additional work to define the appropriate endpoint for a specific patient's ADT notification.

---

### Meeting Artifacts

http://confluence.hl7.org:8090/pages/viewpage.action?pageId=51225446

---

Note: a build takes 2-3 minutes after a commit to complete. You can...

Check the build progress on [Zulip committers notification stream](https://chat.fhir.org/#narrow/stream/179297-committers.2Fnotification/topic/ig-build)

Find your rendered IG automatically available at
http://build.fhir.org/ig/HL7/davinci-alerts/branches/master/index.html

Find debugging info about the build
http://build.fhir.org/ig/HL7/davinci-alerts/branches/master/build.log
