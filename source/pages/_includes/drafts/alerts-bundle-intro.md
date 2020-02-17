{% assign base_id = {{page.id}} %}
{% assign base_type = {{site.data.structuredefinitions.[base_id].type}} %}

{{site.data.structuredefinitions.[base_id].description}}  This profile sets minimum expectations for the [{{base_type}}] resource to record the necessary context for the alert notifications.   It identifies the mandatory core elements, extensions, vocabularies and value sets which **SHALL** be present in the {{base_type}} resource.

### Mandatory and Must Support Data Elements

The following data-elements are mandatory (i.e., data MUST be present) or must be supported if the data is present in the sending system ([Must Support] definition). They are presented below in a simple human-readable explanation.  Profile specific guidance and examples are provided as well.  The [Formal Profile Definition] below provides the  formal summary, definitions, and  terminology requirements.

**Each {{{base_type}} must have:**

1. a type code of `collection`
1. a Da Vinci Alerts Communication Profile
1. a request method of `POST`

**Each {{base_type}} must support:**

1.  a US Core Patient Profile
1.  a US Core Encounter Profile
1.  other resource entries as described in the next section

**Additional Profile specific implementation guidance:**

- The Resources referenced in the [Da Vinci Communication Profile] payload element are typically included in the alert Bundle.  See the Alert Scenario summary table for a list of which resources are included in the bundle.

### Examples

- [Alert Bundle Example](Bundle-communication-alert-admit-01.html)

{% include link-list.md %}
