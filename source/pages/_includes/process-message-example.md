### Examples
{:.no_toc}

**Scenario:**

Patient Y has been admitted to Provider X 's facility.  Acting in the role of Alert Sender Provider X alerts Payer Z who is acting in the role Alert Recipient of the admission.  The Alert is transacted as the `[$process-message]` operation. The body of the operation is a Message Bundle containing:

1. The Message Header which is the first resource in the bundle and contains the the message event code - that identifies the nature of the request message.
1. The other resources in the bundle depend on the type of the Alert event use case as defined by the MessageDefinition and GraphDefinition.

An HTTP Status success code is returned on successful submission.

**Push Alert Notification using the $process-message**

`POST [base]/$process-message`

**Request body**

~~~
{
  "resourceType" : "Bundle",
  "id" : "201908201155.55-admit-01",
  "type" : "message",
  "timestamp" : "2019-08-21T08:08:47Z",
  "entry" : [
    {
      "fullUrl" : "urn:uuid:267b18ce-3d37-4581-9baa-6fada338038b",
      "resource" : {
        "resourceType" : "MessageHeader",
        "id" : "267b18ce-3d37-4581-9baa-6fada338038b",
        "meta" : {
          "profile" : [
            "http://hl7.org/fhir/us/davinci-alerts/MessageDefinition/alert"
          ]
        },
        "text" : {
          "status" : "generated",
          "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p><b>Generated Narrative with Details</b></p><p><b>id</b>: 267b18ce-3d37-4581-9baa-6fada338038b</p><p><b>meta</b>: </p><p><b>event</b>: Alert admit (Details: http://hl7.org/fhir/us/davinci-alerts/CodeSystem/communication-topic code alert-admit = 'Alert admit', stated as 'null')</p><h3>Destinations</h3><table class=\"grid\"><tr><td>-</td><td><b>Name</b></td><td><b>Target</b></td><td><b>Endpoint</b></td><td><b>Receiver</b></td></tr><tr><td>*</td><td>Acme Message Gateway</td><td>Device/example</td><td><a href=\"llp:10.11.12.14:5432\">llp:10.11.12.14:5432</a></td><td><a href=\"http://acme.com/ehr/fhir/PractitionerRole/example\">http://acme.com/ehr/fhir/PractitionerRole/example</a></td></tr></table><p><b>sender</b>: <a href=\"7221aa91-d9e1-44fa-8b90-c5a8c7caeade\">7221aa91-d9e1-44fa-8b90-c5a8c7caeade</a></p><p><b>enterer</b>: <a href=\"http://acme.com/ehr/fhir/Practitioner/example-1\">http://acme.com/ehr/fhir/Practitioner/example-1</a></p><p><b>author</b>: <a href=\"http://acme.com/ehr/fhir/Practitioner/example-1\">http://acme.com/ehr/fhir/Practitioner/example-1</a></p><h3>Sources</h3><table class=\"grid\"><tr><td>-</td><td><b>Name</b></td><td><b>Software</b></td><td><b>Version</b></td><td><b>Contact</b></td><td><b>Endpoint</b></td></tr><tr><td>*</td><td>Acme Central Patient Registry</td><td>FooBar Patient Manager</td><td>3.1.45.AABB</td><td>ph: +1 (555) 123 4567</td><td><a href=\"llp:10.11.12.13:5432\">llp:10.11.12.13:5432</a></td></tr></table><p><b>focus</b>: <a href=\"http://acme.com/ehr/fhir/Encounter/example-1\">http://acme.com/ehr/fhir/Encounter/example-1</a></p><p><b>definition</b>: <a href=\"http://hl7.org/fhir/us/davinci-alerts/MessageDefinition/alert-admit\">http://hl7.org/fhir/us/davinci-alerts/MessageDefinition/alert-admit</a></p></div>"
        },
        "eventCoding" : {
          "system" : "http://hl7.org/fhir/us/davinci-alerts/CodeSystem/communication-topic",
          "code" : "alert-admit"
        },
        "destination" : [
          {
            "name" : "Acme Message Gateway",
            "target" : {
              "display" : "Device/example"
            },
            "endpoint" : "llp:10.11.12.14:5432",
            "receiver" : {
              "reference" : "http://acme.com/ehr/fhir/PractitionerRole/example"
            }
          }
        ],
        "sender" : {
          "reference" : "7221aa91-d9e1-44fa-8b90-c5a8c7caeade"
        },
        "enterer" : {
          "reference" : "http://acme.com/ehr/fhir/Practitioner/example-1"
        },
        "author" : {
          "reference" : "http://acme.com/ehr/fhir/Practitioner/example-1"
        },
        "source" : {
          "name" : "Acme Central Patient Registry",
          "software" : "FooBar Patient Manager",
          "version" : "3.1.45.AABB",
          "contact" : {
            "system" : "phone",
            "value" : "+1 (555) 123 4567"
          },
          "endpoint" : "llp:10.11.12.13:5432"
        },
        "focus" : [
          {
            "reference" : "http://acme.com/ehr/fhir/Encounter/example-1"
          }
        ],
        "definition" : "http://hl7.org/fhir/us/davinci-alerts/MessageDefinition/alert-admit"
      }
    },
    {
      "fullUrl" : "urn:uuid:a33d1eed-c4ad-4def-8087-042b7ac0f2b7",
      "resource" : {
        "resourceType" : "Encounter",
        "id" : "a33d1eed-c4ad-4def-8087-042b7ac0f2b7",
        "meta" : {
          "profile" : [
            "http://hl7.org/fhir/us/core/StructureDefinition/us-core-encounter"
          ]
        },
        "text" : {
          "status" : "generated",
          "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p><b>Generated Narrative with Details</b></p><p><b>id</b>: a33d1eed-c4ad-4def-8087-042b7ac0f2b7</p><p><b>meta</b>: </p><p><b>status</b>: finished</p><p><b>class</b>: inpatient encounter (Details: http://terminology.hl7.org/CodeSystem/v3-ActCode code IMP = 'inpatient encounter', stated as 'inpatient encounter')</p><p><b>type</b>: Inpatient hospital care <span style=\"background: LightGoldenRodYellow\">(Details : {http://www.ama-assn.org/go/cpt code '99234' = '99234)</span></p><p><b>subject</b>: <a href=\"e442c924-df77-47fa-838f-24a8253bbdd4\">e442c924-df77-47fa-838f-24a8253bbdd4</a></p><p><b>period</b>: Nov 1, 2015, 2:00:14 PM --&gt; Nov 1, 2015, 3:00:14 PM</p><h3>Diagnoses</h3><table class=\"grid\"><tr><td>-</td><td><b>Condition</b></td></tr><tr><td>*</td><td><a href=\"54f0ea3f-dc89-4e71-8d98-8774a5add41e\">54f0ea3f-dc89-4e71-8d98-8774a5add41e</a></td></tr></table><h3>Locations</h3><table class=\"grid\"><tr><td>-</td><td><b>Location</b></td></tr><tr><td>*</td><td><a href=\"Location-hl7east.html\">Generated Summary: id: hl7east; 29; status: active; name: Health Level Seven International - Amherst; description: HL7 Headquarters - East; ph: (+1) 734-677-7777</a></td></tr></table></div>"
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
            "text" : "Inpatient hospital care"
          }
        ],
        "subject" : {
          "reference" : "e442c924-df77-47fa-838f-24a8253bbdd4"
        },
        "period" : {
          "start" : "2015-11-01T17:00:14-05:00",
          "end" : "2015-11-01T18:00:14-05:00"
        },
        "diagnosis" : [
          {
            "condition" : {
              "reference" : "54f0ea3f-dc89-4e71-8d98-8774a5add41e"
            }
          }
        ],
        "location" : [
          {
            "location" : {
              "reference" : "Location/hl7east"
            }
          }
        ]
      }
    },
    {
      "fullUrl" : "urn:uuid:e442c924-df77-47fa-838f-24a8253bbdd4",
      "resource" : {
        "resourceType" : "Patient",
        "id" : "e442c924-df77-47fa-838f-24a8253bbdd4",
        "meta" : {
          "profile" : [
            "http://hl7.org/fhir/us/core/StructureDefinition/us-core-patient"
          ]
        },
        "text" : {
          "status" : "generated",
          "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\">\n\t\t\t\t\t\t<p>\n\t\t\t\t\t\t\t<b>Generated Narrative with Details</b>\n\t\t\t\t\t\t</p>\n\t\t\t\t\t\t<p>\n\t\t\t\t\t\t\t<b>id</b>: example</p>\n\t\t\t\t\t\t<p>\n\t\t\t\t\t\t\t<b>identifier</b>: Medical Record Number = 1032702 (USUAL)</p>\n\t\t\t\t\t\t<p>\n\t\t\t\t\t\t\t<b>active</b>: true</p>\n\t\t\t\t\t\t<p>\n\t\t\t\t\t\t\t<b>name</b>: Amy V. Shaw </p>\n\t\t\t\t\t\t<p>\n\t\t\t\t\t\t\t<b>telecom</b>: ph: 555-555-5555(HOME), amy.shaw@example.com</p>\n\t\t\t\t\t\t<p>\n\t\t\t\t\t\t\t<b>gender</b>: </p>\n\t\t\t\t\t\t<p>\n\t\t\t\t\t\t\t<b>birthsex</b>: Female</p>\n\t\t\t\t\t\t<p>\n\t\t\t\t\t\t\t<b>birthDate</b>: Feb 20, 2007</p>\n\t\t\t\t\t\t<p>\n\t\t\t\t\t\t\t<b>address</b>: 49 Meadow St Mounds OK 74047 US </p>\n\t\t\t\t\t\t<p>\n\t\t\t\t\t\t\t<b>race</b>: White, American Indian or Alaska Native, Asian, Shoshone, Filipino</p>\n\t\t\t\t\t\t<p>\n\t\t\t\t\t\t\t<b>ethnicity</b>: Hispanic or Latino, Dominican, Mexican</p>\n\t\t\t\t\t</div>"
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
      }
    },
    {
      "fullUrl" : "urn:uuid:54f0ea3f-dc89-4e71-8d98-8774a5add41e",
      "resource" : {
        "resourceType" : "Condition",
        "id" : "54f0ea3f-dc89-4e71-8d98-8774a5add41e",
        "meta" : {
          "profile" : [
            "http://hl7.org/fhir/us/core/StructureDefinition/us-core-condition"
          ]
        },
        "text" : {
          "status" : "generated",
          "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p><b>Generated Narrative with Details</b></p><p><b>id</b>: 54f0ea3f-dc89-4e71-8d98-8774a5add41e</p><p><b>meta</b>: </p><p><b>clinicalStatus</b>: Active <span style=\"background: LightGoldenRodYellow\">(Details : {http://terminology.hl7.org/CodeSystem/condition-clinical code 'active' = 'Active', given as 'Active'})</span></p><p><b>verificationStatus</b>: Confirmed <span style=\"background: LightGoldenRodYellow\">(Details : {http://terminology.hl7.org/CodeSystem/condition-ver-status code 'confirmed' = 'Confirmed', given as 'Confirmed'})</span></p><p><b>category</b>: Problem <span style=\"background: LightGoldenRodYellow\">(Details : {http://terminology.hl7.org/CodeSystem/condition-category code 'problem-list-item' = 'Problem List Item', given as 'Problem List Item'})</span></p><p><b>code</b>: Single liveborn, born in hospital <span style=\"background: LightGoldenRodYellow\">(Details : {SNOMED CT code '442311008' = 'Liveborn born in hospital', given as 'Liveborn born in hospital'})</span></p><p><b>subject</b>: <a href=\"e442c924-df77-47fa-838f-24a8253bbdd4\">Amy V. Shaw</a></p><p><b>onset</b>: Aug 10, 2016, 12:00:00 AM</p></div>"
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
          "reference" : "e442c924-df77-47fa-838f-24a8253bbdd4",
          "display" : "Amy V. Shaw"
        },
        "onsetDateTime" : "2016-08-10"
      }
    },
    {
      "fullUrl" : "urn:uuid:c470de5b-345c-4945-bc4a-cbdec7d86f54",
      "resource" : {
        "resourceType" : "Coverage",
        "id" : "c470de5b-345c-4945-bc4a-cbdec7d86f54",
        "meta" : {
          "profile" : [
            "http://hl7.org/fhir/us/davinci-hrex/StructureDefinition/hrex-coverage"
          ]
        },
        "text" : {
          "status" : "generated",
          "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p><b>Generated Narrative with Details</b></p><p><b>id</b>: c470de5b-345c-4945-bc4a-cbdec7d86f54</p><p><b>meta</b>: </p><p><b>identifier</b>: DZW9200000000</p><p><b>status</b>: active</p><p><b>type</b>: health insurance plan policy <span style=\"background: LightGoldenRodYellow\">(Details : {http://terminology.hl7.org/CodeSystem/v3-ActCode code 'HIP' = 'health insurance plan policy', given as 'health insurance plan policy'})</span></p><p><b>subscriber</b>: <a href=\"e442c924-df77-47fa-838f-24a8253bbdd4\">First M LastName Jr</a></p><p><b>subscriberId</b>: DZW9200000000</p><p><b>beneficiary</b>: <a href=\"e442c924-df77-47fa-838f-24a8253bbdd4\">e442c924-df77-47fa-838f-24a8253bbdd4</a></p><p><b>relationship</b>: Self <span style=\"background: LightGoldenRodYellow\">(Details : {http://terminology.hl7.org/CodeSystem/subscriber-relationship code 'self' = 'Self', given as 'Self'})</span></p><p><b>period</b>: Jan 1, 2016, 12:00:00 AM --&gt; (ongoing)</p><p><b>payor</b>: Anthem Blue Cross of California</p><h3>Classes</h3><table class=\"grid\"><tr><td>-</td><td><b>Type</b></td><td><b>Value</b></td><td><b>Name</b></td></tr><tr><td>*</td><td>Plan <span style=\"background: LightGoldenRodYellow\">(Details : {http://terminology.hl7.org/CodeSystem/coverage-class code 'plan' = 'Plan)</span></td><td>1FZQ</td><td>Anthem Bronze 60 D HSA PPO</td></tr></table></div>"
        },
        "identifier" : [
          {
            "system" : "https://www.anthem.com/ca",
            "value" : "DZW9200000000"
          }
        ],
        "status" : "active",
        "type" : {
          "coding" : [
            {
              "system" : "http://terminology.hl7.org/CodeSystem/v3-ActCode",
              "code" : "HIP",
              "display" : "health insurance plan policy"
            }
          ]
        },
        "subscriber" : {
          "reference" : "e442c924-df77-47fa-838f-24a8253bbdd4",
          "display" : "First M LastName Jr"
        },
        "subscriberId" : "DZW9200000000",
        "beneficiary" : {
          "reference" : "e442c924-df77-47fa-838f-24a8253bbdd4"
        },
        "relationship" : {
          "coding" : [
            {
              "system" : "http://terminology.hl7.org/CodeSystem/subscriber-relationship",
              "code" : "self",
              "display" : "Self"
            }
          ]
        },
        "period" : {
          "start" : "2016-01-01"
        },
        "payor" : [
          {
            "display" : "Anthem Blue Cross of California"
          }
        ],
        "class" : [
          {
            "type" : {
              "coding" : [
                {
                  "system" : "http://terminology.hl7.org/CodeSystem/coverage-class",
                  "code" : "plan"
                }
              ]
            },
            "value" : "1FZQ",
            "name" : "Anthem Bronze 60 D HSA PPO"
          }
        ]
      }
    },
    {
      "fullUrl" : "urn:uuid:7221aa91-d9e1-44fa-8b90-c5a8c7caeade",
      "resource" : {
        "resourceType" : "Organization",
        "id" : "7221aa91-d9e1-44fa-8b90-c5a8c7caeade",
        "meta" : {
          "profile" : [
            "http://hl7.org/fhir/us/core/StructureDefinition/us-core-organization"
          ]
        },
        "text" : {
          "status" : "generated",
          "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p><b>Generated Narrative with Details</b></p><p><b>id</b>: 7221aa91-d9e1-44fa-8b90-c5a8c7caeade</p><p><b>meta</b>: </p><p><b>identifier</b>: 1407071236, 121111111</p><p><b>active</b>: true</p><p><b>type</b>: Healthcare Provider <span style=\"background: LightGoldenRodYellow\">(Details : {http://terminology.hl7.org/CodeSystem/organization-type code 'prov' = 'Healthcare Provider', given as 'Healthcare Provider'})</span></p><p><b>name</b>: Acme Clinic</p><p><b>telecom</b>: ph: (+1) 734-677-7777, customer-service@acme-clinic.org</p><p><b>address</b>: 3300 Washtenaw Avenue, Suite 227 Amherst MA 01002 USA </p><p><b>endpoint</b>: <a href=\"9ac634f6-b6c2-42ff-b3f6-8b650ec345f4\">Acme Hospital EHR FHIR R4 Server</a></p></div>"
        },
        "identifier" : [
          {
            "system" : "http://hl7.org.fhir/sid/us-npi",
            "value" : "1407071236"
          },
          {
            "system" : "http://example.org/fhir/sid/us-tin",
            "value" : "121111111"
          }
        ],
        "active" : true,
        "type" : [
          {
            "coding" : [
              {
                "system" : "http://terminology.hl7.org/CodeSystem/organization-type",
                "code" : "prov",
                "display" : "Healthcare Provider"
              }
            ]
          }
        ],
        "name" : "Acme Clinic",
        "telecom" : [
          {
            "system" : "phone",
            "value" : "(+1) 734-677-7777"
          },
          {
            "system" : "email",
            "value" : "customer-service@acme-clinic.org"
          }
        ],
        "address" : [
          {
            "line" : [
              "3300 Washtenaw Avenue, Suite 227"
            ],
            "city" : "Amherst",
            "state" : "MA",
            "postalCode" : "01002",
            "country" : "USA"
          }
        ],
        "endpoint" : [
          {
            "reference" : "9ac634f6-b6c2-42ff-b3f6-8b650ec345f4",
            "display" : "Acme Hospital EHR FHIR R4 Server"
          }
        ]
      }
    },
    {
      "fullUrl" : "urn:uuid:9ac634f6-b6c2-42ff-b3f6-8b650ec345f4",
      "resource" : {
        "resourceType" : "Endpoint",
        "id" : "9ac634f6-b6c2-42ff-b3f6-8b650ec345f4",
        "meta" : {
          "profile" : [
            "http://hl7.org/fhir/us/davinci-alerts/StructureDefinition/alerts-endpoint"
          ]
        },
        "text" : {
          "status" : "generated",
          "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p><b>Generated Narrative with Details</b></p><p><b>id</b>: 9ac634f6-b6c2-42ff-b3f6-8b650ec345f4</p><p><b>meta</b>: </p><p><b>status</b>: active</p><p><b>connectionType</b>: HL7 FHIR (Details: http://terminology.hl7.org/CodeSystem/endpoint-connection-type code hl7-fhir-rest = 'HL7 FHIR', stated as 'null')</p><p><b>name</b>: Acme Hospital EHR FHIR R4 Server</p><p><b>payloadType</b>: n/a <span style=\"background: LightGoldenRodYellow\">(Details )</span></p><p><b>address</b>: <a href=\"https://fhir-ehr.acme/r4/1234/\">https://fhir-ehr.acme/r4/1234/</a></p><p><b>header</b>: Authorization: Bearer eyJraWQiOiIyMDE5LTA3LTE3VDIzOjA1OjQ4LjY3NC5lYyIsInR5cCI6IkpXVCIsImFsZyI6IkVTMjU2In0.eyJzdWIiOiJwb3J0YWwiLCJ1cm46Y29tOmNlcm5lcjphdXRob3JpemF0aW9uOmNsYWltcyI6eyJ2ZXIiOiIxLjAiLCJ0bnQiOiIwYjhhMDExMS1lOGU2LTRjMjYtYTkxYy01MDY5Y2JjNmIxY2EiLCJhenMiOiJ1c2VyXC9DYXBhYmlsaXR5U3RhdGVtZW50LnJlYWQgdXNlclwvQWxsZXJneUludG9sZXJhbmNlLnJlYWQgdXNlclwvQXBwb2ludG1lbnQucmVhZCB1c2VyXC9FbmNvdW50ZXIucmVhZCB1c2VyXC9QYXRpZW50LnJlYWQgdXNlclwvUHJhY3RpdGlvbmVyLnJlYWQgdXNlclwvUmVsYXRlZFBlcnNvbi5yZWFkIn0sImF6cCI6IjgwMjg5YjQ4LTYzMjYtNDcxNi04NDQ1LThmYjIxNTkxNTkwZiIsImlzcyI6Imh0dHBzOlwvXC9hdXRob3JpemF0aW9uLnNhbmRib3hjZXJuZXIuY29tXC8iLCJleHAiOjE1NjM1MDQ2MTksImlhdCI6MTU2MzUwNDAxOSwianRpIjoiNDI1Y2E3NGQtNDFhMy00N2U5LTk2OTEtMGVmYThhYTUzYTdlIiwidXJuOmNlcm5lcjphdXRob3JpemF0aW9uOmNsYWltczp2ZXJzaW9uOjEiOnsidmVyIjoiMS4wIiwicHJvZmlsZXMiOnsic21hcnQtdjEiOnsiYXpzIjoidXNlclwvQ2FwYWJpbGl0eVN0YXRlbWVudC5yZWFkIHVzZXJcL0FsbGVyZ3lJbnRvbGVyYW5jZS5yZWFkIHVzZXJcL0FwcG9pbnRtZW50LnJlYWQgdXNlclwvRW5jb3VudGVyLnJlYWQgdXNlclwvUGF0aWVudC5yZWFkIHVzZXJcL1ByYWN0aXRpb25lci5yZWFkIHVzZXJcL1JlbGF0ZWRQZXJzb24ucmVhZCJ9fSwiY2xpZW50Ijp7Im5hbWUiOiJ0ZXN0LXI0IiwiaWQiOiI4MDI4OWI0OC02MzI2LTQ3MTYtODQ0NS04ZmIyMTU5MTU5MGYifSwidXNlciI6eyJwcmluY2lwYWwiOiJwb3J0YWwiLCJwZXJzb25hIjoicHJvdmlkZXIiLCJpZHNwIjoiMGI4YTAxMTEtZThlNi00YzI2LWE5MWMtNTA2OWNiYzZiMWNhIiwic2Vzc2lvbl9pZCI6Ijk0ZjYyZjhlLTJhMDAtNDAwMi05OWYwLWZkOWYzMjIwM2UwNCIsInByaW5jaXBhbFR5cGUiOiJVTkRFRklORUQiLCJwcmluY2lwYWxVcmkiOiJodHRwczpcL1wvbWlsbGVubmlhLnNhbmRib3hjZXJuZXIuY29tXC9pbnN0YW5jZVwvMGI4YTAxMTEtZThlNi00YzI2LWE5MWMtNTA2OWNiYzZiMWNhXC9wcmluY2lwYWxcLzAwMDAuMDAwMC4wMDQ0LjFEODciLCJpZHNwVXJpIjoiaHR0cHM6XC9cL21pbGxlbm5pYS5zYW5kYm94Y2VybmVyLmNvbVwvYWNjb3VudHNcL2ZoaXJwbGF5LnRlbXBfcmhvLmNlcm5lcmFzcC5jb21cLzBiOGEwMTExLWU4ZTYtNGMyNi1hOTFjLTUwNjljYmM2YjFjYVwvbG9naW4ifSwidGVuYW50IjoiMGI4YTAxMTEtZThlNi00YzI2LWE5MWMtNTA2OWNiYzZiMWNhIn19.weCcKK-zziKrsXlUKHunHTkbUJOZTV0AEzteZeaYdGjhF9581LlBCCp4EnaaUIQbkaWkQ-btukZ_GLw7-cy2Ag</p></div>"
        },
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
      "fullUrl" : "urn:uuid:58ac7d17-5391-4ffa-a56e-5e26d74b8662",
      "resource" : {
        "resourceType" : "MessageDefinition",
        "id" : "58ac7d17-5391-4ffa-a56e-5e26d74b8662",
        "text" : {
          "status" : "generated",
          "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p><b>Generated Narrative with Details</b></p><p><b>id</b>: 58ac7d17-5391-4ffa-a56e-5e26d74b8662</p><p><b>url</b>: <a href=\"http://hl7.org/fhir/us/davinci-alerts/MessageDefinition/alert-admit\">http://hl7.org/fhir/us/davinci-alerts/MessageDefinition/alert-admit</a></p><p><b>name</b>: AlertAdmit</p><p><b>title</b>: Da Vinci Alert Admit Message Definition</p><p><b>status</b>: active</p><p><b>date</b>: Aug 20, 2019, 12:00:00 AM</p><p><b>publisher</b>: Da Vinci Project</p><p><b>contact</b>: </p><p><b>purpose</b>: Defines Da Vinci Alerts patient admission notification message bundle.</p><p><b>event</b>: Alert admit (Details: http://hl7.org/fhir/us/davinci-alerts/CodeSystem/communication-topic code alert-admit = 'Alert admit', stated as 'null')</p><p><b>category</b>: notification</p><h3>Focus</h3><table class=\"grid\"><tr><td>-</td><td><b>Code</b></td><td><b>Min</b></td><td><b>Max</b></td></tr><tr><td>*</td><td>Encounter</td><td>1</td><td>1</td></tr></table><p><b>graph</b>: <a href=\"http://hl7.org/fhir/us/davinci-alerts/GraphDefinition/143332\">http://hl7.org/fhir/us/davinci-alerts/GraphDefinition/143332</a></p></div>"
        },
        "url" : "http://hl7.org/fhir/us/davinci-alerts/MessageDefinition/alert-admit",
        "name" : "AlertAdmit",
        "title" : "Da Vinci Alert Admit Message Definition",
        "status" : "active",
        "date" : "2019-08-20",
        "publisher" : "Da Vinci Project",
        "contact" : [
          {
            "telecom" : [
              {
                "system" : "url",
                "value" : "http://www.hl7.org/about/davinci/"
              }
            ]
          }
        ],
        "purpose" : "Defines Da Vinci Alerts patient admission notification message bundle.",
        "eventCoding" : {
          "system" : "http://hl7.org/fhir/us/davinci-alerts/CodeSystem/communication-topic",
          "code" : "alert-admit"
        },
        "category" : "notification",
        "focus" : [
          {
            "code" : "Encounter",
            "min" : 1,
            "max" : "1"
          }
        ],
        "graph" : [
          "http://hl7.org/fhir/us/davinci-alerts/GraphDefinition/143332"
        ]
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
