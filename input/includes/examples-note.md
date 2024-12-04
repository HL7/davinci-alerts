
### Examples

For examples of this profile within a bundle, see these message Bundles examples:

{% for example in site.data.example_profile_list -%}
{% if example[1] contains profile_url -%}
- [{{example[0]}}]
{% endif -%}
{% endfor %} 
