---
title: Profiles defined as part of this Guide
layout: default
active: profiles
---
### Resource Profiles

The following Profiles for FHIR *resources* have been defined for this implementation guide.

**Base Da Vinci Notification Profiles**

- [Da Vinci Notifications Bundle Profile](StructureDefinition-notifications-bundle.html)
- [Da Vinci Notifications MessageDefinition Profile](StructureDefinition-admit-notifications-messagedefinition.html)
- [Da Vinci Notifications MessageHeader Profile](StructureDefinition-admit-notifications-messageheader.html) 

**Da Vinci Admission Notification Profiles**

- [Da Vinci Admit Notification Bundle Profile](StructureDefinition-admit-notification-bundle.html)
- [Da Vinci Admit Notification MessageHeader Profile](StructureDefinition-admit-notify-messageheader.html)

**Da Vinci Discharge Notification Profiles**

- [Da Vinci Discharge Notification Bundle Profile](StructureDefinition-discharge-notification-bundle.html)
- [Da Vinci Discharge Notification MessageHeader Profile](StructureDefinition-discharge-notify-messageheader.html)




<!-- {% raw %}
{% include list-simple-profiles.xhtml %}



{% for sd_hash in site.data.structuredefinitions -%}
  {%- assign sd = sd_hash[1] -%}
  {%- if sd.kind  == "resource" -%}
    - [{{sd.name}}]({{sd.path}})
  {%- endif -%}
{%- endfor -%}

{% endraw %} -->

<!-- {% raw %}

### Extensions

These extensions have been defined for this implementation guide.

{% include list-extensions.xhtml %}

{% endraw %} -->

<br />

{% include link-list.md %}
