
{% assign base_id = {{include.id}} %}
{% assign base_type = {{site.data.structuredefinitions.[base_id].type}} %}

### Mandatory and Must Support Data Elements

The following data-elements are mandatory (i.e., data MUST be present) or must be supported if the data is present in the sending system ([Must Support] definition). They are presented below in a simple human-readable explanation.  Profile specific guidance and examples are provided as well.  The [Formal Profile Definition] below provides the  formal summary, definitions, and  terminology requirements.

**Each {{base_type}} must have:**

1. A beneficiary
1. A reference to a payor

**Each {{base_type}} must support:**

1. A business identifier
1. A subscriber id

**Additional Profile specific implementation guidance:**

- Note that for the admission/transfer/discharge scenario, the `Coverage.beneficiary` is a "reverse link" to the Patient resource and cannot be traversed from the MessageHeader within the Message Bundle.  There is no mechanism to enforce profiles in a message on a reverse link except via GraphDefinition.
- The `Coverage.payor` references the [DEQM Organization Profile] profile to mandate an identifier and support additional identifier types.

### Examples

{% include examples-note.md %}

- [{{base_type}} Example]({{base_type}}-{{base_id}}-01.html)

{% include link-list.md %}
