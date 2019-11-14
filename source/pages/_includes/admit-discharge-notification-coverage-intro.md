
{% assign base_id = {{page.id}} %}
{% assign base_type = {{site.data.structuredefinitions.[base_id].type}} %}

{{site.data.structuredefinitions.[base_id].description}}

**Additional Profile specific implementation guidance:**

Note that for the admission/discharge scenario, the `Coverage.beneficiary` is a "reverse link" to the Encounter resource and cannot be traversed from the MessageHeader within the Message Bundle.

### Examples

- [{{base_type}} Example]({{base_type}}-{{base_id}}-01.html)

{% include link-list.md %}
