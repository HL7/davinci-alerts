
### Resource Profiles

The following Profiles for FHIR *resources* have been defined for this implementation guide.

**Base Da Vinci Notification Profiles**

- [Da Vinci Notifications MessageHeader Profile]
- [Da Vinci Notifications Bundle Profile]
- [Da Vinci Notifications MessageDefinition Profile]
- [Da Vinci Notifications GraphDefinition Profile]

**Da Vinci Admission/Discharge Notification Profiles**

- [Da Vinci Admit Notification MessageHeader Profile]
- [Da Vinci Discharge Notification MessageHeader Profile]
- [Da Vinci Admit/Discharge Notification Condition Profile]
- [Da Vinci Admit/Discharge Notification Coverage Profile]
- [Da Vinci Admit/Discharge Notification Encounter Profile]


<!-- {% raw %}
{% include list-simple-profiles.xhtml %}

{% for sd_hash in site.data.structuredefinitions -%}
  {%- assign sd = sd_hash[1] -%}
  {%- if sd.kind  == "resource" -%}
    - [{{sd.name}}]({{sd.path}})
  {%- endif -%}
{%- endfor -%}

{% endraw %} -->



### Extensions

The following Extensions have been defined for this implementation guide.

- [Da Vinci Notifications Must Support Extension]

<br />

{% include link-list.md %}
