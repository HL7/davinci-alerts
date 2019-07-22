### Examples
{:.no_toc}

**Scenario:**

Patient Y has been admitted to Provider X 's facility.  Acting in the role of Alert Sender Provider X alerts Payer Z who is acting in the role Alert Recipient of the admission.  The Alert is transacted as the `$notify` operation. Since there is only a single resource parameter, the body of the operation is an Alert Bundle containing the required Alert Communication profile and required resources for this Alert event use case.  An HTTP Status success code is returned on successful submission and a Bundle with type `transaction-response` that contains one entry for each entry in the request, in the same order, with the outcome of processing the entry.

**Push Alert Notification using the $notify operation**

`POST [base]Communication/$notify`

**Request body**

~~~
{
    "id": "admit-01",
    "entry": [
        {
            "fullUrl": "urn:uuid:3852d906-a361-11e9-86cd-a4d18ccf5172",
            "request": {
                "method": "POST",
                "url": "Patient"
            },
            "resource": {
                "meta": {
                    "profile": [
                        "http://hl7.org/fhir/us/core/StructureDefinition/us-core-patient"
                    ]
                },
                "extension": [
                    {
                        "extension": [
                            {
                                "url": "ombCategory",
                                "valueCoding": {
                                    "code": "2106-3",
                                    "display": "White",
                                    "system": "urn:oid:2.16.840.1.113883.6.238"
                                }
                            },
                            {
                                "url": "ombCategory",
                                "valueCoding": {
                                    "code": "1002-5",
                                    "display": "American Indian or Alaska Native",
                                    "system": "urn:oid:2.16.840.1.113883.6.238"
                                }
                            },
                            {
                                "url": "ombCategory",
                                "valueCoding": {
                                    "code": "2028-9",
                                    "display": "Asian",
                                    "system": "urn:oid:2.16.840.1.113883.6.238"
                                }
                            },
                            {
                                "url": "detailed",
                                "valueCoding": {
                                    "code": "1586-7",
                                    "display": "Shoshone",
                                    "system": "urn:oid:2.16.840.1.113883.6.238"
                                }
                            },
                            {
                                "url": "detailed",
                                "valueCoding": {
                                    "code": "2036-2",
                                    "display": "Filipino",
                                    "system": "urn:oid:2.16.840.1.113883.6.238"
                                }
                            },
                            {
                                "url": "text",
                                "valueString": "Mixed"
                            }
                        ],
                        "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-race"
                    },
                    {
                        "extension": [
                            {
                                "url": "ombCategory",
                                "valueCoding": {
                                    "code": "2135-2",
                                    "display": "Hispanic or Latino",
                                    "system": "urn:oid:2.16.840.1.113883.6.238"
                                }
                            },
                            {
                                "url": "detailed",
                                "valueCoding": {
                                    "code": "2184-0",
                                    "display": "Dominican",
                                    "system": "urn:oid:2.16.840.1.113883.6.238"
                                }
                            },
                            {
                                "url": "detailed",
                                "valueCoding": {
                                    "code": "2148-5",
                                    "display": "Mexican",
                                    "system": "urn:oid:2.16.840.1.113883.6.238"
                                }
                            },
                            {
                                "url": "text",
                                "valueString": "Hispanic or Latino"
                            }
                        ],
                        "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-ethnicity"
                    },
                    {
                        "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-birthsex",
                        "valueCode": "F"
                    }
                ],
                "active": true,
                "address": [
                    {
                        "city": "Mounds",
                        "country": "US",
                        "line": [
                            "49 Meadow St"
                        ],
                        "postalCode": "74047",
                        "state": "OK"
                    }
                ],
                "birthDate": "2007-02-20",
                "gender": "female",
                "identifier": [
                    {
                        "system": "http://hospital.smarthealthit.org",
                        "type": {
                            "coding": [
                                {
                                    "code": "MR",
                                    "display": "Medical Record Number",
                                    "system": "http://terminology.hl7.org/CodeSystem/v2-0203"
                                }
                            ],
                            "text": "Medical Record Number"
                        },
                        "use": "usual",
                        "value": "1032702"
                    }
                ],
                "name": [
                    {
                        "family": "Shaw",
                        "given": [
                            "Amy",
                            "V."
                        ]
                    }
                ],
                "telecom": [
                    {
                        "system": "phone",
                        "use": "home",
                        "value": "555-555-5555"
                    },
                    {
                        "system": "email",
                        "value": "amy.shaw@example.com"
                    }
                ],
                "resourceType": "Patient"
            }
        },
        {
            "fullUrl": "urn:uuid:3857dfb4-a361-11e9-86cd-a4d18ccf5172",
            "request": {
                "method": "POST",
                "url": "Encounter"
            },
            "resource": {
                "meta": {
                    "lastUpdated": "2017-05-26T11:56:57.250-04:00",
                    "profile": [
                        "http://hl7.org/fhir/us/core/StructureDefinition/us-core-encounter"
                    ]
                },
                "class": {
                    "code": "AMB",
                    "display": "ambulatory",
                    "system": "http://terminology.hl7.org/CodeSystem/v3-ActCode"
                },
                "location": [
                    {
                        "location": {
                            "reference": "Location/hl7east"
                        }
                    }
                ],
                "period": {
                    "end": "2015-11-01T18:00:14-05:00",
                    "start": "2015-11-01T17:00:14-05:00"
                },
                "status": "finished",
                "subject": {
                    "reference": "urn:uuid:3852d906-a361-11e9-86cd-a4d18ccf5172"
                },
                "type": [
                    {
                        "coding": [
                            {
                                "code": "99201",
                                "system": "http://www.ama-assn.org/go/cpt"
                            }
                        ],
                        "text": "Office Visit"
                    }
                ],
                "resourceType": "Encounter"
            }
        },
        {
            "fullUrl": "urn:uuid:385a65e0-a361-11e9-86cd-a4d18ccf5172",
            "request": {
                "method": "POST",
                "url": "Condition"
            },
            "resource": {
                "meta": {
                    "profile": [
                        "http://hl7.org/fhir/us/core/StructureDefinition/us-core-condition"
                    ]
                },
                "category": [
                    {
                        "coding": [
                            {
                                "code": "problem-list-item",
                                "display": "Problem List Item",
                                "system": "http://terminology.hl7.org/CodeSystem/condition-category"
                            }
                        ],
                        "text": "Problem"
                    }
                ],
                "clinicalStatus": {
                    "coding": [
                        {
                            "code": "active",
                            "display": "Active",
                            "system": "http://terminology.hl7.org/CodeSystem/condition-clinical"
                        }
                    ],
                    "text": "Active"
                },
                "code": {
                    "coding": [
                        {
                            "code": "442311008",
                            "display": "Liveborn born in hospital",
                            "system": "http://snomed.info/sct"
                        }
                    ],
                    "text": "Single liveborn, born in hospital"
                },
                "onsetDateTime": "2016-08-10",
                "subject": {
                    "display": "Amy V. Shaw",
                    "reference": "urn:uuid:3852d906-a361-11e9-86cd-a4d18ccf5172"
                },
                "verificationStatus": {
                    "coding": [
                        {
                            "code": "confirmed",
                            "display": "Confirmed",
                            "system": "http://terminology.hl7.org/CodeSystem/condition-ver-status"
                        }
                    ],
                    "text": "Confirmed"
                },
                "resourceType": "Condition"
            }
        },
        {
            "fullUrl": "urn:uuid:385bceb2-a361-11e9-86cd-a4d18ccf5172",
            "request": {
                "method": "POST",
                "url": "Communication"
            },
            "resource": {
                "meta": {
                    "profile": [
                        "http://hl7.org/fhir/us/davinci-alerts/StructureDefinition/alerts-communication"
                    ]
                },
                "about": [
                    {
                        "reference": "Coverage/example-1"
                    }
                ],
                "category": [
                    {
                        "coding": [
                            {
                                "code": "alert",
                                "system": "http://terminology.hl7.org/CodeSystem/communication-category"
                            }
                        ],
                        "text": "Alert"
                    }
                ],
                "encounter": {
                    "reference": "urn:uuid:3857dfb4-a361-11e9-86cd-a4d18ccf5172"
                },
                "identifier": [
                    {
                        "system": "urn:oid:1.3.4.5.6.7",
                        "value": "2345678901"
                    }
                ],
                "payload": [
                    {
                        "contentString": "Admit to xyz"
                    },
                    {
                        "contentReference": {
                            "reference": "urn:uuid:3857dfb4-a361-11e9-86cd-a4d18ccf5172"
                        }
                    },
                    {
                        "contentReference": {
                            "reference": "urn:uuid:385a65e0-a361-11e9-86cd-a4d18ccf5172"
                        }
                    }
                ],
                "priority": "routine",
                "recipient": [
                    {
                        "reference": "PractitionerRole/example"
                    }
                ],
                "sender": {
                    "reference": "Organization/example-2"
                },
                "sent": "2019-07-04T18:01:10-08:00",
                "status": "completed",
                "subject": {
                    "reference": "urn:uuid:3852d906-a361-11e9-86cd-a4d18ccf5172"
                },
                "topic": {
                    "coding": [
                        {
                            "code": "blah",
                            "system": "http://hl7.org/fhir/us/davinci-alerts/CodeSystem/blah-codes"
                        }
                    ],
                    "text": "Blah"
                },
                "resourceType": "Communication"
            }
        }
    ],
    "type": "transaction",
    "resourceType": "Bundle"
}
~~~

**Response**

~~~
HTTP/1.1 200 OK
[other headers]
~~~

**Response body**

~~~
{
    "resourceType": "Bundle",
    "id": "42941562-0747-498d-8c02-e37f312f3e99",
    "type": "transaction-response",
    "link": [
        {
            "relation": "self",
            "url": "http://hapi.fhir.org/baseR4"
        }
    ],
    "entry": [
        {
            "response": {
                "status": "201 Created",
                "location": "Patient/87904/_history/1",
                "etag": "1",
                "lastModified": "2019-07-10T22:56:19.306+00:00"
            }
        },
        {
            "response": {
                "status": "201 Created",
                "location": "Encounter/87905/_history/1",
                "etag": "1",
                "lastModified": "2019-07-10T22:56:19.306+00:00"
            }
        },
        {
            "response": {
                "status": "201 Created",
                "location": "Condition/87906/_history/1",
                "etag": "1",
                "lastModified": "2019-07-10T22:56:19.306+00:00"
            }
        },
        {
            "response": {
                "status": "201 Created",
                "location": "Communication/87907/_history/1",
                "etag": "1",
                "lastModified": "2019-07-10T22:56:19.306+00:00"
            }
        }
    ]
}
~~~
