
{% assign base_id = {{include.id}} %}
{% assign base_type = {{site.data.structuredefinitions.[base_id].type}} %}

### Mandatory and Must Support Data Elements

The following data-elements are mandatory (i.e., data MUST be present) or must be supported if the data is present in the sending system ([Must Support] definition). They are presented below in a simple human-readable explanation.  Profile specific guidance and examples are provided as well.  The [Formal Profile Definition] below provides the  formal summary, definitions, and  terminology requirements.

**Each {{base_type}} must have:**

1. A reference to Da Vinci Admit/Transfer/Discharge Notification Encounter Profile which will be bundled in the message

**Additional Profile specific implementation guidance:**

- Note that for the admission/transfer/discharge scenario, `Condition.encounter` is a "reverse link" to the Encounter resource and cannot be traversed from the MessageHeader within the Message Bundle.
- The `reference` attribute is required for `Condition.encounter` so there is no question how to find the resource inside the bundle - the use of *only* an `identifier` attribute (in other words, a logical reference) is not permitted.

### Examples

{% include examples-note.md %}

- [{{base_type}} Example]({{base_type}}-{{base_id}}-01.html)

{% include link-list.md %}
