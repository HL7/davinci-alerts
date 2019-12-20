CoverageTypeAndClass


a) HealthLX are going to be at the CMS Connectathon 8,9 January to lead the Notifications track?  Yes yay..
     - Eric will be there for another (US Core) track
     - Need to participate to be at HIMMS Showcase

b) See if we can coordinate on some Synthea test data.

c) Update the RI to choose from a set of events in the test data ( recources as persistance layer or in a db) and dynamically build a message from them.

d) stretch goal of creating transaction bundle.
     - need information test data..
     - basic demographic data of the patient pool  ( test data )

d) Stretch goal of validation against the MessageDefinition and GraphDefinition

e) Connectathon ... RI client -
Hapi java client looks for metadata and fails if none found,, and if the server responds with a 200 and no response message is client failing because the
client is expecting a response or (we think a 204)
- we think that is a client bug.  James following up on Zulip
- ideally success is any of 200, 202, 204.+/- operationoutcome and no Response message.
