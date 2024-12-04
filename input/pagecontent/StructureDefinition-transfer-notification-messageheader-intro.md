{% assign base_id = {{include.id}} %}
{% assign profile_url = {{site.data.structuredefinitions.[base_id].url}} %}

### Mandatory and Must Support Data Elements

The following data-elements are mandatory (i.e., data MUST be present) or must be supported if the data is present in the sending system ([Must Support] definition). They are presented below in a simple human-readable explanation.  Profile specific guidance and examples are provided as well.  The [Formal Profile Definition] below provides the  formal summary, definitions, and  terminology requirements.

**Each {{{base_type}} must have:**

1. An event code of "notification-transfer"
1. An event focus reference to the Da Vinci Admit/Discharge/Transfer Notification Encounter Profile which will be bundled in the message

{% include examples-note.md %}

{% include link-list.md %}