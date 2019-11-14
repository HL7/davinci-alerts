---
title: Profiles defined as part of this Guide
layout: default
active: profiles
---
### Resource Profiles

The following Profiles for FHIR *resources* have been defined for this implementation guide.

**Base Da Vinci Notification Profiles**

- [Da Vinci Notifications MessageHeader Profile](StructureDefinition-notifications-message-header.html)
- [Da Vinci Notifications Bundle Profile](StructureDefinition-notifications-bundle.html)
- [Da Vinci Notifications MessageDefinition Profile](StructureDefinition-notifications-message-definition.html)

**Da Vinci Admission/Discharge Notification Profiles**

- [Da Vinci Admit Notification MessageHeader Profile](StructureDefinition-admit-notification-messageheader.html)
- [Da Vinci Discharge Notification MessageHeader Profile](StructureDefinition-discharge-notification-messageheader.html)
- [Da Vinci Admit/Discharge Notification Condition Profile](StructureDefinition-admit-discharge-notification-condition.html)
- [Da Vinci Admit/Discharge Notification Coverage Profile](StructureDefinition-admit-discharge-notification-coverage.html)
- [Da Vinci Admit/Discharge Notification Encounter Profile](StructureDefinition-admit-discharge-notification-encounter.html)


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
