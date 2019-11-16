{% assign base_id = {{page.id}} %}
{% assign base_type = {{site.data.structuredefinitions.[base_id].type}} %}

{{site.data.structuredefinitions.[base_id].description}}

### Mandatory and Must Support Data Elements

The following data-elements are mandatory (i.e data MUST be present) or must be supported if the data is present in the sending system ([Must Support] definition). They are presented below in a simple human-readable explanation.  Profile specific guidance and examples are provided as well.  The [Formal Profile Definition] below provides the  formal summary, definitions, and  terminology requirements.

**Each {{{base_type}} must have:**

1. A canonical url
1. A status
1. A date
1. An EventCoding
1. A category of "notification"
1. An event focus reference
1. A GraphDefinition to define the Bundle contents


**Each {{base_type}} must support:**

1. A version
1. A name
1. A title
1. A publisher
1. A description

**Additional Profile specific implementation guidance:**

none

### Examples

- [Da Vinci Notification Admit Message Definition]
- [Da Vinci Notification Discharge Message Definition]

{% include link-list.md %}
