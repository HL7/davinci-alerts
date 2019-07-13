{% assign base_id = {{page.id}} %}
{% assign base_type = {{site.data.structuredefinitions.[base_id].type}} %}

{{site.data.structuredefinitions.[base_id].description}}  This profile sets minimum expectations for the [{{base_type}}] resource to record the necessary context for the alert notifications.   It identifies the mandatory core elements, extensions, vocabularies and value sets which **SHALL** be present in the {{base_type}} resource.

**Example Usage Scenarios:**

The following are example usage scenarios for the {{base_type}}
 profile:

- Included in the Alert notification bundle when a patient is admitted or discharged.

### Mandatory and Must Support Data Elements

The following data-elements are mandatory (i.e data MUST be present) or must be supported if the data is present in the sending system ([Must Support] definition). They are presented below in a simple human-readable explanation.  Profile specific guidance and examples are provided as well.  The [Formal Profile Definition] below provides the  formal summary, definitions, and  terminology requirements.

**Each {{{base_type}} must have:**

1.  a status
1.  a category code of `alert`
1.  a patient
1.  a code representing the purpose of the alert
1.  the patient encounter
1.  who sent the alert

Note to Balloters: We are actively seeking input on whether a code representing the purpose of the alert is needed ('Communication.topic').  This concept can be obtained from the associated Encounter resource.  In FHIR, however, context conduction is not assumed and resources must form a complete representation by themselves. The question is whether a coded topic is simply redundant or is the Communication resource an incomplete record of a communication without it.
{:.note-to-balloters}

**Each {{base_type}} must support:**

1.  a business identifier
1.  an alert priority code
1.  coverage information
1.  who received the alert
1.  what supporting information was included in the notification in the form of free text or references to attachment(s) or resource(s) for the recipient.


**Profile specific implementation guidance:**

- The [Alert Scenario] table lists the Resources that may be referenced in the Da Vinci Communication Profile payload element and included in the alert Bundle.

### Examples

- [{{base_type}}-example](Communication-example-1.html)
- [Communication Example in Alert Bundle](Bundle-admit-01.html)

{% include link-list.md %}
