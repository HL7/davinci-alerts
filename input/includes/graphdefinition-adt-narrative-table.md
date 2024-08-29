
|Link|Source Profile|Path|Target Profile |Min|Max|
|---|---|---|---|---|---|
|1|Da Vinci Notification MessageHeader Profile|MessageHeader.focus|Da Vinci Admit/Discharge/Transfer Notification Encounter Profile|1|1|
|2|Da Vinci Admit/Discharge/Transfer Notification Encounter Profile|Encounter.location|US Core Location Profile|1|*|
|3|Da Vinci Admit/Discharge/Transfer Notification Encounter Profile|Encounter.participant.individual|US Core Practitioner Profile|0|*|
|4|Da Vinci Admit/Discharge/Transfer Notification Encounter Profile|Encounter.subject|US Core Patient Profile|1|1|
|5|Da Vinci Admit/Discharge/Transfer Notification Coverage Profile|Coverage.beneficary|US Core Patient Profile|0|1|
|6|US Core Condition Encounter Diagnosis Profile|Condition.encounter|Da Vinci Admit/Discharge/Transfer Notification Encounter Profile|0|*|
|7|Da Vinci Notification MessageHeader Profile|MessageHeader.sender|US Core Practitioner Profile\|US Core PractitionerRole Profile\|US Core Organization Profile|0|1|
|8|Da Vinci Notification MessageHeader Profile|MessageHeader.responsible|US Core Practitioner Profile\|US Core PractitionerRole Profile\|US Core Organization Profile|0|1|
|9|Da Vinci Notification MessageHeader Profile|MessageHeader.author|US Core Practitioner Profile\|US Core PractitionerRole Profile|0|1|
