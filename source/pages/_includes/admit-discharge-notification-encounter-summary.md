**Encounter**

#### Summary of the Mandatory Requirements
1.  A Patient Reference  in `Encounter.subject`

#### Summary of the Must Support Requirements
1. One or more  Participants  in `Encounter.participant`
   - which should have an Individual Reference value  in `Encounter.participant.individual`
1. One or more  Locations  in `Encounter.location`
   - which must have a Location Reference value  in `Encounter.location.location`