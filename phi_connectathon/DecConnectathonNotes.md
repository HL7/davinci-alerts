
## Servers: (all open)

1. Cigna: https://ttbfdsk0pc.execute-api.us-east-1.amazonaws.com/dev
1. Ref implementation ( Logica ): https://davinci-alerts-receiver.logicahealth.org/fhir/$process-message
1. WildFhir (Aegis):  http://wildfhir4.aegis.net/fhir4-0-0


## Clients:

1. Ref implementation (Logica)
2. Keith Boone: (converted ADT v2 to Da Vinci Notification Messages)
3. Eric Haas: Flask app facade using Synthea generated data from FHIR reference Servers - pending

**Message Successfully Sent to all Servers**

## Accomplishments:

#### Sync v Async Messaging

- Established that for notifications (vs for example requests) will be *synchronous* messaging.
- If there is a need to batch a large number of messages (1000's) the bulk data guidance should be used.
- However,batching smaller number of messages can use transaction bundles synchronously.

#### Error paths:

Guide only covers the "happy path".  Errors are covered in the `$process-message` documentation in the FHIR specification.  Polled the participants to determine if more guidance is needed.

In addition to basic guidance in FHIR specification for `$process-message`:

- `200`,`202`,`204`+/- OperationOutcome all ok for successful transactions
- `401`,`404`+/- OperationOutcome no point in retry
- `429` +/- OperationOutcome  retry but slow down traffic
- `500+` +/- OperationOutcome - server issues  may retry a few times

#### FHIR Specification issues
- `MessageHeader.author` definition mentions device, but choice of Device not available:  Tracker pending
- Messaging section states that all messages expect response message which is not how notifications is written. For notification - only expect either only an http response or an OperationOutcome Tracker pending

#### `Encounter.type` codes at time of notification

- `Encounter.type` may not be known when send notification.
- Keith review 1/2 million v2 ADT's only.
   - 10% had PV1-4 (Admission Type) codes
   - 20% had PV1-18 (Patient Types) codes

   FYI 'Encounter.reasonCode' codes at time of ADT
    - 4% had PV2-3 (admit reason) codes
    - ~50% had PV2-3 (admit reason) free text

  Options if data is not available

  1. is to drop US Core profile and make own DaVinci Notification Profile
  1. use the appropriate “unknown” concept code from the value set if available
