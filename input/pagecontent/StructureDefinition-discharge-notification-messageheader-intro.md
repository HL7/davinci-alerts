{% assign base_id = {{include.id}} %}
{% assign base_type = {{site.data.structuredefinitions.[base_id].type}} %}

### Introduction

{{ site.data.structuredefinitions.[base_id].description }}

### Mandatory and Must Support Data Elements

The following data-elements are mandatory (i.e., data MUST be present) or must be supported if the data is present in the sending system ([Must Support] definition). They are presented below in a simple human-readable explanation.  Profile specific guidance and examples are provided as well.  The [Formal Profile Definition] below provides the  formal summary, definitions, and  terminology requirements.

**Each {{{base_type}} must have:**

1. An event code of "notification-discharge"
1. An event focus reference to the Da Vinci Admit/Discharge/Transfer Notification Encounter Profile which will be bundled in the message

<!-- {% raw %} ### Examples

{% include examples-note.md %}

- [{{base_type}} Example]({{base_type}}-{{base_id}}-01.html) {% endraw %} -->

{% include link-list.md %}
