<!-- This liquid script creates the Direct ADT notifications mapping table. The source table for it is the file input/data/DirectToDaVinciMap.csv
-->

{% assign rows = site.data.DirectToDaVinciMap %}

<table class="grid" markdown="1">
{% for item in rows %}
    {% if forloop.first %}
        <thead>
        <tr>
        <!-- <th>Row #</th> -->
        <th>Direct Trust ADT Message Data Element</th>
        <th>Da Vinci Notification Message Element</th>
        <th>Mapping Comments</th>
        </tr>
        </thead>
        <tbody>
    {% endif %}

    {% assign adt = item["V2 Segment Name"] | append: "-"] | append: item[" V2 Field Identifier"] | append: " "] | append: item["Data element name"] %} 
    {% assign dv_notification_path = item["joined"] %}
    {% assign comments = item["FHIR Value set, other notes"] %}
    <tr>
    <!-- <td>{{forloop.index}}</td> -->
    <td>{{adt}}</td>
    <td>{{dv_notification_path | safe }}</td>
    <td>{{comments}}</td>
    </tr>
    
    {% if forloop.last %}
        </tbody>
        </table>
    {% endif %}
{% endfor %}


