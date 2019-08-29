### Examples
{:.no_toc}

**Scenario:**

Patient Y has been admitted to Provider X 's facility.  Acting in the role of Alert Sender Provider X alerts Payer Z who is acting in the role Alert Recipient of the admission.  The Alert is transacted as the `$notify` operation. The body of the operation is a Parameter resource containing two parts:

1. The Alert Endpoint which provides the recipient with the technical details of an endpoint for getting additional information from the medical record for this event.
1. The Alert Bundle containing the required Alert Communication profile and required resources for this Alert event use case.

An HTTP Status success code is returned on successful submission<!-- and a Bundle with type `transaction-response` that contains one entry for each entry in the request, in the same order, with the outcome of processing the entry.-->

**Push Alert Notification using the $notify operation**

`POST [base]Communication/$notify`

**Request body**

~~~
{
  "resourceType" : "Parameters",
  "id" : "admit-1",
  "parameter" : [
    {
      "name" : "alert",
      "part" : [
        {
          "name" : "alert-endpoint",
          "resource" : {
            "resourceType" : "Endpoint",
            "status" : "active",
            "connectionType" : {
              "system" : "http://terminology.hl7.org/CodeSystem/endpoint-connection-type",
              "code" : "hl7-fhir-rest"
            },
            "name" : "Acme Hospital EHR FHIR R4 Server",
            "payloadType" : [
              {
                "text" : "n/a"
              }
            ],
            "address" : "https://fhir-ehr.acme/r4/1234/",
            "header" : [
              "Authorization: Bearer eyJraWQiOiIyMDE5LTA3LTE3VDIzOjA1OjQ4LjY3NC5lYyIsInR5cCI6IkpXVCIsImFsZyI6IkVTMjU2In0.eyJzdWIiOiJwb3J0YWwiLCJ1cm46Y29tOmNlcm5lcjphdXRob3JpemF0aW9uOmNsYWltcyI6eyJ2ZXIiOiIxLjAiLCJ0bnQiOiIwYjhhMDExMS1lOGU2LTRjMjYtYTkxYy01MDY5Y2JjNmIxY2EiLCJhenMiOiJ1c2VyXC9DYXBhYmlsaXR5U3RhdGVtZW50LnJlYWQgdXNlclwvQWxsZXJneUludG9sZXJhbmNlLnJlYWQgdXNlclwvQXBwb2ludG1lbnQucmVhZCB1c2VyXC9FbmNvdW50ZXIucmVhZCB1c2VyXC9QYXRpZW50LnJlYWQgdXNlclwvUHJhY3RpdGlvbmVyLnJlYWQgdXNlclwvUmVsYXRlZFBlcnNvbi5yZWFkIn0sImF6cCI6IjgwMjg5YjQ4LTYzMjYtNDcxNi04NDQ1LThmYjIxNTkxNTkwZiIsImlzcyI6Imh0dHBzOlwvXC9hdXRob3JpemF0aW9uLnNhbmRib3hjZXJuZXIuY29tXC8iLCJleHAiOjE1NjM1MDQ2MTksImlhdCI6MTU2MzUwNDAxOSwianRpIjoiNDI1Y2E3NGQtNDFhMy00N2U5LTk2OTEtMGVmYThhYTUzYTdlIiwidXJuOmNlcm5lcjphdXRob3JpemF0aW9uOmNsYWltczp2ZXJzaW9uOjEiOnsidmVyIjoiMS4wIiwicHJvZmlsZXMiOnsic21hcnQtdjEiOnsiYXpzIjoidXNlclwvQ2FwYWJpbGl0eVN0YXRlbWVudC5yZWFkIHVzZXJcL0FsbGVyZ3lJbnRvbGVyYW5jZS5yZWFkIHVzZXJcL0FwcG9pbnRtZW50LnJlYWQgdXNlclwvRW5jb3VudGVyLnJlYWQgdXNlclwvUGF0aWVudC5yZWFkIHVzZXJcL1ByYWN0aXRpb25lci5yZWFkIHVzZXJcL1JlbGF0ZWRQZXJzb24ucmVhZCJ9fSwiY2xpZW50Ijp7Im5hbWUiOiJ0ZXN0LXI0IiwiaWQiOiI4MDI4OWI0OC02MzI2LTQ3MTYtODQ0NS04ZmIyMTU5MTU5MGYifSwidXNlciI6eyJwcmluY2lwYWwiOiJwb3J0YWwiLCJwZXJzb25hIjoicHJvdmlkZXIiLCJpZHNwIjoiMGI4YTAxMTEtZThlNi00YzI2LWE5MWMtNTA2OWNiYzZiMWNhIiwic2Vzc2lvbl9pZCI6Ijk0ZjYyZjhlLTJhMDAtNDAwMi05OWYwLWZkOWYzMjIwM2UwNCIsInByaW5jaXBhbFR5cGUiOiJVTkRFRklORUQiLCJwcmluY2lwYWxVcmkiOiJodHRwczpcL1wvbWlsbGVubmlhLnNhbmRib3hjZXJuZXIuY29tXC9pbnN0YW5jZVwvMGI4YTAxMTEtZThlNi00YzI2LWE5MWMtNTA2OWNiYzZiMWNhXC9wcmluY2lwYWxcLzAwMDAuMDAwMC4wMDQ0LjFEODciLCJpZHNwVXJpIjoiaHR0cHM6XC9cL21pbGxlbm5pYS5zYW5kYm94Y2VybmVyLmNvbVwvYWNjb3VudHNcL2ZoaXJwbGF5LnRlbXBfcmhvLmNlcm5lcmFzcC5jb21cLzBiOGEwMTExLWU4ZTYtNGMyNi1hOTFjLTUwNjljYmM2YjFjYVwvbG9naW4ifSwidGVuYW50IjoiMGI4YTAxMTEtZThlNi00YzI2LWE5MWMtNTA2OWNiYzZiMWNhIn19.weCcKK-zziKrsXlUKHunHTkbUJOZTV0AEzteZeaYdGjhF9581LlBCCp4EnaaUIQbkaWkQ-btukZ_GLw7-cy2Ag"
            ]
          }
        },
        {
          "name" : "alert-bundle",
          "resource" : {
            "resourceType" : "Bundle",
            "id" : "admit-01",
            "type" : "collection",
            "entry" : [
              {
                "fullUrl" : "urn:uuid:3852d906-a361-11e9-86cd-a4d18ccf5172",
                "resource" : {
                  "resourceType" : "Patient",
                  "meta" : {
                    "profile" : [
                      "http://hl7.org/fhir/us/core/StructureDefinition/us-core-patient"
                    ]
                  },
                  "extension" : [
                    {
                      "url" : "http://hl7.org/fhir/us/core/StructureDefinition/us-core-race",
                      "extension" : [
                        {
                          "url" : "ombCategory",
                          "valueCoding" : {
                            "system" : "urn:oid:2.16.840.1.113883.6.238",
                            "code" : "2106-3",
                            "display" : "White"
                          }
                        },
                        {
                          "url" : "ombCategory",
                          "valueCoding" : {
                            "system" : "urn:oid:2.16.840.1.113883.6.238",
                            "code" : "1002-5",
                            "display" : "American Indian or Alaska Native"
                          }
                        },
                        {
                          "url" : "ombCategory",
                          "valueCoding" : {
                            "system" : "urn:oid:2.16.840.1.113883.6.238",
                            "code" : "2028-9",
                            "display" : "Asian"
                          }
                        },
                        {
                          "url" : "detailed",
                          "valueCoding" : {
                            "system" : "urn:oid:2.16.840.1.113883.6.238",
                            "code" : "1586-7",
                            "display" : "Shoshone"
                          }
                        },
                        {
                          "url" : "detailed",
                          "valueCoding" : {
                            "system" : "urn:oid:2.16.840.1.113883.6.238",
                            "code" : "2036-2",
                            "display" : "Filipino"
                          }
                        },
                        {
                          "url" : "text",
                          "valueString" : "Mixed"
                        }
                      ]
                    },
                    {
                      "url" : "http://hl7.org/fhir/us/core/StructureDefinition/us-core-ethnicity",
                      "extension" : [
                        {
                          "url" : "ombCategory",
                          "valueCoding" : {
                            "system" : "urn:oid:2.16.840.1.113883.6.238",
                            "code" : "2135-2",
                            "display" : "Hispanic or Latino"
                          }
                        },
                        {
                          "url" : "detailed",
                          "valueCoding" : {
                            "system" : "urn:oid:2.16.840.1.113883.6.238",
                            "code" : "2184-0",
                            "display" : "Dominican"
                          }
                        },
                        {
                          "url" : "detailed",
                          "valueCoding" : {
                            "system" : "urn:oid:2.16.840.1.113883.6.238",
                            "code" : "2148-5",
                            "display" : "Mexican"
                          }
                        },
                        {
                          "url" : "text",
                          "valueString" : "Hispanic or Latino"
                        }
                      ]
                    },
                    {
                      "url" : "http://hl7.org/fhir/us/core/StructureDefinition/us-core-birthsex",
                      "valueCode" : "F"
                    }
                  ],
                  "identifier" : [
                    {
                      "use" : "usual",
                      "type" : {
                        "coding" : [
                          {
                            "system" : "http://terminology.hl7.org/CodeSystem/v2-0203",
                            "code" : "MR",
                            "display" : "Medical Record Number"
                          }
                        ],
                        "text" : "Medical Record Number"
                      },
                      "system" : "http://hospital.smarthealthit.org",
                      "value" : "1032702"
                    }
                  ],
                  "active" : true,
                  "name" : [
                    {
                      "family" : "Shaw",
                      "given" : [
                        "Amy",
                        "V."
                      ]
                    }
                  ],
                  "telecom" : [
                    {
                      "system" : "phone",
                      "value" : "555-555-5555",
                      "use" : "home"
                    },
                    {
                      "system" : "email",
                      "value" : "amy.shaw@example.com"
                    }
                  ],
                  "gender" : "female",
                  "birthDate" : "2007-02-20",
                  "address" : [
                    {
                      "line" : [
                        "49 Meadow St"
                      ],
                      "city" : "Mounds",
                      "state" : "OK",
                      "postalCode" : "74047",
                      "country" : "US"
                    }
                  ]
                },
                "request" : {
                  "method" : "POST",
                  "url" : "Patient"
                }
              },
              {
                "fullUrl" : "urn:uuid:3857dfb4-a361-11e9-86cd-a4d18ccf5172",
                "resource" : {
                  "resourceType" : "Encounter",
                  "meta" : {
                    "lastUpdated" : "2017-05-26T11:56:57.250-04:00",
                    "profile" : [
                      "http://hl7.org/fhir/us/core/StructureDefinition/us-core-encounter"
                    ]
                  },
                  "status" : "finished",
                  "class" : {
                    "system" : "http://terminology.hl7.org/CodeSystem/v3-ActCode",
                    "code" : "IMP",
                    "display" : "inpatient encounter"
                  },
                  "type" : [
                    {
                      "coding" : [
                        {
                          "system" : "http://www.ama-assn.org/go/cpt",
                          "code" : "99234"
                        }
                      ],
                      "text" : "inpatient hospital care"
                    }
                  ],
                  "subject" : {
                    "reference" : "urn:uuid:3852d906-a361-11e9-86cd-a4d18ccf5172"
                  },
                  "period" : {
                    "start" : "2015-11-01T17:00:14-05:00",
                    "end" : "2015-11-01T18:00:14-05:00"
                  },
                  "location" : [
                    {
                      "location" : {
                        "reference" : "Location/hl7east"
                      }
                    }
                  ]
                },
                "request" : {
                  "method" : "POST",
                  "url" : "Encounter"
                }
              },
              {
                "fullUrl" : "urn:uuid:385a65e0-a361-11e9-86cd-a4d18ccf5172",
                "resource" : {
                  "resourceType" : "Condition",
                  "meta" : {
                    "profile" : [
                      "http://hl7.org/fhir/us/core/StructureDefinition/us-core-condition"
                    ]
                  },
                  "clinicalStatus" : {
                    "coding" : [
                      {
                        "system" : "http://terminology.hl7.org/CodeSystem/condition-clinical",
                        "code" : "active",
                        "display" : "Active"
                      }
                    ],
                    "text" : "Active"
                  },
                  "verificationStatus" : {
                    "coding" : [
                      {
                        "system" : "http://terminology.hl7.org/CodeSystem/condition-ver-status",
                        "code" : "confirmed",
                        "display" : "Confirmed"
                      }
                    ],
                    "text" : "Confirmed"
                  },
                  "category" : [
                    {
                      "coding" : [
                        {
                          "system" : "http://terminology.hl7.org/CodeSystem/condition-category",
                          "code" : "problem-list-item",
                          "display" : "Problem List Item"
                        }
                      ],
                      "text" : "Problem"
                    }
                  ],
                  "code" : {
                    "coding" : [
                      {
                        "system" : "http://snomed.info/sct",
                        "code" : "442311008",
                        "display" : "Liveborn born in hospital"
                      }
                    ],
                    "text" : "Single liveborn, born in hospital"
                  },
                  "subject" : {
                    "reference" : "urn:uuid:3852d906-a361-11e9-86cd-a4d18ccf5172",
                    "display" : "Amy V. Shaw"
                  },
                  "onsetDateTime" : "2016-08-10"
                },
                "request" : {
                  "method" : "POST",
                  "url" : "Condition"
                }
              },
              {
                "fullUrl" : "urn:uuid:385bceb2-a361-11e9-86cd-a4d18ccf5172",
                "resource" : {
                  "resourceType" : "Communication",
                  "meta" : {
                    "profile" : [
                      "http://hl7.org/fhir/us/davinci-alerts/StructureDefinition/alerts-communication"
                    ]
                  },
                  "identifier" : [
                    {
                      "system" : "urn:oid:1.3.4.5.6.7",
                      "value" : "2345678901"
                    }
                  ],
                  "status" : "completed",
                  "category" : [
                    {
                      "coding" : [
                        {
                          "system" : "http://terminology.hl7.org/CodeSystem/communication-category",
                          "code" : "alert"
                        }
                      ],
                      "text" : "Alert"
                    }
                  ],
                  "priority" : "routine",
                  "subject" : {
                    "reference" : "urn:uuid:3852d906-a361-11e9-86cd-a4d18ccf5172"
                  },
                  "topic" : {
                    "coding" : [
                      {
                        "system" : "http://hl7.org/fhir/us/davinci-alerts/CodeSystem/communication-topic",
                        "code" : "alert-admit-inpatient"
                      }
                    ],
                    "text" : "Alert Admit Inpatient"
                  },
                  "about" : [
                    {
                      "reference" : "Coverage/example-1",
                      "type" : "Coverage"
                    }
                  ],
                  "encounter" : {
                    "reference" : "urn:uuid:3857dfb4-a361-11e9-86cd-a4d18ccf5172"
                  },
                  "sent" : "2019-07-04T18:01:10-08:00",
                  "recipient" : [
                    {
                      "reference" : "PractitionerRole/example"
                    }
                  ],
                  "sender" : {
                    "reference" : "Organization/example-2"
                  },
                  "payload" : [
                    {
                      "contentString" : "Admit to xyz"
                    },
                    {
                      "contentReference" : {
                        "reference" : "urn:uuid:3857dfb4-a361-11e9-86cd-a4d18ccf5172"
                      }
                    },
                    {
                      "contentReference" : {
                        "reference" : "urn:uuid:385a65e0-a361-11e9-86cd-a4d18ccf5172"
                      }
                    }
                  ]
                },
                "request" : {
                  "method" : "POST",
                  "url" : "Communication"
                }
              }
            ]
          }
        }
      ]
    }
  ]
}
~~~

**Response**

~~~
HTTP/1.1 200 OK
[other headers]
~~~
<!--
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
-->
