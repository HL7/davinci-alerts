{% assign base_id = {{include.id}} %}
{% assign profile_url = {{site.data.structuredefinitions.[base_id].url}} %}



### Mandatory and Must Support Data Elements

The following data-elements are mandatory (i.e., data MUST be present) or must be supported if the data is present in the sending system ([Must Support] definition). They are presented below in a simple human-readable explanation.  Profile specific guidance and examples are provided as well.  The [Formal Profile Definition] below provides the  formal summary, definitions, and  terminology requirements.

**Each {{{base_type}} must have:**

1. A logical id
1. A code for the type of event
1. The message source application
1. A reference to the event's focus resource(s) which will be bundled in the message

**Each {{base_type}} must support:**

1. A destination
1. A reference to the sender which will be bundled in the message
1. A reference to author which will be bundled in the message
1. A reference to responsible party which will be bundled in the message

**Additional Profile specific implementation guidance:**

- The `destination.endpoint` and `source.endpoint` can be in any form of url the server understands (usually, https: or mllp:). The URI is allowed to be relative; in which case, it is relative to the server end-point
- The `reference` attribute is required for `MessageHeader.sender`, `MessageHeader.author`, `MessageHeader.responsible`, and `MessageHeader.focus` so there is no question how to find the resource inside the bundle - the use of *only* an `identifier` attribute (in other words, a logical reference) is not permitted.
- This profile uses the [Alternate Reference] extension to allow a Device to be a sender or author, because in some automated systems there may be no human provider involved in certain notifications.  This pattern aligns with [FHIR R5 MessageHeader] for these elements.  See the [Admit Notification Message Bundle 02] for how this is implemented.

{% include examples-note.md %}

{% include link-list.md %}
