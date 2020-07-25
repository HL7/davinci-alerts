
|Link|Source Profile|Path|Target Profile |Min|Max|Must Support|
|---|---|---|---|---|---|---|
|1|Da Vinci Notification MessageHeader Profile|MessageHeader.focus|US Core Encounter Profile|1|1|true|
|2|US Core Encounter Profile|Encounter.location|US Core Location Profile|1|*|true|
|3|US Core Encounter Profile|Encounter.participant.individual|US Core Practitioner Profile|0|*|true|
|4|US Core Encounter Profile|Encounter.subject|US Core Patient Profile|1|1|true|
|5|Da Vinci HRex Coverage Profile|Coverage.beneficary|US Core Patient Profile|0|1|true|
|6|US Core Condition Profile|Condition.encounter|US Core Encounter Profile|0|*|true|
|7|Da Vinci Notification MessageHeader Profile|MessageHeader.sender|US Core Practitioner Profile\|US Core PractitionerRole Profile\|US Core Organization Profile|0|1|true|
|8|Da Vinci Notification MessageHeader Profile|MessageHeader.responsible|US Core Practitioner Profile\|US Core PractitionerRole Profile\|US Core Organization Profile|0|1|true|
|9|Da Vinci Notification MessageHeader Profile|MessageHeader.author|US Core Practitioner Profile\|US Core PractitionerRole Profile|0|1|true|
