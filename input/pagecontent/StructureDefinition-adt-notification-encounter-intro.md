
{% assign base_id = {{include.id}} %}
{% assign profile_url = {{site.data.structuredefinitions.[base_id].url}} %}



### Mandatory and Must Support Data Elements

The following data-elements are mandatory (i.e., data MUST be present) or must be supported if the data is present in the sending system ([Must Support] definition). They are presented below in a simple human-readable explanation.  Profile specific guidance and examples are provided as well.  The [Formal Profile Definition] below provides the  formal summary, definitions, and  terminology requirements.

**Each {{base_type}} must have:**

1. A reference(s) to US Core Patient which will be bundled in the message

**Each {{base_type}} must support:**

1. A reference(s) to US Core Practitioner which will be bundled in the message
1. A reference(s) to US Core Location which will be bundled in the message

**Additional Profile specific implementation guidance:**

- Following [US Core guidance] the [Da Vinci Admit/Discharge/Transfer Notification Condition Profile] resource references the Encounter resource instead using `Encounter.diagnosis.condition` to create a forward link from the encounter to the related diagnoses.
- The `reference` attribute is required for `Encounter.subject`, `Encounter.participant.individual`, and `Encounter.location.location` so there is no question how to find the resource inside the bundle - the use of *only* an `identifier` attribute (in other words, a logical reference) is not permitted.

{% include examples-note.md %}

{% include link-list.md %}