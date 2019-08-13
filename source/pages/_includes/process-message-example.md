### Examples
{:.no_toc}

**Scenario:**

Patient Y has been admitted to Provider X 's facility.  Acting in the role of Alert Sender Provider X alerts Payer Z who is acting in the role Alert Recipient of the admission.  The Alert is transacted as the `[$process-message]` operation. The body of the operation is a Message Bundle containing:

1. The Message Header which is the first resource in the bundle and contains the the message event code- that identifies the nature of the request message.
1. The other resources in the bundle depend on the type of the Alert event use case.

An HTTP Status success code is returned on successful submission.

**Push Alert Notification using the $process-message**

`POST [base]/$process-message`

**Request body**

~~~
{
	"resourceType": "Bundle",
	"id": "201908121155.55-admit-01",
	"type": "message",
	"entry": [
		{
			"fullUrl": "urn:uuid:b4eb5ff2-6220-400d-be9f-603db6be35",
			"resource": {
				"resourceType": "MessageHeader",
				"id": "b4eb5ff2-6220-400d-be9f-603db6be35",
				"meta": {
					"versionId": "1",
					"lastUpdated": "2019-03-06T09:33:05.501Z"
				},
				"eventCoding": {
					"system": "http://example.org/fhir/message-events",
					"code": "dv-alert"
				},
				"destination": [
					{
						"name": "Acme Message Gateway",
						"target": {
							"reference": "Device/example"
						},
						"endpoint": "llp:10.11.12.14:5432",
						"receiver": {
							"reference": "http://acme.com/ehr/fhir/Practitioner/2323-33-4"
						}
					}
				],
				"sender": {
					"reference": "http://acme.com/ehr/fhir/Organization/1"
				},
				"source": {
					"name": "Acme Central Patient Registry",
					"software": "ACME",
					"endpoint": "http://acme.com/ehr/fhir"
				},
				"reason": {
					"coding": [
						{
							"system": "http://hl7.org/fhir/us/davinci-alerts/CodeSystem/communication-topic",
							"code": "alert-admit",
							"display": "Alert admit"
						}
					]
				},
				"focus": [
					{
						"reference": "Encounter/admit-1"
					}
				]
			}
		}, {
			"fullUrl": "http://acme.com/ehr/fhir/Patient/example",
			"resource": {
				"resourceType": "Patient",
				"id": "example",
				"meta": {
					"profile": [
						"http://hl7.org/fhir/us/core/StructureDefinition/us-core-patient"
					]
				},
				"extension": [
					{
						"url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-race",
						"extension": [
							{
								"url": "ombCategory",
								"valueCoding": {
									"system": "urn:oid:2.16.840.1.113883.6.238",
									"code": "2106-3",
									"display": "White"
								}
							}, {
								"url": "ombCategory",
								"valueCoding": {
									"system": "urn:oid:2.16.840.1.113883.6.238",
									"code": "1002-5",
									"display": "American Indian or Alaska Native"
								}
							}, {
								"url": "ombCategory",
								"valueCoding": {
									"system": "urn:oid:2.16.840.1.113883.6.238",
									"code": "2028-9",
									"display": "Asian"
								}
							}, {
								"url": "detailed",
								"valueCoding": {
									"system": "urn:oid:2.16.840.1.113883.6.238",
									"code": "1586-7",
									"display": "Shoshone"
								}
							}, {
								"url": "detailed",
								"valueCoding": {
									"system": "urn:oid:2.16.840.1.113883.6.238",
									"code": "2036-2",
									"display": "Filipino"
								}
							}, {
								"url": "text",
								"valueString": "Mixed"
							}
						]
					}, {
						"url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-ethnicity",
						"extension": [
							{
								"url": "ombCategory",
								"valueCoding": {
									"system": "urn:oid:2.16.840.1.113883.6.238",
									"code": "2135-2",
									"display": "Hispanic or Latino"
								}
							}, {
								"url": "detailed",
								"valueCoding": {
									"system": "urn:oid:2.16.840.1.113883.6.238",
									"code": "2184-0",
									"display": "Dominican"
								}
							}, {
								"url": "detailed",
								"valueCoding": {
									"system": "urn:oid:2.16.840.1.113883.6.238",
									"code": "2148-5",
									"display": "Mexican"
								}
							}, {
								"url": "text",
								"valueString": "Hispanic or Latino"
							}
						]
					}, {
						"url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-birthsex",
						"valueCode": "F"
					}
				],
				"identifier": [
					{
						"use": "usual",
						"type": {
							"coding": [
								{
									"system": "http://terminology.hl7.org/CodeSystem/v2-0203",
									"code": "MR",
									"display": "Medical Record Number"
								}
							],
							"text": "Medical Record Number"
						},
						"system": "http://hospital.smarthealthit.org",
						"value": "1032702"
					}
				],
				"active": true,
				"name": [
					{
						"family": "Shaw",
						"given": [
							"Amy", "V."
						]
					}
				],
				"telecom": [
					{
						"system": "phone",
						"value": "555-555-5555",
						"use": "home"
					}, {
						"system": "email",
						"value": "amy.shaw@example.com"
					}
				],
				"gender": "female",
				"birthDate": "2007-02-20",
				"address": [
					{
						"line": [
							"49 Meadow St"
						],
						"city": "Mounds",
						"state": "OK",
						"postalCode": "74047",
						"country": "US"
					}
				]
			}
		}, {
			"fullUrl": "http://acme.com/ehr/fhir/Encounter/admit-1",
			"resource": {
				"resourceType": "Encounter",
				"id": "admit-1",
				"meta": {
					"lastUpdated": "2017-05-26T11:56:57.250-04:00",
					"profile": [
						"http://hl7.org/fhir/us/core/StructureDefinition/us-core-encounter"
					]
				},
				"status": "finished",
				"class": {
					"system": "http://terminology.hl7.org/CodeSystem/v3-ActCode",
					"code": "IMP",
					"display": "inpatient encounter"
				},
				"type": [
					{
						"coding": [
							{
								"system": "http://www.ama-assn.org/go/cpt",
								"code": "99234"
							}
						],
						"text": "inpatient hospital care"
					}
				],
				"subject": {
					"reference": "Patient/example"
				},
				"period": {
					"start": "2015-11-01T17:00:14-05:00",
					"end": "2015-11-01T18:00:14-05:00"
				},
				"location": [
					{
						"location": {
							"reference": "Location/hl7east"
						}
					}
				],
				"diagnosis": [
					{
						"condition": {
							"reference": "Condition/admit-1",
							"display": "Complications from Roel's TPF chemotherapy on January 28th, 2013"
						}
					}
				]
			}
		}, {
			"fullUrl": "http://acme.com/ehr/fhir/Condition/admit-1",
			"resource": {
				"resourceType": "Condition",
				"id": "admit-1",
				"meta": {
					"profile": [
						"http://hl7.org/fhir/us/core/StructureDefinition/us-core-condition"
					]
				},
				"clinicalStatus": {
					"coding": [
						{
							"system": "http://terminology.hl7.org/CodeSystem/condition-clinical",
							"code": "active",
							"display": "Active"
						}
					],
					"text": "Active"
				},
				"verificationStatus": {
					"coding": [
						{
							"system": "http://terminology.hl7.org/CodeSystem/condition-ver-status",
							"code": "confirmed",
							"display": "Confirmed"
						}
					],
					"text": "Confirmed"
				},
				"category": [
					{
						"coding": [
							{
								"system": "http://terminology.hl7.org/CodeSystem/condition-category",
								"code": "problem-list-item",
								"display": "Problem List Item"
							}
						],
						"text": "Problem"
					}
				],
				"code": {
					"coding": [
						{
							"system": "http://snomed.info/sct",
							"code": "442311008",
							"display": "Liveborn born in hospital"
						}
					],
					"text": "Single liveborn, born in hospital"
				},
				"subject": {
					"reference": "urn:uuid:3852d906-a361-11e9-86cd-a4d18ccf5172",
					"display": "Amy V. Shaw"
				},
				"onsetDateTime": "2016-08-10"
			}
		}
	]
}
~~~

**Response**

~~~
HTTP/1.1 200 OK
[other headers]
~~~
