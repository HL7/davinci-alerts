---
title: Profiles defined as part of this Guide
layout: default
active: profiles
---
### Resource Profiles

The following Profiles for FHIR *resources* have been defined for this implementation guide.

- [Da Vinci Notification Message Bundle]
- [Da Vinci Notifications MessageHeader Profile]

<!-- {% raw %}
{% include list-profiles.xhtml %}
{% endraw %} -->

{% for sd_hash in site.data.structuredefinitions -%}
  {%- assign sd = sd_hash[1] -%}
  {%- if sd.kind  == "resource" -%}
    - [{{sd.name}}]({{sd.path}})
  {%- endif -%}
{%- endfor -%}

<br />

<!-- {% raw %}

### Extensions

These extensions have been defined for this implementation guide.


{% include list-extensions.xhtml %}
{% endraw %} -->

{% include link-list.md %}
