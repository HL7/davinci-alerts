
{% assign base_id = {{page.id}} %}
{% assign base_type = {{site.data.structuredefinitions.[base_id].type}} %}

{{site.data.structuredefinitions.[base_id].description}}

### Mandatory and Must Support Data Elements

The following data-elements are mandatory (i.e., data MUST be present) or must be supported if the data is present in the sending system ([Must Support] definition). They are presented below in a simple human-readable explanation.  Profile specific guidance and examples are provided as well.  The [Formal Profile Definition] below provides the  formal summary, definitions, and  terminology requirements.

**Each {{{base_type}} must have:**

1. A Da Vinci Dicharge Notification MessageHeader Profile entry
1. One or more US Core Encounter Profile entries
1. A US Core Patient Profile entry
1. One or more US Core Location Profile entries

**Each {{base_type}} must support one or more:**

1. US Core Condition Profile entries
1. Da Vinci HRex Coverage Profile entries
1. US Core Practitioner Profile entries
1. US Core PractitionerRole Profile entries
1. US Core Organization Profile entries

### Examples

- [Alert Bundle Example](Bundle-communication-alert-admit-01.html)

{% include link-list.md %}
