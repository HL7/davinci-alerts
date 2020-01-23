CMS Connectathon Notes

- error if send message 2x  - code? 400 or 409 + oo = conflict need identifier on MH so can uniquely identify the instance.


https://dev.fhir.onemedical.io/r4/$process-message


bearer token: heqfnVgiMGCJuef

2PM Breakout with Subscriptions:

- MH.focus vs Subscriptions topic
- differences
    - Sub - asked
    - Not - not asked
- Not - Graph of details.  intent was to be able to give enough information to do something useful.
    for sub - just the identifier given that there is a graphs.
    should the graph be static or use case specific or open.

- want them to mesh together...

- unifying principles that tie together.

- trigger - focal resources, triggering event computationally,

- may request in Subscriptions with Graph

- Topic defines state changes - can we use this for defining triggers for unsolicited Notification.

- hybrid use cases

- IHE Mobile Access to Health Documents.



### Convergance :  

## US Core:

  INferno testing
  Postman testing

  servers - Cerner, Epic

  INferno issues....

  Add text calling out Location/PR not being referenced by other resources - intentional.
     - resolution
  Discuss whether should limit MR profile: with intent = 'order'  to be computable.
  Tehnnical corrections
    - fix 2 bullet in med list guidance to clarify in intent = 'order'  (should be sub bullet)
    - in USCDI Table = 'MedStatement' change to 'MedRequest'
    - add Write to DocRef QuickStart
    - revisit provenance - remove location, org, medication, practrole, Practitioner
    - add SHALL support search with status as explicit
    - clarify text in clinical note on minimum required to reference only the DocRef. and that the DiagnosticReport codes are strongly suggested but not required.
    - AllergyIntolerance.clinicalStatus
Condition.clinicalStatus
DocumentReference.status
Immunization.status
Goal.lifecycleStatus need follow up for trackers to Hl7

Referencing resource - not required.  make a warning.



send list of potential argo prooposal to Prashanth Tharakan interest in dynamic reg.

  reviewed issues with
  Provenance, SecuritS
  Guidance on SHALLS

  add write back into QuickStart

  tracker to update med list text on intent = order - combine with first bullet.


## Notification

  get HIMMS endpoints set up to work with RI:

  sign up on endpoint.

  Cigna,
  Guidewell/Edifecs - checked and request to change endpoint ot $process-message
      -  need existing patient to resolve


  HIMMS Stuff - checking the scenario, check the spreadsheet, confirm with Carrie that have all the information

  IBC - not present.
