{% assign base_id = {{page.id}} %}
{% assign base_type = {{site.data.structuredefinitions.[base_id].type}} %}

{{site.data.structuredefinitions.[base_id].description}}

### Mandatory and Must Support Data Elements

The following data-elements are mandatory (i.e data MUST be present) or must be supported if the data is present in the sending system ([Must Support] definition). They are presented below in a simple human-readable explanation.  Profile specific guidance and examples are provided as well.  The [Formal Profile Definition] below provides the  formal summary, definitions, and  terminology requirements.

**Each {{{base_type}} must have:**

1. A code for the type of event
1. A reference to the event's focus resource

**Each {{base_type}} must support:**

1. A destination
1. A sender
1. An author
1. The responsible party

**Additional Profile specific implementation guidance:**

none

### Examples

- [Alert Bundle Example](Bundle-communication-alert-admit-01.html)

{% include link-list.md %}
