{% assign base_id = {{page.id}} %}
{% assign base_type = {{site.data.structuredefinitions.[base_id].type}} %}

{{site.data.structuredefinitions.[base_id].description}}  This profile sets minimum expectations for the [{{base_type}}] resource to record the necessary context for the alert notifications.   It identifies the mandatory core elements, extensions, vocabularies and value sets which **SHALL** be present in the {{base_type}} resource.

### Mandatory and Must Support Data Elements

The following data-elements are mandatory (i.e data MUST be present) or must be supported if the data is present in the sending system ([Must Support] definition). They are presented below in a simple human-readable explanation.  Profile specific guidance and examples are provided as well.  The [Formal Profile Definition] below provides the  formal summary, definitions, and  terminology requirements.

**Each {{{base_type}} must have:**

1. a status
1. a connectionType of `hl7-fhir-rest`
1. a payloadType text only value of "n/a"
1. An endpoint address

**Each {{base_type}} must support:**

1.  one or more header strings*

**Additional Profile specific implementation guidance:**

- An endpoint supplied in this profile may be different or same as the endpoint that may be obtained from `Communication.sender` references: Organization or PractitionerRole.
- \*An authentication token may be supplied in `Endpoint.header`  by the Alert Sender to allow *direct* recipients of the Alert (whether an Alert Recipient or Alert Intermediary) to access additional information. This and other supplied headers, if any are given, are appended to the GET request. Sending these tokens has obvious security consequences. The server and client are responsible for ensuring that the content is appropriately secured.

### Examples

- [Alert Endpoint Example](Endpoint-example-1.html)

{% include link-list.md %}
