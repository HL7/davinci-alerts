
### Resource Profiles

The following Profiles for FHIR *resources* have been defined for this implementation guide.

**Base Da Vinci Notification Profiles**

- [Da Vinci Notifications MessageHeader Profile]
- [Da Vinci Notifications Bundle Profile]

**Da Vinci Admission/Transfer/Discharge Notification Profiles**

- [Da Vinci Admit Notification MessageHeader Profile]
- [Da Vinci Discharge Notification MessageHeader Profile]
- [Da Vinci Transfer Notification MessageHeader Profile]
- [Da Vinci Admit/Transfer/Discharge Notification Condition Profile]
- [Da Vinci Admit/Transfer/Discharge Notification Coverage Profile]
- [Da Vinci Admit/Transfer/Discharge Notification Encounter Profile]


<!-- {% raw %}
{% include list-simple-profiles.xhtml %}

{% for sd_hash in site.data.structuredefinitions -%}
  {%- assign sd = sd_hash[1] -%}
  {%- if sd.kind  == "resource" -%}
    - [{{sd.name}}]({{sd.path}})
  {%- endif -%}
{%- endfor -%}


### Extensions

The following Extensions have been defined for this implementation guide.

- [Da Vinci Notifications Must Support Extension]

<br />

{% endraw %} -->

{% include link-list.md %}
