|Link|Source Profile|Path|Target Profile |Min|Max|
|---|---|---|---|---|---|
|1|Da Vinci Notification MessageHeader Profile|MessageHeader.focus|US Core Encounter Profile|1|1|
|2|US Core Encounter Profile|Encounter.location|US Core Location Profile|1|*|
|3|US Core Encounter Profile|Encounter.participant.individual|US Core Practitioner Profile|0|*|
|4|US Core Encounter Profile|Encounter.subject|US Core Patient Profile|1|1|
|5|Da Vinci HRex Coverage Profile|Coverage.beneficary|US Core Patient Profile|0|1|
|6|US Core Condition Profile|Condition.encounter|US Core Encounter Profile|0|*|
|12|Da Vinci Notification MessageHeader Profile|MessageHeader.sender|US Core Practitioner Profile\|US Core PractitionerRole Profile\|US Core Organization Profile|0|1|
|12|Da Vinci Notification MessageHeader Profile|MessageHeader.responsible|US Core Practitioner Profile\|US Core PractitionerRole Profile\|US Core Organization Profile|0|1|
|13|Da Vinci Notification MessageHeader Profile|MessageHeader.author|US Core Practitioner Profile\|US Core PractitionerRole Profile|0|1|
