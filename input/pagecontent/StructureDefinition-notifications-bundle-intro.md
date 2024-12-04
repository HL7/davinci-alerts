{% assign base_id = {{include.id}} %}
{% assign base_type = {{site.data.structuredefinitions.[base_id].type}} %}

### Introduction

{{ site.data.structuredefinitions.[base_id].description }}

### Mandatory and Must Support Data Elements

The following data-elements are mandatory (i.e., data MUST be present) or must be supported if the data is present in the sending system ([Must Support] definition). They are presented below in a simple human-readable explanation.  Profile specific guidance and examples are provided as well.  The [Formal Profile Definition] below provides the  formal summary, definitions, and  terminology requirements.

**Each {{{base_type}} must have:**

1. A logical id
1. A type code of "message"
1. A timestamp
1. An entry for the MessageHeader
1. An entry for the event or request resource reference by 'MessageHeader.focus'

**Additional Profile specific implementation guidance:**

The elements `Bundle.total`, `Bundle.entry.search`, `Bundle.entry.request`, and `Bundle.entry.response` are Cardinality = 0..0 (in other words, constrained out) because of the invariants `bdl-1`.`bdl-3`.`bdl-3`. and `bdl-4` defined in the FHIR Bundle resource.

<!-- {% raw %} ### Examples

- [Bundle Admit Notification Message Bundle 01]
- [Bundle Discharge Notification Message Bundle 01] {% endraw %} -->

{% include link-list.md %}
