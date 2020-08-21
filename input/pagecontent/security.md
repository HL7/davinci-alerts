
Da Vinci Unsolicited Notifications involves the server sending a communication that could reveal information about the client and server relationship, as well as sensitive administrative or clinical information.  Servers are responsible for ensuring appropriate security is employed and for following the [FHIR security guidance]. Sensitive data should only be exchanged over secured channels therefore a variety of communication protocols may be appropriate given the nature of the existing inter-party communication channels. This guide does not address these concerns directly; it is assumed that these are administered by other configuration processes.  Alao, FHIR does not mandate a single technical approach to security and privacy; rather, the specification provides a set of building blocks that can be applied to create secure, private systems.  For example, the defacto security layer for FHIR RESTful transactions is SMART's profile of OAuth2:

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
